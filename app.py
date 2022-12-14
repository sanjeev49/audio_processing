from audio_processing.component.record_mic_play import record_audio, save_audio, play_audio
from audio_processing.utils.common import get_current_time, read_yaml, create_directories
from audio_processing.component.plot_audio import plotAudio
from audio_processing.component.reduce_noise import redc_noise
from audio_processing.component.declip import (
    get_segments,
    declip_segments,
    plot_special_segment,
    save_bad_file,
    save_file
)
from audio_processing.exception import audioException

import numpy as np
from scipy.io.wavfile import read
import pyaudio
import os
from fastapi import FastAPI

# read yaml file 
config = read_yaml('configs/configs.yaml')

# getting variables  , define directories
root_dir = os.getcwd()
artifacts = config["artifacts"]
artifacts_dir = os.path.join(root_dir, artifacts["ARTIFACTS_DIR"])
input_dir = os.path.join(artifacts_dir, artifacts["INPUT_DIR"])
output_dir = os.path.join(artifacts_dir, artifacts["OUTPUT_DIR"])
removed_noise_dir = os.path.join(artifacts_dir, artifacts["REMOVED_NOISE_DIR"])
declipped_dir = os.path.join(artifacts_dir, artifacts["DECLIPPED_DIR"])
bad_dir = os.path.join(artifacts_dir, artifacts["BAD_DIR"])
create_directories([artifacts_dir, input_dir, output_dir, removed_noise_dir, declipped_dir, bad_dir])
frames_per_buffer = artifacts["FRAMES_PER_BUFFER"]
channels = artifacts["CHANNELS"]
rate = artifacts["RATE"]
seconds = artifacts["SECONDS"]
FORMAT = pyaudio.paInt16

# Initialiing filename on curretn timestamp
CURRENT_TIME_STAMP = get_current_time()
filename = f"recordeded_file_{CURRENT_TIME_STAMP}.wav"

recorded_filename = os.path.join(output_dir, filename)
noise_removed_file_name = os.path.join(removed_noise_dir, filename)
bad_file_name = os.path.join(bad_dir, filename)
declipped_filename = os.path.join(declipped_dir, filename)

p = pyaudio.PyAudio()

stream = p.open(
    format= FORMAT,
    channels=channels,
    rate = rate,
    input = True, 
    frames_per_buffer=frames_per_buffer
)


# Recording audio stream
app = FastAPI()

@app.get('/record_and_save/')
async def recordandsave():
    try:
        audio_frames = record_audio(stream = stream,p=p, FRAMES_PER_BUFFER=frames_per_buffer,
                                                                RATE=rate,seconds=seconds)
        save_audio(location_to_save=recorded_filename, p = p, CHANNELS=channels, FORMAT=FORMAT,
        RATE=rate, FRAMES=audio_frames)
        return {"Audio is recorded and saved at location":recorded_filename}
    except Exception as e:
        raise audioException(e, sys) from e

# Creating routes for fastapi application

@app.get("/play/")
async def read_item(filename):
    try:
        if os.path.exists(filename):
            return play_audio(filename)
    except Exception as e:
        return {"Plese enter correct filepath"}

# Plot audio stream with matplotlib
@app.get("/plot_audio/")
async def plotaud(filename):
    try:
        if os.path.exists(filename):
            print(filename)
            plotAudio(filename)
    except Exception as e:
        return {f"Exception is {e}"}


# if you want to reduce noise from the audio
@app.get('/reduce_noise')
async def reduceN(filename):
    try:
        if os.path.exists(filename):
            redc_noise(filename, noise_removed_file_name)
    except Exception as e:
        return {"someting bad happends"}

# If one audio signal is too loud for the microphone diaphram its become clipped. So we need to declipp it.
@app.get('/declip_audio/')
async def declip_audio(filename):
    sample_rate, file_info = read(filename)
    np_array = np.array(file_info, dtype=float)  # load int16 wav file

    #plot the special segment from the tutorial wav file
    plot_special_segment(np_array)

    # identify bad segments
    segments = get_segments(np_array)

    # declip the segments
    new_array = declip_segments(segments, np_array)

    # plot the special segment from the tutorial wav file
    plot_special_segment(new_array)

    #save bad array from tutorial to demonstrate that we need to rescale
    save_bad_file(sample_rate, new_array, bad_file_location=bad_file_name)

    # save new wav file
    save_file(sample_rate, new_array, declipped_filename)

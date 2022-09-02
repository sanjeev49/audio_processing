from audio_processign.src.record_mic_play import record_audio, save_audio, play_audio
from audio_processign.utils.helper_function import get_current_time
from audio_processign.src.plot_audio import plotAudio
from audio_processign.src.reduce_noise import redc_noise
import pyaudio
import os 
import wave
from fastapi import FastAPI

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 16000
ROOT_DIR = os.getcwd()
AUDIO_DIR = os.path.join(ROOT_DIR, "data")
AUDIO_INPUT_FILE = os.path.join(AUDIO_DIR, "inputs")
AUDIO_OUTPUT_FILE = os.path.join(AUDIO_DIR, "outputs")
#filename = os.path.join(AUDIO_OUTPUT_FILE, "output.wav")

reduced_noise_dir = os.path.join(AUDIO_DIR, "noise_removed")


CURRENT_TIME_STAMP = get_current_time()
filename = f"recordeded_file_{CURRENT_TIME_STAMP}.wav"
file_loc = os.path.join(AUDIO_OUTPUT_FILE, filename)

noise_removed_file_name = os.path.join(reduced_noise_dir, filename)

# filename = os.path.join(AUDIO_OUTPUT_FILE, filename)

# function to creat file name in output file name 

file_for_plot = os.path.join(AUDIO_OUTPUT_FILE, filename)

p = pyaudio.PyAudio()

stream = p.open(
    format= FORMAT,
    channels=CHANNELS,
    rate = RATE,
    input = True, 
    frames_per_buffer=FRAMES_PER_BUFFER
)

# Recording audio stream
app = FastAPI()

@app.get('/record_save')
async def recordandsave():
    try:
        audio_frames = record_audio(stream = stream,p=p, FRAMES_PER_BUFFER=FRAMES_PER_BUFFER,
                                                                RATE=RATE,seconds=10)
        save_audio(location_to_save=file_loc, p = p, CHANNELS=CHANNELS, FORMAT=FORMAT,
        RATE=RATE, FRAMES=audio_frames)
        return {"Adio saved at location":"locatoin"}
    except Exception as e:
        print("Someting bad happends")

# # saving audio stream in wave file extension
# save_audio(location_to_save=file_loc,p=p, CHANNELS=CHANNELS,FORMAT=FORMAT,
# RATE=RATE,FRAMES=audio_frames)

# Playing audio stream in wave file extension

@app.get("/play/")
def read_item(filename):
    try:
        if os.path.exists(filename):
            return play_audio(filename)
    except Exception as e:
        return {"Plese enter correct filepath"}

# Plot audio stream with matplotlib
#plotAudio(file_for_plot)
@app.get("/plot/")
async def plotaud(filename):
    try:
        if os.path.exists(filename):
            plotAudio(filename)
    except Exception as e:
        return {"Plese enter correct filepath"}


# if you want to reduce noise from the audio
@app.get('/reduce_noise')
async def reduceN(filename):
    try:
        if os.path.exists(filename):
            redc_noise(filename, noise_removed_file_name)
    except Exception as e:
        return {"someting bad happends"}

# 


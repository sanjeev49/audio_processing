import wave 
from pygame import mixer
import logging
import os 
import sys
from audio_processing.exception import audioException

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def record_audio(stream,p, FRAMES_PER_BUFFER,RATE, seconds):
    try:
        frames = []
        print("Start recording")
        logging.info("Recording started")
        for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
            data = stream.read(FRAMES_PER_BUFFER)
            frames.append(data)
        print("End recording")
        logging.info(f"Recoded file for {seconds} seconds and ended")
        stream.close()
        stream.stop_stream()
        p.terminate()
        return frames
    except Exception as e:
        raise audioException(e, sys) from e


def save_audio(location_to_save:str,p,  CHANNELS, FORMAT, RATE, FRAMES):
    """
    this function will take the signal and save it the given location 
    return: None

    """
    try:
        obj = wave.open(location_to_save, "wb")
        obj.setnchannels(CHANNELS)
        obj.setsampwidth(p.get_sample_size(FORMAT))
        obj.setframerate(RATE)
        obj.writeframes(b"".join(FRAMES))
        obj.close()
        logging.info(f"Saved audio at location {location_to_save} ")
    except Exception as e:
        raise audioException(e, sys) from e 
  
def play_audio(filename):
    try:
        mixer.init()

        # Loading the song
        mixer.music.load(filename)

        # Setting the volume
        mixer.music.set_volume(0.7)

        # Start playing the song
        logging.info(f"Start playing {filename}")
        mixer.music.play()
        logging.info(f"Finished playing {filename}")
    except Exception as e:
        logging.info(f"Error playing {filename}")
        raise audioException(e, sys) from e 
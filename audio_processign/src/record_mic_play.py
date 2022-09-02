import wave 
from pygame import mixer

def record_audio(stream,p, FRAMES_PER_BUFFER,RATE, seconds):
    frames = []
    print("Start recording")
    for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)
    print("End recording")
    stream.close()
    stream.stop_stream()
    p.terminate()
    return frames


def save_audio(location_to_save:str,p,  CHANNELS, FORMAT, RATE, FRAMES):
    obj = wave.open(location_to_save, "wb")
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(RATE)
    obj.writeframes(b"".join(FRAMES))
    obj.close()



#define stream chunk   
def play_audio(filename):
    mixer.init()

    # Loading the song
    mixer.music.load(filename)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()
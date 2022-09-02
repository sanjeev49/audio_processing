import pyaudio
import wave 
from pygame import mixer

# FRAMES_PER_BUFFER = 3200
# FORMAT = pyaudio.paInt16
# CHANNELS = 1 
# RATE = 16000


# p = pyaudio.PyAudio()

# stream = p.open(
#     format= FORMAT,
#     channels=CHANNELS,
#     rate = RATE,
#     input = True, 
#     frames_per_buffer=FRAMES_PER_BUFFER
# )

# print("Start recording...")
# seconds = 5 
# frames = []
# for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
#     data = stream.read(FRAMES_PER_BUFFER)
#     frames.append(data)
# stream.close()

# stream.stop_stream()
# stream.close()
# p.terminate()

# obj = wave.open("new_output.wav", "rb")
# obj.setnchannels(CHANNELS)
# obj.setsampwidth(p.get_sample_size(FORMAT))
# obj.setframerate(RATE)
# obj.writeframes(b"".join(frames))
# obj.close()


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

    # infinite loop
    # while True:
        
    # 	print("Press 'p' to pause, 'r' to resume")
    # 	print("Press 'e' to exit the program")
    # 	query = input(" ")
        
    # 	if query == 'p':

    # 		# Pausing the music
    # 		mixer.music.pause()	
    # 	elif query == 'r':

    # 		# Resuming the music
    # 		mixer.music.unpause()
    # 	elif query == 'e':

    # 		# Stop the mixer
    # 		mixer.music.stop()
    # 		break


# 

# # Starting the mixer
# mixer.init()

# # Loading the song
# mixer.music.load("03-01-01-01-01-01-12.wav")

# # Setting the volume
# mixer.music.set_volume(0.7)

# # Start playing the song
# mixer.music.play()

# # infinite loop
# while True:
	
# 	print("Press 'p' to pause, 'r' to resume")
# 	print("Press 'e' to exit the program")
# 	query = input(" ")
	
# 	if query == 'p':

# 		# Pausing the music
# 		mixer.music.pause()	
# 	elif query == 'r':

# 		# Resuming the music
# 		mixer.music.unpause()
# 	elif query == 'e':

# 		# Stop the mixer
# 		mixer.music.stop()
# 		break


    
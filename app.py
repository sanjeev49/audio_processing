import wave 

# Audio signal parameters 

# -numbers of channels
# - sample width 
# - framerate/sample_rate: 44,100 Hz
#  - number of frames 
# - value of a frame 

# Load a file 

obj = wave.open("output.wav", "rb")

print("Number of channels", obj.getnchannels())

print("Sample width", obj.getsampwidth())

print("Frame rate", obj.getframerate())

print("number of frames", obj.getnframes())

print("parameters", obj.getparams())

t_audio = obj.getnframes()/ obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames)/2)
obj.close()

obj_new = wave.open("sanjeev_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)
obj_new.writeframes(frames)
obj_new.close()
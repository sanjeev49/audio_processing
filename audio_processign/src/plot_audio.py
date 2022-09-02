import wave 
import matplotlib.pyplot as plt 
import numpy as np 

# obj = wave.open("output.wav", "rb")

# sample_freq = obj.getframerate()
# n_samples =  obj.getnframes()
# signal_wave = obj.readframes(-1)

# obj.close()

# t_audio = n_samples/sample_freq

# print(t_audio)

# signal_array = np.frombuffer(signal_wave, dtype = np.int16)

# times = np.linspace(0, t_audio, num = n_samples)

# plt.figure(figsize=(15,5))
# plt.plot(times, signal_array)
# plt.title("Aduio signal ")
# plt.ylabel("Signal wave")
# plt.xlabel("time (s)")
# plt.xlim(0, t_audio)
# plt.show()

# function to plot the signal wave with matplotlib plotAudio
def plotAudio(filename):
        # this function is used to plot the signal wave with matplotlib plotAudio
        obj = wave.open("output.wav", "rb")

        sample_freq = obj.getframerate()
        n_samples =  obj.getnframes()
        signal_wave = obj.readframes(-1)
        obj.close()

        t_audio = n_samples/sample_freq

        signal_array = np.frombuffer(signal_wave, dtype = np.int16)

        times = np.linspace(0, t_audio, num = n_samples)
        plt.figure(figsize=(10,5))
        plt.plot(times, signal_array)
        plt.title("Aduio signal ")
        plt.ylabel("Signal wave")
        plt.xlabel("time (s)")
        plt.xlim(0, t_audio)
        plt.show()

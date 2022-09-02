from scipy.io import wavfile
import noisereduce as nr
# load data
# rate, data = wavfile.read("mywav.wav")
# # perform noise reduction
# reduced_noise = nr.reduce_noise(y=data, sr=rate)
# wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)

# obj = wave.open("output.wav", "rb")

# sample_freq = obj.getframerate()

def redc_noise(filename:str, loc_to_save_reduced_noise:str):
    rate, data = wavfile.read(filename)
    reduced_noise = nr.reduce_noise(y = data, sr = rate)
    wavfile.write(loc_to_save_reduced_noise, rate, reduced_noise)


from scipy.io import wavfile
import noisereduce as nr


def redc_noise(filename:str, loc_to_save_reduced_noise:str):
    rate, data = wavfile.read(filename)
    reduced_noise = nr.reduce_noise(y = data, sr = rate)
    wavfile.write(loc_to_save_reduced_noise, rate, reduced_noise)


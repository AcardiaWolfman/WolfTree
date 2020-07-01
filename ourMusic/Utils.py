#pip3 install --user numpy
#pip3 install --user simpleaudio
#pip3 install --user wave

import numpy as np
import simpleaudio as sa
import wave

def play(File):
    wave_read = wave.open(File, 'rb')
    frames = wave_read.getnframes()
    audio_data = wave_read.readframes(wave_read.getnframes())
    num_channels = wave_read.getnchannels()
    bytes_per_sample = wave_read.getsampwidth()
    sample_rate = wave_read.getframerate()
    print("num_channels")
    print(num_channels)
    print("bytes_per_sample")
    print(bytes_per_sample)
    print("sample_rate")
    print(sample_rate)
    wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
    play_obj = wave_obj.play()
    #play_obj.wait_done()
    input("teclea enter para detener")
    play_obj.stop()

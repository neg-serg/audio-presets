#!/usr/bin/env python
import numpy as np
from scipy.io import wavfile

sampleRate = 44100
t = np.linspace(0, 20, sampleRate * 10)  #  Produces a 5 second Audio-File
y = np.sin(440 * t)  #  Should have frequency of 440Hz
wavfile.write('Sine.wav', sampleRate, y)

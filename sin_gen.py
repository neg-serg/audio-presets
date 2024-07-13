#!/usr/bin/env python
import numpy
from scipy.io.wavfile import write
volume = 1
sample_rate = 48000
duration = 10
frequency = 1000
samples = (numpy.sin(2 * numpy.pi * numpy.arange(sample_rate * duration) * frequency / sample_rate)).astype(numpy.float32)
write('test.wav', sample_rate, samples)

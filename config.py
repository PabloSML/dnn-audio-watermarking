from utils import bwh

BATCH_SIZE = 64
FS = 16000
FC = 4000
SIGNAL_SHAPE = (512, 64, 2) 
MESSAGE_SHAPE = (16, 2, 512)
NUM_BITS = 512
COEFFICIENT = 15
BUTTERWORTH = bwh(n = 16, fc = FC, fs = FS, length = 25)
NOISE_STRENGHT = 0.009
NUM_SAMPLES = 1000
HOP_LENGTH = 511
STEP_SIZE = 32768 - 511
WINDOW_LENGTH = 1023
POOL_SIZE = 6
# import numpy as np
# import pandas as pd
from eeg_signal import EEG
from read_eeg import read_edf

eeg_signal, eeg_hdr = read_edf('Data/S001R01.edf')
eeg = EEG(eeg_signal, eeg_hdr)

test = ['1','2','5']
for i in enumerate(test):
    print(i[0])
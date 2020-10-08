import numpy as np
import pandas as pd


class EEG:
    def __init__(self, eeg_signal, eeg_header = None):
        self.signal = np.array(eeg_signal, dtype = np.double)
        self.header = pd.DataFrame(eeg_header)





if __name__ == '__main__':
    print('hi')
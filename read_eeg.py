from pyedflib import highlevel
import numpy as np
import pandas as pd


def read_edf(edf_file):
    signal, signal_headers, header = highlevel.read_edf(edf_file)
    return signal, signal_headers

def read_txt(txt_file):
    signal = np.loadtxt(txt_file, delimiter=',')
    return signal


if __name__ == '__main__':
    sigs, sig_headers = read_edf('Data/S001R01.edf')
    df = pd.DataFrame(sig_headers)
    print(sigs.shape, (sig_headers[0]['label']), type(sig_headers))
    x = (sig_headers[0]['label'])
    print(x)
    print(df.head())
    print(df['sample_rate'])
    print(sig_headers)

    new_signal = read_txt('Data/S00R01.txt')
    print(new_signal)
    print(type(new_signal))

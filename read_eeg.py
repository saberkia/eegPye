from pyedflib import highlevel
import numpy as np
import pandas as pd
import scipy.io
import pickle
import h5py


def read_edf(edf_file):
    signal, signal_headers, header = highlevel.read_edf(edf_file)
    return signal, signal_headers

def read_txt(txt_file):
    file = open(txt_file, mode='r')
    str_ = file.read()
    file.close()
    new_str = str_.translate({ord('\n'): None, ord(' '): None})
    signal_str = new_str.split(sep=',', maxsplit=-1)
    signal = np.zeros(len(signal_str))
    for index in enumerate(signal_str):
        signal[index[0]] = np.double(signal_str[index[0]])
    return signal

def read_csv(csv_file):
    signal = pd.read_csv(csv_file)
    return signal

def raed_mat(mat_file):
    signal = scipy.io.loadmat(mat_file)
    return signal

def read_pickle(pickle_file):
    with open(pickle_file, 'rb') as file:
        signal = pickle.load(file)
    return signal

def read_hdf5(hdf5_file):
    signal = h5py.File(hdf5_file, 'r')
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

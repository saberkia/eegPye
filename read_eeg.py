from pyedflib import highlevel
import numpy as np
import pandas as pd


def read_edf(edf_file):
    signal, signal_headers, header = highlevel.read_edf(edf_file)
    return signal, signal_headers

def read_txt(txt_file):
    file = open(txt_file, mode='r')
    str = file.read()
    file.close()
    str = str.translate({ord('\n'): None , ord(' '): None})
    signal_str = str.split(sep=',', maxsplit=-1)
    signal = np.zeros(len(signal_str))
    for index in enumerate(signal_str):
        signal[index[0]] = np.double(signal_str[index[0]])
    return signal
# TODO :
#       Addind Support for csv file
#       Addind Support for mat file
#       Addind Support for pickle file
#       Addind Support for hdf5 file

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
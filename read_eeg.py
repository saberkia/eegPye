from pyedflib import highlevel
import numpy as np
import pandas as pd


def read_edf(edf_signal):
    signals, signal_headers, header = highlevel.read_edf(edf_signal)
    # signals =
    return signals, signal_headers


if __name__ == '__main__':
    sigs, sig_headers = read_edf('Data/S001R01.edf')
    df = pd.DataFrame(sig_headers)
    print(sigs.shape, (sig_headers[0]['label']), type(sig_headers))
    x = (sig_headers[0]['label'])
    print(x)
    print(df.head())
    print(df['sample_rate'])
    print(sig_headers)

from pyedflib import highlevel
import numpy as np


def read_edf(edf_signal):
    signals, signal_headers, header = highlevel.read_edf(edf_signal)
    # signals =
    return signals, signal_headers, header


if __name__ == '__main__':
    sigs, sig_headers, hdr = read_edf('Data/S001R01.edf')
    print(sigs.shape, (sig_headers[0]['label']), type(hdr))
    x = (sig_headers[0]['label'])
    print(x)
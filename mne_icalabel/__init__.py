"""Automatic ICA labeling for MEG, EEG and iEEG data."""

# Authors: Adam Li <ali39@jhu.edu>
#          Jacob Feitelberg <>
#
# License: BSD (3-clause)

__version__ = '0.1dev0'

from .ica_features import rpsd, autocorr_fftw, topoplot
from .ica_label import eeg_features, ica_label
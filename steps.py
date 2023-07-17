#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import peakdet as pk
from phys2denoise.metrics import (
    heart_rate_variability,
    respiratory_variance,
    respiratory_variance_time,
)
from phys2denoise.metrics.utils import export_metric

# #################
#  Fair disclaimer
# #################

# By the time you are seeing this, there might have been updates in physiopy's libraries.
# Please check the latest versions of online tutorials to see how it changed.

# #######################################
#  Part 1: preprocess physiological data
# #######################################

# Read file
data = np.genfromtxt("sub-007_ses-05_task-rest_run-01_physio.tsv.gz")

# Find index of time 0
idx_0 = np.argmax(data[:, 0] >= 0)

# Extract respiratory belt channel and initialise the data
phys = pk.Physio(data[idx_0:, 1], fs=10000)

# First plot
pk.plot_physio(phys)
plt.show()

# Downsample the signal - we don't need more than 40 Hz with our MRI data sampling
ph = pk.operations.interpolate_physio(phys, 40.0, kind="linear")

# Apply a lowpass filter to remove the extreme high frequencies
ph = pk.operations.filter_physio(ph, 2, method="lowpass", order=7)

pk.plot_physio(ph)
plt.show()

# Initialise the automatic peak detection to find a peak not less than every ~ 1.5s
# We're using a low peak threshold because the signal is highly variable
# Still, this is a fast breathing period.
thr = 0.1
dist = 60  # 1.5 s * 40 Hz
ph = pk.operations.peakfind_physio(ph, thresh=thr, dist=dist)

# Manually edit peaks - yes, you do need to at least check them.
ph = pk.operations.edit_physio(ph)

# Check the file history
ph.history

# Export the file
pk.save_physio("sub-007_ses-05_task-rest_run-01_resp_peaks.phys", ph)


# Extract cardiac channel and initialise the data
phys = pk.Physio(data[idx_0:, 3], fs=10000)

# First plot
pk.plot_physio(phys)
plt.show()

# Downsample the signal - we don't need more than 40 Hz with our MRI data sampling
ph = pk.operations.interpolate_physio(phys, 40.0, kind="linear")

# Apply a lowpass filter to remove the extreme high frequencies
# This is specific to our application. Might not universally apply.
ph = pk.operations.filter_physio(ph, 2, method="lowpass", order=7)

pk.plot_physio(ph)
plt.show()

# Initialise the automatic peak detection to find a peak not less than every ~ 1s
# We're still using a low peak threshold because the signal is variable
thr = 0.3
dist = 40  # 1 s * 40 Hz
ph = pk.operations.peakfind_physio(ph, thresh=thr, dist=dist)

# Manually edit peaks - yes, you do need to at least check them.
ph = pk.operations.edit_physio(ph)
# {'add': [6150, 6320, 17096, 19494, 21235, 25708, 25746, 25792]}

# Check the file history
ph.history

# Export the file
pk.save_physio("sub-007_ses-05_task-rest_run-01_card_peaks.phys", ph)


# ######################################
#  Part 2: prepare physiological models
# ######################################

# Load the saved cardiac physiological file → allow pickle!!!
card = pk.load_physio(
    "sub-007_ses-05_task-rest_run-01_card_peaks.phys", allow_pickle=True
)

# Check the file
card
card.history

# Compute HRV
help(heart_rate_variability)
HRV = heart_rate_variability(card.data, card.peaks, card.fs)

# export HRV
export_metric(
    HRV, card.fs, tr=1.5, fileprefix="sub-007_ses-05_task-rest_run-01_HRV", ntp=400
)
plt.plot(HRV)
plt.show()


# Load the saved respiratory physiological file → allow pickle!!!
resp = pk.load_physio(
    "sub-007_ses-05_task-rest_run-01_resp_peaks.phys", allow_pickle=True
)

# Check the file
resp
resp.history

# Compute RVT
help(respiratory_variance_time)
RVT = respiratory_variance_time(
    resp.data, resp.peaks, resp.troughs, resp.fs, lags=(0, 4, 8, 12)
)

# export RV
export_metric(
    RVT,
    resp.fs,
    tr=1.5,
    fileprefix="sub-007_ses-05_task-rest_run-01_RVT",
    ntp=400,
    is_convolved=False,
    has_lags=True,
)
plt.plot(RVT)
plt.show()

# Compute RV
help(respiratory_variance)
RV = respiratory_variance(resp.data, resp.fs)

# export RV
export_metric(
    RV, resp.fs, tr=1.5, fileprefix="sub-007_ses-05_task-rest_run-01_RV", ntp=400
)
plt.plot(RV)
plt.show()

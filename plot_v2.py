import matplotlib.pyplot as plt
from os import path
import nmrplot as npl
import pandas as pd
import numpy as np
from matplotlib import transforms

'''Define parameters for users'''
file_locations = ["/Volumes/LaCie/Karolinska/NMR/DNP/221025_KI_duplex/10/",
                  "/Volumes/LaCie/Karolinska/NMR/DNP/221024_KI/14/",
                  "/Volumes/LaCie/Karolinska/NMR/DNP/221025_KI_duplex/1/"]
colors = ['red', "blue", 'green']           # Colors for 2D plots
pdata_name = [1, 1, 1, 1]

''' Parameters for 2D plotting '''
threshold = [3.5, 2, 3.5]
clev_factor = [1.1, 1.1, 1.1]
countour_levels = [20, 26, 32]
transparent = [0.6, 0.5, 0.5]

'''Plotting parameters for 1D on 2D'''
normalize = False                       # True if you want to normalize the 1D spectra (very slow)
color1d = "black"                       # Color for 1D
offset = 100                             # Y-axis offset
factor = 1                              # Factor for scaling the 1D spectrum
show_yaxis = True
'''Limits for the x-axis and y-axis'''
xaxis_limits = [155, 144]
yaxis_limits = [120, 110]

'''Do you want to save the figure?'''
savefigure = False
save_path = ""
dpi = 300

'''End of defining parameters by users'''

#######################################################
'''
Coding starts (do not touch)
'''


def load_1d(expno, pdata=1):
    pdata_path = path.join(expno, f"pdata/{pdata}/ascii-spec.txt")
    return pdata_path


def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i / inch for i in tupl[0])
    else:
        return tuple(i / inch for i in tupl)


def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr



spectra = []
ndim = []
for i in range(len(file_locations)):
    spectrum = npl.Spectrum(file_locations[i], pdata=pdata_name[i])
    ndim.append(spectrum.ndim)
    spectra.append(spectrum)

fig, ax = plt.subplots()
for i in range(len(spectra)):

    if ndim[i] > 1:
        spectra[i].threshold = threshold[i]
        xdata, ydata, clevs, extent, cmap, xlabel, ylabel = spectra[i].plot_multi(nlevs=countour_levels[i],
                                                                                  cmap=colors[i],
                                                                                  factor=clev_factor[i])
        ax.contour(*xdata, ydata, clevs, extent=extent, cmap=cmap, alpha=transparent[i])
    if ndim[i] == 1:
        xdata1d, ydata1d = spectra[i].plot_multi()
        ax1 = ax.twinx()
        ax1.set_ylim(-10, 50 + max(ydata1d))
        ax1.plot(xdata1d, offset+factor*ydata1d, color=color1d)
        if show_yaxis == False:
            ax1.set_yticks([])
        else:
            ax1.tick_params(labelsize=14)
            ax1.set_ylabel("Intensity (AU)", fontsize=14)
            plt.subplots_adjust(right=0.85)

    plt.xlim(xaxis_limits[0], xaxis_limits[1])
    ax.set_ylim(yaxis_limits[0], yaxis_limits[1])
    ax.set_xlabel(f"{xlabel} (ppm)", fontsize=14)
    ax.set_ylabel(f"{ylabel} (ppm)", fontsize=14)
    ax.tick_params(labelsize=14)
    plt.subplots_adjust(left=0.15)
    plt.subplots_adjust(bottom=0.15)
plt.show()

if savefigure:
    plt.savefig(save_path, dpi=dpi)

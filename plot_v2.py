import matplotlib.pyplot as plt
from os import path
import nmrplot as npl
import pandas as pd
import numpy as np
from matplotlib import transforms


'''Define parameters for users'''
file_locations = ["/Volumes/LaCie/Karolinska/NMR/DNP/221025_KI_duplex/10/",
                  "/Volumes/LaCie/Karolinska/NMR/DNP/221024_KI/14/"]
colors = ['red', "blue", 'green']
threshold = [3.5, 2, 3.5]
clev_factor = [1.1, 1.1, 1.1]
countour_levels = [20, 26, 32]
pdata_name_2d = [1, 1, 1]
transparent = [0.6, 0.5, 0.5]

xaxis_limits = [155, 144]
yaxis_limits = [120, 110]

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
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)


spectra = []
for i in range(len(file_locations)):
    spectrum = npl.Spectrum(file_locations[i], pdata=pdata_name_2d[i])
    spectra.append(spectrum)

fig, ax = plt.subplots()
for i in range(len(spectra)):
    spectra[i].threshold = threshold[i]
    xdata, ydata, clevs, extent, cmap, xlabel, ylabel = spectra[i].plot_multi(nlevs=countour_levels[i], cmap=colors[i],
                                                              factor=clev_factor[i])
    plt.contour(*xdata, ydata, clevs, extent=extent, cmap=cmap, alpha=transparent[i])
    plt.xlim(xaxis_limits[0], xaxis_limits[1])
    plt.ylim(yaxis_limits[0], yaxis_limits[1])
    plt.xlabel(f"{xlabel} (ppm)", fontsize=14)
    plt.ylabel(f"{ylabel} (ppm)", fontsize=14)
    plt.tick_params(labelsize=14)
    plt.subplots_adjust(left=0.15)
    plt.subplots_adjust(bottom=0.15)
plt.show()

if savefigure:
    plt.savefig(save_path, dpi=dpi)


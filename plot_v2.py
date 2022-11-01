import matplotlib.pyplot as plt
from os import path
import nmrplot as npl
import pandas as pd
import numpy as np
from matplotlib import transforms


file_locations = ["/Volumes/LaCie/Karolinska/NMR/DNP/221025_KI_duplex/10/",
                  "/Volumes/LaCie/Karolinska/NMR/DNP/221025_KI_duplex/11/"]
colors = ['red', "blue"]
threshold = [3.5, 3.5]
clev_factor = [1.1, 1.1]
countour_levels = [32, 32]
pdata_name_2d = [1, 1]
transparent = [0.5, 1]


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

fig, ax = plt.subplots(figsize=cm2inch(6, 12))
for i in range(len(spectra)):
    spectra[i].threshold = threshold[i]
    xdata, ydata, clevs, extent, cmap = spectra[i].plot_multi(nlevs=countour_levels[i], cmap=colors[i],
                                                              factor=clev_factor[i])
    plt.contour(*xdata, ydata, clevs, extent=extent, cmap=cmap, alpha=transparent[i])
    plt.xlim(150.3, 146)
    plt.ylim(95, 35)
    plt.subplots_adjust(left=0.2)
    plt.subplots_adjust(top=0.95)
plt.show()


# plt.savefig("/Users/rubindasgupta/Desktop/test1.png", dpi=300)


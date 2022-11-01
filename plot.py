import matplotlib.pyplot as plt
from os import path
import nmrplot as npl
import pandas as pd
from matplotlib import transforms

file = "/Volumes/LaCie/Karolinska/NMR/DNP/221025_KI_duplex/10/"
file1 = "/Volumes/LaCie/Karolinska/NMR/DNP/20221014_DNP_Bcl2_miR34a_298k/7/"

file1d = "/Volumes/LaCie/Karolinska/NMR/DNP/20221014_DNP_Bcl2_miR34a_298k/7/"


def load_1d(expno, pdata=1):
    pdata_path = path.join(expno, f"pdata/{pdata}/ascii-spec.txt")
    return pdata_path

def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)


data1 = pd.read_table(load_1d(file1d, pdata=1233),
                       sep=',', names=["no", "intensity", "skip", "ppm"])
data2 = pd.read_table(load_1d(file1d, pdata=583),
                       sep=',', names=["no", "intensity", "skip", "ppm"])
data3 = pd.read_table(load_1d(file1d, pdata=734),
                       sep=',', names=["no", "intensity", "skip", "ppm"])
data4 = pd.read_table(load_1d(file1d, pdata=827),
                       sep=',', names=["no", "intensity", "skip", "ppm"])
data5 = pd.read_table(load_1d(file1d, pdata=966),
                       sep=',', names=["no", "intensity", "skip", "ppm"])
data6 = pd.read_table(load_1d(file1d, pdata=1185),
                       sep=',', names=["no", "intensity", "skip", "ppm"])
data7 = pd.read_table(load_1d(file1d, pdata=1308),
                       sep=',', names=["no", "intensity", "skip", "ppm"])

spectrum = npl.Spectrum(file)
spectrum1 = npl.Spectrum(file1)
spectrum.threshold = 3.5
spectrum1.threshold = 3.5


base = plt.gca().transData
rot = transforms.Affine2D().rotate_deg(90)

xdata, ydata, clevs, extent, cmap = spectrum.plot_multi(nlevs=20)
xdata1, ydata1, clevs1, extent1, cmap1 = spectrum1.plot_multi(nlevs=32, cmap='red')
fig, ax = plt.subplots(figsize=cm2inch(6, 12))
ax.contour(*xdata, ydata, clevs, extent=extent, cmap=cmap)
ax.set_xlim(150.3, 146)
ax.set_ylim(95, 35)
ax1 = ax.twinx()
ax1.plot(data1["ppm"], data1["intensity"], color="red")
ax1.plot(data2["ppm"], data2["intensity"], color="red")
ax1.plot(data3["ppm"], data3["intensity"], color="red")
ax1.plot(data4["ppm"], data4["intensity"], color="red")
ax1.plot(data5["ppm"], data5["intensity"], color="red")
ax1.plot(data6["ppm"], data6["intensity"], color="red")
ax1.plot(data7["ppm"], data7["intensity"], color="red")
ax1.set_ylim(-25e4, 5e4 + max(data1["intensity"]))
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(top=0.95)
ax1.set_yticks([])
plt.savefig("/Users/rubindasgupta/Desktop/test1.png", dpi=300)
plt.show()


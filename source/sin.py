import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.major.width"] = 1.0
plt.rcParams["ytick.major.width"] = 1.0
plt.rcParams["xtick.minor.width"] = 0.5
plt.rcParams["xtick.major.size"] = 3
plt.rcParams["ytick.major.size"] = 3
plt.rcParams["xtick.minor.size"] = 2
plt.rcParams["font.size"] = 20
# plt.rcParams["axes.titlesize"] = 24
plt.rcParams["axes.labelsize"] = 20
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams["lines.linewidth"] = 2.0

def sin(x):
    return np.sin(16 * x)

if __name__ == "__main__":
    x = np.linspace(0, 2 * np.pi, 1000)
    y = sin(x)

    plt.plot(x, y)
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\sin(16x)$")
    plt.xticks([0, 0.5 * np.pi, np.pi, 1.5 * np.pi, 2 * np.pi], [0, r"$\pi/2$", r"$\pi$", r"$3/2 \pi$", r"$2\pi$"])
    plt.grid()
    plt.savefig('sin'+'.pdf', format = 'pdf', dpi = 300, bbox_inches = 'tight')
    plt.savefig('sin'+'.png', format = 'png', dpi = 300, bbox_inches = 'tight')
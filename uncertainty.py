import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def fit_func(alpha, ph, A, B):
    return A*np.cos(2*np.pi*T*T*alpha + ph) + B

k = 4*np.pi/780e-9
T = 5010e-6

file_path = r'testdata\T_5010_us.csv' 
data = np.genfromtxt(file_path, delimiter=',', dtype=None, skip_header=1)

alpha = data[:,0]
ampl = data[:,1]

alpha = alpha[402:603]
ampl = ampl[402:603]

fig, ax = plt.subplots(figsize=(6,5))

ax.scatter(alpha, ampl, color="b")

initial_guess = [0, 0.03, 0.31]
bounds = ([-np.pi, -1, -1], [np.pi, 1, 1])
popt, pcov = curve_fit(fit_func, alpha, ampl, p0=initial_guess, bounds=bounds)

alpha_pic = np.linspace(alpha[0], alpha[200], 1000)
ax.plot(alpha_pic, fit_func(alpha_pic, *popt), color="r")


perr = np.sqrt(np.diag(pcov))
dph = perr[1]  # Стандартная ошибка для фазы
ph = popt[1]

print("popt", popt)
print("ph=", ph)
print("dph=", dph)
print("dg=", dph/k/T**2*1e8, "uGal")
print("Dg=", 2*np.pi/T**2/k*1e2, "Gal")


g = ph/k/T**2
print("g=", g)

g_m = [9.16020078887115e-5, 9.217528280349871e-5, 9.325298907078002e-5]
dg = np.std(g_m)

plt.show()
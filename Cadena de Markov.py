import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
#
r = 0.06  # Tasa de Interés
beta = 0.9  # Paráemtros dados por Utility Theore
gamma = 0.5
#
N = 20  # Número de Etapas
X = np.linspace(0.001, 2, 100)  # Espacio de Estados (Expresando en millones de pesos)
valFUNCTs = np.zeros((N, len(X)))  # Funciones de Valor.
OPTpolicy = np.zeros((N-1,len(X)))  # Políticas Optimas.


valFUNCTs[-1] = beta ** N * X ** (1-gamma)
#
for k in range(N - 1):
    for x in range(len(X)):
        A = np.linspace(0.00001, X[x])

        cs = CubicSpline(X, valFUNCTs[N-k-1])
        vcs = np.array([cs(t) for t in (1+r)*(X[x] - A)])
        valFUNCTs[N - k - 2,x]  = np.max((beta** (N-k)) * (A ** (1-gamma)) + vcs)
        a = list((beta** (N-k)) * (A ** (1-gamma)) + vcs).index(valFUNCTs[N-k - 2,x])
        OPTpolicy[N - k - 2, x] = A[a]


print(OPTpolicy.shape)
plt.plot(X, OPTpolicy[0])
plt.plot(X, OPTpolicy[N-3])
plt.plot(X, OPTpolicy[N-2])
plt.show()

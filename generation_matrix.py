import numpy as np

# An array of 30 probabilities, each between 0.00 and 0.50 to represent the
# probability of mutation for each gene
pbpA = np.float_(1.9e-2)
pbpB = np.float_(1.6e-1)
pbpC = np.float_(1.4e-2)

fnr = np.float_(1.4e-1)
nap = np.float_(1.3e-2)
nar = np.float_(3.2e-2)

mreB = np.float_(1.17e-2)
mrdA = np.float_(1.96e-2)
mrdB = np.float_(9.14e-3)

rpsL = np.float_(4.13e-3)
rpsG = np.float_(2.01e-3)
rrn = np.float_(1.50e-2)

mdtABC = np.float_(3.0e-2)
mdtEF = np.float_(2.5e-2)
emrAB = np.float_(2.7e-1)
emrKY = np.float_(2.0e-2)

ompF = np.float_(1.1e-2)
ompC = np.float_(1.2e-2)
ompR = np.float_(1.2e-1)
envZ = np.float_(1.5e-1)

mutS = np.float_(2.4e-3)
mutL = np.float_(1.9e-3)
mutH = np.float_(7.5e-4)
uvrA = np.float_(2.7e-3)
uvrB = np.float_(2.4e-3)
uvrC = np.float_(9.0e-4)
recA = np.float_(1.1e-4)

tra = np.float_(7.0e-3)
pil = np.float_(1.0e-2)
oriT = np.float_(1.0e-4)

mutation_probabilities = [
    pbpA, pbpB, pbpC, fnr, nap, nar, mreB, mrdA, mrdB, rpsL, rpsG, rrn, mdtABC,
    mdtEF, emrAB, emrKY, ompF, ompC, ompR, envZ, mutS, mutL, mutH, uvrA, uvrB,
    uvrC, recA, tra, pil, oriT
]

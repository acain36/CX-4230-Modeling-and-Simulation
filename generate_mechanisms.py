import numpy as np

# Input is a txt file
def GenMechanismsFromFile(fileName):
    bacteria = {} # Dict for bacteria types
    i = 0

    #  Populate bact dict with indices and associated gene vectors
    with open(fileName, 'r') as file:
        for line in file:
            gene = [int(i) for i in line.split(', ')]
            bacteria.update({i: gene})
            i += 1

    # Iterate through dict and select values at indices in gene vector which describes the number of genes for specific bact features
    # E.G. [2, 1, 1, 1, 1, 1, 1, 1] indicates 2 genes for Cell Wall features, etc.
    for index in bacteria:
        cw = bacteria[index][0]
        ri = bacteria[index][1] + cw
        pbp = bacteria[index][2] + ri
        ep = bacteria[index][3] + pbp
        dna = bacteria[index][4] + ep
        pm = bacteria[index][5] + dna
        iv = bacteria[index][6] + pm
        por = bacteria[index][7] + iv

        CELL_WALL = np.s_[0:cw]
        RIBOSOMES = np.s_[cw:ri]
        PBP = np.s_[ri:pbp]
        EFFLUX_PUMPS = np.s_[pbp:ep]
        DNA = np.s_[ep:dna]
        PLASMA_MEMBRANE = np.s_[dna:pm]
        INACTIVATION = np.s_[pm:iv]
        PORIN = np.s_[iv:por]

        MECHANISMS = [CELL_WALL, RIBOSOMES, PBP, EFFLUX_PUMPS, DNA,
                      PLASMA_MEMBRANE, INACTIVATION, PORIN]
        bacteria.update({index: MECHANISMS}) # Update bact dict so that it contains the slices for specific features in the bact

    return bacteria

# Same as GenMechanismsFromFile but iterates over a single matrix
def GenMechanismsFromMatrix(bacteria):
        cw = bacteria[0]
        ri = bacteria[1] + cw
        pbp = bacteria[2] + ri
        ep = bacteria[3] + pbp
        dna = bacteria[4] + ep
        pm = bacteria[5] + dna
        iv = bacteria[6] + pm
        por = bacteria[7] + iv

        CELL_WALL = np.s_[0:cw]
        RIBOSOMES = np.s_[cw:ri]
        PBP = np.s_[ri:pbp]
        EFFLUX_PUMPS = np.s_[pbp:ep]
        DNA = np.s_[ep:dna]
        PLASMA_MEMBRANE = np.s_[dna:pm]
        INACTIVATION = np.s_[pm:iv]
        PORIN = np.s_[iv:por]

        MECHANISMS = [CELL_WALL, RIBOSOMES, PBP, EFFLUX_PUMPS, DNA,
                      PLASMA_MEMBRANE, INACTIVATION, PORIN]
        
        return MECHANISMS
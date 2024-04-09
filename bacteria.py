import numpy as np
from generation_matrix import mutation_probabilities

# Default bacteria parameters
DEFAULT_GEN_TIME = 15
# Natural log of 2, for converting generation time to division probability
LN_2 = np.log(2)

class Bacteria:
    def __init__(self, genes, gen_time=DEFAULT_GEN_TIME):
        self.is_alive = True
        self.genes = genes
        self.phenotype = self.determine_phenotypes(genes)
        self.division_prob = LN_2 / gen_time
        self.can_divide = False

    def age(self, rng):
        self.can_divide = rng.random() < self.division_prob

    def die(self):
        self.is_alive = False

    def attempt_division(self, rng, stats):
        offspring = None
        if self.can_divide:
            stats.attempted_divisions += 1
            new_genes = self.mutate_genome(rng, stats)
            offspring = Bacteria(new_genes)
        return offspring

    def mutate_genome(self, rng, stats):
        # Initialize the offspring gene state
        offspring_genes = self.genes.copy()

        # Iterate over each gene in the offspring genome
        for i in range(len(offspring_genes)):
            if rng.random() < mutation_probabilities[i]:
                stats.mutation_count += 1
                # Flip the gene bit
                offspring_genes[i] = 1 if offspring_genes[i] == 0 else 0
        return offspring_genes


    def determine_phenotypes(self, initial_state):
        # Cell Wall: genes initial_state[0:3] = (pbpA, pbpB, pbpC)
        # phenotypes: (LF - Long Filament, SD - Severe Shape Defect, LFSD - Long Filament and Severe Shape Defect)
        cw_genes = initial_state[0:3]
        cw_phens = [0 for _ in range(3)]

        if (cw_genes[0] == 1 and cw_genes[1] == 1) or (cw_genes[1] == 1 and cw_genes[2] == 1):
            cw_phens[2] = 1
        elif cw_genes[0] == 1 and cw_genes[1] == 0 and cw_genes[2] == 1:
            cw_phens[1] = 1
        elif cw_genes[0] == 0 and cw_genes[1] == 1 and cw_genes[2] == 0:
            cw_phens[0] = 1

        # Aerobic/Anaerobic Respiration: genes initial_state[3:6] = (fnr, nap, nar)
        # phenotypes: (DAN - Defective Anaerobic Growth, DARN - Defective Aerobic and Anaerobic, DARNN - Defective Aerobic and Anaerobic and No Nitrate Use)
        resp_genes = initial_state[3:6]
        resp_phens = [0 for _ in range(3)]

        if (resp_genes[0] == 1 and resp_genes[1] == 1) or (resp_genes[0] == 1 and resp_genes[2] == 1):
            resp_phens[2] = 1
        elif resp_genes[0] == 0 and resp_genes[1] == 1:
            resp_phens[1] = 1
        elif (resp_genes[0] == 0 and resp_genes[1] == 0 and resp_genes[2] == 1) or (resp_genes[0] == 1 and resp_genes[1] == 0 and resp_genes[2] == 0):
            resp_phens[0] = 1

        # Cocci vs Bacilli: genes initial_state[6:9] = (mreB, mrdA, mrdB)
        # phenotypes: (CC - Cocci Cells, CM - Severe Cocci Morphology, CCEF - Cocci Cells and Elongated Filamentation)
        cb_genes = initial_state[6:9]
        cb_phens = [0 for _ in range(3)]

        if (cb_genes[0] == 0 and cb_genes[1] == 1 and cb_genes[2] == 1) or (cb_genes[0] == 1 and cb_genes[1] == 0 and cb_genes[2] == 1):
            cb_phens[2] = 1
        elif cb_genes[0] == 1 and cb_genes[1] == 1:
            cb_phens[1] = 1
        elif (cb_genes[2] == 1 and cb_genes[1] == 0) or (cb_genes[1] == 1 and cb_genes[0] == 0) or (cb_genes[0] == 1 and cb_genes[2] == 0):
            cb_phens[0] = 1

        # Ribosomes: genes initial_state[9:12] = (rpsL, rpsG, rrn)
        # phenotypes: (IP - Impaired Protein Synthesis, RR - Reduced Ribosomes, IPRR - Reduced Protein Synthesis and Reduced Ribosome Stability and Reduced Ribosome Number)
        rib_genes = initial_state[9:12]
        rib_phens = [0 for _ in range(3)]

        if rib_genes[0] == 1 and rib_genes[2] == 1 and rib_genes[1] == 1:
            rib_phens[2] = 1
        elif (rib_genes[2] == 1 and rib_genes[0] == 0) or (cb_genes[2] == 1 and cb_genes[1] == 0):
            rib_phens[1] = 1
        elif (rib_genes[2] == 0 and rib_genes[1] == 1) or (cb_genes[0] == 1 and cb_genes[1] == 0):
            rib_phens[0] = 1

        # Efflux Pumps: genes initial_state[12:16] = (mdtABC, mdtAB, emrAB, emrKY)
        # phenotypes: (RMFS - Reduces MFS, RMFS/SMR - Reduced MFS/SMR, LMFS/LMF - Loss MFS/Loss MF, LMFS - Loss MFS, LMF - Loss MF, LSMR - Loss SMR, LMF/LSMR - Loss MF/Loss SMR)
        ef_genes = initial_state[12:16]
        ef_phens = [0 for _ in range(7)]

        if ef_genes[1] == 1 and ef_genes[3] == 1 and ef_genes[0] == 0 and ef_genes[2] == 0:
            ef_phens[6] = 1
        elif ef_genes[1] == 1 and ef_genes[3] == 0 and ef_genes[0] == 0 and ef_genes[2] == 0:
            ef_phens[5] = 1
        elif ef_genes[3] == 1 and ef_genes[0] == 0 and ef_genes[1] == 0 and ef_genes[2] == 0:
            ef_phens[4] = 1
        elif (ef_genes[2] == 1 and ef_genes[1] == 0) or (ef_genes[2] == 1 and ef_genes[3] == 0) or (ef_genes[2] == 1 and ef_genes[0] == 0):
            ef_phens[3] = 1
        elif (ef_genes[2] == 1 and ef_genes[3] == 1 and ef_genes[0] == 0) or (ef_genes[2] == 1 and ef_genes[3] == 1 and ef_genes[1] == 0) or (ef_genes[0] == 1 and ef_genes[1] == 1 and ef_genes[3] == 1 and ef_genes[2] == 0):
            ef_phens[2] = 1
        elif (ef_genes[0] == 1 and ef_genes[1] == 1 and ef_genes[2] == 0) or (ef_genes[0] == 1 and ef_genes[1] == 1 and ef_genes[3] == 0):
            ef_phens[1] = 1
        elif (ef_genes[0] == 1 and ef_genes[1] == 0) or (ef_genes[0] == 1 and ef_genes[2] == 0) or (ef_genes[0] == 1 and ef_genes[3] == 0):
            ef_phens[0] = 1

        # Porins: genes initial_state[16:20] = (ompF, ompC, ompR, envZ)
        # phenotypes: (ROF - Reduced OmpF, ROP - Reduced OmpC, AOC/F - Altered OmpF and Reduced OmpC, ROF/C - Reduced OmpF and Reduced OmpC, ROF/AOC - Reduced OmpF and Altered OmpC, ROC/AOF - Altered OmpF and Reduced OmpC)
        porins_genes = initial_state[16:20]
        porins_phens = [0 for _ in range(6)]

        if (porins_genes[0] == 1 and porins_genes[1] == 1) or (porins_genes[0] == 1 and porins_genes[2] == 1) or (porins_genes[0] == 1 and porins_genes[3] == 1):
            porins_phens[5] = 1
        elif (porins_genes[1] == 1 and porins_genes[2] == 1) or (porins_genes[1] == 1 and porins_genes[3] == 1):
            porins_phens[4] = 1
        elif porins_genes[0] == 1 and porins_genes[1] == 0 and porins_genes[2] == 0 and porins_genes[3] == 0:
            porins_phens[3] = 1
        elif porins_genes[0] == 0 and porins_genes[1] == 1 and porins_genes[2] == 0 and porins_genes[3] == 0:
            porins_phens[2] = 1
        elif porins_genes[0] == 1 and porins_genes[1] == 1 and porins_genes[2] == 0 and porins_genes[3] == 0:
            porins_phens[1] = 1
        elif porins_genes[0] == 0 and porins_genes[1] == 1 and porins_genes[2] == 1 and porins_genes[3] == 0:
            porins_phens[0] = 1

        # DNA Repair: genes initial_state[20:27] = (mutS, mutL, mutH, uvrA, uvrB, uvrC, recA)
        # phenotypes: (DM - defective mismatch repair, DNER - defective nucleotide excision repair, DR - defective recombination, DNER/DM - defective nucleotide excision repair and mismatch repair, DNER/DR - defective nucleotide excision repair and recombination, DNER/DM/DR - defective nucleotide excision repair, mismatch repair, and recombination)
        dna_rep_genes = initial_state[20:27]
        dna_phens = [0 for _ in range(6)]

        if (dna_rep_genes[0] == 1 and dna_rep_genes[1] == 1 and dna_rep_genes[2] == 1) or (dna_rep_genes[3] == 1 and dna_rep_genes[4] == 1 and dna_rep_genes[5] == 1):
            dna_phens[5] = 1
        elif (dna_rep_genes[0] == 1 and dna_rep_genes[1] == 1) or (dna_rep_genes[0] == 1 and dna_rep_genes[2] == 1) or (dna_rep_genes[1] == 1 and dna_rep_genes[2] == 1):
            dna_phens[4] = 1
        elif (dna_rep_genes[3] == 1 and dna_rep_genes[4] == 1) or (dna_rep_genes[3] == 1 and dna_rep_genes[5] == 1) or (dna_rep_genes[4] == 1 and dna_rep_genes[5] == 1):
            dna_phens[3] = 1
        elif (dna_rep_genes[0] == 1 and dna_rep_genes[1] == 0 and dna_rep_genes[2] == 0) or (dna_rep_genes[0] == 0 and dna_rep_genes[1] == 1 and dna_rep_genes[2] == 0) or (dna_rep_genes[0] == 0 and dna_rep_genes[1] == 0 and dna_rep_genes[2] == 1):
            dna_phens[2] = 1
        elif (dna_rep_genes[3] == 1 and dna_rep_genes[4] == 0 and dna_rep_genes[5] == 0) or (dna_rep_genes[3] == 0 and dna_rep_genes[4] == 1 and dna_rep_genes[5] == 0) or (dna_rep_genes[3] == 0 and dna_rep_genes[4] == 0 and dna_rep_genes[5] == 1):
            dna_phens[1] = 1
        elif (dna_rep_genes[0] == 1 and dna_rep_genes[1] == 1 and dna_rep_genes[2] == 0) or (dna_rep_genes[0] == 1 and dna_rep_genes[1] == 0 and dna_rep_genes[2] == 1) or (dna_rep_genes[0] == 0 and dna_rep_genes[1] == 1 and dna_rep_genes[2] == 1):
            dna_phens[0] = 1

        # Plasmids: genes initial_state[27:30] = (tra, pil, oriT)
        # phenotypes: (DT - defective plasmid conjugal transfer, NP - non-piliated defective recipient ability, NM - plasmid non-mobilizable, DT/NM - defective plasmid conjugal transfer and plasmid non-mobilizable, NP/NM - non-piliated defective recipient ability and plasmid non-mobilizable)
        plas_genes = initial_state[27:30]
        plas_phens = [0 for _ in range(5)]

        if plas_genes[0] == 1 and plas_genes[1] == 1 and plas_genes[2] == 1:
            plas_phens[4] = 1
        elif plas_genes[0] == 1 and plas_genes[1] == 1:
            plas_phens[3] = 1
        elif plas_genes[2] == 1:
            plas_phens[2] = 1
        elif plas_genes[0] == 1 and plas_genes[1] == 0 and plas_genes[2] == 0:
            plas_phens[1] = 1
        elif plas_genes[1] == 1 and plas_genes[0] == 0 and plas_genes[2] == 0:
            plas_phens[0] = 1

        phenotype_list = []
        phenotype_list += cw_phens
        phenotype_list += resp_phens
        phenotype_list += cb_phens
        phenotype_list += rib_phens
        phenotype_list += ef_phens
        phenotype_list += porins_phens
        phenotype_list += dna_phens
        phenotype_list += plas_phens

        return phenotype_list

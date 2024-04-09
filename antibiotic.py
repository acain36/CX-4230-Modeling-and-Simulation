from bacteria import Bacteria
from generate_mechanisms import GenMechanismsFromMatrix
from state_recorder import IterationStats

import random
import numpy as np
from numpy.random import Generator

# Default antibiotic parameters
DEFAULT_NAME = "Cefazolin"
DEFAULT_MECH = [0, 0, 1] + [random.randint(0, 1) for _ in range(33)]
DEFAULT_HALF_LIFE = 1.8
PHENOTYPE_SLICES = GenMechanismsFromMatrix([3, 3, 3, 3, 7, 6, 6, 5])
DEFAULT_PROB = [1, 1, 1] + [random.uniform(0.2, 0.5) for _ in range(33)]
# Natural log of 2, for converting half-life to decay probability
LN_2 = np.log(2)

class Antibiotic:
    def __init__(self, name=DEFAULT_NAME, mechanisms=DEFAULT_MECH,
                 half_life=DEFAULT_HALF_LIFE, slices=PHENOTYPE_SLICES,
                 probabilities=DEFAULT_PROB):
        self.is_active = True
        self.name = name
        self.mechanisms = mechanisms
        self.decay_prob = LN_2 / half_life
        self.slices = slices
        self.probabilities = probabilities

    def attempt_decay(self, rng: Generator, stats: IterationStats):
        if rng.random() < self.decay_prob:
            stats.antibiotic_decays += 1
            self.is_active = False

    def target(self, bacteria: Bacteria, stats: IterationStats):
        mechanisms = self.mechanisms
        genes = bacteria.phenotype
        is_valid_target = False

        # Probabilistic determination of bacterial death
        for i in self.slices:
            if np.sum(np.bitwise_and(mechanisms[i], genes[i])) != 0:
                prob_death = np.multiply(mechanisms[i], genes[i])
                prob_death = np.sum(
                    np.multiply(prob_death, self.probabilities[i])
                )

                if random.random() <= prob_death:
                    is_valid_target = True

        if is_valid_target:
            stats.lethal_collision_count += 1
            self.is_active = False
            bacteria.die()

    def testing(self, bacteria: Bacteria):
        mechanisms = self.mechanisms
        genes = bacteria.phenotype
        is_valid_target = False

        # Probabilistic determination of bacterial death
        for i in self.slices:
            if np.sum(np.bitwise_and(mechanisms[i], genes[i])) != 0:
                prob_death = np.multiply(mechanisms[i], genes[i])
                prob_death = np.sum(
                    np.multiply(prob_death, self.probabilities[i])
                )

                if random.random() <= prob_death:
                    is_valid_target = True

        if is_valid_target:
            self.is_active = False
            bacteria.die()

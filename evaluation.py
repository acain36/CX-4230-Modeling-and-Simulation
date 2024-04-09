import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.patches import Patch
from pathlib import Path

DIRECTORY = 'output'
TESTS = ['dose', 'pop', 'interval']
DOSE_CONC = [0.05, 0.10, 0.15, 0.20, 0.25]
STARTING_POP = [1] + [i for i in range(10, 101, 10)]
DOSE_INTERVALS = [4, 6, 8, 12, 24, 48]
TIME_STEPS = 24 * 14

class Evaluation:
    def __init__(self, test: str):
        self.test = test
        if test == 'dose':
            self.label = DOSE_CONC
            self.title = "Dose Concentration"
        elif test == 'pop':
            self.label = STARTING_POP
            self.title = "Bacteria Starting Population"
        elif test == 'interval':
            self.label = DOSE_INTERVALS
            self.title = "Dose Intervals"
        else:
            self.label = None
            self.title = None
        self.stat_files = list(Path(DIRECTORY).glob(f'{test}*.pkl'))
        self.grid_files = list(Path(DIRECTORY).glob(f'{test}*.npy'))
        self.time_steps = list(range(TIME_STEPS))
        self.init_grids()
        self.init_stats()

    def init_stats(self) -> None:
        bact_pop = []
        antibiotic_pop = []
        collision_count = []
        lethal_collision_count = []
        mutation_count = []
        attempted_divisions = []
        successful_divisions = []
        antibiotic_decays = []
        mutation_count = []

        # Iterate over the IterationStats for the given test
        for file in self.stat_files:
            stat = np.load(file, allow_pickle=True)
            # Iterate over length of stats - 1 due to last datapoint in
            # stats being 0
            for i in range(len(stat) - 1):
                bact_pop.append(stat[i].bacteria_count)
                antibiotic_pop.append(stat[i].antibiotic_count)
                collision_count.append(stat[i].collision_count)
                lethal_collision_count.append(stat[i].lethal_collision_count)
                mutation_count.append(stat[i].mutation_count)
                attempted_divisions.append(stat[i].attempted_divisions)
                successful_divisions.append(stat[i].successful_divisions)
                antibiotic_decays.append(stat[i].antibiotic_decays)

        # Reshape arrays to correspond to varrying stats in the tests
        self.bact_pops = np.reshape(bact_pop, (-1, TIME_STEPS))
        self.antibiotic_pops = np.reshape(antibiotic_pop, (-1, TIME_STEPS))
        self.collision_counts = np.reshape(collision_count, (-1, TIME_STEPS))
        self.lethal_collision_counts = np.reshape(lethal_collision_count, (-1, TIME_STEPS))
        self.mutation_count = np.reshape(mutation_count, (-1, TIME_STEPS))
        self.attempted_divisions = np.reshape(attempted_divisions, (-1, TIME_STEPS))
        self.successful_divisions = np.reshape(successful_divisions, (-1, TIME_STEPS))
        self.antibiotic_decays = np.reshape(antibiotic_decays, (-1, TIME_STEPS))

    def init_grids(self) -> None:
        grids = {}

        for i, file in enumerate(self.grid_files):
            grid = np.load(file)
            grids[self.label[i]] = grid

        self.grids = grids

    def plot_bacteria(self) -> None:
        plt.title(f'Bacteria Population with Varying {self.title}')
        plt.xlabel('Time step')
        plt.ylabel('Bacteria Population')
        for idx, data in enumerate(self.bact_pops):
            plt.plot(self.time_steps, data, label=f'{self.label[idx]}')
        plt.legend(title=self.title)
        plt.show()

    def plot_antibiotics(self) -> None:
        plt.title(f'Number of Antibiotics with Varying {self.title}')
        plt.xlabel('Time step')
        plt.ylabel('Antibiotic Population')
        for idx, data in enumerate(self.antibiotic_pops):
            plt.plot(self.time_steps, data, label=f'{self.label[idx]}')
        plt.legend(title=self.title)
        plt.show()

    def plot_collision_count(self) -> None:
        plt.title(f'Number of Collisions with Varying {self.title}')
        plt.xlabel('Time step')
        plt.ylabel('Collision Counts')
        for idx, data in enumerate(self.collision_counts):
            plt.plot(self.time_steps, data, label=f'{self.label[idx]}')
        plt.legend(title=self.title)
        plt.show()

    def plot_lethal_collision_count(self) -> None:
        plt.title(f'Number of Lethal Collisions with Varying {self.title}')
        plt.xlabel('Time step')
        plt.ylabel('Lethal Collision Counts')
        for idx, data in enumerate(self.lethal_collision_counts):
            plt.plot(self.time_steps, data, label=f'{self.label[idx]}')
        plt.legend(title=self.title)
        plt.show()

    def plot_mutation_count(self) -> None:
        plt.title(f'Number of Mutations with Varying {self.title}')
        plt.xlabel('Time step')
        plt.ylabel('Mutation Count')
        for idx, data in enumerate(self.mutation_count):
            plt.plot(self.time_steps, data, label=f'{self.label[idx]}')
        plt.legend(title=self.title)
        plt.show()

    def plot_attempted_divisions(self) -> None:
        plt.title(f'Number of Attempted Divisions with Varying {self.title}')
        plt.xlabel('Time step')
        plt.ylabel('Attempted Divisions')
        for idx, data in enumerate(self.attempted_divisions):
            plt.plot(self.time_steps, data, label=f'{self.label[idx]}')
        plt.legend(title=self.title)
        plt.show()

    def plot_successful_divisions(self) -> None:
        plt.title(f'Number of Successful Divisions with Varying {self.title}')
        plt.xlabel('Time step')
        plt.ylabel('Successful Divisions')
        for idx, data in enumerate(self.successful_divisions):
            plt.plot(self.time_steps, data, label=f'{self.label[idx]}')
        plt.legend(title=self.title)
        plt.show()

    def show_grid(self, param: float) -> None:
        fig, ax = plt.subplots()
        cmap_b = colors.ListedColormap([(0, 0, 0, 0), (0, 0, 1, 0.5)])
        cmap_a = colors.ListedColormap([(0, 0, 0, 0), (1, 0, 0, 0.5)])
        legend_b = Patch(color=(0, 0, 1, 0.5), label='Bacteria')
        legend_a = Patch(color=(1, 0, 0, 0.5), label='Antibiotics')
        fig.legend(handles=[legend_b, legend_a])
        for i in range(TIME_STEPS):
            ax.clear()
            ax.imshow(self.grids[param][i, 0],
                      vmin=0, vmax=1, cmap=cmap_b)
            ax.imshow(self.grids[param][i, 1],
                      vmin=0, vmax=1, cmap=cmap_a)
            ax.set_title(f'time step {i}')
            plt.pause(0.1)

    def print_files(self) -> None:
        for file in self.files:
            print(file)


doses = Evaluation('dose')
pop = Evaluation('pop')
interval = Evaluation('interval')

# View runs here
# doses.show_grid(DOSE_CONC[3])

# Start plots here
# doses.plot_bacteria()
# pop.plot_bacteria()
# interval.plot_bacteria()
# doses.plot_mutation_count()

# x_labels = [str(i) for i in DOSE_CONC]
# plt.bar(x_labels, doses.bact_pops[:, -1])
# plt.show()

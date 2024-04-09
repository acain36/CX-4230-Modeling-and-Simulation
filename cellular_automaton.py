from typing import Literal
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.patches import Patch
import numpy as np
import random
from bacteria import Bacteria
from antibiotic import Antibiotic
from state_recorder import StateRecorder

# Grid layers
BACTERIA_LAYER = 0
ANTIBIOTIC_LAYER = 1
Layer = Literal[0, 1]
# Grid cell states
EMPTY = 0
OCCUPIED = 1
# Time constants
ONE_DAY = 24
TWO_WEEKS = ONE_DAY * 14

class CellularAutomaton:
    def __init__(self, grid_size: int, init_pop: int, dose_concentration: int,
                 dosing_interval: int, seed: int = None,
                 max_steps: int = TWO_WEEKS, save_interval: int = ONE_DAY,
                 testing: str = None) -> None:
        self.t = 0
        self.rng = np.random.default_rng(seed)
        # Create 3D cellular automaton grid of size 2xNxN
        self.grid_size = grid_size
        self.grid = np.zeros((2, grid_size, grid_size), dtype=np.int8)
        # Initialize bacteria population
        self.bacteria_dict = {}
        for i in range(init_pop):
            self.add_bacteria()
        self.pop = len(self.bacteria_dict)
        # Record simulation state
        self.max_steps = max_steps
        self.state_recorder = StateRecorder(
            max_steps=max_steps,
            save_interval=save_interval,
            grid_size=grid_size,
            testing=testing
        )
        # Administer initial antibiotic dose
        self.antibiotic_dict = {}
        self.dose_concentration = dose_concentration
        self.dosing_interval = dosing_interval
        self.administer_antibiotics()

    def add_bacteria(self, bacteria: Bacteria = None,
                     coords: tuple[int, int] = None) -> None:
        if bacteria is None:
            genes = [random.randint(0, 1) for _ in range(30)]
            bacteria = Bacteria(genes)
        x_pos, y_pos = coords if coords is not None else (
            self.rng.integers(self.grid_size),
            self.rng.integers(self.grid_size)
        )
        self.grid[BACTERIA_LAYER][x_pos][y_pos] = OCCUPIED
        self.bacteria_dict[(x_pos, y_pos)] = bacteria

    def add_antibiotic(self, antibiotic: Antibiotic = None,
                       coords: tuple[int, int] = None) -> None:
        if antibiotic is None:
            antibiotic = Antibiotic()
        x_pos, y_pos = coords if coords is not None else (
            self.rng.integers(self.grid_size),
            self.rng.integers(self.grid_size)
        )
        self.grid[ANTIBIOTIC_LAYER][x_pos][y_pos] = OCCUPIED
        self.antibiotic_dict[(x_pos, y_pos)] = antibiotic

    def administer_antibiotics(self) -> None:
        probs = self.rng.random((self.grid_size, self.grid_size))
        it = np.nditer(self.grid[ANTIBIOTIC_LAYER], flags=['multi_index'])
        stats = self.state_recorder.get_stats()
        for a in it:
            if a == EMPTY and probs[it.multi_index] < self.dose_concentration:
                stats.dose_size += 1
                self.add_antibiotic(coords=it.multi_index)

    def detect_collisions(self) -> None:
        it = np.nditer(
            [self.grid[BACTERIA_LAYER], self.grid[ANTIBIOTIC_LAYER]],
            flags=['multi_index']
        )
        stats = self.state_recorder.get_stats()
        for b, a in it:
            if b == OCCUPIED and a == OCCUPIED:
                stats.collision_count += 1
                bacteria = self.bacteria_dict[it.multi_index]
                antibiotic = self.antibiotic_dict[it.multi_index]
                antibiotic.target(bacteria, stats)

    def random_adjacent(self, coords: tuple[int, int],
                        layer: Layer) -> tuple[int, int]:
        x, y = coords
        grid = self.grid[layer]
        adjacent = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        adjacent = [
            tuple(new_coords)
            for new_coords in np.clip(adjacent, 0, self.grid_size - 1)
        ]
        legal_cells = [
            new_coords
            for new_coords in adjacent
            if new_coords != coords and grid[new_coords] == EMPTY
        ]
        if len(legal_cells) != 0:
            return tuple(self.rng.choice(legal_cells))
        else:
            return coords

    def handle_cell_division(self, bacteria: Bacteria,
                             coords: tuple[int, int]) -> None:
        stats = self.state_recorder.get_stats()
        offspring = bacteria.attempt_division(self.rng, stats)
        if offspring is None:
            return
        offspring_coords = self.random_adjacent(coords, BACTERIA_LAYER)
        if offspring_coords != coords:
            stats.successful_divisions += 1
            self.add_bacteria(offspring, offspring_coords)

    def update(self) -> None:
        stats = self.state_recorder.get_stats()
        # Detect bacteria that have been successfully killed by an antibiotic
        self.detect_collisions()
        # Save old grid state and reinitialize new grid
        old_grid = self.grid
        self.state_recorder.set_grid(old_grid)
        self.grid = np.zeros((2, self.grid_size, self.grid_size),
                             dtype=np.int8)
        # Add living bacteria to new grid with updated position
        old_bacteria_dict = self.bacteria_dict.copy()
        stats.bacteria_count = len(old_bacteria_dict)
        self.bacteria_dict = {}
        for coords, bacteria in old_bacteria_dict.items():
            if bacteria.is_alive and not bacteria.can_divide:
                new_coords = self.random_adjacent(coords, BACTERIA_LAYER)
                if old_grid[BACTERIA_LAYER][new_coords] == EMPTY:
                    self.add_bacteria(bacteria, new_coords)
                else:
                    self.add_bacteria(bacteria, coords)
        for coords, bacteria in old_bacteria_dict.items():
            if bacteria.is_alive and bacteria.can_divide:
                self.add_bacteria(bacteria, coords)
                self.handle_cell_division(bacteria, coords)
        for bacteria in self.bacteria_dict.values():
            bacteria.age(self.rng)
        # Add active antibiotics to new grid
        old_antibiotic_dict = self.antibiotic_dict.copy()
        stats.antibiotic_count = len(old_antibiotic_dict)
        self.antibiotic_dict = {}
        for (old_x, old_y), antibiotic in old_antibiotic_dict.items():
            antibiotic.attempt_decay(self.rng, stats)
            if antibiotic.is_active:
                self.add_antibiotic(antibiotic, (old_x, old_y))
        # Re-dose antibiotics if dosing interval has passed
        if self.t != 0 and self.t % self.dosing_interval == 0:
            self.administer_antibiotics()
        # Increment time step
        self.t += 1
        self.state_recorder.advance_time()

    def run(self) -> None:
        fig, ax = plt.subplots()
        cmap_b = colors.ListedColormap([(0, 0, 0, 0), (0, 0, 1, 0.5)])
        cmap_a = colors.ListedColormap([(0, 0, 0, 0), (1, 0, 0, 0.5)])
        legend_b = Patch(color=(0, 0, 1, 0.5), label='Bacteria')
        legend_a = Patch(color=(1, 0, 0, 0.5), label='Antibiotics')
        fig.legend(handles=[legend_b, legend_a])
        for i in range(self.max_steps):
            ax.clear()
            ax.imshow(self.grid[BACTERIA_LAYER],
                      vmin=0, vmax=1, cmap=cmap_b)
            ax.imshow(self.grid[ANTIBIOTIC_LAYER],
                      vmin=0, vmax=1, cmap=cmap_a)
            ax.set_title(f'time step {self.t}')
            plt.pause(0.1)
            self.update()

    def run_headless(self) -> None:
        for i in range(self.max_steps):
            self.update()


# ca = CellularAutomaton(
#     grid_size=100,
#     init_pop=10,
#     dose_concentration=0.25,
#     dosing_interval=8,
#     seed=22
# )
# ca.run()

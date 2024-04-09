import pickle
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from threading import Thread

import numpy as np
from numpy.typing import NDArray

@dataclass
class IterationStats:
    time_step: int
    bacteria_count: int = 0
    antibiotic_count: int = 0
    collision_count: int = 0
    lethal_collision_count: int = 0
    mutation_count: int = 0
    attempted_divisions: int = 0
    successful_divisions: int = 0
    antibiotic_decays: int = 0
    dose_size: int = 0

class StateRecorder:
    def __init__(self, max_steps: int, save_interval: int, grid_size: int,
                 testing: str):
        Path('output').mkdir(parents=True, exist_ok=True)
        self.testing = testing
        timestamp = int(datetime.now().timestamp())
        if testing is None:
            self.grid_file = f'output/{timestamp}_grids.npy'
            self.stats_file = f'output/{timestamp}_stats.pkl'
        else:
            self.grid_file = f'output/{testing}_{timestamp}_grids.npy'
            self.stats_file = f'output/{testing}_{timestamp}_stats.pkl'
        self.max_steps = max_steps
        self.save_interval = save_interval
        self.grid_size = grid_size
        self.grid_mmap = np.lib.format.open_memmap(
            self.grid_file,
            mode='w+',
            dtype=np.int8,
            shape=(max_steps, 2, grid_size, grid_size)
        )
        self.init_grid_slice()
        self.stats = [IterationStats(0)]
        self.t = 0

    def init_grid_slice(self) -> None:
        self.grid_slice = np.empty(
            (self.save_interval, 2, self.grid_size, self.grid_size),
            dtype=np.int8
        )

    def copy_grid_slice(self, start: int, end: int,
                        grid_slice: NDArray[np.int8]) -> None:
        self.grid_mmap[start:end] = grid_slice[:]
        self.grid_mmap.flush()

    def save_stats(self, stats: list[IterationStats]) -> None:
        with open(self.stats_file, 'wb') as file:
            pickle.dump(stats, file)

    def advance_time(self) -> None:
        self.t += 1
        self.stats.append(IterationStats(self.t))
        if self.t % self.save_interval == 0:
            # Save grid slice to disk
            old_grid_slice = self.grid_slice
            start = self.t - self.save_interval
            end = self.t
            grid_thread = Thread(target=self.copy_grid_slice,
                                 args=(start, end, old_grid_slice))
            grid_thread.run()
            self.init_grid_slice()
            # Save current stats to disk
            stats = self.stats.copy()
            stats_thread = Thread(target=self.save_stats, args=(stats,))
            stats_thread.run()

    def set_grid(self, grid: NDArray[np.int8]) -> None:
        self.grid_slice[self.t % self.save_interval] = grid

    def get_stats(self) -> IterationStats:
        return self.stats[self.t]

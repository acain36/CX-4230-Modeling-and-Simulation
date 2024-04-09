from cellular_automaton import CellularAutomaton

# Test different dose concentrations
concentrations = [0.05, 0.10, 0.15, 0.20, 0.25]
eval_conc = []
for i in concentrations:
    ca = CellularAutomaton(
        grid_size=100,
        init_pop=10,
        dose_concentration=i,
        dosing_interval=8,
        seed=22,
        testing="dose"
    )
    ca.run_headless()
    eval_conc.append(ca.state_recorder)

# Test different starting population
starting_pop = [1] + [i for i in range(10, 101, 10)]
eval_pop = []
for i in starting_pop:
    ca = CellularAutomaton(
        grid_size=100,
        init_pop=i,
        dose_concentration=0.25,
        dosing_interval=8,
        seed=22,
        testing="pop"
    )
    ca.run_headless()
    eval_pop.append(ca.state_recorder)

# Test different dosing interval
intervals = [4, 6, 8, 12, 24, 48]
eval_intervals = []
for i in intervals:
    ca = CellularAutomaton(
        grid_size=100,
        init_pop=10,
        dose_concentration=0.25,
        dosing_interval=i,
        seed=22,
        testing="interval"
    )
    ca.run_headless()
    eval_intervals.append(ca.state_recorder)

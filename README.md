##Demo Video
https://mediaspace.gatech.edu/media/%5BTeam+22%5D+Modeling+and+Simulation+of+Antibacterial+Resistance+in+E.+Coli/1_0sd56bip

## Abstract
Antibiotic resistance poses a major threat to public health. To better understand how antibiotic resistance evolves, we are developing an agent-based model that simulates the interactions between a bacterial population and antibiotic exposure over time. The model represents individual bacteria as agents with adaptable genomes that can acquire mutations conferring antibiotic resistance. Antibiotic molecules are also modeled as individual agents that kill susceptible bacteria on contact. Our simulation integrates existing computational models of bacterial growth, division, mutation, and antibiotic pharmacodynamics. We use a cellular automaton framework to capture the spatial relationships between bacteria and antibiotics. Our goal is to explore how factors like antibiotic concentration, bacterial population density, and mutation rates influence the evolution of antibiotic resistance. By simulating resistance emergence in a spatially explicit environment, our model can provide novel insights into strategies for combating antibiotic resistance.
## How to run
### Requirements
This project was tested with:
- python 3.12.0
- matplotlib 3.8.0
- numpy 1.26.0
### Starting the simulation
The cellular automaton can be started by running
```
python cellular_automaton.py
```
### Running tests
To run the tests that generate files, run
```
python run_tests.py
```
### Evaluation
Once you have run the tests, you can create plots and analyze results by running
```
python evaluation.py
```

import random
from antibiotic import Antibiotic
from bacteria import Bacteria
from generate_mechanisms import GenMechanismsFromMatrix

SLICES = GenMechanismsFromMatrix([3, 3, 3, 3, 7, 6, 6, 5])

# Test targeting of cell wall
anti1 = [1, 0, 0] + [0]*33
anti2 = [0, 1, 0] + [0]*33
anti3 = [0, 0, 1] + [0]*33
bact = [1]*3 + [0]*27

slice = SLICES[0]

antibiotic1 = Antibiotic('', anti1, probabilities=[1 for _ in range(36)])
antibiotic2 = Antibiotic('', anti2, probabilities=[1 for _ in range(36)])
antibiotic3 = Antibiotic('', anti3, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact)
bacteria2 = Bacteria(bact)
bacteria3 = Bacteria(bact)

print("CELL WALL TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - Antibiotic: {antibiotic1.mechanisms[slice]}, Bacteria: {bacteria1.phenotype[slice]}, Is Alive: {bacteria1.is_alive}, Correct: {bacteria1.is_alive == True}')

antibiotic2.testing(bacteria2)
print(f'Test2 - Antibiotic: {antibiotic2.mechanisms[slice]}, Bacteria: {bacteria2.phenotype[slice]}, Is Alive: {bacteria2.is_alive}, Correct: {bacteria2.is_alive == True}')

antibiotic3.testing(bacteria3)
print(f'Test3 - Antibiotic: {antibiotic3.mechanisms[slice]}, Bacteria: {bacteria3.phenotype[slice]}, Is Alive: {bacteria3.is_alive}, Correct: {bacteria3.is_alive == False}')
print()

# Test targeting of respiration
anti1 = [0]*3 + [1, 0, 0] + [0]*30
anti2 = [0]*3 + [0, 1, 0] + [0]*30
anti3 = [0]*3 + [0, 0, 1] + [0]*30
bact = [0]*3 + [1]*3 + [0]*24

slice = SLICES[1]

antibiotic1 = Antibiotic('', anti1, probabilities=[1 for _ in range(36)])
antibiotic2 = Antibiotic('', anti2, probabilities=[1 for _ in range(36)])
antibiotic3 = Antibiotic('', anti3, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact)
bacteria2 = Bacteria(bact)
bacteria3 = Bacteria(bact)

print("RESPIRATION TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - Antibiotic: {antibiotic1.mechanisms[slice]}, Bacteria: {bacteria1.phenotype[slice]}, Is Alive: {bacteria1.is_alive}, Correct: {bacteria1.is_alive == True}')

antibiotic2.testing(bacteria2)
print(f'Test2 - Antibiotic: {antibiotic2.mechanisms[slice]}, Bacteria: {bacteria2.phenotype[slice]}, Is Alive: {bacteria2.is_alive}, Correct: {bacteria2.is_alive == True}')

antibiotic3.testing(bacteria3)
print(f'Test3 - Antibiotic: {antibiotic3.mechanisms[slice]}, Bacteria: {bacteria3.phenotype[slice]}, Is Alive: {bacteria3.is_alive}, Correct: {bacteria3.is_alive == False}')
print()

# Test targeting of cell shape
anti1 = [0]*6 + [1, 0, 0] + [0]*27
anti2 = [0]*6 + [0, 1, 0] + [0]*27
anti3 = [0]*6 + [0, 0, 1] + [0]*27
bact = [0]*6 + [1]*3 + [0]*21

slice = SLICES[2]

antibiotic1 = Antibiotic('', anti1, probabilities=[1 for _ in range(36)])
antibiotic2 = Antibiotic('', anti2, probabilities=[1 for _ in range(36)])
antibiotic3 = Antibiotic('', anti3, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact)
bacteria2 = Bacteria(bact)
bacteria3 = Bacteria(bact)

print("CELL SHAPE TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - Antibiotic: {antibiotic1.mechanisms[slice]}, Bacteria: {bacteria1.phenotype[slice]}, Is Alive: {bacteria1.is_alive}, Correct: {bacteria1.is_alive == True}')

antibiotic2.testing(bacteria2)
print(f'Test2 - Antibiotic: {antibiotic2.mechanisms[slice]}, Bacteria: {bacteria2.phenotype[slice]}, Is Alive: {bacteria2.is_alive}, Correct: {bacteria2.is_alive == False}')

antibiotic3.testing(bacteria3)
print(f'Test3 - Antibiotic: {antibiotic3.mechanisms[slice]}, Bacteria: {bacteria3.phenotype[slice]}, Is Alive: {bacteria3.is_alive}, Correct: {bacteria3.is_alive == True}')
print()

# Test targeting of ribosomes
anti1 = [0]*9 + [1, 0, 0] + [0]*24
anti2 = [0]*9 + [0, 1, 0] + [0]*24
anti3 = [0]*9 + [0, 0, 1] + [0]*24
bact = [0]*9 + [1]*3 + [0]*18

slice = SLICES[3]

antibiotic1 = Antibiotic('', anti1, probabilities=[1 for _ in range(36)])
antibiotic2 = Antibiotic('', anti2, probabilities=[1 for _ in range(36)])
antibiotic3 = Antibiotic('', anti3, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact)
bacteria2 = Bacteria(bact)
bacteria3 = Bacteria(bact)

print("RIBOSOME TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - Antibiotic: {antibiotic1.mechanisms[slice]}, Bacteria: {bacteria1.phenotype[slice]}, Is Alive: {bacteria1.is_alive}, Correct: {bacteria1.is_alive == True}')

antibiotic2.testing(bacteria2)
print(f'Test2 - Antibiotic: {antibiotic2.mechanisms[slice]}, Bacteria: {bacteria2.phenotype[slice]}, Is Alive: {bacteria2.is_alive}, Correct: {bacteria2.is_alive == True}')

antibiotic3.testing(bacteria3)
print(f'Test3 - Antibiotic: {antibiotic3.mechanisms[slice]}, Bacteria: {bacteria3.phenotype[slice]}, Is Alive: {bacteria3.is_alive}, Correct: {bacteria3.is_alive == False}')
print()

# Test targeting of efflux pumps
anti1 = [0]*12 + [1, 0, 0, 0, 0, 0, 0] + [0]*17
anti2 = [0]*12 + [0, 1, 0, 0, 0, 0, 0] + [0]*17
anti3 = [0]*12 + [0, 0, 1, 0, 0, 0, 0] + [0]*17
anti4 = [0]*12 + [0, 0, 0, 1, 0, 0, 0] + [0]*17
anti5 = [0]*12 + [0, 0, 0, 0, 1, 0, 0] + [0]*17
anti6 = [0]*12 + [0, 0, 0, 0, 0, 1, 0] + [0]*17
anti7 = [0]*12 + [0, 0, 0, 0, 0, 0, 1] + [0]*17
bact = [0]*12 + [1, 0, 1, 0] + [0]*14

slice = SLICES[4]

antibiotic1 = Antibiotic('', anti1, probabilities=[1 for _ in range(36)])
antibiotic2 = Antibiotic('', anti2, probabilities=[1 for _ in range(36)])
antibiotic3 = Antibiotic('', anti3, probabilities=[1 for _ in range(36)])
antibiotic4 = Antibiotic('', anti4, probabilities=[1 for _ in range(36)])
antibiotic5 = Antibiotic('', anti5, probabilities=[1 for _ in range(36)])
antibiotic6 = Antibiotic('', anti6, probabilities=[1 for _ in range(36)])
antibiotic7 = Antibiotic('', anti7, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact)
bacteria2 = Bacteria(bact)
bacteria3 = Bacteria(bact)
bacteria4 = Bacteria(bact)
bacteria5 = Bacteria(bact)
bacteria6 = Bacteria(bact)
bacteria7 = Bacteria(bact)

print("EFFLUX PUMPS TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - Antibiotic: {antibiotic1.mechanisms[slice]}, Bacteria: {bacteria1.phenotype[slice]}, Is Alive: {bacteria1.is_alive}, Correct: {bacteria1.is_alive == True}')

antibiotic2.testing(bacteria2)
print(f'Test2 - Antibiotic: {antibiotic2.mechanisms[slice]}, Bacteria: {bacteria2.phenotype[slice]}, Is Alive: {bacteria2.is_alive}, Correct: {bacteria2.is_alive == True}')

antibiotic3.testing(bacteria3)
print(f'Test3 - Antibiotic: {antibiotic3.mechanisms[slice]}, Bacteria: {bacteria3.phenotype[slice]}, Is Alive: {bacteria3.is_alive}, Correct: {bacteria3.is_alive == True}')

antibiotic4.testing(bacteria4)
print(f'Test4 - Antibiotic: {antibiotic4.mechanisms[slice]}, Bacteria: {bacteria4.phenotype[slice]}, Is Alive: {bacteria4.is_alive}, Correct: {bacteria4.is_alive == False}')

antibiotic5.testing(bacteria5)
print(f'Test5 - Antibiotic: {antibiotic5.mechanisms[slice]}, Bacteria: {bacteria5.phenotype[slice]}, Is Alive: {bacteria5.is_alive}, Correct: {bacteria5.is_alive == True}')

antibiotic6.testing(bacteria6)
print(f'Test6 - Antibiotic: {antibiotic6.mechanisms[slice]}, Bacteria: {bacteria6.phenotype[slice]}, Is Alive: {bacteria6.is_alive}, Correct: {bacteria6.is_alive == True}')

antibiotic7.testing(bacteria7)
print(f'Test7 - Antibiotic: {antibiotic7.mechanisms[slice]}, Bacteria: {bacteria7.phenotype[slice]}, Is Alive: {bacteria7.is_alive}, Correct: {bacteria7.is_alive == True}')
print()

# Test targeting of porins
anti1 = [0]*19 + [1, 0, 0, 0, 0, 0] + [0]*11
anti2 = [0]*19 + [0, 1, 0, 0, 0, 0] + [0]*11
anti3 = [0]*19 + [0, 0, 1, 0, 0, 0] + [0]*11
anti4 = [0]*19 + [0, 0, 0, 1, 0, 0] + [0]*11
anti5 = [0]*19 + [0, 0, 0, 0, 1, 0] + [0]*11
anti6 = [0]*19 + [0, 0, 0, 0, 0, 1] + [0]*11
bact = [0]*16 + [1]*4 + [0]*10

slice = SLICES[5]

antibiotic1 = Antibiotic('', anti1, probabilities=[1 for _ in range(36)])
antibiotic2 = Antibiotic('', anti2, probabilities=[1 for _ in range(36)])
antibiotic3 = Antibiotic('', anti3, probabilities=[1 for _ in range(36)])
antibiotic4 = Antibiotic('', anti4, probabilities=[1 for _ in range(36)])
antibiotic5 = Antibiotic('', anti5, probabilities=[1 for _ in range(36)])
antibiotic6 = Antibiotic('', anti6, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact)
bacteria2 = Bacteria(bact)
bacteria3 = Bacteria(bact)
bacteria4 = Bacteria(bact)
bacteria5 = Bacteria(bact)
bacteria6 = Bacteria(bact)

print("PORINS TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - Antibiotic: {antibiotic1.mechanisms[slice]}, Bacteria: {bacteria1.phenotype[slice]}, Is Alive: {bacteria1.is_alive}, Correct: {bacteria1.is_alive == True}')

antibiotic2.testing(bacteria2)
print(f'Test2 - Antibiotic: {antibiotic2.mechanisms[slice]}, Bacteria: {bacteria2.phenotype[slice]}, Is Alive: {bacteria2.is_alive}, Correct: {bacteria2.is_alive == True}')

antibiotic3.testing(bacteria3)
print(f'Test3 - Antibiotic: {antibiotic3.mechanisms[slice]}, Bacteria: {bacteria3.phenotype[slice]}, Is Alive: {bacteria3.is_alive}, Correct: {bacteria3.is_alive == True}')

antibiotic4.testing(bacteria4)
print(f'Test4 - Antibiotic: {antibiotic4.mechanisms[slice]}, Bacteria: {bacteria4.phenotype[slice]}, Is Alive: {bacteria4.is_alive}, Correct: {bacteria4.is_alive == True}')

antibiotic5.testing(bacteria5)
print(f'Test5 - Antibiotic: {antibiotic5.mechanisms[slice]}, Bacteria: {bacteria5.phenotype[slice]}, Is Alive: {bacteria5.is_alive}, Correct: {bacteria5.is_alive == True}')

antibiotic6.testing(bacteria6)
print(f'Test6 - Antibiotic: {antibiotic6.mechanisms[slice]}, Bacteria: {bacteria6.phenotype[slice]}, Is Alive: {bacteria6.is_alive}, Correct: {bacteria6.is_alive == False}')
print()

# Test targeting of DNA
anti1 = [0]*25 + [1, 0, 0, 0, 0, 0] + [0]*5
anti2 = [0]*25 + [0, 1, 0, 0, 0, 0] + [0]*5
anti3 = [0]*25 + [0, 0, 1, 0, 0, 0] + [0]*5
anti4 = [0]*25 + [0, 0, 0, 1, 0, 0] + [0]*5
anti5 = [0]*25 + [0, 0, 0, 0, 1, 0] + [0]*5
anti6 = [0]*25 + [0, 0, 0, 0, 0, 1] + [0]*5
bact = [0]*20 + [1]*7 + [0]*3

slice = SLICES[6]

antibiotic1 = Antibiotic('', anti1, probabilities=[1 for _ in range(36)])
antibiotic2 = Antibiotic('', anti2, probabilities=[1 for _ in range(36)])
antibiotic3 = Antibiotic('', anti3, probabilities=[1 for _ in range(36)])
antibiotic4 = Antibiotic('', anti4, probabilities=[1 for _ in range(36)])
antibiotic5 = Antibiotic('', anti5, probabilities=[1 for _ in range(36)])
antibiotic6 = Antibiotic('', anti6, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact)
bacteria2 = Bacteria(bact)
bacteria3 = Bacteria(bact)
bacteria4 = Bacteria(bact)
bacteria5 = Bacteria(bact)
bacteria6 = Bacteria(bact)

print("DNA TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - Antibiotic: {antibiotic1.mechanisms[slice]}, Bacteria: {bacteria1.phenotype[slice]}, Is Alive: {bacteria1.is_alive}, Correct: {bacteria1.is_alive == True}')

antibiotic2.testing(bacteria2)
print(f'Test2 - Antibiotic: {antibiotic2.mechanisms[slice]}, Bacteria: {bacteria2.phenotype[slice]}, Is Alive: {bacteria2.is_alive}, Correct: {bacteria2.is_alive == True}')

antibiotic3.testing(bacteria3)
print(f'Test3 - Antibiotic: {antibiotic3.mechanisms[slice]}, Bacteria: {bacteria3.phenotype[slice]}, Is Alive: {bacteria3.is_alive}, Correct: {bacteria3.is_alive == True}')

antibiotic4.testing(bacteria4)
print(f'Test4 - Antibiotic: {antibiotic4.mechanisms[slice]}, Bacteria: {bacteria4.phenotype[slice]}, Is Alive: {bacteria4.is_alive}, Correct: {bacteria4.is_alive == True}')

antibiotic5.testing(bacteria5)
print(f'Test5 - Antibiotic: {antibiotic5.mechanisms[slice]}, Bacteria: {bacteria5.phenotype[slice]}, Is Alive: {bacteria5.is_alive}, Correct: {bacteria5.is_alive == True}')

antibiotic6.testing(bacteria6)
print(f'Test6 - Antibiotic: {antibiotic6.mechanisms[slice]}, Bacteria: {bacteria6.phenotype[slice]}, Is Alive: {bacteria6.is_alive}, Correct: {bacteria6.is_alive == False}')
print()

# Test targeting of plasmids
anti1 = [0]*31 + [1, 0, 0, 0, 0]
anti2 = [0]*31 + [0, 1, 0, 0, 0]
anti3 = [0]*31 + [0, 0, 1, 0, 0]
anti4 = [0]*31 + [0, 0, 0, 1, 0]
anti5 = [0]*31 + [0, 0, 0, 0, 1]
bact = [0]*27 + [1]*3

slice = SLICES[7]

antibiotic1 = Antibiotic('', anti1, probabilities=[1 for _ in range(36)])
antibiotic2 = Antibiotic('', anti2, probabilities=[1 for _ in range(36)])
antibiotic3 = Antibiotic('', anti3, probabilities=[1 for _ in range(36)])
antibiotic4 = Antibiotic('', anti4, probabilities=[1 for _ in range(36)])
antibiotic5 = Antibiotic('', anti5, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact)
bacteria2 = Bacteria(bact)
bacteria3 = Bacteria(bact)
bacteria4 = Bacteria(bact)
bacteria5 = Bacteria(bact)

print("PLASMID TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - Antibiotic: {antibiotic1.mechanisms[slice]}, Bacteria: {bacteria1.phenotype[slice]}, Is Alive: {bacteria1.is_alive}, Correct: {bacteria1.is_alive == True}')

antibiotic2.testing(bacteria2)
print(f'Test2 - Antibiotic: {antibiotic2.mechanisms[slice]}, Bacteria: {bacteria2.phenotype[slice]}, Is Alive: {bacteria2.is_alive}, Correct: {bacteria2.is_alive == True}')

antibiotic3.testing(bacteria3)
print(f'Test3 - Antibiotic: {antibiotic3.mechanisms[slice]}, Bacteria: {bacteria3.phenotype[slice]}, Is Alive: {bacteria3.is_alive}, Correct: {bacteria3.is_alive == True}')

antibiotic4.testing(bacteria4)
print(f'Test4 - Antibiotic: {antibiotic4.mechanisms[slice]}, Bacteria: {bacteria4.phenotype[slice]}, Is Alive: {bacteria4.is_alive}, Correct: {bacteria4.is_alive == True}')

antibiotic5.testing(bacteria5)
print(f'Test5 - Antibiotic: {antibiotic5.mechanisms[slice]}, Bacteria: {bacteria5.phenotype[slice]}, Is Alive: {bacteria5.is_alive}, Correct: {bacteria5.is_alive == False}')
print()

# Test targetting with randomly generated vectors
anti = [random.randint(0, 1) for _ in range(36)]
bact1 = [random.randint(0, 1) for _ in range(30)]
bact2 = [random.randint(0, 1) for _ in range(30)]
bact3 = [random.randint(0, 1) for _ in range(30)]
bact4 = [random.randint(0, 1) for _ in range(30)]
bact5 = [random.randint(0, 1) for _ in range(30)]
bact6 = [random.randint(0, 1) for _ in range(30)]

antibiotic = Antibiotic('', anti, probabilities=[1 for _ in range(36)])
bacteria1 = Bacteria(bact1)
bacteria2 = Bacteria(bact2)
bacteria3 = Bacteria(bact3)
bacteria4 = Bacteria(bact4)
bacteria5 = Bacteria(bact5)
bacteria6 = Bacteria(bact6)

print("RANDOMNESS TESTS:")
antibiotic.testing(bacteria1)
print(f'Test1 - \nAntibiotic: {antibiotic.mechanisms}, \nBacteria:   {bacteria1.phenotype}, \nIs Alive: {bacteria1.is_alive}')
print()

antibiotic.testing(bacteria2)
print(f'Test2 - \nAntibiotic: {antibiotic.mechanisms}, \nBacteria:   {bacteria2.phenotype}, \nIs Alive: {bacteria2.is_alive}')
print()

antibiotic.testing(bacteria3)
print(f'Test3 - \nAntibiotic: {antibiotic.mechanisms}, \nBacteria:   {bacteria3.phenotype}, \nIs Alive: {bacteria3.is_alive}')
print()

antibiotic.testing(bacteria4)
print(f'Test4 - \nAntibiotic: {antibiotic.mechanisms}, \nBacteria:   {bacteria4.phenotype}, \nIs Alive: {bacteria4.is_alive}')
print()

antibiotic.testing(bacteria5)
print(f'Test5 - \nAntibiotic: {antibiotic.mechanisms}, \nBacteria:   {bacteria5.phenotype}, \nIs Alive: {bacteria5.is_alive}')
print()

antibiotic.testing(bacteria6)
print(f'Test6 - \nAntibiotic: {antibiotic.mechanisms}, \nBacteria:   {bacteria6.phenotype}, \nIs Alive: {bacteria6.is_alive}')
print()

# Test targeting for Cefazolin
anti = [0, 0, 1] + [random.randint(0, 1) for _ in range(33)]
bact1 = [1, 1, 0] +  [0 for _ in range(27)]
bact2 = [0, 1, 0] +  [0 for _ in range(27)]
bact3 = [random.randint(0, 1) for _ in range(30)]
bact4 = [random.randint(0, 1) for _ in range(30)]
bact5 = [random.randint(0, 1) for _ in range(30)]
bact6 = [random.randint(0, 1) for _ in range(30)]

antibiotic1 = Antibiotic('', anti, probabilities=[1, 1, 1] + [0]*33)
antibiotic2 = Antibiotic('', anti)
bacteria1 = Bacteria(bact1)
bacteria2 = Bacteria(bact2)
bacteria3 = Bacteria(bact3)
bacteria4 = Bacteria(bact4)
bacteria5 = Bacteria(bact5)
bacteria6 = Bacteria(bact6)

print("CEFAZOLIN TESTS:")
antibiotic1.testing(bacteria1)
print(f'Test1 - \nAntibiotic: {antibiotic1.mechanisms}, \nBacteria:   {bacteria1.phenotype}, \nIs Alive: {bacteria1.is_alive}')
print()

antibiotic1.testing(bacteria2)
print(f'Test2 - \nAntibiotic: {antibiotic1.mechanisms}, \nBacteria:   {bacteria2.phenotype}, \nIs Alive: {bacteria2.is_alive}')
print()

antibiotic2.testing(bacteria3)
print(f'Test3 - \nAntibiotic: {antibiotic2.mechanisms}, \nBacteria:   {bacteria3.phenotype}, \nIs Alive: {bacteria3.is_alive}')
print()

antibiotic2.testing(bacteria4)
print(f'Test4 - \nAntibiotic: {antibiotic2.mechanisms}, \nBacteria:   {bacteria4.phenotype}, \nIs Alive: {bacteria4.is_alive}')
print()

antibiotic2.testing(bacteria5)
print(f'Test5 - \nAntibiotic: {antibiotic2.mechanisms}, \nBacteria:   {bacteria5.phenotype}, \nIs Alive: {bacteria5.is_alive}')
print()

antibiotic2.testing(bacteria6)
print(f'Test6 - \nAntibiotic: {antibiotic2.mechanisms}, \nBacteria:   {bacteria6.phenotype}, \nIs Alive: {bacteria6.is_alive}')
print()
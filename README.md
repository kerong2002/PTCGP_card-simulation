# PTCGP_card-simulation
This Python project simulates the probability distribution of drawing rare cards from card packs in a gacha-style system. The simulation takes into account the probability of obtaining rare cards from both standard and rare card packs, and calculates the expected outcomes over a large number of trials.

## Result
##### Simulation Result: 60 Card Packs, 10,000 Trials
![Simulation Result: 60 Card Packs, 10,000 Trials](https://github.com/kerong2002/PTCGP_card-simulation/blob/main/simulation.png)

##### Simulation Result: 60 Card Packs, 1,000,000 Trials

## Project Overview

In this simulation, there are two types of card packs:

1. **Rare Card Pack (0.05% probability)**
2. **Standard Card Pack (99.95% probability)**

Each pack contains 5 cards, and only certain cards in the standard pack have a chance to be rare. The simulation calculates the probability of obtaining rare cards under the following conditions:

- **Standard Pack (4th and 5th Card)**:
    - **4th Card**: 
        - Gold Card: 0.04% * 2
        - Time Mirror Card: 0.222%
        - Full-Image & Colored Border EX Cards: 0.041% * 9
        - Regular EX Cards: 0.333% * 5
    - **5th Card**:
        - Gold Card: 0.08% * 2
        - Time Mirror Card: 0.888%
        - Full-Image & Colored Border EX Cards: 0.166% * 9
        - Regular EX Cards: 1.332% * 5

- **Rare Card Pack (1st to 5th Card)**:
    - Gold Card: 3.846%
    - Time Mirror Card: 3.846%
    - Full-Image & Colored Border EX Cards: 3.846% * 9
    - No Regular EX Cards

### Goal
The primary goal is to calculate the number of rare cards drawn from 60 packs over 10,000 tests, simulating a gacha system where you can obtain rare cards from either standard or rare card packs. The simulation outputs the probability distribution of rare card counts across the tests.

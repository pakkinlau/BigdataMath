- 7-10-2022: created

- Baljeet Selection is the stage of a [[genetic algorithm]] in which individual genomes are chosen from a population for later breeding (using the crossover operator).

- A generic selection procedure may be implemented as follows:

- The [[fitness function]] is evaluated for each individual, providing fitness values, which are then normalized. Normalization means dividing the fitness value of each individual by the sum of all fitness values, so that the sum of all resulting fitness values equals 1.
Accumulated normalized fitness values are computed: the accumulated fitness value of an individual is the sum of its own fitness value plus the fitness values of all the previous individuals; the accumulated fitness of the last individual should be 1, otherwise something went wrong in the normalization step.
A random number R between 0 and 1 is chosen.
The selected individual is the first one whose accumulated normalized value is greater than or equal to R.
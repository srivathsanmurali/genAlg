#!/usr/bin/python

from population import population
from dna import dna
import sys
def main():
    p = population(1000, sys.argv[1])
    for i in range(1000):
        print i, p.getTotalScore()
        p.advanceGeneration()
        goodGenes = [d for d in p.phrases if d.fitness(p.target) == 1]
        if not len(goodGenes) == 0:
            print "found in gen", i, goodGenes[0].genes
            break


if __name__ == "__main__":
    main()


from dna import dna
import random
import sys

class population:
    def __init__(self, populationSize, target):
        self.populationSize       = populationSize;
        self.target               = target.lower()
        self.size                 = len(target)
        self.phrases              = [dna(self.size) for x in range(populationSize)]

    def getTotalScore(self):
        return sum([p.fitness(self.target) for p in self.phrases])/self.populationSize

    def advanceGeneration(self):
        matingPool = [p for p in self.phrases for _ in range(int(p.fitness(self.target) * 100)) ]
        self.phrases = []
        for _ in range(self.populationSize):
            pA = random.choice(matingPool)
            pB = random.choice(matingPool)
            child = dna(self.size)
            child.crossover(pA,pB)
            child.mutate()
            self.phrases.append(child)

        goodGenes =  [d for d in self.phrases if d.fitness(self.target) == 1]
        if (len(goodGenes) > 0):
          return True
        else:
          return False

    def advanceGenerations(self,numGenerations):
        for i in range(numGenerations):
            sys.stdout.write("\r" + "{0}: avg fitness = {1}".format(i, self.getTotalScore()))
            sys.stdout.flush()

            if(self.advanceGeneration()):
                sys.stdout.write("\n")
                sys.stdout.flush()
                return i
        sys.stdout.write("\n")
        sys.stdout.flush()
        return -1




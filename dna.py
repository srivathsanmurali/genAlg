import string
import random

class dna:
    def __init__(self, size):
        self.size       = size;
        self.genes      = "".join(random.choice(string.ascii_lowercase) for _ in range(self.size))
        self.crossOverProbabilty  = 0.5;
        self.mutationProbabilty   = 0.1;

    def fitness(self, target):
        score = 0.0
        for i in range(self.size):
            if target[i] == self.genes[i]:
                score = score + 1
        return score/self.size

    def crossover(self, pA, pB):
        self.genes = ""
        for i in range(self.size):
            p = random.uniform(0,1)
            if p < self.crossOverProbabilty:
                self.genes = self.genes + pA.genes[i]
            else:
                self.genes = self.genes + pB.genes[i]

    def mutate(self):
        newGenes = ""
        for i in range(self.size):
            p = random.uniform(0,1)
            if p < self.mutationProbabilty:
                newGenes = newGenes + random.choice(string.ascii_lowercase)
            else:
                newGenes = newGenes + self.genes[i]
        self.genes = newGenes

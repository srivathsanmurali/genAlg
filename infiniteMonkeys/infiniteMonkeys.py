#!/usr/bin/python

from population import population
import sys

found = 0

def main():
    p = population(1000, sys.argv[1])
    found = p.advanceGenerations(1000)
    print "found in gen", found, p.target


if __name__ == "__main__":
    main()


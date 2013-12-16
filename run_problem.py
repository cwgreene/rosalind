#!/usr/bin/env python
import sys
import imp

sys.path.append("lib")
import rosalind

def run_program(program):
    rosalind.filename = "datasets/rosalind_%s.txt" % program
    __import__("solutions."+program)

def main(args):
    run_program(args[0])

if __name__=="__main__":
    main(sys.argv[1:])

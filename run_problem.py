#!/usr/bin/env python
import sys
import imp

import rosalind

def run_program(program, args):
    if args:
        rosalind.set_filename(args[0])
    else: 
        rosalind.set_filename("datasets/rosalind_%s.txt" % program)
    __import__("solutions."+program)

def main(args):
    run_program(args[0], args[1:])

if __name__=="__main__":
    main(sys.argv[1:])

#!/usr/bin/env python
import sys
import StringIO
import glob
import argparse
import re

import rosalind

def run_program(program, filename):
    if filename:
        rosalind.set_filename(filename)
    else: 
        rosalind.set_filename("datasets/rosalind_%s.txt" % program)
    __import__("solutions."+program)

def ignore_list():
    return [line.strip() for line in open("solutions/.ignore")]

def maybe_test_program(program, filename, should_test):
    if should_test:
        print "{} :".format(program),
        actual_stdout = sys.stdout
        sys.stdout = StringIO.StringIO()
    run_program(program, filename)
    if should_test:
        sys.stdout.seek(0)
        output = sys.stdout.read()
        solution = open("dataset_solutions/rosalind_{}.solution.out".format(program)).read()
        sys.stdout = actual_stdout
        if output.strip() != solution.strip():
            raise Exception("Does not match solution")
    if should_test:
        print "Test pass!"

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--test-all", action="store_true")
    parser.add_argument("program", nargs="?", default=None)
    parser.add_argument("filename", nargs="?", default=None)
    options = parser.parse_args(args)


    if options.test_all:
        programs = [re.findall(".*/([^.*]*).py", solution_file)[0]
                 for solution_file in glob.glob("solutions/[!_]*.py")]
        for x in ignore_list():
            programs.remove(x)
        options.test = True
    elif options.program:
        programs = [options.program]
    else:
        parser.parse_args(["--help"])

    for program in programs:
        maybe_test_program(program, options.filename, options.test)

if __name__=="__main__":
    main(sys.argv[1:])

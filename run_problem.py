#!/usr/bin/env python
import sys
import StringIO
import glob
import argparse
import re

import rosalind
import colorama
from colorama import Fore

import time

colorama.init()

SOLUTION_FILE_FORMAT="dataset_solutions/rosalind_{}.solution.out"

def red(string): return Fore.RED+string+Fore.RESET
def green(string): return Fore.GREEN+string+Fore.RESET
def yellow(string): return Fore.YELLOW+string+Fore.RESET

def run_program(program, filename):
    if filename:
        rosalind.set_filename(filename)
    else: 
        rosalind.set_filename("datasets/rosalind_%s.txt" % program)
    __import__("solutions."+program)

def ignore_list():
    return [line.strip() for line in open("solutions/.ignore")]

def maybe_test_program(program, filename, should_test, should_commit):
    actual_stdout = sys.stdout
    try:
        if should_test:
            start_time = time.time()
            print "{:<5}:".format(program),
            sys.stdout.flush()
            sys.stdout = StringIO.StringIO()
        if should_commit:
            sys.stdout = StringIO.StringIO()
        run_program(program, filename)
        if should_test:
            sys.stdout.seek(0)
            output = sys.stdout.read()
            solution = open(SOLUTION_FILE_FORMAT.format(program)).read()
            sys.stdout = actual_stdout
            if output.strip() != solution.strip():
                raise Exception("Does not match solution")
            print green("Test pass!"), "({0:.2f} ms)".format(1000*(time.time() - start_time))
        if should_commit:
            output = open(SOLUTION_FILE_FORMAT.format(program), "w")
            sys.stdout.seek(0)
            output.write(sys.stdout.read())
    finally:
        sys.stdout = actual_stdout

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true",
        help="checks the output of the program against the stored solutions file")
    parser.add_argument("--test-all", action="store_true",
        help="tests all programs (except: %s)"%",".join(ignore_list()))
    parser.add_argument("--commit", action="store_true",
        help="saves the output of the programs run as the canonical answer")
    parser.add_argument("--list", action="store_true",
        help="list all programs")
    parser.add_argument("program", nargs="?", default=None,
        help="program to run, use --list to show programs")
    parser.add_argument("filename", nargs="?", default=None,
        help="filename of input, default is 'datasets/rosalind_PROGNAME.txt'")
    options = parser.parse_args(args)

    programs = [re.findall(".*/([^.*]*).py", solution_file)[0]
                 for solution_file in glob.glob("solutions/[!_]*.py")]

    if options.test_all:
        for x in ignore_list():
            programs.remove(x)
        options.test = True
    elif options.list:
        for program in programs:
            program_color = green
            if program in ignore_list():
                program_color = red
            print program_color("{:<5}".format(program)), yellow("http://rosalind.info/problems/%s/"% program)
        return 0
    elif options.program:
        programs = [options.program]
    else:
        parser.parse_args(["--help"])

    if ignore_list():
        print "Skipping:", ",".join(ignore_list())
    failure = 0
    start_time = time.time()
    for program in programs:
        try:
            maybe_test_program(program, options.filename, options.test, options.commit)
        except Exception as e:
            print red("Failure! "), e
            failure = 1
    print "Total time: %s s" % ((time.time()-start_time))
    return failure

if __name__=="__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python

import os
import sys

URL = "https://github.com/cwgreene/rosalind/issues/"

def main(args):
    lines = sys.stdin.readlines()
    if not lines:
        print>>sys.stderr, "No commit message!"
        sys.exit(1)
    if len(lines) < 2:
        print>>sys.stderr, "Message body is empty"
        sys.exit(1)
    try:
        issue, subject = lines[0].split(" ", 1)
        project, issue = issue.split("-")
    except ValueError as e:
        raise Exception("Subject line is not of the form 'ROSALIND-XXX Subject'")
    issue_type = lines[-2]
    if issue_type.lower().startswith("ref"):
        lines[-2] = "%s%s" % (URL, issue)
    elif issue_type.lower().startswith("fixes"):
        lines[-2] = "Fixes %s%s\n" % (URL, issue)
    else:
        lines.append("Fixes %s%s\n" % (URL, issue))
    print "".join(lines)
    
if __name__=="__main__":
    main(sys.argv[1:])

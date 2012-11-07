#!/usr/bin/env python
""" The sh module, continued.  Part 2 """

# Bash style piping is performed using function composition.
from sh import echo, ls, grep

print "Without grep"
print ls(l=True)

print "With grep"
print grep(ls(l=True), "method4")

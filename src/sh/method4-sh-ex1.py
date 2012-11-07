#!/usr/bin/env python
""" The sh module.

sh (previously pbs) is a full-fledged subprocess interface for Python 2.6 - 3.2
that allows you to call any program as if it were a function::

    from sh import ifconfig
    print ifconfig("eth0")

sh is not a collection of system commands implemented in Python.

Pythonic.  Magical.

"""


print "Commands"
print "--------"

import sh

print sh.echo("hai there")
print sh.ls(a=True, l=True, h=True)




print "The 'from' syntax"
print "-----------------"

from sh import ls

print ls()

#!/usr/bin/env python
""" The commands module.

Deprecated, but straightforward.

Returns error code *and* output.  Nice!
"""

import commands

status, output = commands.getstatusoutput("echo hai there")
print status, output

status, output = commands.getstatusoutput("ls -alh")
print status, output

status, output = commands.getstatusoutput("echo bai now")
print status, output

#!/usr/bin/env python
""" The os.system call.

Straightforward.  Returns error code.
stdout and stderr aren't captured for processing.
"""

import os

os.system("echo hai there")     # Finds things on the standard PATH
os.system("ls -alh")
os.system("echo bai now")

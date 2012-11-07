#!/usr/bin/env python
""" The subprocess module.

Standard, but it feels complicated.

I have much more control over how things are executed.

"""

import subprocess


proc = subprocess.Popen(["echo hai there"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=True,
                        executable='/bin/bash')
output, error = proc.communicate()
print(output)
print(error)

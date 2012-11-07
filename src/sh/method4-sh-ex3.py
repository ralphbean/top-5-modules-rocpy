""" The sh module, part 3.

Iterating over output.
"""

from sh import tail

for line in tail("-f", "some_file.txt", _iter=True):
    if "ERROR" in line:
        send_an_email_to_support(line)

""" The sh module, part 4.  Ridiculous. """

from sh import gcc, git

for line in gcc("-o", "awesome_binary", "awesome_source.c", _iter=True):
    if "warning" in line:
        # parse out the relevant info
        filename, line, char, message = line.split(":", 3)

        # find the commit using git
        commit = git("blame", "-e", filename, L="%d,%d" % (line, line))

        # send them an email
        email_address = parse_email_from_commit_line(commit)
        send_email(email_address, message)

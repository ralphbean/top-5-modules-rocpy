from fabulous.image import Image
from fabulous.text import Text

def breakline(n=25):
    raw_input()
    print "\n" * n

print Text("Ralph's", fsize=25)
print Text("5 favorite", fsize=30)
print Text("python modules")
breakline()

print Image("resources/me.png")
breakline()

print Image("resources/redhat-logo.png")
breakline()

print Image("resources/fedora-logo.png")
breakline()

print Image("resources/fedmsg.png")
print Text("fedmsg", fsize=45)
breakline()

print Text("Agenda!", fsize=45)
breakline(5)
print Text("  sqlalchemy", skew=1)
print Text("  sh", skew=1)
print Text("  fabulous", skew=1)
print Text("  BeautifulSoup", skew=1)
print Text("  pandas", skew=1)

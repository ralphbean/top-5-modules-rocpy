from fabulous.image import Image
from fabulous.text import Text

def breakline(n=25):
    raw_input()
    print "\n" * n

print Text("Ralph's", fsize=25, font='stix')
print Text("5 favorite", fsize=30, font='stix')
print Text("python", fsize=25, font='stix')
print Text("modules", fsize=25, font='stix')
breakline()

print Image("resources/me.png")
breakline()

print Image("resources/redhat-logo.png")
breakline()

print Image("resources/fedora-logo.png")
breakline()

print Image("resources/fedmsg.png")
print Text("fedmsg", fsize=45, font='stix')
breakline()

print Text("Agenda!", fsize=45, font='stix')
breakline(5)
print Text("sqlalchemy", fsize=26, font='stix')
print Text("sh", fsize=26, font='stix')
print Text("fabulous", fsize=26, font='stix')
print Text("BeautifulSoup", fsize=26, font='stix')
print Text("pandas", fsize=26, font='stix')

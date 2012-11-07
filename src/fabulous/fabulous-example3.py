import os
from fabulous.image import Image

filename = os.path.expanduser("~/yay.png")
print Image(filename)

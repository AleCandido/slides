#!/usr/bin/env python3

import argparse
import subprocess
from io import BytesIO
from base64 import b64decode

from PIL import Image
import pyperclip

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("-i", "--image", action="store_true")
args = parser.parse_args()

if not args.image:
    imagestr = pyperclip.paste()

    im = Image.open(BytesIO(b64decode(imagestr.split(",")[1])))
    im.save(f"{args.name}.png")
else:
    result = subprocess.run(
        f"xclip -selection clipboard -t image/png -o".split(), stdout=subprocess.PIPE
    )
    with open(f"{args.name}.png", "wb") as fd:
        fd.write(result.stdout)

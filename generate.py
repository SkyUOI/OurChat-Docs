#!/usr/bin/env python3

import os
import sys

if len(sys.argv) > 1:
    lang = sys.argv[1]
else:
    lang = "en"
os.putenv("READTHEDOCS_LANGUAGE", lang)
os.chdir("docs")
os.system("make html")
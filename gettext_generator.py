#!/usr/bin/env python3

import os

os.chdir("docs")
os.system("make gettext")
os.system("sphinx-intl update -p build/gettext -l en")
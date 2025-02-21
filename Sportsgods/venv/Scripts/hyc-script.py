#!c:\users\special.desktop-qfkaeub\sportsgods\venv\scripts\python.exe
# -*- coding: utf-8 -*-
# EASY-INSTALL-ENTRY-SCRIPT: 'hy==1.0.0','console_scripts','hyc'
__requires__ = 'hy==1.0.0'
import re
import sys

from hy.cmdline import hyc_main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(hyc_main())

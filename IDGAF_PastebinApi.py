#!/usr/bin/env python

import argparse
import sys
import os
sys.path.append(os.getcwd()+'/src')
from pdc import PsDump

# version = '0.0.1'
# parser = argparse.ArgumentParser(prog='IDGAF_PastebinAPI', description="IDGAF-PastebinAPI\nVersion:"+version)
# parser.add_argument('--version', action='version', version="%(prog)s \nVersion: "+version)
# args = parser.parse_args()

# TODO: 
# 1. Add File check for all Required SRC files 
# 2. Implement argParse
# O. Output to a file
# 4. Input Sanitization

print(PsDump.check_psDump(sys.argv[1]))

#!/usr/bin/env python

import argparse
import sys
import os
from datetime import datetime

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

def get_psDump(keyword):
    
    # -- Check for Output directory, if not exist it creates --
    if os.path.exists('Outputs') == 0:
        os.makedirs('Outputs')

    # -- Open a write mode file --
    psOutFile = open('Outputs/output_'+ datetime.now().strftime("%d%m%Y-%H%M%S")+'.csv','w')
    psOutFile.writelines('KEYWORD,URL\n')

    # -- Check for bin dumps in psdump --
    dumpList = PsDump.check_psDump(keyword)

    # -- Check if List is empty --
    if dumpList == []:
        print("Keyword: "+keyword+ "\nNo result Found !!!\nOmitting saving this to the output")
    
    # -- Print and save output
    else:
        for urls in dumpList:
            print(urls) 
            psOutFile.writelines(keyword+','+urls+"\n")



if __name__ == '__main__':
    get_psDump(sys.argv[1])
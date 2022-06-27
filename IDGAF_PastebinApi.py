#!/usr/bin/env python

import argparse
import sys
import os
from datetime import datetime
import textwrap

sys.path.append(os.getcwd()+'/src')
from pdc import PsDump

version = '1.0.0'
parser = argparse.ArgumentParser(
    prog='IDGAF_PastebinAPI', 
    description=textwrap.dedent('''\
    IDGAF-PastebinAPI | 
    Version:'''+version+ ''' |
    Code by: HexC0d3
    '''))
# parser.add_argument('--version', action='version', version="%(prog)s \nVersion: "+version)
# parser.add_argument('-s',type=str, help="Keyword to Search" )
# parser.add_argument('-iL',type=str, help="Input Text File containing list of Keywords" )
inputGroup = parser.add_mutually_exclusive_group()
inputGroup.add_argument('-s' , '--search', type=str, help="Keyword to Search")
inputGroup.add_argument('-iL', '--input', type=str, help="Input Text File containing list of Keywords")
args = parser.parse_args()

# TODO: 
# 1. Add File check for all Required SRC files 
# 2. Implement argParse
# O. Output to a file
# 4. Input Sanitization

# Set Keyword a single query or file
if (args.search):
    keyword = args.search
elif (args.input):
    keyword = args.input

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
    get_psDump(keyword)
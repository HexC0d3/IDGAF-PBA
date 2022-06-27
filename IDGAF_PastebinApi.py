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

inputGroup = parser.add_mutually_exclusive_group()
inputGroup.add_argument('-s' , '--search', type=str, help="Keyword to Search")
inputGroup.add_argument('-iL', '--input', type=str, help="Input Text File containing list of Keywords")
args = parser.parse_args()

# TODO: 
# 1. Add File check for all Required SRC files 
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
    psOutFile = open('Outputs/output_'+ datetime.now().strftime("%d%m%Y-%H%M%S")+'.csv','a')
    psOutFile.writelines('KEYWORD,URL\n')

    # -- Querying from a File (if arg passed) --
    # -- Check if File exist, if exists File Arg was passed else keyword query.
    if (os.path.exists(keyword)):
        inFile = open(keyword,'r')
        queries = inFile.readlines()
        
        for query in queries:
            dumpList = PsDump.check_psDump(query)
            if dumpList == []:
                print("Keyword: "+query+ "\nNo result Found !!!\nOmitting saving this to the output")
            else:
                print('Keyword: '+query)
                for urls in dumpList:
                    print(urls) 
                    psOutFile.writelines(query+','+urls+"\n")
        # -- Close opened input file -- 
        inFile.close()

    
    else : 
        # -- Check for bin dumps in psdump --
        dumpList = PsDump.check_psDump(keyword)

        # -- Check if List is empty --
        if dumpList == []:
            print("Keyword: "+keyword+ "\nNo result Found !!!\nOmitting saving this to the output")
        
        # -- Print and save output
        else:
            print('Keyword: '+keyword)
            for urls in dumpList:
                print(urls) 
                psOutFile.writelines(keyword+','+urls+"\n")
    
    # -- Close all open files --
    psOutFile.close()
    






if __name__ == '__main__':
    get_psDump(keyword)
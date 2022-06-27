#!/usr/bin/env python
from multiprocessing.sharedctypes import Value
import requests
from bs4 import BeautifulSoup
import sys
import re


class pdc:
    def check_psDump(searchKeyword):
        psUrl = 'https://psbdmp.ws/'

        headers = {
            'authority': 'psbdmp.ws',
            'cache-control': 'max-age=0',
            'origin': 'https://psbdmp.ws/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'referer': 'https://psbdmp.ws/',
            'accept-language': 'en-US,en;q=0.9'

        }

        # -- Insecure Arg is used change later
        data = {
            '_token':'',
            'search': searchKeyword
        }

        with requests.Session() as s:
            # -- Initial Request for Token --
            firstResponse = s.get(url='https://psbdmp.ws/', headers=headers)

            # -- Looking for Token --
            firstSoup = BeautifulSoup(firstResponse.text,'html.parser')
            token = firstSoup.find('input',{'name':'_token'})['value']
            #print('token: ', token )

            # -- Run Post with new Token --
            data['_token'] = token

            searchResponse = s.post(url='https://psbdmp.ws/search', data=data, headers=headers )

            # -- Get All Lists of the Results --

            if (searchResponse.status_code == 200):
                rawList = BeautifulSoup(searchResponse.text,'html.parser').find_all('p',{'class':'title is-4'})
                
                # -- Use Regex to further filter the raw list to actual dump lists --
                
                reLinks = re.compile(r'/dump/[a-zA-Z0-9]+')
                dumpList = reLinks.findall(str(rawList))

                # -- Iterate over dumpList to get URL part of the pastebin --

                for paste in dumpList:
                    print('https://pastebin.com/'+ paste.split('/')[2])


if __name__ == '__main__':
    pdc.check_psDump(sys.argv[1])

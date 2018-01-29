#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Radio Petrov Now Playing
Copyright © 2018-2020 Petr Cizmar

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import requests
import random
import os
import sys
import time
import getopt
import json

# Getting http proxy from environment
proxy_string = os.environ.get("http_proxy")
prxs = {'https': proxy_string} if proxy_string else {}

def usage():
    print("Radio Petrov Now Playing")
    print("Petr Cizmar, 2018")
    print()
    print("Usage: {0} [-h/--help] [-w/--watch]".format(sys.argv[0]))

def get_petrov_palying_now():
    """gets the info from the web"""
    time_string = time.strftime('%Y%m%d%H%M%S')
    url = "https://data.radia.cz/data/pravehraje/new-272-currentnext.json?time={}".format(time_string)
    r = requests.get(url, proxies = prxs)
    data = json.loads(r.text)['current']
    return data['interpret'], data['song']

def print_it():
    a,s = get_petrov_palying_now()
    print("{0}: {1}".format(a,s))

def watch_it():
    prev = None
    while (True):
        a, s = get_petrov_palying_now()
        if prev != s:
            prev = s
            print("{0}: {1}".format(a,s))
        time.sleep(60)

def main(): 
    """main"""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hw", ["help", "watch"])

    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(1)

    for option, argument in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit(1)
        elif option in ("-w", "--watch"):
            watch_it()
            sys.exit(0)
            
    print_it()

if __name__ == '__main__':
    main()

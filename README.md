# RepuChecker @2019


	 _   ___                ___ _           _                 _   __    _ 
	| | | _ \___ _ __ _  _ / __| |_  ___ __| |_____ _ _  __ _/ | /  \  | |
	| | |   / -_) '_ \ || | (__| ' \/ -_) _| / / -_) '_| \ V / || () | | |
	| | |_|_\___| .__/\_,_|\___|_||_\___\__|_\_\___|_|    \_/|_(_)__/  | |
	|_|         |_|                                                    |_|
		
		The Reputation Checker on VT - McAffee - AbuseIpDB [ @2019 ]

Developed by @FerdiGul  
You have an idea about project? Contact me : @0xfrd1

Note: Details of project are on my blog: https://ferdigul.com/repuchecker-v1tool

RepuChecker Tool help you to check URL/IP reputation on some platform such as security engines and ip database..

For now, only these engines I've listed as you can see below:

McAfee ( https://www.trustedsource.org/ | McAfee Web Gateway v7.x/6.9.x (Resident) ),
VirusTotal ( https://www.virustotal.com/gui/home/url ),
AbuseIpDB ( https://www.abuseipdb.com/ ),

So, what can we perform via engines or dbs ?:

In All of engines or dbs listed options, cheackable only single url/ip or one more than one urls or ips. 


Which version of Python do I need?
Any Python 2.x version >= 2.7.0. mechanize does not currently support python 3.
#Install Python 2.7.x: https://www.python.org/downloads/release/python-2716/

What dependencies does mechanize need?
html5lib

Install pip on Windows:
	https://bootstrap.pypa.io/get-pip.py
	python get-pip.py

Install Modules for project:
	import mechanize
	from BeautifulSoup import BeautifulSoup
	import sys
	import datetime
	import Tkinter
	import tkFileDialog
	import requests
	import time
	from random import choice
	
Example: >pip install mechanize

Note: on VT option you can see some notice about usage of api key: 
	The Public API is limited to 4 requests per minute.
	The Public API must not be used in commercial products or services.
	The Private API returns more threat data and exposes more endpoints.
	The Private API is governed by an SLA that guarantees readiness of data.
But you can send random http headers and api keys for pass it :). But if you want to use your premium api key, yes only you can add your api key in this section:

def checkDomain_VT(urlist):

	api = ['   <api key is here>   ']


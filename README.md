# RepuChecker @2019


	 _   ___                ___ _           _                 _   __    _ 
	| | | _ \___ _ __ _  _ / __| |_  ___ __| |_____ _ _  __ _/ | /  \  | |
	| | |   / -_) '_ \ || | (__| ' \/ -_) _| / / -_) '_| \ V / || () | | |
	| | |_|_\___| .__/\_,_|\___|_||_\___\__|_\_\___|_|    \_/|_(_)__/  | |
	|_|         |_|                                                    |_|
		
		The Reputation Checker on VT - McAffee - AbuseIpDB [ @2019 ]

Developed by @FerdiGul  
You have an idea about project? Contact me : @0xfrd1


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

#Check Reputation of url on VT,McAffee and AbuseIpDB
#Developed by Ferdi Gül  | @0xfrd1

# -*- coding: utf-8 -*-

import mechanize
from BeautifulSoup import BeautifulSoup
import sys
import datetime
import Tkinter
import tkFileDialog
import requests
import time
from random import choice



br= mechanize.Browser()
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
count=0
#set randomly user-agent..
def agent(p):
	desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
						 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
						 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
						 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
						 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
						 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
						 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
						 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
						 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11']
	
		

	br.addheaders=[('User-Agent',desktop_agents[p]),('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Charset','ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding','none'),('Accept-Language','en-US,en;q=0.8'),('Connection','keep-alive')] 
			
	
	
	return br.addheaders
		
def checkDomain_VT(urlist):
	
	
	api = ['4c0682eb9257c663c6e3dd594b43431cdf1e4919b25cf83ed7111ecd31fecc44','b8482dde75fba3bd03bab2771a82e547d5ba651e366bc901d07e00ee2abde28c','93f8ca6bba891cbca1bd7d8a1850c839a0ca8e528ddcdd1d5c18e049dfe04d08','ac682438e4c5fbe08191647ca359c8a1158ff21978a4315f6599e3b5fb3490e1']
	
	r=0
	x=0
	global p
	p=0
	
	for blacklist in urlist:
		
		#agent()
		#url = 'https://www.virustotal.com/vtapi/v2/url/scan'

		
		
		if r<3:
			agent(p)
			time.sleep(1)
				#OK! for user-agentdesktop_agents[p]
			item = api[x]
			url = 'https://www.virustotal.com/vtapi/v2/url/scan'
			params = {'apikey':item, 'url':blacklist}
			response = requests.post(url, data=params)
			time.sleep(3)
			r+=1
			p+=1
			if p==5:
				p=0
			#print "api: {item}".format(item=item)
			time.sleep(1)
			
			
		if r>=3:
			x+=1
			r=0
			p=0
			agent(p)
			time.sleep(1)
			item = api[x]
			url = 'https://www.virustotal.com/vtapi/v2/url/scan'
			params = {'apikey':item, 'url':blacklist}
			response = requests.post(url, data=params)
			time.sleep(3)
			r+=1
			p+=1
			if p==5:
				p=0
			print "api:" + item
			time.sleep(1)
			
		"""
		if r>=3 and r<5:
			agent()
			url = 'https://www.virustotal.com/vtapi/v2/url/scan'
			item = api[1]
			params = {'apikey':item, 'url':blacklist}
			response = requests.post(url, data=params)
			r+=1
			print item
		"""
		
		
		#print response.json()
		json_response = response.json()
		time.sleep(1)
		result=br.open(json_response.values()[0])
		time.sleep(1)
		soup = BeautifulSoup(result.read())
		time.sleep(1)
		resultTable=soup.findAll('table')[0]
		engines = soup.findAll('table')[1]
		#column_name=resultTable.findAll('b')
		#t_name=resultTable.findAll('td')
		#t1=t_name[2].text
		#t2=t_name[3].text

		#print t1,t2+"\n"
		

		for summary in resultTable.findAll('tr')[0:2]:
			result=summary.text
			print result+":"+"\n"+30*"-"	
		i=0
		n=1
		list_of_rows=[]
		
		with open(r'C:\Users\fgcom\Desktop\vt.html','a+') as output:
			output.writelines( "<br>"+"""<html><font color="black"><b> Report [ {domain} ]:   Detection [ {detect}] </b></font></html>""".format(domain=blacklist,detect=result)+"<br><br>")
			output.close()
				
		for row in engines.findAll('tr')[1:5]:
			list_of_cells = []
			for cell in row.findAll('td'):
				text = cell.text
				list_of_cells.append(text)
					
			list_of_rows.append(list_of_cells)
			print list_of_rows[i][0] +"\t"+list_of_rows[i][n]
			
			
			with open(r'C:\Users\fgcom\Desktop\vt.html','a+') as output:
				output.writelines("""<html>
					<body style=" background-position: center;
						 background-repeat: no-repeat;
						 background-size: cover; background-image:url('logo_vt.png');">
						 <table cellpadding="3" cellspacing="1" border="1" width="600px" style="margin-top: 0px; " align="center">
							<tbody>
							
							<tr>
								<th align="left" valign="middle" width="200px" bgcolor="#33adff">
									<b>Engine</b>
								</th>
								<th align="left" valign="middle" width="100px" bgcolor="#33adff">
									<b>Status</b>
								</th>
								
								
							</tr>
			
							<tr bgcolor="#ffffff">
								<td align="left" valign="top" nowrap="nowrap" width="200px " >{value_name1}</td>
								<td align="left" valign="top" nowrap="nowrap" width="100px " >{value_name2}</td>
								
							</tr>	
							</tbody>
						</table>
							
							
					</body>
				</html>""".format(value_name1=list_of_rows[i][0],value_name2=list_of_rows[i][n]))
				
					
			output.close()
			i+=1







def checkDomain_McAfee(urlist):
	
	p=0
	for blacklist in urlist:
		agent(p)
		time.sleep(1)
		#print br.addheaders
		br.open("https://trustedsource.org/sources/index.pl")
		time.sleep(2)
		br.form = list(br.forms())[0]  
		control=br.form.find_control("product").items
		#print blacklist
		for item in control:
			if item.name =='15-xl':
				item.selected = True
				br.form['url']=blacklist
				response=br.submit()
				time.sleep(3)

		soup = BeautifulSoup(response.read())
		time.sleep(2)
		resultTable=soup.findAll('table')[1]
		#column_name=resultTable.findAll('b')
		tr=resultTable.findAll('tr')[1]
		value_name=tr.findAll('td')
		v1=value_name[1].text
		v2=value_name[2].text
		v3=value_name[3].text
		if v3 =="":
			v3="**********"
		v4=value_name[4].text
		if v4=="High Risk":
			colorCode ="bgcolor=#ff0000"
		if v4=="Minimal Risk":
			colorCode ="bgcolor=#00b300"
		else:
			colorCode ="bgcolor=white"
		today=datetime.datetime.now()
		v5=today.strftime('%Y-%m-%d %H:%M:%S')
		
	
		
		"""
		print value_name[1].text #url name
		print value_name[2].text #url name
		print value_name[3].text #url name
		print value_name[4].text #url name
		"""
		#result=resultTable.findAll('tr',{'bgcolor':"#ffffff"})
		#a=resultTable.find('tbody')
		#output.truncate()
		time.sleep(2)
		with open(r'C:\Users\fgcom\Desktop\result.html','a+') as output:
			output.writelines("""<html><body style="background-image:url('logo.png'); background-position: center;
		 background-repeat: no-repeat;
		 background-size: cover; bgcolor="black";><table cellpadding="3" cellspacing="1" border="1" width="600px" style="margin-top: 15px; " align="center">
			<tbody>
			<tr>
				<th align="left" valign="middle" width="200px" bgcolor="#33adff">
					<b>URL</b>
				</th>
				<th align="left" valign="middle" width="100px" bgcolor="#33adff">
					<b>Status</b>
				</th>
				<th align="left" valign="middle" width="300px" bgcolor="#33adff">
					<b>Categorization</b>
				</th>
				<th align="left" valign="middle"  width="200px" bgcolor="#33adff">
					<b>Reputation</b>
				</th>
				<th align="left" valign="middle"  width="100px" bgcolor="#33adff">
					<b>Checked Time</b>
				</th>
			</tr>
			<tr bgcolor="#ffffff">
				<td align="left" valign="top" nowrap="nowrap" width="200px " {color}>{value_name1}</td>
					<td align="left" valign="top" nowrap="nowrap" width="100px " {color}>{value_name2}</td>
					<td align="left" valign="top" nowrap="nowrap" width="300px " {color}>{value_name3}<br></td>
					<td align="left" valign="top" nowrap="nowrap" width="200px " {color}>{value_name4}<br></td>
					<td align="left" valign="top" nowrap="nowrap" width="200px " {color}>{value_name5}<br></td>

			</tbody></table>
			
			
			</body></html>""".format(value_name1=v1,value_name2=v2,value_name3=v3,color=colorCode,value_name4=v4,value_name5=v5))

		print 50*"-"+"\n"+"Checked: {v1}\n\nStatus: {v2}\tCategorization: {v3}".format(v1=v1,v2=v2,v3=v3)
		global count
		count +=1
	#output.close()

def checkDomain_abuseipdb(urlist):
	global p
	p=0
	for blacklist in urlist:
		agent(p)
		time.sleep(2)
		#print br.addheaders
		br.open("https://www.abuseipdb.com/")
		time.sleep(1)
		br.form = list(br.forms())[0]  
		br.form["query"]=blacklist
		response=br.submit()
		
		#print response.read()
		time.sleep(3)
		soup = BeautifulSoup(response.read())
		time.sleep(2)
		localhost=soup.findAll('i')[0]
		p+=1
		if p==6:
			p=0
			
		if localhost.text=='127.0.0.1':
			print "\n\n [ {ip} ] is Local Host Ip: 127.0.0.1".format(ip=blacklist)+"\n"
		
		tek=soup.findAll('b')[1]
		#tekx=soup.findAll('b')[0]
		
		if tek.text!='We can\'t resolve the domain {dom}!'.format(dom=blacklist) and localhost.text!='127.0.0.1':
			
			resulth3=soup.findAll('h3')[0]
			##print ">>>> "+resulth3.text
				
			resultP = soup.findAll('p')[1] #total 14 p 
			#print resultP.text +"\n\n\n\n"
			
			
			#resultPx = soup.findAll('p')[3]
			#print len(resultPx.text)

			resultPx = soup.findAll('p')[2]
			#print resultPx.text
			#if len(resultPx.text)!=60:
			
			if "not" not in resultPx.text:
				resultTable=soup.findAll('table')[1]
				#print len(resultTable)
				print resultP.text +"\n\n"
				i=0
				n=1
				list_of_rows=[]
				today=datetime.datetime.now()
				v4=today.strftime('%Y-%m-%d %H:%M:%S')
				
				with open(r'C:\Users\fgcom\Desktop\aidb.html','a+') as output:
					output.writelines( """<html><font color="white"><b> Report [ {domain} ]: </b></font></html>""".format(domain=blacklist))
				output.close()
			
		
				while i<3:
					
					for row in resultTable.findAll('tr')[1:]:
						list_of_cells = []
						for cell in row.findAll('td'):
							text = cell.text
							list_of_cells.append(text)
						list_of_rows.append(list_of_cells)
					print list_of_rows[i][0]+" 	| 	"+list_of_rows[i][1]+" 	| 	"+list_of_rows[i][3]
					
					time.sleep(3)
					with open(r'C:\Users\fgcom\Desktop\aidb.html','a+') as output:
							output.writelines("""<html>
					<body style=" background-position: center;
						 background-repeat: no-repeat;
						 background-size: cover; background-image:url('logo_aidb.png');">
						 <table cellpadding="3" cellspacing="1" border="1" width="600px" style="margin-top: 0px; " align="center">
							<tbody>
							<tr>
								<th align="left" valign="middle" width="200px" bgcolor="#33adff">
									<b>Reporter</b>
								</th>
								<th align="left" valign="middle" width="100px" bgcolor="#33adff">
									<b>Date</b>
								</th>
								<th align="left" valign="middle" width="300px" bgcolor="#33adff">
									<b>Categories</b>
								</th>
								
							</tr>
							
							
							
							<tr bgcolor="#ffffff">
								<td align="left" valign="top" nowrap="nowrap" width="200px " >{value_name1}</td>
								<td align="left" valign="top" nowrap="nowrap" width="100px " >{value_name2}</td>
								<td align="left" valign="top" nowrap="nowrap" width="300px " >{value_name3}<br></td>
							</tr>	
							</tbody>
						</table>
							
							
					</body>
				</html>""".format(value_name1=list_of_rows[i][0],value_name2=list_of_rows[i][1],value_name3=list_of_rows[i][3],value_name4=v4))
				
					i+=1
				
					
				output.close()
			

			else:
				print "\n"+"!!!!! "+resulth3.text +"\n"
			
		

		if tek.text=='We can\'t resolve the domain {dom}!'.format(dom=blacklist):
			print 'We can\'t resolve the domain {dom}!'.format(dom=blacklist)
		
		
		
def api_random():

	api = ['ac682438e4c5fbe08191647ca359c8a1158ff21978a4315f6599e3b5fb3490e1','4c0682eb9257c663c6e3dd594b43431cdf1e4919b25cf83ed7111ecd31fecc44','b8482dde75fba3bd03bab2771a82e547d5ba651e366bc901d07e00ee2abde28c','93f8ca6bba891cbca1bd7d8a1850c839a0ca8e528ddcdd1d5c18e049dfe04d08']
	
	#napi=choice(api)
	item = random.choice(api)
	
	return item



	
def main():
	try:
		print("\n"+"Please select your option:	"+"\n\n"+"[1].McAfee"+"\n"+"[2].VT"+"\n"+"[3].AbuseIpDB"+"\n"+":")
		option=raw_input()

		if option=='1':
			print("\n"+"Please select your option:	"+"\n\n"+"[1].Check Single URL.."+"\n"+"[2].Check URL List File.."+"\n"+":")
			selection=raw_input()
			
			if selection=='1':
				singleUrl = raw_input('Enter the single url : ')
				urlist = singleUrl.split()
				print """\n\n Single URL is checking on VT..Please wait..\n\n\n\n """
				checkDomain_McAfee(urlist)


			if selection=='2':
				
				Tkinter.Tk().withdraw() # Close the root window
				in_path = tkFileDialog.askopenfilename()
				urlist = tuple(open(in_path,'r'))
				print """\n\nAll Urls are checking on VT..Please wait..\n\n\n\n"""
				checkDomain_McAfee(urlist)
				
				print (20*"-"+"""Total Url : [ {toplam} ]"""+20*"-").format(toplam=count)
			else:
				
				time.sleep(0.5)
				sys.exit(0)
		
		if option=='2':
			print("\n"+"Please select your option:	"+"\n\n"+"[1].Check Single URL.."+"\n"+"[2].Check URL List File.."+"\n"+":")
			selection=raw_input()
			
			if selection=='1':
				singleUrl = raw_input('Enter the single url : ')
				urlist = singleUrl.split()
				print """\n\n Single URL is checking on McAffee DB..Please wait..\n\n\n\n """
				checkDomain_VT(urlist)
			if selection=='2':
				
				Tkinter.Tk().withdraw() # Close the root window
				in_path = tkFileDialog.askopenfilename()
				urlist = tuple(open(in_path,'r'))
				print """\n\nAll Urls are checking on McAffee DB..Please wait..\n\n\n\n"""
				checkDomain_VT(urlist)
				cnt=len(urlist)
				print (20*"-"+"""Total Url : [ {toplam} ]"""+20*"-").format(toplam=cnt)
			else:
				time.sleep(0.5)
				sys.exit(0)
				
			
		if option=='3':
			print("\n"+"Please select your option:	"+"\n\n"+"[1].Check Single URL.."+"\n"+"[2].Check URL List File.."+"\n\n"+":")
			selection=raw_input()
			if selection=='1':
				singleUrl = raw_input('Enter the single url : ')
				urlist = singleUrl.split()
				print """\n\n Single URL is checking on ABUSE IP DB..Please wait..\n\n\n\n """
				#checkDomain_VT(urlist)	
				checkDomain_abuseipdb(urlist)
			elif selection=='2':
				Tkinter.Tk().withdraw() # Close the root window
				in_path = tkFileDialog.askopenfilename()
				urlist = tuple(open(in_path,'r'))
				print """\n\nAll Urls are checking on ABUSE IP DB..Please wait..\n\n\n\n"""
				checkDomain_abuseipdb(urlist)
				cnt=len(urlist)
				print (20*"-"+"""Total Url : [ {toplam} ]"""+20*"-").format(toplam=cnt)
			else:
				print ("""Program is being closing...""")
				time.sleep(0.5)
				sys.exit(0)
			
		else:
			print ("""Program is being closing...""")
			time.sleep(0.5)
			sys.exit(0)
	
			
	except:
			pass

if "__name__=__main__":
	main()

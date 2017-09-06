#!/usr/local/bin/python3
import json
 
hostlist = {'db':['10.200.11.10','10.200.11.11'],'web':['10.200.11.17','10.200.11.180'],'zabbix':['10.200.11.180']}
 
print (json.dumps(hostlist))

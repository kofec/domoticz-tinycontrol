#!/usr/bin/python3
import urllib.request
import xmltodict
import argparse

parser = argparse.ArgumentParser(description='Comunicate with Tinycontrol.')
parser.add_argument('IPaddress', help='IP address of TinyControl' )
parser.add_argument('--user', help='User name to login to', default='admin')
parser.add_argument('--password', help='Password to login to', default='admin')

args = parser.parse_args()
print(args)

urll = 'http://' + args.IPaddress + '/st0.xml'
username = args.user
password = args.password

# create a password manager
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# Add the username and password.
# If we knew the realm, we could use it instead of None.
passman.add_password(None, urll, username, password)

authhandler = urllib.request.HTTPBasicAuthHandler(passman)
# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(authhandler)
# use the opener to fetch a URL
pagehandle = opener.open(urll)

data = pagehandle.read()
pagehandle.close()
print (data)

data = xmltodict.parse(data)
print(data)
data = data['response']
print(data)
print("Number of items in dictionary: ", len(data.keys()))

urll = 'http://' + args.IPaddress + '/st2.xml'

# create a password manager
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# Add the username and password.
# If we knew the realm, we could use it instead of None.
passman.add_password(None, urll, username, password)

authhandler = urllib.request.HTTPBasicAuthHandler(passman)
# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(authhandler)
# use the opener to fetch a URL
pagehandle = opener.open(urll)

data = pagehandle.read()
pagehandle.close()
print (data)

data = xmltodict.parse(data)
print(data)
data = data['response']
print(data)
print("Hardware version:", data['hw'], "Software version:", data['ver'])
print("Number of items in dictionary: ", len(data.keys()))
print("Number of hw key", list(data.keys()).index('hw'))

urll = 'http://' + args.IPaddress + '/outs.cgi?out1=0'
passman.add_password(None, urll, username, password)

authhandler = urllib.request.HTTPBasicAuthHandler(passman)
# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(authhandler)
# use the opener to fetch a URL
pagehandle = opener.open(urll)

data = pagehandle.read()
pagehandle.close()
print (data)



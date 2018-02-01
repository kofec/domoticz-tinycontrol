#!/usr/bin/python3
import urllib.request
import argparse
import subprocess
import sys
import os
from pathlib import Path
pathOfPackages='/usr/local/lib/python3.5/dist-packages'

parser = argparse.ArgumentParser(description='Comunicate with Tinycontrol.')
parser.add_argument('IPaddress', help='IP address of TinyControl' )
parser.add_argument('--user', help='Username to login to', default='admin')
parser.add_argument('--password', help='Password to login to', default='admin')
parser.add_argument('--st2', action='store_true', help='if define output of st2.xml is printed')
parser.add_argument('--out', nargs=2, metavar=('<port number>', 'ON/OFF'), help='eg. --out 1 ON - when turn ON out1')
parser.add_argument('--debug', action='store_true', help='if define more output is printed')

args = parser.parse_args()
if args.debug:
    print(args)

if args.debug:
    print("Current paths where search for modules: " + str(sys.path))

if Path(pathOfPackages).exists():
    if args.debug:
        print("Adding path: " + pathOfPackages)
    sys.path.append(pathOfPackages)
    import xmltodict
else:
    print("It can be an issue with import package xmltodict")
    print("Find where is located package xmltodict and correct variable: pathOfPackages")
    print("pathOfPackages:", pathOfPackages)
    import xmltodict

username = args.user
password = args.password

try:
    subprocess.call(["bash", "--version"])
except OSError as e:
    if e.errno == os.errno.ENOENT:
        print("Cannot find wget command")
        exit()
    else:
        print("Error when checking if wget exist")
        raise

try:
    subprocess.call(["wget", "--version"])
except OSError as e:
    if e.errno == os.errno.ENOENT:
        print("Cannot find wget command")
        exit()
    else:
        print("Error when checking if wget exist")
        raise

if args.debug:
    print(subprocess.check_output(['bash', '-c', 'wget --version']))

if args.out:
    if int(args.out[0]) in range(6) and (args.out[1] in ["OFF", "ON"]):
        if args.out[1] == "ON":
            args.out[1] = "1"
        else:
            args.out[1] = "0"
        urll = 'http://' + args.IPaddress + '/outs.cgi?out' + args.out[0] + '=' + args.out[1]
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
        if args.debug:
            print (data)
    else:
        print("Incorrect parameters")
        # change to exception


if args.st2:
    urll = 'http://' + args.IPaddress + '/st2.xml'
else:
    urll = 'http://' + args.IPaddress + '/st0.xml'

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
if args.debug:
    print(data)
# chop b' .... '
print(str(data)[2:-1])
if args.debug:
    data = xmltodict.parse(data)
    print(data)
    data = data['response']
    print(data)
    print("Number of items in dictionary: ", len(data.keys()))


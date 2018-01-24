#!/usr/bin/python3
import urllib.request
import argparse
import sys

from pathlib import Path
pathOfPackages='/usr/local/lib/python3.5/dist-packages'

if Path(pathOfPackages).exists():
    sys.path.append('/usr/local/lib/python3.5/dist-packages')
    import xmltodict
else:
    Print("It can be an issue with import package xmltodict")
    Print("Find where is located package xmltodict and correct variable: pathOfPackages")
    Print("pathOfPackages:", pathOfPackages)
    import xmltodict

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

username = args.user
password = args.password

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


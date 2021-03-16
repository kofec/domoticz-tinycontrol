#!/usr/bin/python3
import argparse
import subprocess
import sys
import os
from pathlib import Path
pathOfPackages='/usr/local/lib/python3.9/dist-packages'

parser = argparse.ArgumentParser(description='Comunicate with Tinycontrol.')
parser.add_argument('IPaddress', help='IP address of TinyControl' )
parser.add_argument('--user', help='Username to login to', default='admin')
parser.add_argument('--password', help='Password to login to', default='admin')
parser.add_argument('--st2', action='store_true', help='if define output of st2.xml is printed')
parser.add_argument('--out', nargs=2, metavar=('<port number>', 'ON/OFF'), help='eg. --out 1 ON - when turn ON out1')


args = parser.parse_args()
print(args)
print("Current paths where search for modules: " + str(sys.path))

if Path(pathOfPackages).exists():
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

print(subprocess.check_output(['bash', '-c', 'which wget']).decode())

if args.out:
    if int(args.out[0]) in range(6) and (args.out[1] in ["OFF", "ON"]):
        if args.out[1] == "ON":
            args.out[1] = "1"
        else:
            args.out[1] = "0"
        url = "http://"
        if username and password:
            url += username + ':' + password + '@'
        url += str(args.IPaddress) + '/outs.cgi?out' + args.out[0] + '=' + args.out[1]
        print("Connect via wget to website: wget -q -O - " + url)
        data = subprocess.check_output(['bash', '-c', 'wget -q -O - ' + url])
        print(data.decode())
    else:
        print("Incorrect parameters")
        # change to exception


url = "http://"
if username and password:
    url += username + ':' + password + '@'

if args.st2:
    url += args.IPaddress + '/st2.xml'
else:
    url += args.IPaddress + '/st0.xml'

print("Connect via wget to website: wget -q -O -" + url)
try:
    data = subprocess.check_output(['bash', '-c', 'wget -q -O - ' + url])
    print(data)
    data = xmltodict.parse(data)
    print(data)
    data = data['response']
    print(data)
    print("Number of items in dictionary: ", len(data.keys()))
except subprocess.CalledProcessError as e:
    print("wget return error:")
    print(e.output)
    print(e.cmd)
    print(e.stderr)
    print(e.returncode)
    url = "http://"
    if username and password:
        url += username + ':' + password + '@'
    url += args.IPaddress + '/xml/ix.xml'
    print("Connect via wget to website: wget -q -O -" + url)
    try:
        data = subprocess.check_output(['bash', '-c', 'wget -q -O - ' + url])
        print(data)
        data = xmltodict.parse(data)
        print(data)
        data = data['response']
        print(data)
        print("Number of items in dictionary: ", len(data.keys()))
    except subprocess.CalledProcessError as e:
        print("wget return error:")
        print(e.output)
        print(e.cmd)
        print(e.stderr)
        print(e.returncode)



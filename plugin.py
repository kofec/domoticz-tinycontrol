#           Enigma2 Python Plugin for Domoticz
#
#
#           Dev. Platform : Win10 x64 & Py 3.5.3 x86
#
#           Author:     kofec, 2017
#           1.0.0:  initial release
#
#
#           Resposne for Lan Controler v1
#           ./tinycontrol.py 192.168.1.100
#           Namespace(IPaddress='192.168.1.100',password='admin', user='admin')
# b'<response><out0>1</out0><out1>1</out1><out2>1</out2><out3>1</out3><out4>1</out4
# ><out5>0</out5><di0>up</di0><di1>up</di1><di2>up</di2><di3>up</di3><ia0>381</ia0><ia1>133</ia1><ia2>-528</ia2><ia3
# >-528</ia3><ia4>0</ia4><ia5>8863</ia5><ia6>0</ia6><ia7>315</ia7><ia8>326</ia8><ia9>321</ia9><ia10>315</ia10><ia11
# >324</ia11><ia12>318</ia12><ia13>0</ia13><ia14>0</ia14><ia15>0</ia15><ia16>0</ia16><ia17>0</ia17><ia18>0</ia18
# ><ia19>18</ia19><freq>2553</freq><duty>0</duty><pwm>1</pwm><sec0>37</sec0><sec1>43</sec1><sec2>23</sec2><sec3>13
# </sec3><sec4>165771</sec4></response>'
#
# OrderedDict([('response', OrderedDict([('out0', '1'), ('out1', '1'),
# ('out2', '1'), ('out3', '1'), ('out4', '1'), ('out5', '0'), ('di0', 'up'), ('di1', 'up'), ('di2', 'up'), ('di3',
# 'up'), ('ia0', '381'), ('ia1', '133'), ('ia2', '-528'), ('ia3', '-528'), ('ia4', '0'), ('ia5', '8863'), ('ia6',
# '0'), ('ia7', '315'), ('ia8', '326'), ('ia9', '321'), ('ia10', '315'), ('ia11', '324'), ('ia12', '318'), ('ia13',
# '0'), ('ia14', '0'), ('ia15', '0'), ('ia16', '0'), ('ia17', '0'), ('ia18', '0'), ('ia19', '18'), ('freq', '2553'),
# ('duty', '0'), ('pwm', '1'), ('sec0', '37'), ('sec1', '43'), ('sec2', '23'), ('sec3', '13'), ('sec4',
# '165771')]))])
#
# OrderedDict([('out0', '1'), ('out1', '1'), ('out2', '1'), ('out3', '1'), ('out4', '1'), ('out5',
# '0'), ('di0', 'up'), ('di1', 'up'), ('di2', 'up'), ('di3', 'up'), ('ia0', '381'), ('ia1', '133'), ('ia2', '-528'),
# ('ia3', '-528'), ('ia4', '0'), ('ia5', '8863'), ('ia6', '0'), ('ia7', '315'), ('ia8', '326'), ('ia9', '321'),
# ('ia10', '315'), ('ia11', '324'), ('ia12', '318'), ('ia13', '0'), ('ia14', '0'), ('ia15', '0'), ('ia16', '0'),
# ('ia17', '0'), ('ia18', '0'), ('ia19', '18'), ('freq', '2553'), ('duty', '0'), ('pwm', '1'), ('sec0', '37'),
# ('sec1', '43'), ('sec2', '23'), ('sec3', '13'), ('sec4', '165771')])
# Number of items in dictionary:  38
#
# b'<response><out0>1</out0><out1>1</out1><out2>1</out2><out3>1</out3><out4>1</out4><out5>0</out5><freq>2553</freq
# ><duty>0</duty><ver>3.22</ver><ser>2438</ser><hw>1</hw><na>TINYPIETRO+++++</na><ins>0</ins><k0>0</k0><k1>0</k1><k2
# >0</k2><k3>0</k3><k4>0</k4><k5>10</k5><pt>2</pt><pt2>0</pt2><r0>0</r0><r1>0</r1><r2>0</r2><r3>0</r3><r4>0</r4><r5
# >NotUsed</r5><r6>Out1</r6><r7>Sypialni</r7><r8>Bartek</r8><r9>Ala</r9><a>65535*65535*65535*65535*65535*65535*65535
# *65535*65535*65535*</a><as>0</as><d>Bartek*Sypialni*Lazienka*powrot*Ala*Poddasze*INPD*INPD*INPD*INPD*</d><db>255
# </db><dz>1000</dz><mm>kwh</mm><mh>3</mh><pw>255</pw><ia>1</ia></response>' OrderedDict([('response', OrderedDict([(
# 'out0', '1'), ('out1', '1'), ('out2', '1'), ('out3', '1'), ('out4', '1'), ('out5', '0'), ('freq', '2553'), ('duty',
#  '0'), ('ver', '3.22'), ('ser', '2438'), ('hw', '1'), ('na', 'TINYPIETRO+++++'), ('ins', '0'), ('k0', '0'), ('k1',
# '0'), ('k2', '0'), ('k3', '0'), ('k4', '0'), ('k5', '10'), ('pt', '2'), ('pt2', '0'), ('r0', '0'), ('r1', '0'),
# ('r2', '0'), ('r3', '0'), ('r4', '0'), ('r5', 'NotUsed'), ('r6', 'Out1'), ('r7', 'Sypialni'), ('r8', 'Bartek'),
# ('r9', 'Ala'), ('a', '65535*65535*65535*65535*65535*65535*65535*65535*65535*65535*'), ('as', '0'), ('d',
# 'Bartek*Sypialni*Lazienka*powrot*Ala*Poddasze*INPD*INPD*INPD*INPD*'), ('db', '255'), ('dz', '1000'), ('mm', 'kwh'),
#  ('mh', '3'), ('pw', '255'), ('ia', '1')]))]) OrderedDict([('out0', '1'), ('out1', '1'), ('out2', '1'), ('out3',
# '1'), ('out4', '1'), ('out5', '0'), ('freq', '2553'), ('duty', '0'), ('ver', '3.22'), ('ser', '2438'), ('hw', '1'),
#  ('na', 'TINYPIETRO+++++'), ('ins', '0'), ('k0', '0'), ('k1', '0'), ('k2', '0'), ('k3', '0'), ('k4', '0'), ('k5',
# '10'), ('pt', '2'), ('pt2', '0'), ('r0', '0'), ('r1', '0'), ('r2', '0'), ('r3', '0'), ('r4', '0'), ('r5',
# 'NotUsed'), ('r6', 'Out1'), ('r7', 'Sypialni'), ('r8', 'Bartek'), ('r9', 'Ala'), ('a',
# '65535*65535*65535*65535*65535*65535*65535*65535*65535*65535*'), ('as', '0'), ('d',
# 'Bartek*Sypialni*Lazienka*powrot*Ala*Poddasze*INPD*INPD*INPD*INPD*'), ('db', '255'), ('dz', '1000'), ('mm', 'kwh'),
#  ('mh', '3'), ('pw', '255'), ('ia', '1')])
# Hardware version: 1 Software version: 3.22
# Number of items in dictionary: 40
# Number of hw key 10 b'101111'
#
#
#       
#           Base on website: http://tinycontrol.pl/en/
#           Miscellaneous
#
# Below is what will be displayed in Domoticz GUI under HW
#
"""
<plugin key="LanControler" name="Lan Controler from tinycontrol.pl" author="kofec" version="1.0.0" wikilink="no" externallink="http://tinycontrol.pl/en/lan-controler-v2/">
    <params>
        <param field="Address" label="IP Address" width="200px" required="true" default="127.0.0.1"/>
        <param field="Port" label="Port" width="40px" required="true" default="80"/>
        <param field="Mode1" label="Username" width="200px" required="false" default="admin"/>
        <param field="Mode2" label="Password" width="200px" required="false" default="admin"/>
        <param field="Mode3" label="Which devices should be tracked" width="400px" default=""/>
        <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"  default="True" />
            </options>
        </param>
    </params>
</plugin>
"""
#
# Main Import
import Domoticz
import sys
import os
import argparse

# Python framework in Domoticz do not include OS dependent path
#

if sys.platform.startswith('linux'):
    # linux specific code here#
    sys.path.append('/usr/local/lib/python3.5/dist-packages')
elif sys.platform.startswith('darwin'):
    # mac
    sys.path.append(os.path.dirname(os.__file__) + '/site-packages')
elif sys.platform.startswith('win32'):
    #  win specific
    sys.path.append(os.path.dirname(os.__file__) + '\site-packages')

import urllib.request
import socket
import xmltodict

socket.setdefaulttimeout(2)

class BasePlugin:
    # Connection Status
    isConnected = False

# known and supported keys
    KEY = {
        "out0"          : "Switch",          # Relay/Switch
        "out1"          : "Switch",          # Relay/Switch
        "out2"          : "Switch",          # Relay/Switch
        "out3"          : "Switch",          # Relay/Switch
        "out4"          : "Switch",          # Relay/Switch
        "out5"          : "Switch",          # Relay/Switch
        "ia0"           : "Temperature",    # Board Temperature
        "ia1"           : "Voltage",        # VCC SUPPLY
        "ia7"           : "Temperature",    # ds18b20 Temperature
        "ia8"           : "Temperature",    # ds18b20 Temperature
        "ia9"           : "Temperature",    # ds18b20 Temperature
        "ia10"          : "Temperature",    # ds18b20 Temperature
        "ia11"          : "Temperature",    # ds18b20 Temperature
        "ia12"          : "Temperature"     # ds18b20 Temperature

    }
    # resolve issue when cannot take name from response - search names if doesn't exist take key
    NAMES = {
        "ia0"           : "Board Temperature",  # Board Temperature
        "ia1"           : "VCC SUPPLY",     # VCC SUPPLY
        "ia7"           : "d0",             # ds18b20 Temperature
        "ia8"           : "d1",             # ds18b20 Temperature
        "ia9"           : "d2",             # ds18b20 Temperature
        "ia10"          : "d3",             # ds18b20 Temperature
        "ia11"          : "d4",             # ds18b20 Temperature
        "ia12"          : "d5"              # ds18b20 Temperature
    }

    NAMES_v1 = {
        "out0"          : "r5",             # Relay/Switch
        "out1"          : "r6",             # Relay/Switch
        "out2"          : "r7",             # Relay/Switch
        "out3"          : "r8",             # Relay/Switch
        "out4"          : "r9",             # Relay/Switch
        "out5"          : "r10",            # Relay/Switch
    }

    NAMES_v2 = {
        "out0"          : "r6",             # Relay/Switch
        "out1"          : "r7",             # Relay/Switch
        "out2"          : "r8",             # Relay/Switch
        "out3"          : "r9",             # Relay/Switch
        "out4"          : "r10",            # Relay/Switch
        "out5"          : "r11",            # Relay/Switch
    }

    config = ''
    # Domoticz call back functions
    #
    # Executed once at HW creation/ update. Can create up to 255 devices.

    def onStart(self):
        if Parameters["Mode6"] == "Debug":
            Domoticz.Debugging(1)
            DumpConfigToLog()

        Domoticz.Heartbeat(20)

        self.config = {
            "description": "Domoticz",
            "user": Parameters["Mode1"],
            "password": Parameters["Mode2"],
            "host": Parameters["Address"],
            "port": int(Parameters["Port"]),
        }

        Domoticz.Log("Connecting to: " + Parameters["Address"] + ":" + Parameters["Port"])

        self.isAlive()

        #        if (self.isConnected == True):
        #            if Parameters["Mode6"] == "Debug":
        #                Domoticz.Log("Devices are connected - Initialisation")
        #            UpdateDevice(self.UNIT_STATUS_REMOTE, 1, 'Enigma2 Available')
        #            self.EnigmaDetails()
        #            UpdateDevice(self.UNIT_POWER_CONTROL, 40, '40')

        urll = 'http://' + str(Parameters["Address"]) + '/st0.xml'
        username = str(Parameters["Mode1"])
        password = str(Parameters["Mode2"])
        if Parameters["Mode6"] == "Debug":
            Domoticz.Log("Connect to website: " + str(urll) + " user: " + username + " password: " + password)
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
        st0 = pagehandle.read()
        pagehandle.close()
        st0 = xmltodict.parse(st0)
        st0 = st0['response']

        if Parameters["Mode6"] == "Debug":
            Domoticz.Log("st0.xml :")
            for x in st0.keys():
                Domoticz.Log(str(x) + " => " + str(st0[x]))

        urll = 'http://' + str(Parameters["Address"]) + '/st2.xml'
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
        st2 = pagehandle.read()
        pagehandle.close()
        st2 = xmltodict.parse(st2)
        st2 = st2['response']

        if Parameters["Mode6"] == "Debug":
            Domoticz.Log("st2.xml :")
            for x in st2.keys():
                Domoticz.Log(str(x) + " => " + str(st2[x]))

        if st2['ver'] == '3.22':
            self.NAMES.update(self.NAMES_v1)
        elif st2['ver'] == '3.18':
            self.NAMES.update(self.NAMES_v2)

        for x in Parameters["Mode3"].split(';'):
            if x in self.NAMES.keys() and self.NAMES[x] in st2.keys():
                self.NAMES[x] = st2[self.NAMES[x]]

        if Parameters["Mode6"] == "Debug":
            Domoticz.Log("NAMES dict :")
            for x in self.NAMES.keys():
                Domoticz.Log(str(x) + " => " + str(self.NAMES[x]))

        for x in Parameters["Mode3"].split(';'):
            if x in self.NAMES.keys() and x in self.KEY and list(st0.keys()).index(x)+1 not in Devices:
                Domoticz.Device(Name=self.NAMES[x], Unit=list(st0.keys()).index(x)+1, TypeName=self.KEY[x]).Create()
                if Parameters["Mode6"] == "Debug":
                    Domoticz.Log("Name=" + self.NAMES[x] + " Unit=" + str(list(st0.keys()).index(x)+1) + " TypeName=" + self.KEY[x])


        return True

    # Check if Samsung TV is On and connected to Network
    # Need to do in this way as TV accept connection and disconnect immediately
    def isAlive(self):
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.config["host"], self.config["port"]))
            self.isConnected = True
        except socket.error as e:
            self.isConnected = False
        s.close()
        if Parameters["Mode6"] == "Debug":
            Domoticz.Log("isAlive status :" + str(self.isConnected))
        return

    # executed each time we click on device thru domoticz GUI
    def onCommand(self, Unit, Command, Level, Hue):
        Domoticz.Log("onCommand called for Unit " + str(Unit) + ": Parameter '" + str(Command) + "', Level: " + str(Level) + ", Connected: " + str(self.isConnected))
        return

    def onHeartbeat(self):
        Domoticz.Log("onHeartbeat called")
        self.isAlive()
#        if (self.isConnected == True):
#            urll = 'http://' + str(Parameters["Address"]) + '/web/powerstate?'
#            username = str(Parameters["Mode1"])
#            password = str(Parameters["Mode2"])
#            # create a password manager
#            passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#            # Add the username and password.
#            # If we knew the realm, we could use it instead of None.
#            passman.add_password(None, urll, username, password)
#
#            authhandler = urllib.request.HTTPBasicAuthHandler(passman)
#            # create "opener" (OpenerDirector instance)
#            opener = urllib.request.build_opener(authhandler)
#            # use the opener to fetch a URL
#            pagehandle = opener.open(urll)
#            data = pagehandle.read()
#            pagehandle.close()
#            data = xmltodict.parse(data)
#            data = str(data["e2powerstate"]["e2instandby"])
#            if Parameters["Mode6"] == "Debug":
#                Domoticz.Log('data["e2powerstate"]["e2instandby"] => '+str(data))
#            if data == "false":
#                UpdateDevice(self.UNIT_POWER_CONTROL, 40, '40')
#            else:
#                UpdateDevice(self.UNIT_POWER_CONTROL, 10, '10')
#            UpdateDevice(self.UNIT_STATUS_REMOTE, 1, 'Enigma2 Available')
#        else:
#            UpdateDevice(self.UNIT_STATUS_REMOTE, 0, 'Enigma2 offline')
#            UpdateDevice(self.UNIT_POWER_CONTROL, 0, '0')
        return True

    def onConnect(self, Status, Description):
        Domoticz.Log("onConnect called")
        return

    def onMessage(self, Data, Status, Extra):
        Domoticz.Log("onMessage called")
        return

    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Log("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(
            Priority) + "," + Sound + "," + ImageFile)
        return

    def onDisconnect(self, Connection):
        Domoticz.Log("Device has disconnected")
        return

    def onStop(self):
        Domoticz.Log("onStop called")
        return True


################ base on example ######################
global _plugin
_plugin = BasePlugin()


def onStart():
    global _plugin
    _plugin.onStart()


def onStop():
    global _plugin
    _plugin.onStop()


def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)


def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)


def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)


def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)


def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)


def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()


# Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug("'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Settings count: " + str(len(Settings)))
    for x in Settings:
        Domoticz.Debug("'" + x + "':'" + str(Settings[x]) + "'")
    Domoticz.Debug("Image count: " + str(len(Images)))
    for x in Images:
        Domoticz.Debug("'" + x + "':'" + str(Images[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
        Domoticz.Debug("Device Image:     " + str(Devices[x].Image))
    return


def UpdateDevice(Unit, nValue, sValue):
    # Make sure that the Domoticz device still exists (they can be deleted) before updating it 
    if (Unit in Devices):
        if (Devices[Unit].nValue != nValue) or (Devices[Unit].sValue != sValue):
            Devices[Unit].Update(nValue=nValue, sValue=str(sValue))
            Domoticz.Log("Update " + str(nValue) + ":'" + str(sValue) + "' (" + Devices[Unit].Name + ")")
    return
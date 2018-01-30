# domoticz-tinycontrol
A Python plugin for Domoticz to monitor and control TINYCONTROL device

* Based on repository https://github.com/lrybak/domoticz-airly/
* and script for Samsung TV: https://www.domoticz.com/wiki/Plugins/SamsungTV.html

## Installation

* Make sure your Domoticz instance supports Domoticz Plugin System - see more https://www.domoticz.com/wiki/Using_Python_plugins

* Get plugin data into DOMOTICZ/plugins directory
```
cd YOUR_DOMOTICZ_PATH/plugins
git clone https://github.com/kofec/domoticz-tinycontrol
```
First use script "tinycontrol.py"

e.g 
```
cd YOUR_DOMOTICZ_PATH/plugins/domoticz-tinycontrol

usage: tinycontrol.py [-h] [--user USER] [--password PASSWORD] [--st2]
                      [--out <port number> ON/OFF] [--debug]
                      IPaddress
                      
./tinycontrol.py 192.168.1.1
<response><out0>1</out0><out1>0</out1><out2>0</out2><out3>1</out3><out4>1</out4><out5>1</out5><out6>1</out6><di0>up</di0><di1>up</di1><di2>up</di2><di3>up</di3><ia0>275</ia0><ia1>134</ia1><ia2>0</ia2><ia3>3</ia3><ia4>-7</ia4><ia5>0</ia5><ia6>22</ia6><ia7>605</ia7><ia8>81</ia8><ia9>-600</ia9><ia10>-600</ia10><ia11>-600</ia11><ia12>-600</ia12><ia13>0</ia13><ia14>0</ia14><ia15>0</ia15><ia16>0</ia16><ia17>0</ia17><ia18>0</ia18><ia19>-88</ia19><freq>5008</freq><duty>500</duty><pwm>0</pwm><sec0>35</sec0><sec1>13</sec1><sec2>6</sec2><sec3>25</sec3><sec4>1517348529</sec4></response>

```
* You will probably need install python package "xmltodict" like in issue https://github.com/kofec/domoticz-tinycontrol/issues/1
* and check where it was installed 
if sys.platform.startswith('linux'):
linux specific code here
sys.path.append('/usr/local/lib/python3.5/dist-packages')

* As you can see in above example ther is lots of devices. You will need it in next step

Restart Domoticz
* Go to Setup > Hardware and create new Hardware with type: Domoticz-Enigma2
* Enter name (it's up to you), user name and password if define. If not leave it blank
* Fild "Which devices should be tracked:" you should put device which you would like to monitor. eg: ia0;ia1;ia4;ia7;ia8;out0
ia0 - Board temaperature, ia1 - board voltage, ia4 - PT1000, ia7 i ia8 - DS18B20

## Update
```
cd YOUR_DOMOTICZ_PATH/plugins/domoticz-tinycontrol
git pull
```
* Restart Domoticz

## Troubleshooting

In case of issues, mostly plugin not visible on plugin list, check logs if plugin system is working correctly. See Domoticz wiki for resolution of most typical installation issues http://www.domoticz.com/wiki/Linux#Problems_locating_Python

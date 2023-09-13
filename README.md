# Imposter
This is the linux version of this software, Windows and Mac versions to be released too.
Built using python, *Virtual environment exists in the repo.*

Requirement Specifications of the software: Python/python3.

# [+]How to use??

To run the software, mention the python version you are using followed by the name of the software i.e. imposter.py
proper compilation without error message will be done only when two of the major parameters are provided, Interface( -i, --interface) whos mac isto be changed and the Desired mac address(-m, --mac).

# Remember that mac address is of 6 bytes and each byte is separated by a " : " symbol. Each nibble of a byte can take only and only hexadecimal values(0-f). Any value out of this hexadecimal range will trigger an error.

For better description traverse to the folder where the software is downloaded and type:
> python imposter.py -h

example command:
> python imposter.py -i eth0 -m 00:00:00:00:00
> python3 imposter.py -i eth0 -m 00:00:00:00:00
> python imposter.py --interface eth0 --mac 00:00:00:00:00
> python3 imposter.py -i eth0 -mac 00:00:00:00:00

bad command example:
> python imposter.py 
> python3 imposter.py
> python imposter.py -i eth0
> python imposter.py -m 00:00:00:00:00
> python imposter.py -i eth0 -m x0:yz:a8:lq:pr:la      *Invalid hexadecimal range, argument can only take numeric [0-9] or hexadecimal numeric alphabets[a-f]*

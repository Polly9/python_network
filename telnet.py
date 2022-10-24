import subprocess as sp
from telnetlib import Telnet

res = sp.call(['telnet', '192.168.200.1'])

tlnet = Telnet('192.168.200.1')
tlnet.read_util(b'Passward:')
tlnet.write(b' python_telnet\n')
tlnet.read_util(b'>')
tlnet.write(b'admin\n')
tlnet.read_util(b'Passward:')
tlnet.write(b'python_telnet_admin \n')
tlnet.read_util(b'#')
tlnet.write(b'ip lan3 address 10.10.10.10/24\n')
tlnet.read_util(b'#')
tlnet.write(b'save\n')
tlnet.read_util(b'#')
tlnet.write(b'exit\n')
tlnet.read_util(b'>')
tlnet.write(b'exit\n')

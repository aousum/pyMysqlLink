import uuid
def get_mac_address():
    macId=uuid.UUID(int=uuid.getnode()).hex[-12:]
    return  ':'.join([macId[e:e+2] for e in range(0,11,2)] )

import socket
myName=socket.getfqdn(socket.gethostname())
myAddr=socket.gethostbyname(myName)
print(myName)#用户名
print(myAddr)#本机id
print(get_mac_address())#mac地址

import math
print(dir(math))
help(math.pow)


def get_y(a, b):
    return lambda x: a*x + b
y1 = get_y(1, 1)
print(type(y1(2)))

a='56446231236'
b='sdfsddsfdgf'
print(min(a))
print(max(b))
print('sdf'  in b)
print(ord('A'))
print(chr(65))


alist=[1,2,3,4,5,6]
alist.append(454)
newlist=alist[::-1]
print(newlist)
nnlist=list(reversed(alist))
print(nnlist)
doubleList=alist+newlist
print(doubleList)
alist.extend(newlist)
print(alist)
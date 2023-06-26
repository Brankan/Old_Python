# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 11:25:09 2021

@author: student
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 11:12:14 2021

@author: student
"""
import socket 

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.httpbin.org',80))

s.sendall('GET /html HTTP/1.1\r\nHost:httpbin.org\r\n\r\n'.encode('utf-8'))


data = s.recv(1000).decode("utf-8")

html=data.split('\r\n\r\n')[1]

print(html)
with open ('index.html' ,'w') as f:
    f.write(html)

print("Saved to index.html")
    
s.close()



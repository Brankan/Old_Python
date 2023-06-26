"""s.recv(1).decode("utf-8")"""


import socket 

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.httpbin.org',80))

s.sendall('GET /html HTTP/1.1\r\nHost:httpbin.org\r\n\r\n'.encode('utf-8'))
T=0
data=b''
html=''

while b'\r\n\r\n' not in data:
    data += s.recv(100)
    
    
contentLenght=int(data.decode("utf-8").split("Content-Length:")[1].split('\r\n')[0])

header_lenght=len(data.decode("utf-8").split('\r\n\r\n')[0])

while len(data)<contentLenght:
    data += s.recv(100)

html=html+data.decode("utf-8")
print(html)


"""with open ('index.html' ,'w') as f:
    f.write(html)
print("Saved to index.html")"""

print(html)

s.close() 
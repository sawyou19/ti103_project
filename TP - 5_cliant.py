import http.client
c = http.client.HTTPConnection("www.google.ca")
c.request("GET", "/")
r = c.getresponse()
print(r.status, r.reason)
print(r.read())

# import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('127.0.0.1', 52000))
#     s.sendall(b'Bonjour Monsieur')
#     data = s.recv(4096)
#     print("Le serveur a repondu", repr(data))

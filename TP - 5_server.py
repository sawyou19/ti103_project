# import socket
#
# # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# #     s.bind(('', 52000))
# #     s.listen(1)
# #     c, addr = s.accept()
# #     print("Le client {} m'a contacte"/format(addr))
# #     with c:
# #         while True:
# #             data = c.recv(4096)
# #             if not data:
# #                 break
# #
# #             print("Le client a dit: ", repr(data))
# #             c.sendall(data)
#
# import http.server
# import socketserver
#
# # class MyTCPHandler(socketserver.BaseRequestHandler):
# #     def handle(self):
# #         data = self.request.recv(4096)
# #         print("Le client a dit: ", repr(data))
# #         self.request.sendall(  data)
#
# MyTCPHandler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("0.0.0.0", 52000), MyTCPHandler) as server:
#     server.serve_forever()
import flask

app = flask.Flask("toto")

@app.route('/')
def index():
    return"<h1>toto</h1><p>Bonjour le monde</p>"

app.run("0.0.0.0", 8000)
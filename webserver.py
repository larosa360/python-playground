import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']
server_object = HTTPServer(('localhost', 8088), handler)
server_object.serve_forever()
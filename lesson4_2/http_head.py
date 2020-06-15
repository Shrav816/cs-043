import socket

def http_head(host, page_path):
    sock = socket.create_connection((host, 80))
    sock.sendall(('HEAD ' + page_path + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n').encode())
    data = sock.recv(1000)
    sock.close()
    print(data.decode())


http_head('www.google.com', '/')
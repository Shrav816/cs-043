import socket

def http_get(host, page_path):
    sock = socket.create_connection((host, 80))
    sock.sendall(('GET ' + page_path + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n').encode())
    data = sock.recv(1000)
    sock.close()
    print(data.decode())


http_get('www.google.com', '/')

import socket


def start(config):
    print("Connecting to File Sync Server")

    server = (config['server_ip'], 4000)

    s = socket.socket()
    s.connect(server)

    print("Connected to File Sync Server")

    send_file = open('image.jpg', 'rb')
    file_name = send_file.name
    s.send(file_name.encode('utf-8'))
    s.settimeout(100)
    status = s.recv(1024)
    status = status.decode('utf-8')
    if status == 'OK':
        data = send_file.read(1024)
        while data:
            s.send(data)
            data = send_file.read(1024)
    s.close()

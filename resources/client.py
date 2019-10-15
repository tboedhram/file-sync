import socket


def start(config):
    print("Connecting to File Sync Server")

    server = (config['server_ip'], 4000)

    s = socket.socket()
    s.connect(server)

    print("Connected to File Sync Server")

    send_file = open('image.jpg', 'rb')
    data = send_file.read(1024)
    while data:
        s.send(data)
        data = send_file.read(1024)
    s.close()

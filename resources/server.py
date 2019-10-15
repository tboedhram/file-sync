import socket


def start(config):
    print("Starting File Sync Server")

    s = socket.socket()
    s.bind((config['server_ip'], 4000))
    s.listen(2)

    print("File Sync Server Started")

    while True:
        client, address = s.accept()
        file_name = client.recv(1024)
        client.send("OK".encode('utf-8'))
        received_file = open(file_name, 'wb')
        while True:
            data = client.recv(1024)
            received_file.write(data)
            if not data:
                break
        received_file.close()
        client.close()
    s.close()

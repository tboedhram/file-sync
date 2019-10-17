import socket
import resources.file_transfer as file_transfer


def start(config):
    print("Starting File Sync Server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((config['server_ip'], 4000))
    s.listen(2)
    print("File Sync Server Started")

    while True:
        client, address = s.accept()
        file_transfer.send_file(client, config['root_location'])
        client.close()
    s.close()

import socket
import resources.file_transfer as file_transfer


def start(config):
    print("Connecting to File Sync Server")
    server = (config['server_ip'], 4000)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server)
    print("Connected to File Sync Server")
    file_transfer.receive_file(s, config['root_location'])
    s.close()

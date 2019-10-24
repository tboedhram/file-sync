import socket
import time

import resources.file_transfer as file_transfer


def start(config):
    while True:
        print('Connecting to File Sync Server')
        server = (config['server_ip'], 4000)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(server)
            print('Connected to File Sync Server')
            file_transfer.receive_file(s, config['root_location'])
        except TimeoutError:
            print('Connection to File Sync Server Timed Out')
        except PermissionError:
            print('Cannot copy files to the specified location')
        finally:
            s.close()
        time.sleep(3600)

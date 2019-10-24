import socket
import time

import resources.file_transfer as file_transfer
import resources.helpers as helpers


def start(config):
    while True:                                                # This or statement is temporary
        if config['server_network_ssid'] == helpers.get_ssid() or helpers.get_os() != 'Windows':
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
        else:
            print('Not connected to the same network as the File Sync Server')
        time.sleep(3600)

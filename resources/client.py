import socket
import time

import resources.file_transfer as file_transfer
import resources.helpers as helpers
import resources.logger as logger


def start(config):
    client_logger = logger.create_logger('client')
    while True:
        if config['server_network_ssid'] == helpers.get_ssid() or helpers.get_os() != 'Windows':
            client_logger.info('Connecting to File Sync Server')
            server = (config['server_ip'], 4000)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect(server)
                client_logger.info('Connected to File Sync Server')
                file_transfer.receive_file(s, config['root_location'], client_logger)
            except TimeoutError:
                client_logger.warning('Connection to File Sync Server Timed Out')
            except ConnectionRefusedError:
                client_logger.warning('File Sync Server Refused Connection')
            except PermissionError:
                client_logger.error('Cannot copy files to the specified location')
            except Exception:
                client_logger.exception('An unhandled exception occurred. Please send server.log to the developer')
                exit()
            finally:
                s.close()
        else:
            client_logger.info('Not connected to the same network as the File Sync Server')
        time.sleep(3600)

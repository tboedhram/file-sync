import socket

import resources.file_transfer as file_transfer
import resources.logger as logger


def start(config):
    server_logger = logger.create_logger('server')
    server_logger.info('Starting File Sync Server')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((config['server_ip'], 4000))
    s.listen(2)
    server_logger.info('File Sync Server Started')

    while True:
        client, address = s.accept()
        server_logger.info('Client Connected\tIP: {address}'.format(address=str(address[0])))
        try:
            file_transfer.send_file(client, config['root_location'], config['ignore_files'], server_logger)
            server_logger.info('All files copied to client successfully!')
        except ConnectionAbortedError:
            server_logger.warning('Client {address} disconnected unexpectedly'.format(address=str(address[0])))
        except ConnectionResetError:
            server_logger.warning('Client {address} disconnected unexpectedly'.format(address=str(address[0])))
        finally:
            client.close()
    s.close()

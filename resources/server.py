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
            # This if block sets the clients file transfer mode to the appropriate state
            if config['file_transfer_mode'] == 'send':
                client.send('receive'.encode('utf-8'))
            elif config['file_transfer_mode'] == 'receive':
                client.send('send'.encode('utf-8'))
            elif config['file_transfer_mode'] == 'bidirectional':
                client.send('bidirectional'.encode('utf-8'))
            if config['file_transfer_mode'] == 'send' or config['file_transfer_mode'] == 'bidirectional':
                file_transfer.send_file(client, config['root_location'], config['ignore_files'], server_logger)
                server_logger.info('All files copied to client successfully!')
            if config['file_transfer_mode'] == 'receive' or config['file_transfer_mode'] == 'bidirectional':
                file_transfer.receive_file(client, config['root_location'], server_logger)
        except ConnectionAbortedError:
            server_logger.warning('Client {address} disconnected unexpectedly'.format(address=str(address[0])))
        except ConnectionResetError:
            server_logger.warning('Client {address} disconnected unexpectedly'.format(address=str(address[0])))
        except PermissionError:
            server_logger.error('Cannot copy files to the specified location')
        except Exception:
            server_logger.exception('An unhandled exception occurred. Please send server.log to the developer')
            exit()
        finally:
            client.close()
    s.close()

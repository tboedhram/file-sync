import socket
import resources.file_transfer as file_transfer


def start(config):
    print('Starting File Sync Server')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((config['server_ip'], 4000))
    s.listen(2)
    print('File Sync Server Started\n')

    while True:
        client, address = s.accept()
        print('Client Connected\nIP: ' + str(address[0]))
        try:
            file_transfer.send_file(client, config['root_location'], config['ignore_files'])
            print('\nAll files copied to client successfully!')
        except ConnectionAbortedError:
            print('\nClient ' + str(address[0]) + ' disconnected unexpectedly')
        except ConnectionResetError:
            print('\nClient ' + str(address[0]) + ' disconnected unexpectedly')
        finally:
            client.close()
    s.close()

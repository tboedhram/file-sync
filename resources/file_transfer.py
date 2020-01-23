import os
from socket import timeout


def get_files_to_send(root_location, prefix, ignored_files, logger):
    files_in_directory = os.listdir(os.path.join(root_location, prefix))
    files_to_send = []
    for file in files_in_directory:
        relative_path = os.path.join(prefix, file)
        if relative_path not in ignored_files:
            full_path = os.path.join(root_location, relative_path)
            if os.path.isdir(full_path):
                new_prefix = os.path.join(prefix, file)
                files_to_send = files_to_send + get_files_to_send(root_location, new_prefix, ignored_files, logger)
            else:
                files_to_send.append(os.path.join(prefix, file))
        else:
            logger.info('Ignored {file}'.format(file=os.path.join(root_location, relative_path)))
    return files_to_send


def send_file(socket, root_location, ignored_files_string, logger):
    socket.settimeout(None)
    ignored_files = ignored_files_string.split('||')
    files_to_send = get_files_to_send(root_location, '', ignored_files, logger)
    logger.info('Found {number_of_files} files to sync'.format(number_of_files=str(len(files_to_send))))
    for file in files_to_send:
        file_path = os.path.join(root_location, file)
        file_to_send = open(file_path, 'rb')
        socket.send(file.encode('utf-8'))
        status = socket.recv(1024)
        status = status.decode('utf-8')
        if status == 'OK':
            data = file_to_send.read()
            file_to_send.close()
            logger.info('Sent {file}'.format(file=file_path))
            socket.sendall(data)
            status = socket.recv(1024)
            status = status.decode('utf-8')
            if status == 'NEXT':
                pass
            else:
                break
        elif status == 'SKIP':
            logger.info('Skipped {file}'.format(file=file_path))
            pass
    socket.send('DONE'.encode('utf-8'))


def check_for_directory(path):
    split_path = os.path.split(path)
    directory_path = split_path[0]
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path, exist_ok=True)


def receive_file(socket, root_location, logger):
    while True:
        file_name = socket.recv(1024)
        file_name = file_name.decode('utf-8')
        if file_name == 'DONE':
            return
        else:
            file_path = os.path.join(root_location, file_name)
            check_for_directory(file_path)
            if os.path.isfile(file_path):
                logger.info('Skipped {file}'.format(file=file_path))
                socket.send('SKIP'.encode('utf-8'))
            else:
                received_file = open(file_path, 'wb')
                socket.send('OK'.encode('utf-8'))
                while True:
                    try:
                        socket.settimeout(1)
                        data = socket.recv(4096)
                        if data:
                            received_file.write(data)
                        else:
                            break
                    except timeout:
                        break
                received_file.close()
                logger.info('Copied {file}'.format(file=file_path))
                socket.send('NEXT'.encode('utf-8'))

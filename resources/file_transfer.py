import os
from socket import timeout


def get_files_to_send(root_location, prefix, ignored_files):
    files_in_directory = os.listdir(os.path.join(root_location, prefix))
    files_to_send = []
    for file in files_in_directory:
        relative_path = os.path.join(prefix, file)
        if relative_path not in ignored_files:
            full_path = os.path.join(root_location, relative_path)
            if os.path.isdir(full_path):
                new_prefix = os.path.join(prefix, file)
                files_to_send = files_to_send + get_files_to_send(root_location, new_prefix, ignored_files)
            else:
                files_to_send.append(os.path.join(prefix, file))
        else:
            print('Ignored ' + os.path.join(root_location, relative_path))
    return files_to_send


def send_file(socket, root_location, ignored_files_string):
    ignored_files = ignored_files_string.split('||')
    files_to_send = get_files_to_send(root_location, '', ignored_files)
    print(len(files_to_send))
    for file in files_to_send:
        file_path = os.path.join(root_location, file)
        file_to_send = open(file_path, 'rb')
        socket.send(file.encode('utf-8'))
        status = socket.recv(1024)
        status = status.decode('utf-8')
        if status == 'OK':
            data = file_to_send.read()
            file_to_send.close()
            print('Sent ' + file_path)
            socket.sendall(data)
            status = socket.recv(1024)
            status = status.decode('utf-8')
            if status == 'NEXT':
                pass
            else:
                break
        elif status == 'SKIP':
            print('Skipped ' + file_path)
            pass
    socket.send('DONE'.encode('utf-8'))


def check_for_directory(path):
    path_list = path.split('\\')
    path_list = path_list[:-1]
    directory_path = '\\'.join(path_list)
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path, exist_ok=True)


def receive_file(socket, root_location):
    while True:
        file_name = socket.recv(1024)
        file_name = file_name.decode('utf-8')
        if file_name == 'DONE':
            return
        else:
            file_path = os.path.join(root_location, file_name)
            check_for_directory(file_path)
            if os.path.isfile(file_path):
                print('Skipped ' + file_path)
                socket.send('SKIP'.encode('utf-8'))
            else:
                received_file = open(file_path, 'wb')
                socket.send('OK'.encode('utf-8'))
                while True:
                    try:
                        socket.settimeout(1)
                        data = socket.recv(1024)
                        if data:
                            received_file.write(data)
                        else:
                            break
                    except timeout:
                        break
                received_file.close()
                print('Copied ' + file_path)
                socket.send('NEXT'.encode('utf-8'))

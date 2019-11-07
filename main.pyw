from resources import client as client
from resources import server as server


if __name__ == '__main__':
    config = {}
    with open('config.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    file.close()
    for line in lines:
        option = line.replace('\n', '').split('=')
        config[option[0]] = option[1]
    if config['mode'] == 'server':
        server.start(config)
    else:
        client.start(config)

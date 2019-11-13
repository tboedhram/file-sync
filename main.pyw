from resources import client as client
from resources import server as server
from resources.gui import config as config_ui


def load_config():
    with open('config.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    file.close()
    return lines


def main():
    config = {}
    try:
        lines = load_config()
    except FileNotFoundError:
        config_ui.gui()
        lines = load_config()
    for line in lines:
        option = line.replace('\n', '').split('=')
        config[option[0]] = option[1]
    if config['mode'] == 'server':
        server.start(config)
    else:
        client.start(config)


if __name__ == '__main__':
    main()

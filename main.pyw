import json

from resources import client as client
from resources import server as server
from resources.gui import config as config_ui


def load_config():
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
    return config


def main():
    try:
        config = load_config()
    except FileNotFoundError:
        config_ui.gui()
        config = load_config()
    if config['mode'] == 'server':
        server.start(config)
    else:
        client.start(config)


if __name__ == '__main__':
    main()

import json

from resources import client as client
from resources import server as server
from resources import updater as updater
from resources.gui.config import gui as config_gui


def load_config():
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
        config_file.close()
    return config


def main():
    version = updater.get_version()
    try:
        config = load_config()
    except FileNotFoundError:
        config_gui(version, None)
        config = load_config()
    if config['version'] != version:
        config_gui(version, config)
        config = load_config()
    if config['check_update']:
        updater.check_for_updates(config['auto_update'])
    if config['mode'] == 'server':
        server.start(config)
    else:
        client.start(config)


if __name__ == '__main__':
    main()

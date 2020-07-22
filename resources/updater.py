import requests

import resources.gui.updater_gui as updater_ui


def update():
    pass


def check_for_updates():
    with open('version.info', 'r') as version_info:
        current_version = version_info.read()
        request = requests.get('https://raw.github.com/tboedhram/file-sync/v4.0-auto-updater/version.info')
        github_version = request.text
        if current_version != github_version:
            updater_ui.gui(current_version, github_version)

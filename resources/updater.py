import requests

from zipfile import ZipFile

import resources.gui.updater_gui as updater_ui


def update():
    with open('new_version.zip', 'wb') as new_version:
        request = requests.get('https://github.com/tboedhram/file-sync/zipball/master')
        new_version.write(request.content)
        new_version.close()
    with ZipFile('new_version.zip', 'r') as new_version_zip:
        new_version_zip.extractall()


def check_for_updates():
    with open('version.info', 'r') as version_info:
        current_version = version_info.read()
        request = requests.get('https://raw.github.com/tboedhram/file-sync/v4.0-auto-updater/version.info')
        github_version = request.text
        if current_version != github_version:
            updater_ui.gui(current_version, github_version)

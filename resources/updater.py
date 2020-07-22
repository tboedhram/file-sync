import requests


def check_for_updates():
    with open('version.info', 'r') as version_info:
        current_version = version_info.read()
        request = requests.get('https://raw.github.com/tboedhram/file-sync/v4.0-auto-updater/version.info')
        print(request.text == current_version)
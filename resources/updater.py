import os
import requests
import shutil

from zipfile import ZipFile

import resources.gui.updater_gui as updater_gui


def clean_up():
    os.remove('new_version.zip')
    shutil.rmtree('new_version')


def move_files(root_directory, directory):
    files_in_directory = os.listdir(os.path.join(root_directory, directory))
    for file in files_in_directory:
        source = os.path.join(root_directory, directory, file)
        destination = os.path.join(directory, file)
        if os.path.isdir(source):
            move_files(root_directory, os.path.join(directory, file))
        else:
            os.replace(source, destination)


def update():
    with open('new_version.zip', 'wb') as new_version:
        request = requests.get('https://github.com/tboedhram/file-sync/zipball/master')
        new_version.write(request.content)
        new_version.close()
    with ZipFile('new_version.zip', 'r') as new_version_zip:
        folder = new_version_zip.namelist()[0][:-1]
        directory = os.path.join('new_version', folder)
        new_version_zip.extractall('new_version')
        new_version_zip.close()
    move_files(directory, '')
    clean_up()


def check_for_updates():
    with open('version.info', 'r') as version_info:
        current_version = version_info.read()
        version_info.close()
    request = requests.get('https://raw.github.com/tboedhram/file-sync/v4.0-auto-updater/version.info')
    github_version = request.text
    if current_version != github_version:
        updater_gui.gui(current_version, github_version)

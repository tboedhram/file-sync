import platform
import subprocess
OS = platform.system()


def get_os():
    return OS


def get_ssid():
    if get_os() == 'Windows':
        network_info = subprocess.check_output('netsh wlan show interfaces', creationflags=subprocess.CREATE_NO_WINDOW).decode('ascii').replace(' ', '').split('\r\n')
        for info in network_info:
            parsed_info = info.split(':')
            if parsed_info[0] == 'SSID':
                return parsed_info[1]
    else:
        return ''

import os
import tkinter
import tkinter.scrolledtext

import resources.gui.gui_helpers as gui_helpers


def validate_ip_address(ip_address):
    split_ip_address = ip_address.split('.')
    if len(split_ip_address) != 4:
        return False
    for element in split_ip_address:
        try:
            num_element = int(element)
            if num_element < 0 or num_element > 255:
                return False
        except ValueError:
            return False
        except TypeError:
            return False
    return True


def save_config(window, mode, server_ip, ssid, root_location, ignore_files_input, error_messages):
    for child in error_messages.winfo_children():
        child.destroy()
    error_messages.update()
    ignore_files = ignore_files_input.get(1.0, tkinter.END).replace('\n', '||')
    if server_ip == '':
        gui_helpers.create_error_message(error_messages, 'Server IP Address is a required field.')
    elif not validate_ip_address(server_ip):
        gui_helpers.create_error_message(error_messages, 'Invalid Server IP Address.')
    if root_location == '':
        gui_helpers.create_error_message(error_messages, 'Root Location is a required field.')
    elif not os.path.isdir(root_location):
        gui_helpers.create_error_message(error_messages, 'Root Location is not a valid directory.')
    if len(error_messages.winfo_children()) == 0:
        with open('config.txt', 'w', encoding='utf-8') as config:
            config.write('mode={mode}\nserver_ip={server_ip}\nserver_network_ssid={ssid}\nroot_location={root_location}'
                         '\nignore_files={ignore_files}\n'.format(mode=mode, server_ip=server_ip, ssid=ssid,
                                                                  root_location=root_location,
                                                                  ignore_files=ignore_files))
        config.close()
        window.destroy()


def gui():
    #  Window Setup
    window = gui_helpers.create()

    #  Variables
    mode = tkinter.StringVar(value='server')
    server_ip = tkinter.StringVar()
    ssid = tkinter.StringVar()
    root_location = tkinter.StringVar()

    #  Widgets
    widget_frame = tkinter.Frame(window)
    widget_frame.pack()

    mode_label = tkinter.Label(widget_frame, text='Mode:')
    mode_label.grid(row=0, column=0)
    radio_button_frame = tkinter.Frame(widget_frame)
    radio_button_frame.grid(row=0, column=1, pady=(2, 2))
    mode_server = tkinter.Radiobutton(radio_button_frame, text='Server', variable=mode, value='server')
    mode_server.grid(row=0, column=0)
    mode_client = tkinter.Radiobutton(radio_button_frame, text='Client', variable=mode, value='client')
    mode_client.grid(row=0, column=1)

    ip_label = tkinter.Label(widget_frame, text='Server IP Address:')
    ip_label.grid(row=1, column=0)
    ip_input = tkinter.Entry(widget_frame, textvariable=server_ip)
    ip_input.grid(row=1, column=1, pady=(2, 2))

    ssid_label = tkinter.Label(widget_frame, text='Wi-Fi Name:')
    ssid_label.grid(row=2, column=0)
    ssid_input = tkinter.Entry(widget_frame, textvariable=ssid)
    ssid_input.grid(row=2, column=1, pady=(2, 2))

    root_location_label = tkinter.Label(widget_frame, text='Root Location:')
    root_location_label.grid(row=3, column=0)
    root_location_input = tkinter.Entry(widget_frame, textvariable=root_location)
    root_location_input.grid(row=3, column=1, pady=(2, 2))

    ignore_files_label = tkinter.Label(widget_frame, text='Files To Ignore:')
    ignore_files_label.grid(row=4, column=0)
    ignore_files_input = tkinter.scrolledtext.ScrolledText(widget_frame, height=5, width=20, wrap=tkinter.NONE)
    ignore_files_input.grid(row=4, column=1, pady=(2, 2))

    error_message = tkinter.Frame()
    error_message.pack(pady=(2, 2))

    finish_button = tkinter.Button(text='Finish Setup',
                                   command=lambda: save_config(window, mode.get(), server_ip.get(), ssid.get(),
                                                               root_location.get(), ignore_files_input, error_message))
    finish_button.pack(pady=(5, 5))

    window.mainloop()

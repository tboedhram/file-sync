import tkinter
import tkinter.scrolledtext

import resources.gui.make_window as make_window


def save_config(window, mode, server_ip, ssid, root_location, ignore_files_input):
    ignore_files = ignore_files_input.get(1.0, tkinter.END).replace('\n', '||')
    with open('config.txt', 'w', encoding='utf-8') as config:
        config.write('mode={}\n'.format(mode.get()))
        config.write('server_ip={}\n'.format(server_ip.get()))
        config.write('server_network_ssid={}\n'.format(ssid.get()))
        config.write('root_location={}\n'.format(root_location.get()))
        config.write('ignore_files={}\n'.format(ignore_files))
    config.close()
    window.destroy()


def gui():
    #  Window Setup
    window = make_window.create()

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
    radio_button_frame.grid(row=0, column=1)
    mode_server = tkinter.Radiobutton(radio_button_frame, text='Server', variable=mode, value='server')
    mode_server.grid(row=0, column=0)
    mode_client = tkinter.Radiobutton(radio_button_frame, text='Client', variable=mode, value='client')
    mode_client.grid(row=0, column=1)

    ip_label = tkinter.Label(widget_frame, text='Server IP Address:')
    ip_label.grid(row=1, column=0)
    ip_input = tkinter.Entry(widget_frame, textvariable=server_ip)
    ip_input.grid(row=1, column=1)

    ssid_label = tkinter.Label(widget_frame, text='Wi-Fi Name:')
    ssid_label.grid(row=2, column=0)
    ssid_input = tkinter.Entry(widget_frame, textvariable=ssid)
    ssid_input.grid(row=2, column=1)

    root_location_label = tkinter.Label(widget_frame, text='Root Location:')
    root_location_label.grid(row=3, column=0)
    root_location_input = tkinter.Entry(widget_frame, textvariable=root_location)
    root_location_input.grid(row=3, column=1)

    ignore_files_label = tkinter.Label(widget_frame, text='Files To Ignore:')
    ignore_files_label.grid(row=4, column=0)
    ignore_files_input = tkinter.scrolledtext.ScrolledText(widget_frame, height=3.5, width=20, wrap=tkinter.NONE)
    ignore_files_input.grid(row=4, column=1)

    finish_button = tkinter.Button(text='Finish Setup',
                                   command=lambda: save_config(window, mode, server_ip, ssid, root_location,
                                                               ignore_files_input))
    finish_button.pack()

    window.mainloop()

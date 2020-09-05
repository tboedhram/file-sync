import sys
import tkinter

from resources import updater as updater
import resources.gui.gui_helpers as gui_helpers


def update(window):
    updater.update()
    window.destroy()


def cancel(window):
    window.destroy()


def gui(current_version, new_version):
    #  Window Setup
    window = gui_helpers.create('Updater', 125, 375)

    text = tkinter.Label(text='There is an update available!')
    text.pack()

    current_version_label = tkinter.Label(
        text='Current Version: {current_version}'.format(current_version=current_version))
    current_version_label.pack()

    new_version_label = tkinter.Label(text='New Version: {new_version}'.format(new_version=new_version))
    new_version_label.pack()

    widget_frame = tkinter.Frame(window)
    widget_frame.pack()

    update_button = tkinter.Button(widget_frame, text='Update', command=lambda: update(window))
    update_button.grid(row=0, column=0, padx=5, pady=20)

    update_button = tkinter.Button(widget_frame, text='Cancel', command=lambda: cancel(window))
    update_button.grid(row=0, column=1, padx=5, pady=20)

    window.mainloop()


def finished_gui():
    window = gui_helpers.create('Finished Update', 75, 325)

    text = tkinter.Label(window, text='The update has finished\nPlease restart the application')
    text.pack()

    ok_button = tkinter.Button(window, text='OK', command=lambda: sys.exit(0))
    ok_button.pack()

    window.mainloop()


def update_successful_gui():
    window = gui_helpers.create('Update Successful', 75, 325)

    text = tkinter.Label(window, text='The application has updated successfully\nPlease verify your settings')
    text.pack()

    ok_button = tkinter.Button(window, text='OK', command=lambda: cancel(window))
    ok_button.pack()

    window.mainloop()

import tkinter


def create():
    window = tkinter.Tk()
    window.title('File Sync Setup')
    window.iconbitmap('resources/assets/file_sync.ico')
    window_height = 275
    window_width = 375
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
    return window

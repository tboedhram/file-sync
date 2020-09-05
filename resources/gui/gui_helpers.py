import tkinter


def create(title, height, width):
    window = tkinter.Tk()
    window.title('File Sync | {title}'.format(title=title))
    window.iconbitmap('resources/assets/file_sync.ico')
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    window.geometry("{}x{}+{}+{}".format(width, height, x_coordinate, y_coordinate))
    return window


def create_error_message(frame, message):
    error_label = tkinter.Label(frame, text=message, fg='red')
    error_label.pack()
    return

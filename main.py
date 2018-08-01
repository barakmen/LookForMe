import lookforme
import tkinter
from tkinter import *
from tkinter import messagebox


def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

if __name__ == '__main__':
    w = 500
    h = 500
    wmid = w/2

    root = tkinter.Tk()
    root.geometry(str(w) + 'x' + str(h))
    root.title('Look For Me')

    
    Label(root, text='Look For Me', bg="Black", fg="white").grid(row=0)

    Label(root, text="First Name").grid(row=1)
    Label(root, text="Last Name").grid(row=2)

    e1 = Entry(root)
    e2 = Entry(root)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)


    center(root)
    root.mainloop()




'''
import easygui
folderToSearch = easygui.fileopenbox()
resultFolder = easygui.fileopenbox()
personToFind = easygui.fileopenbox()

pics = lookforme.findAndExport(personToFind,folderToSearch, resultFolder) 
print(pics)'''
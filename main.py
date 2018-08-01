import lookforme
import tkinter
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox
import os

def findAndExport(personToFind, folderToSearch, resultFolder):
    pics = lookforme.findAndExport(personToFind,folderToSearch, resultFolder) 
    tkinter.messagebox.showwarning("Warning"," החיפוש הסתיים, נמצאו " + str(len(pics)) + ' תוצאות')
    print(pics)
    print('Done!')
    

def browse_resultFolder_dir_button():
    global resultFolder
    filename = filedialog.askdirectory()
    resultFolder.set(filename)

def browse_folderToSearch_dir_button():
    global folderToSearch
    filename = filedialog.askdirectory()
    folderToSearch.set(filename)


def browse_personToFind_dir_button():
    global personToFind
    filename = filedialog.askopenfilename()
    personToFind.set(filename)

def center(win):
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
    
    w = 1200
    h = 250
    wmid = w/2

    root = tkinter.Tk()
    root.geometry(str(w) + 'x' + str(h))
    root.title('Look For Me')
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)
    
    Label(root, text='Look For Me', bg="Black", fg="white" ,font=("Courier", 32)).grid(row=1, columnspan=4, sticky=NSEW)

    
    Label(root, text="בחר פנים שברצונך לחפש").grid(row=2, column=3)
    personToFind = StringVar()
    button1 = Button(text="בחר תמונת פנים", command=browse_personToFind_dir_button)
    button1.grid(row=2, column=2)
    lbl0 = Label(master=root,textvariable=personToFind, bg='white')
    lbl0.grid(row=2, column=1)


    Label(root, text="בחר תיקיית תמונות שבתוכה תרצה לחפש").grid(row=3, column=3)
    folderToSearch = StringVar()
    button2 = Button(text="בחר תיקיה", command=browse_folderToSearch_dir_button)
    button2.grid(row=3, column=2)
    lbl1 = Label(master=root,textvariable=folderToSearch, bg='white')
    lbl1.grid(row=3, column=1)
    

    Label(root, text="בחר תיקיה שבה יופיעו תוצאות החיפוש").grid(row=4, column=3)
    resultFolder = StringVar()
    button3 = Button(text="בחר תיקיה", command=browse_resultFolder_dir_button)
    button3.grid(row=4, column=2)
    lbl2 = Label(master=root,textvariable=resultFolder, bg='white')
    lbl2.grid(row=4, column=1)
    
    def OpenResultFolder():
        if(resultFolder and len(resultFolder.get()) > 0):
            os.startfile(resultFolder.get())#('start "' + resultFolder.get() + '"')
        else:
            tkinter.messagebox.showwarning("Warning","בבקשה בחר תיקית יעד לתוצאות החיפוש")
            
    def search():
        if(personToFind and folderToSearch and resultFolder and len(personToFind.get())*len(folderToSearch.get())*len(resultFolder.get()) > 0):
            findAndExport(personToFind.get(),folderToSearch.get() , resultFolder.get())
        else:
            tkinter.messagebox.showwarning("Warning","בבקשה מלא את כל הפרטים")
    
    button_search = Button(text="    חפש    ", bg='black',fg='white' ,command=search)
    button_search.grid(row=5, column=2)

    button_search = Button(text="הצג את תוצאות החיפוש", bg='yellow' ,command=OpenResultFolder)
    button_search.grid(row=6, column=2)




    center(root)
    root.mainloop()


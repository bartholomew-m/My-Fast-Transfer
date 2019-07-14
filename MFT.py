import os
import shutil
from  tkinter import filedialog
from  tkinter import *
def aplication():
    okno = Tk()
    okno.title("Kończenie programu")
    src = filedialog.askdirectory(title = "Wybierz folder, którego zawartość chcesz przenieść: ")
    dest =filedialog.askdirectory(title = "Wybierz folder docelowy: ")
    files = os.listdir(src)
    os.chdir(src)
    for file in files:
        shutil.move(file, dest)
    files2 = os.listdir(dest)
    if files == files2:
        informacja = Label(okno, text='Wszystko przeniesione!').pack()
        exitbutton = Button(okno, text="OK", command=okno.destroy).pack()
        okno.mainloop()
    else:
        informacja = Label(okno, text='Bład podczas przenoszenia!').pack()
        exitbutton = Button(okno, text="OK", command=okno.destroy).pack()
        okno.mainloop()
aplication()
sys.exit()
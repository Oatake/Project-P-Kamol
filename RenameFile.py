import os
import shutil  # library for copy file command
import tkinter
from tkinter import Frame, messagebox
from tkinter.constants import X,LEFT,TRUE,RIGHT
import DataManagement as dm


# def CopyNRename(inputPath, outputPath):
#     inputPath=inputPath+"\\"
#     outputPath=outputPath+"\\"
#     for i in os.listdir(inputPath):
#         print(i)
#         shutil.copyfile(inputPath+i, outputPath+i)              #copy file from example to output
#         os.rename(outputPath+i, outputPath+i+'.txt')            #rename file by adding .txt

# def Rename(inputPath, outputPath):
#     inputPath=inputPath+"\\"
#     outputPath=outputPath+"\\"
#     for i in os.listdir(inputPath):
#         os.rename(outputPath+i, outputPath+i+'.txt')            #rename file by adding .txt

# def FuncButtonRename():
#     inputPath = et1.get()
#     outputPath = et2.get()
#     if (inputPath==outputPath):
#         try : 
#             Rename(inputPath, outputPath)
#             messagebox.showinfo("Rename Process", "Successful" )
#             os.startfile(outputPath)
#         except OSError as e:
#             messagebox.showerror("Rename Process", e.strerror )
#     else:
#         try : 
#             CopyNRename(inputPath, outputPath)
#             messagebox.showinfo("Rename Process", "Successful" )
#             os.startfile(outputPath)
#         except OSError as e:
#             messagebox.showerror("Rename Process", e.strerror )

def updateET2(message):
    x=1

def OnClick():
    position = dm.GetData(et1.get())
    # output.message = "Row "+ position.row + ", Column " + position.column
    message = "Blade position : Row is " + str(position.row) + ". Column is " + str(position.column) + "."
    # output(message)
    # print(output.message)
    tkinter.messagebox.showinfo(title="Position", message=message)

# class output:
#         def __init__(self, message):
#             self.message = message

# GUI section
GUI_Renamefile = tkinter.Tk()                           
GUI_Renamefile.title("Project P'Kamol")   
GUI_Renamefile.geometry("400x100+300+300")                  #dimension "widthxheight+x+y" x&y is grid when open gui

#Frame1
frame1=Frame(GUI_Renamefile)    
frame1.pack(fill=X)     

lbl1 = tkinter.Label(frame1,text="Blade barcode here",width=20)     #Path of your input file
lbl1.pack(side=LEFT,padx=5,pady=5)

et1 = tkinter.Entry(frame1)
et1.pack(fill=X,expand=TRUE)

#Frame2 
frame2=Frame(GUI_Renamefile)    
frame2.pack(fill=X)     

lbl2 = tkinter.Label(frame2,text="Size" ,width=20)    #Where to store output file
lbl2.pack(side=LEFT,padx=5,pady=5)

et1 = tkinter.Entry(frame2)
et1.pack(fill=X, expand=False)

#Frame3
frame3=Frame(GUI_Renamefile)    
frame3.pack(fill=X)     

B_Rename = tkinter.Button(frame3,text="locked", command=OnClick)
B_Rename.pack(side=RIGHT, padx=5,pady=5)

B_Stored = tkinter.Button(frame3,text="unlock", command=OnClick)
B_Stored.pack(side=RIGHT, padx=5,pady=5)
#mainloop
GUI_Renamefile.mainloop()

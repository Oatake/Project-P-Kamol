import tkinter
from tkinter import Frame, messagebox,PhotoImage,Tk
from tkinter.constants import X,Y,BOTH,LEFT,TRUE,RIGHT,BOTTOM,TOP
from functools import partial
import DataManagement as dm
import time

def OnClickLock():
    try :
        lockerid = current_locker_var.get()
        pt = input_pt_var.get()
        size = input_size_var.get()
        status = "Red"
        Time = time.time()
        dm.updateLocker(lockerid,pt,size,status)
        # update status frame
        status_pt_var.set(pt)
        status_var.set(status)
        print(lockerid + "locked")
    except :
        print("please select locker ID")

def OnClickUnlock():
    try :
        lockerid = current_locker_var.get()
        dm.clearLocker(lockerid)
        # update status frame
        status_pt_var.set("")
        status_var.set("")
        print(lockerid + "unlocked")
    except :
        print("Unlock error")   

def create_locker_frame(container):
    frame = tkinter.Frame(container)
    #Grid layout for each locker
    for x in range(4):
        frame.rowconfigure(x, weight=2)
    for y in range (4) :
        frame.columnconfigure(y, weight=2)
    # Attached button to each frame
    for x in range(4*3):
        for y in range(4):
            if (x%3==0) :
                try :
                    lk="Locker"+str(x)+str(y)
                    tkinter.Button(frame, image=dt_img[dm.getLocker(lk)["status"]], command=partial(ShowLocker,row=y,column=x)).grid(row=x, column=y)
                except :
                    tkinter.Button(frame, image=imgGreen, command=partial(ShowLocker,row=y,column=x)).grid(row=x, column=y)
                    print("error")
            elif (x%3==2) :
                tkinter.Label(frame, text= "PT").grid(row=x, column=y)
            else :
                tkinter.Label(frame, text= "Time in.").grid(row=x, column=y)
            
    return frame

def create_input_frame(container):
    frame = tkinter.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=3)

    # PT. Number
    tkinter.Label(frame, text="PT. ").grid(column=0 , row = 0, sticky='W')
    pt_entry = tkinter.Entry(frame, width=30, textvariable=input_pt_var)
    pt_entry.focus()
    pt_entry.grid(column=1, row=0, sticky='WE', columnspan=4)
    
    # Cst. sized
    tkinter.Label(frame, text= "sized").grid(column = 0, row = 1, sticky="W")
    tkinter.Entry(frame, width=30, textvariable=input_size_var).grid(column=1, row=1, sticky="WE", columnspan=4)

    #button    
    tkinter.Button(frame, text="unlocked", command=OnClickUnlock).grid(column=3,row=3, sticky="W")
    tkinter.Button(frame, text="locked", command=OnClickLock).grid(column=4,row=3, sticky="W")

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_status_frame(container):
    frame = tkinter.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=2)

    tkinter.Label(frame, textvariable=current_locker_var, font="arial 18 bold").grid(column=0, row=0, sticky="W")
    tkinter.Label(frame, text="PT No. : ").grid(column=0, row=1, sticky="W")
    tkinter.Label(frame, textvariable=status_pt_var, font="arial 14").grid(column=1, row=1, sticky="W")
    tkinter.Label(frame, text="Status : ").grid(column=0, row=2, sticky="W")
    tkinter.Label(frame, textvariable=status_var, font="arial 14").grid(column=1, row=2, sticky="W")

    return frame

def create_timer_frame(container):
    frame = tkinter.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=2)
    
    tkinter.Label(frame, text="Count down : ").grid(column=0, row=0, sticky="W")
    tkinter.Label(frame, textvariable=timer_var, font="arial 18", background="black",foreground="red").grid(column=0, row=1, sticky="NSWE")
    
    return frame

def ShowLocker(row,column):
    locker_id="Locker"+str(column)+str(row)
    current_locker_var.set(locker_id)
    locker=dm.getLocker(locker_id)
    input_pt_var.set("")
    input_size_var.set("")
    status_pt_var.set(locker["pt"])
    status_var.set(locker["status"])
    print(locker_id)

# GUI section
GUI = tkinter.Tk()                           
GUI.title("Project P'Kamol")   
# GUI.resizable(0,0)
# GUI.geometry("400x100+300+300")                  #dimension "widthxheight+x+y" x&y is grid when open gui

def checkTime():
    lockers = dm.getLockers()
    print(time.strftime('%H:%M:%S'))
    for x in lockers :
        # print (lockers[x]["tick_in"])
        if (((time.time() - lockers[x]["tick_in"]) >= 20) and (lockers[x]["tick_in"] != 0)) :
            print(x, "Alarm")
        elif ((time.time() - lockers[x]["tick_in"]) >= 10 and (lockers[x]["tick_in"] != 0)) :
            print(x, "Warning")
    # locker_frame=create_locker_frame(GUI)
    GUI.after(1000,checkTime) 

input_pt_var = tkinter.StringVar()
input_size_var = tkinter.StringVar()
status_pt_var = tkinter.StringVar()
#status is "available", "busy", "warning", "alarm"
status_var = tkinter.StringVar()
current_locker_var = tkinter.StringVar()
timer_var = tkinter.StringVar()

imgGreen= PhotoImage(file="Asset\\green.png")
imgRed= PhotoImage(file="Asset\\red.png")
imgYellow= PhotoImage(file="Asset\\yellow.png")
dt_img = {
    "available" : imgGreen,
    "busy" : imgGreen,
    "warning" : imgYellow,
    "alarm" : imgRed
}

locker_frame = create_locker_frame(GUI)
locker_frame.grid(row=0,column=0,columnspan=3)   

status_frame = create_status_frame(GUI)
status_frame.grid(row=1,column=1,sticky="N")

timer_frame = create_timer_frame(GUI)
# timer_frame.config(background="Black")
timer_frame.grid(row=1,column=0, sticky="N")

input_frame = create_input_frame(GUI)
input_frame.grid(row=1, column=2, sticky="N")


#end of status session#


#mainloop
GUI.after(1000,checkTime)  #timer interupt
GUI.mainloop()

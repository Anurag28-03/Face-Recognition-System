from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox 
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import train
from facerecognition import facerecognition
from attendence import attendence

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        #first image
        
        img1 = Image.open(r"materials\top.jpg")
        img1 = img1.resize((640,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=640,height=130)
        
        #second image

        img2 = Image.open(r"materials\logo.jpg")
        img2 = img2.resize((300,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=640,y=0,width=640,height=130)

        #third image

        img3 = Image.open(r"materials\top.jpg")
        img3 = img3.resize((640,130))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1280,y=0,width=640,height=130)

        #background image

        img4 = Image.open(r"materials\background1.jpg")
        img4 = img4.resize((1920,950))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1920,height=950)

        title_lbl = Label(bg_img,text="FACE   RECOGNITION    SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1920,height=50)

        # ============time===========
        def time():
            string =strftime('%H:%M:%S    %d/%m/%Y')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman",14,"bold"),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=250,height=50)
        time()

        #student button

        #button1

        img5 = Image.open(r"materials\studentdetail.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=320,width=220,height=50)

        #button2

        img6 = Image.open(r"materials\face_detector.jpg")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=820,y=100,width=220,height=220)

        b1_2 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b1_2.place(x=820,y=320,width=220,height=50)

        #button3

        img7 = Image.open(r"materials\attandance.png")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendence_data)
        b1.place(x=1500,y=100,width=220,height=220)

        b1_3 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b1_3.place(x=1500,y=320,width=220,height=50)

        #button4

        img8 = Image.open(r"materials\train_data.jpg")
        img8 = img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=500,width=220,height=220)

        b2_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b2_1.place(x=200,y=720,width=220,height=50)

        #button5

        img9 = Image.open(r"materials\photos.png")
        img9 = img9.resize((220,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=820,y=500,width=220,height=220)

        b2_2 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b2_2.place(x=820,y=720,width=220,height=50)

        #button6

        img10 = Image.open(r"materials\exit.png")
        img10 = img10.resize((220,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iExit)
        b1.place(x=1500,y=500,width=220,height=220)

        b2_3 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b2_3.place(x=1500,y=720,width=220,height=50)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    # ==============func Button================
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=facerecognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendence(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
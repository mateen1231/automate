# from tkinter import *
# from PIL import ImageTk
# from tkinter import messagebox
# import sqlite3
# import os

# class login_system:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("LOGIN SYSTEM")
#         self.root.geometry("1350x700+0+0")

#         # === images =============
#         self.laptop_image = ImageTk.PhotoImage(file=r"C:\Users\Ahmad\OneDrive\Desktop\TK-PROJECT\project\image1.png")
#         self.lbl_laptop_image = Label(self.root, image=self.laptop_image)
#         self.lbl_laptop_image.place(x=30, y=40)

#         # === login_frame =====
#         self.purchase_id = StringVar()
#         self.Upper_Price = StringVar()
        
#         login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
#         login_frame.place(x=750, y=100, width=350, height=460)

#         title = Label(self.root, text="Login system", font=("Elephant", 30, "bold"))
#         title.place(x=0, y=30, relwidth=1)

#         lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171")
#         lbl_user.place(x=50, y=100)

#         txt_purchase_id = Entry(login_frame, textvariable=self.purchase_id, font=("time new roman", 15), bg="#ECECEC")
#         txt_purchase_id.place(x=50, y=140, width=250)

#         lbl_Upper_Price= Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171")
#         lbl_Upper_Price.place(x=50, y=200)
#         txt_Upper_Price = Entry(login_frame, textvariable=self.Upper_Price, show="*", font=("time new roman", 15), bg="#ECECEC")
#         txt_Upper_Price.place(x=50, y=240, width=250)

#         btn_login = Button(login_frame, command=self.login, text="Log in", font=("arial rounded mt bold", 15),
#                            bg="#00B0F0", activebackground="#00B0F0", fg="white",
#                            activeforeground="white", cursor="hand2")
#         btn_login.place(x=50, y=300, width=250, height=35)

#         hr = Label(login_frame, bg="lightgray")
#         hr.place(x=50, y=370, width=250, height=2)

#         or_label = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("time new roman", 15, "bold"))
#         or_label.place(x=145, y=355)

#         btn_forget = Button(login_frame, text="Forget Password?", font=("time new roman", 13), bg="white",
#                             fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=100, y=390)

#         # =======Frame2======
#         register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
#         register_frame.place(x=750, y=570, width=350, height=60)

#         lbl_reg = Label(register_frame, text="WELCOME REAL ESTATE ", font=("time new roman", 15), bg="white").place(
#             x=40, y=20)

#     def login(self):
#         con = sqlite3.connect(database=r'ims.db')
#         cur = con.cursor()
#         try:
#             if self.purchase_id.get()=="" or self.Upper_Price.get()=="":
#                 messagebox.showerror('Error',"All feilds are required",parent=self.root)
#             else:
#                 cur.execute("SELECT * FROM purchase WHERE purchase_id=? AND Upper_Price=?", (self.purchase_id.get(), self.Upper_Price.get()))
#                 user = cur.fetchone()
            
#                 if user==None:
#                     messagebox.showerror("Error", "Invalid Username or Password\n Try again with correct credentials")
#                 else:
#                     self.root.destory()
#                     os.system("python dashboard.py")
#         except Exception as ex:
#             messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

# # Create the Tkinter root window
# root = Tk()

# # Create an instance of the login_system class and pass the root window to it
# obj = login_system(root)

# # Start the Tkinter event loop
# root.mainloop()



from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os

class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1350x700+0+0")

        # === images =============
        self.laptop_image = ImageTk.PhotoImage(file=r"C:\Users\Ahmad\OneDrive\Desktop\TK-PROJECT\project\image1.png")
        self.lbl_laptop_image = Label(self.root, image=self.laptop_image)
        self.lbl_laptop_image.place(x=30, y=40)

        # === login_frame =====
        self.purchase_id = StringVar()
        self.Upper_Price = StringVar()
        
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=750, y=100, width=350, height=460)

        title = Label(self.root, text="Login system", font=("Elephant", 30, "bold"))
        title.place(x=0, y=30, relwidth=1)

        lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171")
        lbl_user.place(x=50, y=100)

        txt_purchase_id = Entry(login_frame, textvariable=self.purchase_id, font=("time new roman", 15), bg="#ECECEC")
        txt_purchase_id.place(x=50, y=140, width=250)

        lbl_Upper_Price= Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171")
        lbl_Upper_Price.place(x=50, y=200)
        txt_Upper_Price = Entry(login_frame, textvariable=self.Upper_Price, show="*", font=("time new roman", 15), bg="#ECECEC")
        txt_Upper_Price.place(x=50, y=240, width=250)

        btn_login = Button(login_frame, command=self.login, text="Log in", font=("arial rounded mt bold", 15),
                           bg="#00B0F0", activebackground="#00B0F0", fg="white",
                           activeforeground="white", cursor="hand2")
        btn_login.place(x=50, y=300, width=250, height=35)

        hr = Label(login_frame, bg="lightgray")
        hr.place(x=50, y=370, width=250, height=2)

        or_label = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("time new roman", 15, "bold"))
        or_label.place(x=145, y=355)

        btn_forget = Button(login_frame, text="Forget Password?", font=("time new roman", 13), bg="white",
                            fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=100, y=390)

        # =======Frame2======
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=750, y=570, width=350, height=60)

        lbl_reg = Label(register_frame, text="WELCOME REAL ESTATE ", font=("time new roman", 15), bg="white").place(
            x=40, y=20)

    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.purchase_id.get()=="" or self.Upper_Price.get()=="":
                messagebox.showerror('Error',"All fields are required",parent=self.root)
            else:
                cur.execute("SELECT * FROM purchase WHERE purchase_id=? AND Upper_Price=?", (self.purchase_id.get(), self.Upper_Price.get()))
                user = cur.fetchone()
            
                if user is None:
                    messagebox.showerror("Error", "Invalid Username or Password\n Try again with correct credentials")
                else:
                    self.root.destroy()  # Fix typo: destory -> destroy
                    os.system("python dashboard.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

# Create the Tkinter root window
root = Tk()

# Create an instance of the login_system class and pass the root window to it
obj = login_system(root)

# Start the Tkinter event loop
root.mainloop()

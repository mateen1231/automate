from tkinter import *
from PIL import Image, ImageTk
from purchase import purchaseclass
from rent import rentclass
from sell import sellclass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("REAL ESTATE AUTOMATION")
        self.root.config(bg="white")
        
        # =======TITLE=====
        self.icon_title = PhotoImage(file=r"C:\Users\Ahmad\OneDrive\Desktop\TK-PROJECT\project\logo.png")
        title = Label(self.root, text="REAL ESTATE AUTOMATION", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Add a border around the logo label
        border_frame = Frame(self.root, bg="#001a4e")
        border_frame.place(x=0, y=0, relwidth=1, height=70)

        # Logo label inside the border
        title = Label(border_frame, text="REAL ESTATE AUTOMATION", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#001a4e", fg="white", anchor="w", padx=20)
        title.place(relwidth=1, height=70)

        # =====btn_logout====
        btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2")
        btn_logout.place(x=1180, y=10, height=50, width=150)
        
        #=====clock========
        self.lbl_clock = Label(self.root, text="WELCOME TO REAL ESTATE",
                      font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        #=====Left menu======
        self.Menulogo = Image.open(r"C:\Users\Ahmad\OneDrive\Desktop\TK-PROJECT\project\image4.png")
        self.Menulogo = self.Menulogo.resize((200, 150))
        self.Menulogo = ImageTk.PhotoImage(self.Menulogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menulogo = Label(LeftMenu, image=self.Menulogo)
        lbl_menulogo.pack(side=TOP, fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP,fill=X)
        btn_purchase = Button(LeftMenu, text="FOR PURCHASE", command=self.purchase, font=("times new roman", 15,"bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_rent = Button(LeftMenu, text="FOR RENT", command=self.rent, font=("times new roman", 15,"bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_sell = Button(LeftMenu, text="FOR SELL", command=self.sell, font=("times new roman", 15,"bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_back = Button(LeftMenu, text="BACK", font=("times new roman", 15,"bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        
        #======content=======
        self.lbl_purchase = Label(self.root, text="TOTAL PURCHASE\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_purchase.place(x=300, y=120, height=150, width=300)

        self.lbl_rent = Label(self.root, text="TOTAL RENT\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_rent.place(x=650, y=120, height=150, width=300)

        self.lbl_sell = Label(self.root, text="TOTAL SELL\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sell.place(x=1000, y=120, height=150, width=300)

        #=====footer========
        lbl_footer = Label(self.root, text="REA - REAL ESTATE AUTOMATION", font=("times new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        
        self.update_content()

    def purchase(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = purchaseclass(self.new_win)

    def rent(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = rentclass(self.new_win)

    def sell(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = sellclass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from purchase")
            purchase = cur.fetchall()
            self.lbl_purchase.config(text=f'TOTAL PURCHASE\n[ {str(len(purchase))}]')

            cur.execute("Select * from rent")
            rent = cur.fetchall()
            self.lbl_rent.config(text=f'TOTAL RENT\n[ {str(len(rent))}]')

            cur.execute("Select * from sell")
            sell = cur.fetchall()
            self.lbl_sell.config(text=f'TOTAL SELL\n[ {str(len(sell))}]')

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python logindatabase.py")

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()

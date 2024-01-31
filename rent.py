from tkinter import *
from tkinter import ttk
import sqlite3 
from PIL import ImageTk
from tkinter import ttk,messagebox
class rentclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("REAL ESTATE AUTOMATION")
        self.root.config(bg="white")
        self.root.focus_force()
        
         # === images =============
        self.laptop_image = ImageTk.PhotoImage(file=r"C:\Users\Ahmad\OneDrive\Desktop\TK-PROJECT\project\image7.png")
        self.lbl_laptop_image = Label(self.root, image=self.laptop_image)
        self.lbl_laptop_image.place(x=30, y=40)

        # ============================
        # ALL Variables==============
        self.var_searchtype = StringVar()
        self.var_searchtxt = StringVar()

        self.var_rent_id = StringVar()
        self.var_landtype = StringVar()
        self.var_area_sq = StringVar()
        self.var_name = StringVar()
        self.var_location = StringVar()
        self.var_area = StringVar()
        self.var_uprice = StringVar()
        self.var_lprice = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_contact = StringVar()

        # =====searchframe====
        SearchFrame = LabelFrame(self.root, text="Search", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE,
                                 bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # ======options======
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchtype,
                                  values=("Select", "Name", "Contact"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15),
                           bg="lightyellow")
        txt_search.place(x=200, y=10)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white",
                            cursor="hand2")
        btn_search.place(x=410, y=9, width=150, height=30)

        # ======title====
        title = Label(self.root, text="FOR RENT", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(
            x=50, y=100, width=1000)

        # ======content=====
        # =======row1========
        lbl_rentid = Label(self.root, text="Rent ID", font=("goudy old style", 15), bg="white").place(x=50,
                                                                                                               y=150)
        lbl_landtype = Label(self.root, text="Land Type", font=("goudy old style", 15), bg="white").place(x=350,
                                                                                                           y=150)
        lbl_area_sq = Label(self.root, text="Area (SQ)", font=("goudy old style", 15), bg="white").place(x=750,
                                                                                                           y=150)

        txt_rentid = Entry(self.root, textvariable=self.var_rent_id, font=("goudy old style", 15),
                               bg="lightyellow").place(x=170, y=150, width=180)
        cmb_landtype = ttk.Combobox(self.root, textvariable=self.var_landtype,
                                    values=("Select", "Plot", "Built", "Semi Built"), state='readonly',
                                    justify=CENTER, font=("goudy old style", 15))
        cmb_landtype.place(x=500, y=150, width=180)
        cmb_landtype.current(0)
        txt_area_sq = Entry(self.root, textvariable=self.var_area_sq, font=("goudy old style", 15),
                            bg="lightyellow").place(x=850, y=150, width=180)

        # =======row2========
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=190)
        lbl_location = Label(self.root, text="Location", font=("goudy old style", 15), bg="white").place(x=350, y=190)
        lbl_area = Label(self.root, text="Area Type", font=("goudy old style", 15), bg="white").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15),
                         bg="lightyellow").place(x=170, y=190, width=180)
        txt_location = Entry(self.root, textvariable=self.var_location, font=("goudy old style", 15),
                             bg="lightyellow").place(x=500, y=190, width=180)
        cmb_area = ttk.Combobox(self.root, textvariable=self.var_area,
                                values=("Select", "Commercial", "Industrial"), state='readonly',
                                justify=CENTER, font=("goudy old style", 15))
        cmb_area.place(x=850, y=190, width=180)
        cmb_area.current(0)

        # =======row3========
        lbl_uprice = Label(self.root, text="Upper Price", font=("goudy old style", 15), bg="white").place(x=50, y=230)
        lbl_lprice = Label(self.root, text="Lower Price", font=("goudy old style", 15), bg="white").place(x=350, y=230)
        lbl_utype = Label(self.root, text="Usertype", font=("goudy old style", 15), bg="white").place(x=750, y=230)

        txt_uprice = Entry(self.root, textvariable=self.var_uprice, font=("goudy old style", 15),
                           bg="lightyellow").place(x=170, y=230, width=180)
        txt_lprice = Entry(self.root, textvariable=self.var_lprice, font=("goudy old style", 15),
                           bg="lightyellow").place(x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype,
                                 values=("Admin", "Rental"), state='readonly',
                                 justify=CENTER, font=("goudy old style", 15))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        # =======row4========
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white").place(x=50, y=270)
        lbl_contact = Label(self.root, text="Contact No", font=("goudy old style", 15), bg="white").place(x=500, y=270)

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=170, y=270, width=300, height=60)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15),
                            bg="lightyellow").place(x=600, y=270, width=180)

        # ==========button======
        btn_add = Button(self.root, text="Save",command=self.add ,font=("goudy old style", 15), bg="#2196f3", fg="white",
                         cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="UPDATE",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white",
                            cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white",
                            cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_exist = Button(self.root, text="Exit",command=self.exist, font=("goudy old style", 15), bg="#607d8b", fg="white",
                           cursor="hand2").place(x=860, y=305, width=110, height=28)

        # ==========Rent Details=======
        pur_frame = Frame(self.root, bd=3, relief=RIDGE)
        pur_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(pur_frame, orient=VERTICAL)
        scrollx = Scrollbar(pur_frame, orient=HORIZONTAL)

        self.renttable = ttk.Treeview(pur_frame,
                                           columns=("Rent ID", "Land Type", "Area(SQ)", " Name","location",
                                                    "Area_Type", "Upper Price", "Lower Price", "User Type",
                                                    "Address", "Contact"), yscrollcommand=scrolly.set,
                                           xscrollcommand=scrollx.set)
        

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.renttable.xview)
        scrolly.config(command=self.renttable.yview)
        for col in ("Rent ID", "Land Type", "Area(SQ)", " Name","location","Area_Type", "Upper Price", "Lower Price",
                    "User Type", "Address", "Contact"):
            self.renttable.heading(col, text=col)

        self.renttable["show"] = "headings"

        for col in ("Rent ID", "Land Type", "Area(SQ)", " Name", "Area_Type", "Upper Price", "Lower Price",
                    "User Type", "Address", "Contact"):
            self.renttable.column(col, width=100)

        self.renttable.pack(fill=BOTH, expand=1)
        self.renttable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
#================================================================================================================
    # ... (previous code)
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
           cur.execute("Select * from rent")  # Corrected table name
           rows = cur.fetchall()
           self.renttable.delete(*self.renttable.get_children())
           for row in rows:
            self.renttable.insert('', END, values=row)
        except Exception as ex:
           messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

        

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_rent_id.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "Rent ID and Name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM rent WHERE rent_id=?", (self.var_rent_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Rent ID already assigned, try different", parent=self.root)
                else:
                    cur.execute("INSERT INTO rent (rent_id, Land_Type, Area_SQ,Name, location, Area_Type, "
                                "Upper_Price, Lower_Price, User_Type, Address, Contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (
                                    self.var_rent_id.get(),
                                    self.var_landtype.get(),
                                    self.var_area_sq.get(),
                                    self.var_name.get(),
                                    self.var_location.get(),
                                    self.var_area.get(),
                                    self.var_uprice.get(),
                                    self.var_lprice.get(),
                                    self.var_utype.get(),
                                    self.txt_address.get('1.0', END),
                                    self.var_contact.get()
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Rent Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)



    def get_data(self,ev):
        f=self.renttable.focus()
        content=(self.renttable.item(f))
        row=content['values']
        # print(row)
        self.var_rent_id.set(row[0]),
        self.var_landtype.set(row[1]),
        self.var_area_sq.set(row[2]),
        self.var_name.set(row[3]),
        self.var_location.set(row[4]),
        self.var_area.set(row[5]),
        self.var_uprice.set(row[6]),
        self.var_lprice.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert( END,row[9]),
        self.var_contact.set(row[10]) 
    

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_rent_id.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "Rent ID and Name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM rent WHERE rent_id=?", (self.var_rent_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Invalid Rent ID ", parent=self.root)
                else:
                    cur.execute("Update  rent  set Land_Type=?, Area_SQ=?,Name=?, location=?, Area_Type=?,Upper_Price=?, Lower_Price=?, User_Type=?, Address=?, Contact=? where rent_id=?",
                                (
                                    self.var_landtype.get(),
                                    self.var_area_sq.get(),
                                    self.var_name.get(),
                                    self.var_location.get(),
                                    self.var_area.get(),
                                    self.var_uprice.get(),
                                    self.var_lprice.get(),
                                    self.var_utype.get(),
                                    self.txt_address.get('1.0', END),
                                    self.var_contact.get(),
                                    self.var_rent_id.get()
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Rent Update Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_rent_id.get() == "":
               messagebox.showerror("Error", "Rent ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM rent WHERE rent_id=?", (self.var_rent_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Rent ID ", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("Delete from rent where rent_id=?", (self.var_rent_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Rent Deleted Successfully", parent=self.root)
                        self.exist()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def exist(self):
        self.var_rent_id.set(""),
        self.var_landtype.set("select"),
        self.var_area_sq.set(""),
        self.var_name.set(""),
        self.var_location.set(""),
        self.var_area.set(""),
        self.var_uprice.set(""),
        self.var_lprice.set(""),
        self.var_utype.set("Admin"),
        self.txt_address.delete('1.0', END),
        self.var_contact.set(""),
        self.var_searchtxt.set(""),
        self.var_searchtype.set("Select"),
        self.show()

   

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtype.get() == "Select":
               messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchtxt.get() == "":
               messagebox.showerror("Error", "Search area should be required", parent=self.root)
            else:
               cur.execute("Select * from rent where " + self.var_searchtype.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
               rows = cur.fetchall()
               if len(rows) != 0:
                    self.renttable.delete(*self.renttable.get_children())
                    for row in rows:
                        self.renttable.insert('', END, values=row)
               else:
                    messagebox.showerror("Error","N0 record Found!!!!",parent=self.root)
        except Exception as ex:
           messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
 
if __name__ == "__main__":
    root = Tk()
    obj = rentclass(root)
    root.mainloop()

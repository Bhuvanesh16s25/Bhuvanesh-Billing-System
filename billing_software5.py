from tkinter import *
import math, random, os
from tkinter import messagebox
import time


class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")
        self.root.iconbitmap(r'C:\Users\user\Downloads/money_pEK_icon.ico')
        self.root.resizable(False, False)
        self.root.geometry("1350x700+0+0")

        # ==========VARIABLES======================

        # =============CUSTOMER INFO VAR==============================

        self.CnameVar = StringVar()
        self.CPhoneVar = StringVar()
        self.billnoVar = StringVar()

        r_bill = random.randint(1000, 9999)
        self.billnoVar.set(r_bill)

        self.billsearchVar = StringVar()

        # =============PRODUCT FORM VAR==============================
        self.Pro1var = IntVar()
        self.Pro2var = IntVar()
        self.Pro3var = IntVar()
        self.Pro4var = IntVar()
        self.Pro5var = IntVar()
        self.Pro6var = IntVar()
        self.Pro7var = IntVar()
        self.Pro8var = IntVar()
        self.Pro9var = IntVar()
        self.Pro10var = IntVar()

        # =============BOTTOM FORM VAR==============================

        self.totalVar = StringVar()
        self.DisVar = IntVar()
        self.netTotalVar = StringVar()
        self.CpayVar = IntVar()
        self.CreturenVar = StringVar()

        heading = Label(self.root, text="Bhuvanesh Billing System", bg="#8a2ded", fg="white",
                            font=("arial", 20, "bold"), pady=10, bd=7, relief=GROOVE)
        heading.place(x=0, y=0, relwidth=1)
        # ======================== CUSTOMER INFORMATION FRAME================
        CFrame = LabelFrame(self.root, text="Customer Information", font=("arial", 12,), fg="gold", bd=5, bg="#e827de")
        CFrame.place(x=0, y=65, relwidth=1)

        # =====================CUSTOMER INFORMATION FORM====================
        CNamelbl = Label(CFrame, text="Customer Name: ", font=("arial", 12, "bold"), bg="#e827de", fg="white").grid(
            row=0, column=0, padx=10, pady=5, sticky="w")
        CnameEntry = Entry(CFrame, textvariable=self.CnameVar, width=20, font=("arial", 12, "bold"), bd=7,
                           relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        CPhoelbl = Label(CFrame, text="Phone Number: ", font=("arial", 12, "bold"), bg="#e827de", fg="white").grid(row=0,
                                                                                                                  column=2,
                                                                                                                  padx=10,
                                                                                                                  pady=5,
                                                                                                                  sticky="w")
        CPhoneEntry = Entry(CFrame, textvariable=self.CPhoneVar, width=20, font=("arial", 12, "bold"), bd=7,
                            relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        billnumber = Label(CFrame, text="Bill Number: ", font=("arial", 12, "bold"), bg="#e827de", fg="white").grid(
            row=0, column=4, padx=10, pady=5, sticky="w")
        billnumberEntry = Entry(CFrame, textvariable=self.billsearchVar, width=20, font=("arial", 12, "bold"), bd=7,
                                relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        billsearchbtn = Button(CFrame, command=self.search_bill, text="Search Bill", font=("arial", 12, "bold"),
                               bg="skyblue", fg="#222222").grid(row=0, column=6, padx=10, pady=5)

        # ==================PRODUCTS FRAME===============================
        ProFrame = LabelFrame(self.root, text="Product Section", fg="gold", bd=7, relief=GROOVE, bg="#e827de",
                              font=("arial", 12, "bold"))
        ProFrame.place(x=0, y=130, width=888, height=450)

        self.ProductList = [
            "--Select One--",
            "Rice",
            "Oil",
            "Juice",
            "Biscuit",
            "Hair Get",
            "Face Wash",
            "Face Cream",
            "Mustard Oil",
        ]
        self.ProductOne = StringVar()
        self.ProductOne.set(self.ProductList[0])

        self.ProductTwo = StringVar()
        self.ProductTwo.set(self.ProductList[0])

        self.ProductThree = StringVar()
        self.ProductThree.set(self.ProductList[0])

        self.ProductFour = StringVar()
        self.ProductFour.set(self.ProductList[0])

        self.ProductFive = StringVar()
        self.ProductFive.set(self.ProductList[0])

        self.ProductSix = StringVar()
        self.ProductSix.set(self.ProductList[0])

        self.ProductSeven = StringVar()
        self.ProductSeven.set(self.ProductList[0])

        self.ProductEight = StringVar()
        self.ProductEight.set(self.ProductList[0])

        self.ProductNine = StringVar()
        self.ProductNine.set(self.ProductList[0])

        self.ProductTen = StringVar()
        self.ProductTen.set(self.ProductList[0])

        pro1 = OptionMenu(ProFrame, self.ProductOne, *self.ProductList)
        pro1.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        pro1.config(width=12, font=("arail", 10, "bold"))
        pro1Entry = Entry(ProFrame, textvariable=self.Pro1var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        pro2 = OptionMenu(ProFrame, self.ProductTwo, *self.ProductList)
        pro2.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        pro2.config(width=12, font=("arail", 10, "bold"))
        pro2Entry = Entry(ProFrame, textvariable=self.Pro2var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        pro3 = OptionMenu(ProFrame, self.ProductThree, *self.ProductList)
        pro3.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        pro3.config(width=12, font=("arail", 10, "bold"))
        pro3Entry = Entry(ProFrame, textvariable=self.Pro3var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        pro4 = OptionMenu(ProFrame, self.ProductFour, *self.ProductList)
        pro4.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        pro4.config(width=12, font=("arail", 10, "bold"))
        pro4Entry = Entry(ProFrame, textvariable=self.Pro4var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        pro5 = OptionMenu(ProFrame, self.ProductFive, *self.ProductList)
        pro5.grid(row=4, column=0, pady=10, padx=10, sticky="w")
        pro5.config(width=12, font=("arail", 10, "bold"))
        pro5Entry = Entry(ProFrame, textvariable=self.Pro5var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        pro6 = OptionMenu(ProFrame, self.ProductSix, *self.ProductList)
        pro6.grid(row=5, column=0, pady=10, padx=10, sticky="w")
        pro6.config(width=12, font=("arail", 10, "bold"))
        pro6Entry = Entry(ProFrame, textvariable=self.Pro6var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        pro7 = OptionMenu(ProFrame, self.ProductSeven, *self.ProductList)
        pro7.grid(row=6, column=0, pady=10, padx=10, sticky="w")
        pro7.config(width=12, font=("arail", 10, "bold"))
        pro7Entry = Entry(ProFrame, textvariable=self.Pro7var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        pro8 = OptionMenu(ProFrame, self.ProductEight, *self.ProductList)
        pro8.grid(row=7, column=0, pady=10, padx=10, sticky="w")
        pro8.config(width=12, font=("arail", 10, "bold"))
        pro8Entry = Entry(ProFrame, textvariable=self.Pro8var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)

        pro9 = OptionMenu(ProFrame, self.ProductNine, *self.ProductList)
        pro9.grid(row=0, column=2, pady=10, padx=15, sticky="w")
        pro9.config(width=12, font=("arail", 10, "bold"))
        pro9Entry = Entry(ProFrame, textvariable=self.Pro9var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                          relief=SUNKEN).grid(row=0, column=3, padx=15, pady=10)

        pro10 = OptionMenu(ProFrame, self.ProductTen, *self.ProductList)
        pro10.grid(row=1, column=2, pady=10, padx=15, sticky="w")
        pro10.config(width=12, font=("arail", 10, "bold"))
        pro10Entry = Entry(ProFrame, textvariable=self.Pro10var, width=10, font=("arial", 10, "bold"),bg="skyblue", bd=5,
                           relief=SUNKEN).grid(row=1, column=3, padx=15, pady=10)

        # ====================BILLING FRAME============================
        Billframe = Frame(self.root, bd=7, relief=GROOVE)
        Billframe.place(x=800, y=133, height=450, width=550)

        bill_title = Label(Billframe, text="Billing Area", bd=5, relief=GROOVE, font=("arial", 12, "bold"), pady=5)
        bill_title.pack(side=TOP, fill=X)
        scroll_y = Scrollbar(Billframe, orient=VERTICAL)
        self.txtarea = Text(Billframe, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        self.welcombill()

        # ============CALCULATION FRAME============================

        BottomFrame = LabelFrame(self.root, text="Calculations Area", bd=7, relief=GROOVE, fg="gold",
                                 font=("arial", 10, "bold"), bg="#e827de")
        BottomFrame.place(x=0, relwidth=1, height=125, y=583)

        Totallbl = Label(BottomFrame, text="Total Bill: ", font=("arail", 10, "bold"), bg="#e827de", fg="white").grid(
            row=0, column=0, padx=5, pady=5, sticky="w")
        TotalEntry = Entry(BottomFrame, textvariable=self.totalVar, width=10, bd=5, relief=SUNKEN,
                           font=("arail", 10, "bold"),bg="skyblue").grid(row=0, column=1, padx=5, pady=5)

        Discountlbl = Label(BottomFrame, text="Discount: ", font=("arail", 10, "bold"), bg="#e827de", fg="white").grid(
            row=1, column=0, padx=5, pady=5, sticky="w")
        DiscountEntry = Entry(BottomFrame, textvariable=self.DisVar, width=10, bd=5, relief=SUNKEN,
                              font=("arail", 10, "bold"),bg="skyblue").grid(row=1, column=1, padx=5, pady=5)

        NetTotallbl = Label(BottomFrame, text="NET TOTAL: ", font=("arail", 12, "bold"), bg="#e827de", fg="white").grid(
            row=0, column=2, padx=5, pady=5, sticky="w")
        NetTotalEntry = Entry(BottomFrame, textvariable=self.netTotalVar, width=10, bd=5, relief=SUNKEN,
                              font=("arail", 12, "bold"), bg="red", fg="white").grid(row=0, column=3, padx=5, pady=5)

        CPaylbl = Label(BottomFrame, text="Customer Pay: ", font=("arail", 10, "bold"), bg="#e827de", fg="white").grid(
            row=1, column=2, padx=5, pady=5, sticky="w")
        CPayEntry = Entry(BottomFrame, textvariable=self.CpayVar, width=10, bd=5, relief=SUNKEN,
                          font=("arail", 12, "bold"),bg="skyblue").grid(row=1, column=3, padx=5, pady=5)

        CReturnlbl = Label(BottomFrame, text="Customer Return: ", font=("arail", 12, "bold"), bg="#e827de",
                           fg="white").grid(row=0, column=4, padx=5, pady=5, sticky="w")
        CReturnEntry = Entry(BottomFrame, textvariable=self.CreturenVar, width=10, bd=5, relief=SUNKEN,
                             font=("arail", 12, "bold"), bg="skyblue", fg="red").grid(row=0, column=5, padx=5, pady=5)

        # ==================BUTTON FRAME======================
        BtnFrame = Frame(BottomFrame, bd=7, relief=GROOVE)
        BtnFrame.place(x=680, width=660, height=95)

        Totalbtn = Button(BtnFrame, command=self.total_sum, text="Total", font=("arial", 12, "bold"), bg="purple",
                          fg="white", pady=10, width=10, bd=7, activebackground="black", activeforeground="white").grid(
            row=0, column=0, padx=4, pady=10)
        Gbillbtn = Button(BtnFrame, command=self.g_bill, text="Generate Bill", font=("arial", 12, "bold"), bg="purple",
                          fg="white", pady=10, width=10, bd=7, activebackground="black", activeforeground="white").grid(
            row=0, column=1, padx=4, pady=10)
        Clearbillbtn = Button(BtnFrame, command=self.clear_bill, text="Clear", font=("arial", 12, "bold"), bg="purple",
                              fg="white", pady=10, width=10, bd=7, activebackground="black",
                              activeforeground="white").grid(row=0, column=2, padx=4, pady=10)
        printbtn = Button(BtnFrame, text="Print", font=("arial", 12, "bold"), bg="purple", fg="white", pady=10,
                          width=10, bd=7, activebackground="black", activeforeground="white").grid(row=0, column=3,
                                                                                                   padx=4, pady=10)
        exitbtn = Button(BtnFrame, command=self.winexit, text="Exit", font=("arial", 12, "bold"), bg="purple",
                         fg="white", pady=10, width=10, bd=7, activebackground="black", activeforeground="white").grid(
            row=0, column=4, padx=4, pady=10)

    def total_sum(self):
        self.proone = self.Pro1var.get()
        self.protwo = self.Pro2var.get()
        self.prothree = self.Pro3var.get()
        self.profour = self.Pro4var.get()
        self.profive = self.Pro5var.get()
        self.prosix = self.Pro6var.get()
        self.proseven = self.Pro7var.get()
        self.proeight = self.Pro8var.get()
        self.pronine = self.Pro9var.get()
        self.proten = self.Pro10var.get()

        self.totalsum = float(
            self.proone +
            self.protwo +
            self.prothree +
            self.profour +
            self.profive +
            self.prosix +
            self.proseven +
            self.proeight +
            self.pronine +
            self.proten
        )
        self.totalVar.set(str(self.totalsum))

        self.netbill = self.totalsum - self.DisVar.get()
        self.netTotalVar.set(str(self.netbill))

        self.cpaycash = self.CpayVar.get()
        if self.cpaycash != 0:
            self.ccashreturn = self.cpaycash - self.netbill
            self.CreturenVar.set(str(self.ccashreturn))

    def welcombill(self):
        self.edate = time.strftime("%d/%m/%Y")
        self.etime = time.strftime("%H:%M:%S")
        self.txtarea.delete("1.0", END)
        self.txtarea.insert(END, "\t \t \tWelcome to Bill area\n")
        self.txtarea.insert(END, "\t \t \tPhone No: 9962550299\n\n")
        self.txtarea.insert(END, "================================================================\n")
        self.txtarea.insert(END, f"Bill No: {self.billnoVar.get()} \n")
        self.txtarea.insert(END, f"Customer Name: {self.CnameVar.get()}\n")
        self.txtarea.insert(END, f"Phone Number: {self.CPhoneVar.get()}\n")
        self.txtarea.insert(END, f"Date:{self.edate} , Time: {self.etime}\n")
        self.txtarea.insert(END, "================================================================\n")
        self.txtarea.insert(END, f"Product Name \t\t\t\t\t Price \n")
        self.txtarea.insert(END, "================================================================\n")

    def g_bill(self):
        if self.CnameVar.get() == "" and self.CPhoneVar.get() == "":
            messagebox.showerror("Error", "Customer Name And Phone Number Are Requierd!")
        elif self.totalVar.get() == "":
            messagebox.showerror("Error", "No Product Were Selected")
        else:
            self.welcombill()

            if self.Pro1var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductOne.get()} \t\t\t\t\t  {self.Pro1var.get()} \n")

            if self.Pro2var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductTwo.get()} \t\t\t\t  {self.Pro2var.get()} \n")

            if self.Pro3var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductThree.get()} \t\t\t\t  {self.Pro3var.get()} \n")

            if self.Pro4var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductFour.get()} \t\t\t\t  {self.Pro4var.get()} \n")

            if self.Pro5var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductFive.get()} \t\t\t\t  {self.Pro5var.get()} \n")

            if self.Pro6var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductSix.get()} \t\t\t\t  {self.Pro6var.get()} \n")

            if self.Pro7var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductSeven.get()} \t\t\t\t  {self.Pro7var.get()} \n")

            if self.Pro8var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductEight.get()} \t\t\t\t  {self.Pro8var.get()} \n")

            if self.Pro9var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductNine.get()} \t\t\t\t  {self.Pro9var.get()} \n")

            if self.Pro10var.get() != 0:
                self.txtarea.insert(END, f" {self.ProductTen.get()} \t\t\t\t  {self.Pro10var.get()} \n")

            if self.totalVar.get() != 0:
                self.txtarea.insert(END, "================================================================\n")
                self.txtarea.insert(END, f"\t\t\t Total:  {self.totalVar.get()} \n")
            if self.DisVar.get() != 0:
                self.txtarea.insert(END, f"\t\t\t Discount: {self.DisVar.get()} \n")
                self.txtarea.insert(END, "================================================================\n")
            if self.netTotalVar.get() != 0:
                self.txtarea.insert(END, "================================================================\n")
                self.txtarea.insert(END, f"\t\t\t Net Total: {self.netTotalVar.get()} \n")
                self.txtarea.insert(END, "================================================================\n")
                self.save_bill()

    def save_bill(self):
        mess = messagebox.askyesno("Save", "Do You Want To Save The Bill No. " + self.billnoVar.get() + "?")
        if mess > 0:
            self.data = self.txtarea.get("1.0", END)
            file = open("Bills/" + str(self.billnoVar.get()) + ".txt", "w")
            file.write(self.data)
            file.close()
            messagebox.showinfo("Saved", "Bill " + self.billnoVar.get() + " Saved Successfully.")

        else:
            return

    def search_bill(self):
        m = "no"
        for i in os.listdir("Bills/"):
            if i.split(".")[0] == self.billsearchVar.get():
                file = open(f"Bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in file:
                    self.txtarea.insert(END, d)
                file.close()
                m = "yes"
        if m == "no":
            messagebox.showerror("Error", "Invaild Bill Number.")

    def clear_bill(self):
        mess = messagebox.showinfo("Clear", "Do You Want To Clear")

        # ==========VARIABLES======================

        # =============CUSTOMER INFO VAR==============================

        self.CnameVar.set("")
        self.CPhoneVar.set("")
        self.billnoVar.set("")

        r_bill = random.randint(1000, 9999)
        self.billnoVar.set(r_bill)

        self.billsearchVar.set("")

        # =============PRODUCT FORM VAR==============================
        self.Pro1var.set(0)
        self.Pro2var.set(0)
        self.Pro3var.set(0)
        self.Pro4var.set(0)
        self.Pro5var.set(0)
        self.Pro6var.set(0)
        self.Pro7var.set(0)
        self.Pro8var.set(0)
        self.Pro9var.set(0)
        self.Pro10var.set(0)
        self.ProductOne.set(self.ProductList[0])
        self.ProductTwo.set(self.ProductList[0])
        self.ProductThree.set(self.ProductList[0])
        self.ProductFour.set(self.ProductList[0])
        self.ProductFive.set(self.ProductList[0])
        self.ProductSix.set(self.ProductList[0])
        self.ProductSeven.set(self.ProductList[0])
        self.ProductEight.set(self.ProductList[0])
        self.ProductNine.set(self.ProductList[0])
        self.ProductTen.set(self.ProductList[0])

        # =============BOTTOM FORM VAR==============================

        self.totalVar.set("")
        self.DisVar.set(0)
        self.netTotalVar.set("")
        self.CpayVar.set(0)
        self.CreturenVar.set("")
        self.txtarea.delete("1.0", END)
        self.welcombill()

    def winexit(self):
        mess = messagebox.askyesno("Notification", "Do You Want To Close? ")
        if mess > 0:
            self.root.destroy()


root = Tk()
obj = BillingApp(root)
root.mainloop()
#Importing necessary Libraries

from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import mysql

# Creating a Class Object
class Hospital:
    def __init__(self,root):
        #Initializing the root and Setting the GUI for the project accordingly
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        #********************** Creation of Variables for Buttons ********
        self.NameofTablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NoOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInfo = StringVar()
        self.BloodPressure = StringVar()
        self.Storage = StringVar()
        self.NhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DOB = StringVar()
        self.PatientAddress = StringVar()



        # Display of Title
        lbltitle = Label(self.root,text="Hospital Management System", bd=20, relief=RIDGE,fg="Red",bg="white", font=("Arial",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #************************************* Data Frames **********************************************************

        DataFrame = Frame(self.root, bd=10, relief=RIDGE)
        DataFrame.place(x=0,y=130, width=1430 , height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=2, font=("Times New Roman",15,"bold"), text="Patient Information")
        DataFrameLeft.place(x=0,y=5, width=880 , height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE,  font=("Times New Roman", 15, "bold"),
                                   text="Patient Details")
        DataFrameRight.place(x=885, y=5, width=520, height=350)

        # ************************************* Button Frames **********************************************************

        ButtonFrame = Frame(self.root, bd=10, relief=RIDGE)
        ButtonFrame.place(x=0,y=535, width=1430, height=100)

        # ************************************* Details Frame **********************************************************

        DetailsFrame = Frame(self.root, bd=10, relief=RIDGE)
        DetailsFrame.place(x=0, y=640, width=1430, height=170)

        # ************************************* Data Frame Left **********************************************************

        lblNameTablet = Label(DataFrameLeft, text="Name of Tablet:", font=("Times New Roman",12,"bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNAmeTablet = ttk.Combobox(DataFrameLeft, font =("Times New Roman",12,"bold"), width = 30 , textvariable=self.NameofTablets)
        comNAmeTablet['values'] = ("BCCA","Paracetamol","Covishield","Fyzer")
        comNAmeTablet.current(1)
        comNAmeTablet.grid(row=0, column=1)

        # Button Informations and collecting the data......

        lblref = Label(DataFrameLeft, text="Reference:", font=("Times New Roman",12,"bold"), padx=2, pady=6)
        lblref.grid(row=1, column=0,sticky=W)

        txtref = ttk.Entry(DataFrameLeft, width=33,font =("Times New Roman",12,"bold"),textvariable=self.Ref)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, text="Dose:", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblDose.grid(row=2, column=0, sticky=W)

        txtDose = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"),textvariable=self.Dose)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataFrameLeft, text="No of Tablets::", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)

        txtNoOfTablets = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"),textvariable=self.NoOfTablets)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataFrameLeft, text="LOT:", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)

        txtLot = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"),textvariable=self.Lot)
        txtLot.grid(row=4, column=1)

        lblissuedate = Label(DataFrameLeft, text="Issue Date:", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblissuedate.grid(row=5, column=0, sticky=W)

        txtissuedate = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"), textvariable=self.IssueDate)
        txtissuedate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, text="Exp. Date:", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)

        txtExpDate = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"), textvariable=self.ExpDate)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataFrameLeft, text="Daily Dose:", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)

        txtDailyDose = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"),textvariable=self.DailyDose)
        txtDailyDose.grid(row=7, column=1)


        # Other Half

        lblSideEffect = Label(DataFrameLeft, text="Side Effect:", font=("Times New Roman", 12, "bold"), padx=35, pady=6)
        lblSideEffect.grid(row=0, column=2, sticky=W)

        txtSideEffect = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"),textvariable=self.SideEffect)
        txtSideEffect.grid(row=0, column=3)

        lblFurtherInfo = Label(DataFrameLeft, text="Further Info:", font=("Times New Roman", 12, "bold"), padx=35, pady=6)
        lblFurtherInfo.grid(row=1, column=2, sticky=W)

        txtFurtherInfo = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"), textvariable=self.FurtherInfo)
        txtFurtherInfo.grid(row=1, column=3)

        lblBloodPressure = Label(DataFrameLeft, text="Blood Pressure:", font=("Times New Roman", 12, "bold"), padx=35, pady=6)
        lblBloodPressure.grid(row=2, column=2, sticky=W)

        txtBloodPressure = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"), textvariable=self.BloodPressure)
        txtBloodPressure.grid(row=2, column=3)

        lblStorage = Label(DataFrameLeft, text="Storage:", font=("Times New Roman", 12, "bold"), padx=35, pady=6)
        lblStorage.grid(row=3, column=2, sticky=W)

        txtStorage = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"),textvariable=self.Storage)
        txtStorage.grid(row=3, column=3)

        lblNhsNumber = Label(DataFrameLeft, text="Nhs Number:", font=("Times New Roman", 12, "bold"), padx=35, pady=6)
        lblNhsNumber.grid(row=4, column=2, sticky=W)

        txtNhsNumber = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"), textvariable=self.NhsNumber)
        txtNhsNumber.grid(row=4, column=3)

        lblPatientName = Label(DataFrameLeft, text="Patient Name:", font=("Times New Roman", 12, "bold"), padx=35, pady=6)
        lblPatientName.grid(row=5, column=2, sticky=W)

        txtPatientName = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"), textvariable=self.PatientName)
        txtPatientName.grid(row=5, column=3)

        lblDoB = Label(DataFrameLeft, text="DOB:", font=("Times New Roman", 12, "bold"), padx=35, pady=6)
        lblDoB.grid(row=6, column=2, sticky=W)

        txtDoB = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold") ,textvariable=self.DOB)
        txtDoB.grid(row=6, column=3)

        lblPatientAddress = Label(DataFrameLeft, text="Patient Address:", font=("Times New Roman", 12, "bold"), padx=35, pady=6)
        lblPatientAddress.grid(row=7, column=2, sticky=W)

        txtPatientAddress = ttk.Entry(DataFrameLeft, width=33, font=("Times New Roman", 12, "bold"), textvariable=self.PatientAddress)
        txtPatientAddress.grid(row=7, column=3)

        #********************************** Data Frame Right ****************

        self.txtPrescription = Text(DataFrameRight, font=("Times New Roman", 12, "bold"), padx=2, pady=6,width=60, height=15)
        self.txtPrescription.grid(row=0, column=0, padx=10, pady=5)


        #******************************** Buttons **********************************************************

        btnPrescription = Button(ButtonFrame, text = "Prescription", font=("Times New Roman", 12, "bold"), padx=5, pady=5, width=20, height=3,fg="black" ,background="light blue", command=self.iPrescription)

        btnPrescription.grid(row=0, column=1, padx=5)

        btnData = Button(ButtonFrame, text="Prescription Data", font=("Times New Roman", 12, "bold"), padx=5, pady=5,
                                 width=20, height=3, fg="black", background="light blue", command=self.iPrescriptionData)
        btnData.grid(row=0, column=2, padx=5)

        btnUpdate = Button(ButtonFrame, text="Update", font=("Times New Roman", 12, "bold"), padx=5, pady=5,
                                 width=20, height=3, fg="black", background="light blue",command=self.iupdate)
        btnUpdate.grid(row=0, column=3, padx=5)

        btnDelete = Button(ButtonFrame, text="Delete", font=("Times New Roman", 12, "bold"), padx=5, pady=5,
                                 width=20, height=3, fg="black", background="light blue",command=self.idelete)
        btnDelete.grid(row=0, column=4, padx=5)

        btnClear = Button(ButtonFrame, text="Clear", font=("Times New Roman", 12, "bold"), padx=5, pady=5,
                                 width=20, height=3, fg="black", background="light blue",command=self.clear)
        btnClear.grid(row=0, column=5, padx=5)

        btnExit = Button(ButtonFrame, text="Exit", font=("Times New Roman", 12, "bold"), padx=5, pady=5,
                                 width=20, height=3, fg="black", background="light blue", command=self.exit)
        btnExit.grid(row=0, column=6, padx=5)


        #**************************************** Scroll Bar ********************************************************

        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        self.hospital_table = ttk.Treeview(DetailsFrame, style="Treeview", columns=("NameofTablet","Ref","Dose","NoOfTablets","LOT","IssueDate","ExpDate","DailyDose","SideEffect","FurtherInfo","BloodPressure","Storage","NHSNumber","PatientNAme","DOB","PatientAddress"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("NameofTablet",text = "Name of Tablet")
        self.hospital_table.heading("Ref",text = "Reference")
        self.hospital_table.heading("Dose",text = "Dose")
        self.hospital_table.heading("NoOfTablets",text = "Number of Tablets")
        self.hospital_table.heading("LOT",text = "LOT")
        self.hospital_table.heading("IssueDate",text = "Issue Date")
        self.hospital_table.heading("ExpDate",text = "Expiration Date")
        self.hospital_table.heading("DailyDose",text = "Daily Dose")
        self.hospital_table.heading("SideEffect",text = "Side Effect")
        self.hospital_table.heading("FurtherInfo",text = "Further Info")
        self.hospital_table.heading("BloodPressure",text = "Blood Pressure")
        self.hospital_table.heading("Storage",text = "Storage")
        self.hospital_table.heading("NHSNumber",text = "NHS Number")
        self.hospital_table.heading("PatientNAme",text = "Patient Name")
        self.hospital_table.heading("DOB",text = "DOB")
        self.hospital_table.heading("PatientAddress",text = "Address")

        self.hospital_table["show"] = "headings"



        self.hospital_table.column("NameofTablet", width=100)
        self.hospital_table.column("Ref", width=100)
        self.hospital_table.column("Dose", width=100)
        self.hospital_table.column("NoOfTablets", width=100)
        self.hospital_table.column("LOT", width=100)
        self.hospital_table.column("IssueDate", width=100)
        self.hospital_table.column("ExpDate", width=100)
        self.hospital_table.column("DailyDose", width=100)
        self.hospital_table.column("SideEffect", width=100)
        self.hospital_table.column("FurtherInfo", width=100)
        self.hospital_table.column("BloodPressure", width=100)
        self.hospital_table.column("Storage", width=100)
        self.hospital_table.column("NHSNumber", width=100)
        self.hospital_table.column("PatientNAme", width=100)
        self.hospital_table.column("DOB", width=100)
        self.hospital_table.column("PatientAddress", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor) # To fill the data from Details Frame to Data Frame
        self.fetch_data() # Fetches the data function


        #************************************** FUNCTIONALITY DECLARATION *******************************************

    def iPrescriptionData(self):
        if self.NameofTablets.get() == "" or self.Ref.get()=="":
            messagebox.showerror("Error", "Please enter all required fields")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="Tann")
            mycursor = conn.cursor()
            mycursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                             (self.NameofTablets.get(), self.Ref.get(), self.Dose.get(), self.NoOfTablets.get(),
                              self.Lot.get(), self.IssueDate.get(), self.ExpDate.get(), self.DailyDose.get(),
                              self.SideEffect.get(), self.FurtherInfo.get(), self.BloodPressure.get(),
                              self.Storage.get(), self.NhsNumber.get(), self.PatientName.get(), self.DOB.get(),
                              self.PatientAddress.get()))
            messagebox.showinfo("Success", "Prescription Data has been inserted")

            conn.commit()
            self.fetch_data()
            conn.close()


    def iupdate(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="Tann")
        mycursor = conn.cursor()
        mycursor.execute("update hospital set Name_of_Tablet=%s, Dose=%s, No_of_tablets=%s, Lot=%s, issue_date=%s, exp_date=%s, daily_dose=%s, side_effects=%s, further_infp=%s, bloodpressure=%s ,storage=%s, nhs_number=%s, patient_name=%s, DOB=%s, patient_address=%s where ref=%s",(self.NameofTablets.get(), self.Dose.get(), self.NoOfTablets.get(),
                              self.Lot.get(), self.IssueDate.get(), self.ExpDate.get(), self.DailyDose.get(),
                              self.SideEffect.get(), self.FurtherInfo.get(), self.BloodPressure.get(),
                              self.Storage.get(), self.NhsNumber.get(), self.PatientName.get(), self.DOB.get(),
                              self.PatientAddress.get(), self.Ref.get(),))
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Data has been updated")


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="Tann")
        mycursor = conn.cursor()
        mycursor.execute("select * from hospital")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert('', END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=None):
        cursor_row  = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.NameofTablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.NoOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.SideEffect.set(row[8])
        self.FurtherInfo.set(row[9])
        self.BloodPressure.set(row[10])
        self.Storage.set(row[11])
        self.NhsNumber.set(row[12])
        self.PatientName.set(row[13])
        self.DOB.set(row[14])
        self.PatientAddress.set(row[15])


    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t"+self.NameofTablets.get()+"\n")
        self.txtPrescription.insert(END, "Reference Number:\t\t\t" + self.Ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number of Tablets:\t\t\t" + self.NoOfTablets.get() + "\n")
        self.txtPrescription.insert(END, "LOT:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
        self.txtPrescription.insert(END, "Exp. Date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.SideEffect.get() + "\n")
        self.txtPrescription.insert(END, "Further Info:\t\t\t" + self.FurtherInfo.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + self.BloodPressure.get() + "\n")
        self.txtPrescription.insert(END, "Storage:\t\t\t" + self.Storage.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t\t" + self.NhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DOB.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")


    def idelete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="Tann")
        mycursor = conn.cursor()
        query = "delete from hospital where ref=%s"
        value = (self.Ref.get(),)
        mycursor.execute(query,value)
        messagebox.showinfo("Success", "The table has been deleted")
        self.fetch_data()
        conn.commit()
        conn.close()

    def clear(self):
        self.NameofTablets.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.NoOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInfo.set("")
        self.BloodPressure.set("")
        self.Storage.set("")
        self.NhsNumber.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete(1.0, END)

    def exit(self):
        iExit = messagebox.askyesno("Exit", "Do you want to exit?")
        if iExit:
            root.destroy()
            return






root = Tk()
ob = Hospital(root)
root.mainloop()


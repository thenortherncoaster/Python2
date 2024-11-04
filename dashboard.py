from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")
        
# in 1550 width and 800 height, 0+0 means 0 distance from left and 0 distance from top, or x axis and y axis
        self.NameOfTablet=tk.StringVar()
        self.RefrenceNo=tk.StringVar()
        self.Dose=tk.StringVar()
        self.NoOfTablets=tk.StringVar()
        self.LotNo=tk.StringVar()
        self.IssueDate=tk.StringVar()
        self.ExpiryDate=tk.StringVar()
        self.DailyDose=tk.StringVar()
        self.SideEffects=tk.StringVar()
        self.FurtherInformation=tk.StringVar()
        self.BloodPressure=tk.StringVar()
        self.StorageAdvice=tk.StringVar()
        self.Medication=tk.StringVar()
        self.PatientID=tk.StringVar()
        self.NHSNumber=tk.StringVar()
        self.PatientName=tk.StringVar()
        self.DateOfBirth=tk.StringVar()
        self.PatientAddress=tk.StringVar()


        lbltitle=tk.Label(self.root,text="Hospital Management System",font=("times new roman",30,"bold"),bg="white",fg="black",relief=tk.RIDGE)
        lbltitle.pack(side=tk.TOP,fill=tk.X)

# Data Frame
        dataframe=tk.Frame(self.root,bd=2,relief=tk.RIDGE)
        dataframe.place(x=0,y=55,width=1550,height=500)
# Patient Details data frame
        dataframeleft=tk.LabelFrame(dataframe,bd=2,relief=tk.RIDGE,text="Patient Details",font=("times new roman",15,"bold"))
        dataframeleft.place(x=5,y=10,width=1020,height=420)

# Buttons Frame
        buttonframe=tk.Frame(self.root,bd=2,relief=tk.RIDGE)
        buttonframe.place(x=0,y=500,width=1550,height=50)
# Details Frame
        detailsframe=tk.LabelFrame(self.root,bd=2,relief=tk.RIDGE,text="Details",font=("times new roman",15,"bold"))
        detailsframe.place(x=0,y=550,width=1550,height=250)

#  Data Frame Left
        lblnametablet=tk.Label(dataframeleft,text="Name Of Tablet",font=("times new roman",15,"bold"))
        lblnametablet.grid(row=0,column=0,padx=2,pady=6)

        comnametablet=ttk.Combobox(dataframeleft,textvariable=self.NameOfTablet,state="readonly",width=33,font=("times new roman",14))
        comnametablet["values"]=("Adderlin","Aspirin","Bupropion","Citalopram","Duloxetine","Escitalopram","Fluoxetine","Gabapentin","Lamotrigine","Lithium","Mifepristone","Naltrexone","Paroxetine","Phenelzine","Pramipexole","Quetiapine","Risperidone","Sertraline","Stavudine","Tricyclic","Venlafaxine","Zolpidem")
        comnametablet.grid(row=0,column=1,padx=2,pady=6)

        lblreferenceno=tk.Label(dataframeleft,text="Refrence No:",font=("times new roman",15,"bold"),padx=2)
        lblreferenceno.grid(row=1,column=0,padx=2,pady=6)
        txtreferenceno=tk.Entry(dataframeleft,width=35,textvariable=self.RefrenceNo,font=("times new roman",14))
        txtreferenceno.grid(row=1,column=1,padx=2,pady=6)

        lbldose=tk.Label(dataframeleft,text="Dose:",font=("times new roman",15,"bold"),padx=2)
        lbldose.grid(row=2,column=0,padx=2,pady=6)
        txtdose=tk.Entry(dataframeleft,width=35,textvariable=self.Dose,font=("times new roman",14))
        txtdose.grid(row=2,column=1,padx=2,pady=6)

        lblnooftablets=tk.Label(dataframeleft,text="No. Of Tablets:",font=("times new roman",15,"bold"),padx=2)
        lblnooftablets.grid(row=3,column=0,padx=2,pady=6)
        txtnooftablets=tk.Entry(dataframeleft,width=35,textvariable=self.NoOfTablets,font=("times new roman",14))
        txtnooftablets.grid(row=3,column=1,padx=2,pady=6)

        lbllotno=tk.Label(dataframeleft,text="Lot No:",font=("times new roman",15,"bold"),padx=2)
        lbllotno.grid(row=4,column=0,padx=2,pady=6)
        txtlotno=tk.Entry(dataframeleft,width=35,textvariable=self.LotNo,font=("times new roman",14))
        txtlotno.grid(row=4,column=1,padx=2,pady=6)

        lblissuedate=tk.Label(dataframeleft,text="Issue Date:",font=("times new roman",15,"bold"),padx=2)
        lblissuedate.grid(row=5,column=0,padx=2,pady=6)
        txtissuedate=tk.Entry(dataframeleft,width=35,textvariable=self.IssueDate,font=("times new roman",14))
        txtissuedate.grid(row=5,column=1,padx=2,pady=6)

        lblexpirydate=tk.Label(dataframeleft,text="Expiry Date:",font=("times new roman",15,"bold"),padx=2)
        lblexpirydate.grid(row=6,column=0,padx=2,pady=6)
        txtexpirydate=tk.Entry(dataframeleft,width=35,textvariable=self.ExpiryDate,font=("times new roman",14))
        txtexpirydate.grid(row=6,column=1,padx=2,pady=6)

        lbldailydose=tk.Label(dataframeleft,text="Daily Dose:",font=("times new roman",15,"bold"),padx=2)
        lbldailydose.grid(row=7,column=0,padx=2,pady=6)
        txtdailydose=tk.Entry(dataframeleft,width=35,textvariable=self.DailyDose,font=("times new roman",14))
        txtdailydose.grid(row=7,column=1,padx=2,pady=6)

        lblsideeffects=tk.Label(dataframeleft,text="Side Effects:",font=("times new roman",15,"bold"),padx=2)
        lblsideeffects.grid(row=8,column=0,padx=2,pady=6)
        txtsideeffects=tk.Entry(dataframeleft,width=35,textvariable=self.SideEffects,font=("times new roman",14))
        txtsideeffects.grid(row=8,column=1,padx=2,pady=6)

        lblfurtherinformation=tk.Label(dataframeleft,text="Further Information:",font=("times new roman",15,"bold"),padx=2)
        lblfurtherinformation.grid(row=0,column=3,padx=2,pady=6)
        txtfurtherinformation=tk.Entry(dataframeleft,width=35,textvariable=self.FurtherInformation,font=("times new roman",14))
        txtfurtherinformation.grid(row=0,column=4,padx=2,pady=6)

        lblbloodpressure=tk.Label(dataframeleft,text="Blood Pressure:",font=("times new roman",15,"bold"),padx=2)
        lblbloodpressure.grid(row=1,column=3,padx=2,pady=6)
        txtbloodpressure=tk.Entry(dataframeleft,width=35,textvariable=self.BloodPressure,font=("times new roman",14))
        txtbloodpressure.grid(row=1,column=4,padx=2,pady=6)

        lblstoragadvice=tk.Label(dataframeleft,text="Storage Advice:",font=("times new roman",15,"bold"),padx=2)
        lblstoragadvice.grid(row=2,column=3,padx=2,pady=6)
        txtstoragadvice=tk.Entry(dataframeleft,width=35,textvariable=self.StorageAdvice,font=("times new roman",14))
        txtstoragadvice.grid(row=2,column=4,padx=2,pady=6)

        lblmedication=tk.Label(dataframeleft,text="Medication:",font=("times new roman",15,"bold"),padx=2)
        lblmedication.grid(row=3,column=3,padx=2,pady=6)
        txtmedication=tk.Entry(dataframeleft,width=35,textvariable=self.Medication,font=("times new roman",14))
        txtmedication.grid(row=3,column=4,padx=2,pady=6)

        lblpatientid=tk.Label(dataframeleft,text="Patient ID:",font=("times new roman",15,"bold"),padx=2)
        lblpatientid.grid(row=4,column=3,padx=2,pady=6)
        txtpatientid=tk.Entry(dataframeleft,width=35,textvariable=self.PatientID,font=("times new roman",14))
        txtpatientid.grid(row=4,column=4,padx=2,pady=6)

        lblNHSnumber=tk.Label(dataframeleft,text="NHS Number:",font=("times new roman",15,"bold"),padx=2)
        lblNHSnumber.grid(row=5,column=3,padx=2,pady=6)
        txtNHSnumber=tk.Entry(dataframeleft,width=35,textvariable=self.NHSNumber,font=("times new roman",14))
        txtNHSnumber.grid(row=5,column=4,padx=2,pady=6)

        lblpatientname=tk.Label(dataframeleft,text="Patient Name:",font=("times new roman",15,"bold"),padx=2)
        lblpatientname.grid(row=6,column=3,padx=2,pady=6)
        txtpatientname=tk.Entry(dataframeleft,width=35,textvariable=self.PatientName,font=("times new roman",14))
        txtpatientname.grid(row=6,column=4,padx=2,pady=6)

        lbldob=tk.Label(dataframeleft,text="Date of Birth:",font=("times new roman",15,"bold"),padx=2)
        lbldob.grid(row=7,column=3,padx=2,pady=6)
        txtdob=tk.Entry(dataframeleft,width=35,textvariable=self.DateOfBirth,font=("times new roman",14))
        txtdob.grid(row=7,column=4,padx=2,pady=6)

        lblpatientaddress=tk.Label(dataframeleft,text="Patient Address:",font=("times new roman",15,"bold"),padx=2)
        lblpatientaddress.grid(row=8,column=3,padx=2,pady=6)
        txtpatientaddress=tk.Entry(dataframeleft,width=35,textvariable=self.PatientAddress,font=("times new roman",14))
        txtpatientaddress.grid(row=8,column=4,padx=2,pady=6)

# Prescription Details data frame
        dataframeright=tk.LabelFrame(dataframe,bd=2,relief=tk.RIDGE,text="Prescription Details",font=("times new roman",15,"bold"))
        dataframeright.place(x=1050,y=10,width=470,height=420)

# Data Frame Right text field
        self.txtprescription=tk.Text(dataframeright,width=51,height=18,font=("times new roman",14))
        self.txtprescription.grid(row=0, column=0) # Add this line to place the Text widget
# Buttons
        btnprescription=tk.Button(buttonframe,text="Prescription",font=("times new roman",15,"bold"),bg="Green",fg="white",width=20)
        btnprescription.grid(row=0,column=0,padx=1,pady=1)
# Buttons
        btnprescriptiondata=tk.Button(buttonframe,text="Prescription Data",font=("times new roman",15,"bold"),bg="Green",fg="white",width=20,)
        btnprescriptiondata.grid(row=0,column=1,padx=1,pady=1)
# Buttons
        btnupdate=tk.Button(buttonframe,text="Update",font=("times new roman",15,"bold"),bg="Green",fg="white",width=20)
        btnupdate.grid(row=0,column=2,padx=1,pady=1)
# Buttons
        btndelete=tk.Button(buttonframe,text="Delete",font=("times new roman",15,"bold"),bg="Green",fg="white",width=20)
        btndelete.grid(row=0,column=3,padx=1,pady=1)
# Buttons
        btnreset=tk.Button(buttonframe,text="Reset",font=("times new roman",15,"bold"),bg="Green",fg="white",width=20)
        btnreset.grid(row=0,column=4,padx=1,pady=1)
# Buttons
        btnexit=tk.Button(buttonframe,text="Exit",font=("times new roman",15,"bold"),bg="Green",fg="white",width=20)
        btnexit.grid(row=0,column=5,padx=1,pady=1)
# Table ---------------------------------------------------------------------------------------------------------------
        # Scrollbar
        scrollbarxaxis=Scrollbar(detailsframe,orient=HORIZONTAL)
        scrollbaryaxis=Scrollbar(detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(detailsframe,columns=("Patient ID","Patient Name","NHS Number","Date of Birth","Patient Address","Prescription"),xscrollcommand=scrollbarxaxis.set,yscrollcommand=scrollbaryaxis.set)
        scrollbarxaxis.pack(side=BOTTOM,fill=X)
        scrollbaryaxis.pack(side=RIGHT,fill=Y)
        scrollbaryaxis.config(command=self.hospital_table.yview)
        scrollbarxaxis.config(command=self.hospital_table.xview)

        self.hospital_table.column("Patient ID",width=100)
        self.hospital_table.column("Patient Name",width=100)
        self.hospital_table.column("NHS Number",width=100)
        self.hospital_table.column("Date of Birth",width=100)
        self.hospital_table.column("Patient Address",width=100)
        self.hospital_table.column("Prescription",width=100)
        
        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH,expand=1)

        # Function to insert prescription data
        def insert_prescription_data():
            if all(field.get() == "" for field in [self.NameOfTablet, self.RefrenceNo, self.Dose, self.NoOfTablets, self.LotNo, self.IssueDate, self.ExpiryDate, self.DailyDose, self.SideEffects, self.FurtherInformation, self.BloodPressure, self.StorageAdvice, self.Medication, self.PatientID, self.NHSNumber, self.PatientName, self.DateOfBirth, self.PatientAddress]):
                messagebox.showerror("Error", "All Fields are Required")
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="YOUR_PASSWORD", database="hms")  # Replace 'YOUR_PASSWORD' with your actual password
                my_cursor = conn.cursor()

                my_cursor.execute("INSERT INTO hms VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.NameOfTablet.get(),
                    self.RefrenceNo.get(),
                    self.Dose.get(),
                    self.NoOfTablets.get(),
                    self.LotNo.get(),
                    self.IssueDate.get(),
                    self.ExpiryDate.get(),
                    self.DailyDose.get(),
                    self.SideEffects.get(),
                    self.FurtherInformation.get(),
                    self.BloodPressure.get(),
                    self.StorageAdvice.get(),
                    self.Medication.get(),
                    self.PatientID.get(),
                    self.NHSNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get(),
                ))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Prescription Data Inserted Successfully")


root = Tk()
obj = HospitalManagementSystem(root)
root.mainloop()


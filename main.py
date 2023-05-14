import tkinter
import pandas as pd
import subprocess
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import shutil
from tkcalendar import Calendar
from datetime import date
from tkinter import ttk
from datetime import date
import os
from os import startfile


# Creating Main Folder
directory = "Soham_Motors"
parent_dir = "D:/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass

# Creating Sub Folder
directory = "Software_Files"
parent_dir = "D:/Soham_Motors/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass

# Creating Sub Folder
directory = "Aadhar_Card"
parent_dir = "D:/Soham_Motors/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass

# Creating Sub Folder
directory = "Pan_Card"
parent_dir = "D:/Soham_Motors/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass

# Creating Sub Folder
directory = "Buyer_Aadhar_Card"
parent_dir = "D:/Soham_Motors/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass

# Creating Sub Folder
directory = "Buyer_Pan_Card"
parent_dir = "D:/Soham_Motors/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass

# Creating Sub Folder
directory = "Car_Insurance"
parent_dir = "D:/Soham_Motors/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass

# Creating Sub Folder
directory = "Reciept"
parent_dir = "D:/Soham_Motors/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass



# Creating/Loading Login Df
try:
    login_df = pd.read_csv('D:\Soham_Motors\Software_Files\login_file.csv', index_col='Unnamed: 0')

except OSError as error:
    dict2 = {
        "user_id": ["admin"],
        "password": ["admin"]
        }
    empty_csv_df = pd.DataFrame(dict2)
    empty_csv_df.to_csv('D:\Soham_Motors\Software_Files\login_file.csv')

    login_df = pd.read_csv("D:\Soham_Motors\Software_Files\login_file.csv", index_col="Unnamed: 0")

user_id = login_df.user_id[0]
password = login_df.password[0]


def login_window():

    def authentication():
        if username_var.get()==user_id and password_var.get()==password:
            tkinter.messagebox.showinfo("Authentication Successful", "Login Successful")
            login_root.destroy()
            main_menu_window()
        else:
            tkinter.messagebox.showerror("Authentication Unsuccessful", "Incorrect User ID or Password")

    def authentication_bind(event):
        authentication()


    login_root = Tk()
    login_root.geometry("1366x695-0+0")
    login_root.title("Login - Speed Up Billing Software")
    login_root.configure(bg="#315b82")
    login_root.iconbitmap('speed_up_logo.ico')

    # Variables Used
    username_var = StringVar()
    password_var = StringVar()

    # Adding Create Account Image
    f1 = Frame(login_root, borderwidth=1, bg="#315b82")
    f1.pack(pady=50)

    login_photo = PhotoImage(file='login_logo.png')
    login_image = Label(f1, image=login_photo, bg="#315b82").pack(pady=10)
    login_text = Label(f1, text="Login", font=('Arial Black', 35), bg="#315b82", fg="#ebde4d").pack(padx=50)

    f2 = Frame(login_root, borderwidth=1, bg="#315b82")
    f2.pack(pady=20)

    user_label = Label(f2, text="User ID : ", font=('Arial Black', 20), bg="#315b82", fg="white").grid(row=1, column=1, padx=10)
    pass_label = Label(f2, text="Password : ", font=('Arial Black', 20), bg="#315b82", fg="white").grid(row=2, column=1)

    user_entry = Entry(f2, textvariable=username_var, font=('comicsansms', 15))
    user_entry.grid(row=1, column=2)
    pass_entry = Entry(f2, textvariable=password_var, font=('comicsansms', 15), show="*").grid(row=2, column=2)

    user_entry.focus()
    
    case_sensitive_label = Label(f2, text="  (Case Sensitive)", font=('Arial', 13), bg="#315b82", fg="yellow").grid(row=1, column=3)
    case_sensitive_label = Label(f2, text="  (Case Sensitive)", font=('Arial', 13), bg="#315b82", fg="yellow").grid(row=2, column=3)

    f3 = Frame(login_root, borderwidth=1, bg="#315b82")
    f3.pack(pady=40)

    login_but = Button(f3, text="Login", font=('Arial Black', 15), bg='#9df760', command=authentication)
    login_but.pack(pady=20)

    # Binding Enter Key
    login_root.bind('<Return>',authentication_bind)

    login_root.mainloop()


def main_menu_window():

    def add_car_details_func():
        main_menu_root.destroy()
        add_car_details()

    def show_car_details_func():
        main_menu_root.destroy()
        show_car_details()

    def add_client_details_func():
        main_menu_root.destroy()
        add_client_details()

    def show_client_details_func():
        main_menu_root.destroy()
        show_client_details()

    def add_buyer_details_func():
        main_menu_root.destroy()
        add_buyer_details()

    def show_buyer_details_func():
        main_menu_root.destroy()
        show_buyer_details()

    def about_us_func():
        main_menu_root.destroy()
        about_us()

    def exit_func():
        main_menu_root.destroy()

    main_menu_root = Tk()
    main_menu_root.geometry("1366x695-0+0")
    main_menu_root.title("Login - Speed Up Billing Software")
    main_menu_root.configure(bg="#001020")
    main_menu_root.iconbitmap('speed_up_logo.ico')

    f1 = Frame(main_menu_root, borderwidth=1, bg='#001020')
    f1.pack(pady=10)

    company_text_label = Label(f1, text='Soham Motors', bg='#001020', fg='white', font=('Berlin Sans FB Demi',40)).pack(pady=5)
    add1 = Label(f1, text='Drive your Dreams', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).pack()
    
    f2 = Frame(main_menu_root, borderwidth=1, bg='#001020')
    f2.place(x=450, y=150)

    b1 = Button(f2, text="       Add Car        ", font=('Arial Black', 12), bg='#fce779', command=add_car_details_func).grid(row=1, column=1)
    b2 = Button(f2, text="Show Car Details", font=('Arial Black', 12), bg='#fce779', command=show_car_details_func).grid(row=1, column=2, padx=90, pady=20)

    b3 = Button(f2, text="Add Client Inquiry", font=('Arial Black', 12), bg='#d9965b', command=add_client_details_func).grid(row=2, column=1, pady=20)
    b4 = Button(f2, text="Show Client Inquiry", font=('Arial Black', 12), bg='#d9965b', command=show_client_details_func).grid(row=2, column=2, padx=90)
    
    b5 = Button(f2, text="Add Buyer Details", font=('Arial Black', 12), bg='#7fd95b', command=add_buyer_details_func).grid(row=3, column=1, pady=20)
    b6 = Button(f2, text="Show Buyer Details", font=('Arial Black', 12), bg='#7fd95b', command=show_buyer_details_func).grid(row=3, column=2, padx=90)
    
    f3 = Frame(main_menu_root, borderwidth=1, bg='#001020')
    f3.place(x=620, y=410)

    b8 = Button(f3, text="About Us", font=('Arial Black', 12), bg='#0ddbd1', command=about_us_func).pack(pady=30)
    b9 = Button(f3, text="     Exit     ", font=('Arial Black', 12), bg='#ff7070', command=exit_func).pack()

    main_menu_root.mainloop()


def add_car_details():
    global selected_issue_date, selected_expiry_date

    def insurance_issue_func():
        selected_issue_date = insurance_calendar.get_date()
        insurance_issue_var.set(selected_issue_date)
    
    def insurance_expiry_func():
        selected_expiry_date = insurance_calendar.get_date()
        insurance_expiry_var.set(selected_expiry_date)
    
    def add_car_func():

        # Loading Car Details Df
        try:
            car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

        except Exception as error:
            dict2 = {
                "Car_Name": [],
                "Model": [],
                "Year": [],
                "Basic_Cost": [],
                "Tire_Cost": [],
                "Battery": [],
                "Denting_Painting_Cost": [],
                "Other_Expenses": [],
                "Insurance_issue_date": [],
                "Insurance_expiry_date": [],
                "Date_of_Entry": [],
                "Ref_No": []
                }
            empty_csv_df = pd.DataFrame(dict2)
            empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

            car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")


        # Appending Car Details to Csv
        car_name =  car_name_var.get()
        model = model_var.get()
        year = year_var.get()
        basic_cost =  basic_cost_var.get()
        tire =  tire_var.get()
        battery = battery_var.get()
        denting_painting = denting_painting_var.get()
        other_expenses = other_expenses_var.get()
        insurance_issue_date = insurance_issue_var.get()
        insurance_expiry_date = insurance_expiry_var.get()

        today = date.today()
        date_of_entry = today.strftime("%d/%m/%Y")



        car_details_df_len = len(car_details_df)
        try:
            pre_ref_no = int(car_details_df.Ref_No.to_list()[car_details_df_len-1])
        except Exception as Error:
            pre_ref_no = 0
        # print("Pre Ref No: ", pre_ref_no)

        # Checking All Entry Values are Filled
        if car_name=="" or model=="" or year=="" or basic_cost=="" or insurance_issue_date=="" or insurance_expiry_date=="":
            tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")
        else: 
            dict3 = {
                "Car_Name": [car_name],
                "Model": [model],
                "Year": [year],
                "Basic_Cost": [basic_cost],
                "Tire_Cost": [tire],
                "Battery": [battery],
                "Denting_Painting_Cost": [denting_painting],
                "Other_Expenses": [other_expenses],
                "Insurance_issue_date": [insurance_issue_date],
                "Insurance_expiry_date": [insurance_expiry_date],
                "Date_of_Entry": [date_of_entry],
                "Ref_No":[pre_ref_no + 1]
                }
            add_car_details_df = pd.DataFrame(dict3)

            df2 = pd.concat([car_details_df, add_car_details_df], ignore_index=True)
            df2.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")



            if clear_entry_content_var.get()==1:
                car_name_entry.delete(0, END)
                model_entry.delete(0, END)
                year_entry.delete(0, END)
                basic_cost_entry.delete(0, END)
                tire_entry.delete(0, END)
                battery_entry.delete(0, END)
                denting_painting_entry.delete(0, END)
                other_expenses_entry.delete(0, END)
                
                insurance_issue_var.set("")
                insurance_expiry_var.set("")

                tire_var.set(0)
                battery_var.set(0)
                denting_painting_var.set(0)
                other_expenses_var.set(0)
                
                car_name_entry.focus()

            else:
                pass

            tkinter.messagebox.showinfo("Car Details Added Successfully", "Car Details Added Successfully")

    def back_but_func():
        add_car_root.destroy()
        main_menu_window()




    add_car_root = Tk()
    add_car_root.geometry("1366x695-0+0")
    add_car_root.title("Login - Speed Up Billing Software")
    add_car_root.configure(bg="#001020")
    add_car_root.iconbitmap('speed_up_logo.ico')

    # All Variables

    car_name_var = StringVar()
    model_var = StringVar()
    year_var = StringVar()
    basic_cost_var = StringVar()
    tire_var = IntVar()
    battery_var = IntVar()
    denting_painting_var = IntVar()
    other_expenses_var = IntVar()
    clear_entry_content_var = IntVar()

    insurance_issue_var = StringVar()
    insurance_expiry_var = StringVar()

    # -------------- Tkinter Design Starts Here ----------------
    f0 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Add Car Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    f1 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f1.pack(pady=40)

    car_name_label = Label(f1, text='Car Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    car_name_entry = Entry(f1, textvariable=car_name_var, font=('comicsansms', 15))
    car_name_entry.grid(row=1, column=2)

    f2 = Frame(f1, borderwidth=1, bg='#001020')
    f2.grid(row=1, column=3, padx=20)
    
    model_label = Label(f2, text='Model: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    model_entry = Entry(f2, textvariable=model_var, font=('comicsansms', 15))
    model_entry.grid(row=1, column=2)
    
    year_label = Label(f1, text='Year: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=5)
    year_entry = Entry(f1, textvariable=year_var, font=('comicsansms', 15))
    year_entry.grid(row=1, column=6)
    
    basic_cost_label = Label(f1, text='Basic Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    basic_cost_entry = Entry(f1, textvariable=basic_cost_var, font=('comicsansms', 15))
    basic_cost_entry.grid(row=4, column=2)
    
    tire_label = Label(f1, text='Tire Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    tire_entry = Entry(f1, textvariable=tire_var, font=('comicsansms', 15))
    tire_entry.grid(row=5, column=2)
    
    battery_label = Label(f1, text='Battery Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    battery_entry = Entry(f1, textvariable=battery_var, font=('comicsansms', 15))
    battery_entry.grid(row=6, column=2)
    
    denting_painting_label = Label(f1, text='Denting Painting Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    denting_painting_entry = Entry(f1, textvariable=denting_painting_var, font=('comicsansms', 15))
    denting_painting_entry.grid(row=7, column=2)
    
    other_expenses_label = Label(f1, text='Other Expenses: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=8, column=1)
    other_expenses_entry = Entry(f1, textvariable=other_expenses_var, font=('comicsansms', 15))
    other_expenses_entry.grid(row=8, column=2)

    clear_entry_content_button = Checkbutton(f1, text = "Clear Entry Content", bg='#f7ea36', font=('Comicsansms', 10, 'bold') , variable = clear_entry_content_var, onvalue = 1, offvalue = 0, height = 2, width = 20)
    clear_entry_content_button.select()
    clear_entry_content_button.grid(row=7, column=3)

    f3 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f3.pack()

    # Add Calendar

    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    insurance_calendar = Calendar(f3, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    insurance_calendar.grid(row=1, column=1)
    
    f5 = Frame(f3, borderwidth=1, bg='#001020')
    f5.grid(row=1, column=2, padx=10)

    insurance_issue_but = Button(f5, text="Insurance Issue", font=('Arial Black', 10), bg='#fcca5d', command=insurance_issue_func).grid(row=1, column=1, pady=10)
    insurance_expiry_but = Button(f5, text="Insurance Expiry", font=('Arial Black', 10), bg='#fcca5d', command=insurance_expiry_func).grid(row=2, column=1, pady=10)
    
    insurance_issue_label = Label(f5, textvariable=insurance_issue_var, bg='#001020', fg='white', font=('Arial Black',10)).grid(row=1, column=2)
    insurance_expiry_label = Label(f5, textvariable=insurance_expiry_var, bg='#001020', fg='white', font=('Arial Black',10)).grid(row=2, column=2)
    
    f4 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f4.pack(pady=20)

    add_but = Button(f4, text="Add", font=('Arial Black', 13), bg='#5eff8c', command=add_car_func).grid(row=1, column=1, padx=30)
    back_but = Button(f4, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).grid(row=1, column=2)
    
    car_name_entry.focus()

    add_car_root.mainloop()
    # -------------- Tkinter Design Starts Here ----------------


def show_car_details():

    show_car_root = Tk()
    show_car_root.geometry("1366x695-0+0")
    show_car_root.title("Login - Speed Up Billing Software")
    show_car_root.configure(bg="#001020")
    show_car_root.iconbitmap('speed_up_logo.ico')

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Basic_Cost": [],
            "Tire_Cost": [],
            "Battery": [],
            "Denting_Painting_Cost": [],
            "Other_Expenses": [],
            "Insurance_issue_date": [],
            "Insurance_expiry_date": [],
            "Date_of_Entry": [],
            "Ref_No": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    f0 = Frame(show_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Show Car Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    # Adding Filter Search Title
    f2 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f2.pack(fill=BOTH, padx=100, pady=0)

    title1_label = Label(f2, text='Filter Search:', bg='#001020', fg='#f0b754', font=('Berlin Sans FB Demi',20)).grid(row=1, column=1, padx=0, pady=20)
    title2_label = Label(f2, text='', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',10)).grid(row=1, column=2)
    

    def car_box_update(event):
        global model_list, car1_selected

        car_selected = event.widget.get()
        car1_selected = car_selected
        if car_selected!="Select Car":

            # car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()

            model_list = car_details_df[car_details_df.Car_Name==car_selected].drop_duplicates(subset = ["Model"]).Model.to_list()
            model_list.insert(0, "Select Model")
            model_box['values'] = model_list
    
    def model_box_update(event):
        global year_list

        model_selected = event.widget.get()
        if model_selected!="Select Model":
            year_list = car_details_df[car_details_df.Car_Name==car1_selected][car_details_df.Model==model_selected].drop_duplicates(subset = ["Year"]).Year.to_list()
            year_list.insert(0, "Select Year")
            year_box['values'] = year_list


    # Adding Search Options -------- Starts Here

    # ------ Car Name Combobox --------------
    f10 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f10.pack(fill=BOTH, padx=100)

    f3 = Frame(f10, borderwidth=1, bg="#001020")
    f3.grid(row=1, column=1)

    car_name_label = Label(f3, text='Car Name: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    car_name_list = car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()
    car_name_list.insert(0, "Select Car")

    car_name_var = StringVar()
    car_name_var.set(car_name_list[0])

    car_box = ttk.Combobox(f3, width=20, textvariable=car_name_var)
    car_box['values'] = car_name_list
    car_box.grid(row=1, column=2)
    car_box.current(0)
    car_box.bind("<<ComboboxSelected>>", car_box_update)

    # ------ Model Combobox ----------------
    f4 = Frame(f3, borderwidth=1, bg="#001020")
    f4.grid(row=1, column=3, padx=20)

    model_label = Label(f4, text='Model: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    model_list = []
    model_list.insert(0, "Select Model")

    model_var = StringVar()
    model_var.set(model_list[0])

    model_box = ttk.Combobox(f4, width=20, textvariable=model_var)
    model_box['values'] = model_list
    model_box.grid(row=1, column=2)
    model_box.current(0)
    model_box.bind("<<ComboboxSelected>>", model_box_update)


    # ------ Year Combobox ----------------
    f5 = Frame(f3, borderwidth=1, bg="#001020")
    f5.grid(row=1, column=4)

    year_label = Label(f5, text='Year: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    year_list = []
    year_list.insert(0, "Select Year")

    year_var = StringVar()
    year_var.set(year_list[0])

    year_box = ttk.Combobox(f5, width=20, textvariable=year_var)
    year_box['values'] = year_list
    year_box.grid(row=1, column=2)
    year_box.current(0)
    

    def date_of_entry_func():
        selected_entry_date = date_of_entry_calendar.get_date()
        date_of_entry_var.set(selected_entry_date)

        required_car_result = car_details_df[car_details_df.Date_of_Entry == date_of_entry_var.get()]

        iid_number1 =1
        sr_no1 = 1

        for i in tree1.get_children():
            tree1.delete(i)
        for i in range(0, len(required_car_result)):
            total_cost_1 = int(required_car_result.Basic_Cost.to_list()[i]) + required_car_result.Tire_Cost.to_list()[i] + required_car_result.Battery.to_list()[i]+ required_car_result.Denting_Painting_Cost.to_list()[i] + required_car_result.Other_Expenses.to_list()[i]
            tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_car_result.Car_Name.to_list()[i], required_car_result.Model.to_list()[i], required_car_result.Year.to_list()[i], total_cost_1, required_car_result.Insurance_issue_date.to_list()[i], required_car_result.Insurance_expiry_date.to_list()[i], required_car_result.Date_of_Entry.to_list()[i], required_car_result.Ref_No.to_list()[i]))
            iid_number1+=1
            sr_no1+=1        


    f6 = Frame(show_car_root, borderwidth=1, bg='#001020')
    f6.place(x=820, y=100)

    # Add Calendar
    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    date_of_entry_calendar = Calendar(f6, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    date_of_entry_calendar.grid(row=1, column=1)

    date_of_entry_var = StringVar()

    date_of_entry_but = Button(show_car_root, text="Date of Entry", font=('Arial Black', 10), bg='#fcca5d', command=date_of_entry_func).place(x=1110, y=140)
    date_of_entry_label = Label(show_car_root, textvariable=date_of_entry_var, bg='#001020', fg='white', font=('Arial Black',10)).place(x=1120, y=180)


    # Adding Search Options -------- Ends Here

    f1 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f1.pack(fill=BOTH, padx=100, pady=50)

    # ------------Treeview for Displaying Cart Items and its Details---------------------

    tree1 = ttk.Treeview(f1, selectmode="extended", height=10)
    # Column names of Treeview
    tree1['columns'] = ('Sr', 'Name', 'Model', 'Year', 'Total Cost', 'Insurance Issue Date', 'Insurance Expiry Date', 'Date of Entry', 'Ref_No')

    # Adding Columns
    tree1.column('#0', width=0, stretch=NO)
    tree1.column('Sr', anchor=W, width=30, minwidth=0, stretch=NO)
    tree1.column('Name', anchor=W, width=50, minwidth=50)
    tree1.column('Model', anchor=W, width=50, minwidth=50)
    tree1.column('Year', anchor=W, width=50, minwidth=50)
    tree1.column('Total Cost', anchor=W, width=50, minwidth=50)
    tree1.column('Insurance Issue Date', anchor=W, width=50, minwidth=50)
    tree1.column('Insurance Expiry Date', anchor=W, width=50, minwidth=50)
    tree1.column('Date of Entry', anchor=W, width=50, minwidth=50)
    tree1.column('Ref_No', anchor=W, width=50, minwidth=50)
    
    
    # Adding Heading of Columns
    tree1.heading('#0', text='', anchor=W)
    tree1.heading('Sr', text='Sr', anchor=W)
    tree1.heading('Name', text='Name', anchor=W)
    tree1.heading('Model', text='Model', anchor=W)
    tree1.heading('Year', text='Year', anchor=W)
    tree1.heading('Total Cost', text='Total Cost', anchor=W)
    tree1.heading('Insurance Issue Date', text='Insurance Issue Date', anchor=W)
    tree1.heading('Insurance Expiry Date', text='Insurance Expiry Date', anchor=W)
    tree1.heading('Date of Entry', text='Date of Entry', anchor=W)
    tree1.heading('Ref_No', text='Ref_No', anchor=W)
    
    tree1.pack(fill=X, pady=20, expand=YES)

    # Adding Scrollbar
    scrollbar = Scrollbar()
    scrollbar.config(command=tree1.yview)

    iid_number1 = 1
    sr_no1 = 1
    car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")
    for i in range(0, len(car_details_df)):
        total_cost_1 = int(car_details_df.Basic_Cost.to_list()[i]) + car_details_df.Tire_Cost.to_list()[i] + car_details_df.Battery.to_list()[i]+ car_details_df.Denting_Painting_Cost.to_list()[i] + car_details_df.Other_Expenses.to_list()[i]
        tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, car_details_df.Car_Name.to_list()[i], car_details_df.Model.to_list()[i], car_details_df.Year.to_list()[i], total_cost_1, car_details_df.Insurance_issue_date.to_list()[i], car_details_df.Insurance_expiry_date.to_list()[i], car_details_df.Date_of_Entry.to_list()[i], car_details_df.Ref_No.to_list()[i]))
        iid_number1+=1
        sr_no1+=1
    
    f11 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f11.pack(padx=100)

    def search_but_func():
        car_name = car_name_var.get()
        model = model_var.get()

        try:
            if car_name=='Select Car' and model=='Select Model' and year_var.get()=='Select Year':
                iid_number1 = 1
                sr_no1 = 1

                for i in range(0, len(car_details_df)):
                    total_cost_1 = int(car_details_df.Basic_Cost.to_list()[i]) + car_details_df.Tire_Cost.to_list()[i] + car_details_df.Battery.to_list()[i]+ car_details_df.Denting_Painting_Cost.to_list()[i] + car_details_df.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, car_details_df.Car_Name.to_list()[i], car_details_df.Model.to_list()[i], car_details_df.Year.to_list()[i], total_cost_1, car_details_df.Insurance_issue_date.to_list()[i], car_details_df.Insurance_expiry_date.to_list()[i], car_details_df.Date_of_Entry.to_list()[i], car_details_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                # tkinter.messagebox.showerror("Please Select Car/Model/Year", "Please Select Car/Model/Year")

            elif model=='Select Model' and year_var.get()=='Select Year':
                required_car_result = car_details_df[car_details_df.Car_Name == car_name]

                iid_number1 =1
                sr_no1 = 1

                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_car_result)):
                    total_cost_1 = int(required_car_result.Basic_Cost.to_list()[i]) + required_car_result.Tire_Cost.to_list()[i] + required_car_result.Battery.to_list()[i]+ required_car_result.Denting_Painting_Cost.to_list()[i] + required_car_result.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_car_result.Car_Name.to_list()[i], required_car_result.Model.to_list()[i], required_car_result.Year.to_list()[i], total_cost_1, required_car_result.Insurance_issue_date.to_list()[i], required_car_result.Insurance_expiry_date.to_list()[i], required_car_result.Date_of_Entry.to_list()[i], required_car_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                
            elif year_var.get()=='Select Year':

                required_car_result = car_details_df[car_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_model_result)):
                    total_cost_1 = int(required_model_result.Basic_Cost.to_list()[i]) + required_model_result.Tire_Cost.to_list()[i] + required_model_result.Battery.to_list()[i]+ required_model_result.Denting_Painting_Cost.to_list()[i] + required_model_result.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_model_result.Car_Name.to_list()[i], required_model_result.Model.to_list()[i], required_model_result.Year.to_list()[i], total_cost_1, required_model_result.Insurance_issue_date.to_list()[i], required_model_result.Insurance_expiry_date.to_list()[i], required_model_result.Date_of_Entry.to_list()[i], required_model_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
            else:
                year = int(year_var.get())

                required_car_result = car_details_df[car_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]
                search_result_df = required_model_result[required_model_result.Year == year]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(search_result_df)):
                    total_cost_1 = int(search_result_df.Basic_Cost.to_list()[i]) + search_result_df.Tire_Cost.to_list()[i] + search_result_df.Battery.to_list()[i]+ search_result_df.Denting_Painting_Cost.to_list()[i] + search_result_df.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, search_result_df.Car_Name.to_list()[i], search_result_df.Model.to_list()[i], search_result_df.Year.to_list()[i], total_cost_1, search_result_df.Insurance_issue_date.to_list()[i], search_result_df.Insurance_expiry_date.to_list()[i], search_result_df.Date_of_Entry.to_list()[i], search_result_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
        except Exception as error:
            pass


    def view_but_func():
        global selected_ref_no

        try:

            selected = tree1.focus()
            selected_item = tree1.item(selected)

            selected_ref_no = int(selected_item['values'][8])

            show_car_root.destroy()

            view_car_details()

        except Exception as error:
            tkinter.messagebox.showerror("Please Select Car from the Table", "Please Select Car from the Table")

    def back_but_func():
        show_car_root.destroy()
        main_menu_window()

    search_but = Button(f11, text="Search Results", font=('Arial Black', 10), bg='#fc7ced', command=search_but_func).grid(row=1, column=1)
    view_but = Button(f11, text="View Car Details", font=('Arial Black', 10), bg='#8fd149', command=view_but_func).grid(row=1, column=2, padx=50)
    back_but = Button(f11, text="Back", font=('Arial Black', 10), bg='#fcca5d', command=back_but_func).grid(row=1, column=3)
    

    show_car_root.mainloop()


def view_car_details():

    view_car_details_root = Tk()
    view_car_details_root.geometry("1366x695-0+0")
    view_car_details_root.title("Login - Speed Up Billing Software")
    view_car_details_root.configure(bg="#001020")
    view_car_details_root.iconbitmap('speed_up_logo.ico')

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Basic_Cost": [],
            "Tire_Cost": [],
            "Battery": [],
            "Denting_Painting_Cost": [],
            "Other_Expenses": [],
            "Insurance_issue_date": [],
            "Insurance_expiry_date": [],
            "Date_of_Entry": [],
            "Ref_No": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    f0 = Frame(view_car_details_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Car Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)


    f1 = Frame(view_car_details_root, borderwidth=1, bg='#001020')
    f1.pack(pady=40)

    car_name_var = StringVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    car_name_var.set(ref_sort_df.Car_Name.to_list()[0])
    
    car_name_label = Label(f1, text='Car Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    car_name_entry = Label(f1, textvariable=car_name_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=2)

    f2 = Frame(f1, borderwidth=1, bg='#001020')
    f2.grid(row=1, column=3, padx=20)
    
    model_var = StringVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    model_var.set(ref_sort_df.Model.to_list()[0])

    model_label = Label(f2, text='Model: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    model_entry = Label(f2, textvariable=model_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=2)
    
    year_var = StringVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    year_var.set(ref_sort_df.Year.to_list()[0])
    year_label = Label(f1, text='Year: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=5)
    year_entry = Label(f1, textvariable=year_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=6)
    
    basic_cost_var = StringVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    basic_cost_var.set(ref_sort_df.Basic_Cost.to_list()[0])
    basic_cost_label = Label(f1, text='Basic Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    basic_cost_entry = Label(f1, textvariable=basic_cost_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=4, column=2)
    
    tire_var = IntVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    tire_var.set(ref_sort_df.Tire_Cost.to_list()[0])
    tire_label = Label(f1, text='Tire Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    tire_entry = Label(f1, textvariable=tire_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=5, column=2)
    
    battery_var = IntVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    battery_var.set(ref_sort_df.Battery.to_list()[0])
    battery_label = Label(f1, text='Battery Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    battery_entry = Label(f1, textvariable=battery_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=6, column=2)
    
    denting_painting_var = IntVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    denting_painting_var.set(ref_sort_df.Denting_Painting_Cost.to_list()[0])
    denting_painting_label = Label(f1, text='Denting Painting Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    denting_painting_entry = Label(f1, textvariable=denting_painting_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=7, column=2)
    
    other_expenses_var = IntVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    other_expenses_var.set(ref_sort_df.Other_Expenses.to_list()[0])
    other_expenses_label = Label(f1, text='Other Expenses: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=8, column=1)
    other_expenses_entry = Label(f1, textvariable=other_expenses_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=8, column=2)

    total_cost_1 = int(ref_sort_df.Basic_Cost.to_list()[0]) + ref_sort_df.Tire_Cost.to_list()[0] + ref_sort_df.Battery.to_list()[0] + ref_sort_df.Denting_Painting_Cost.to_list()[0] + ref_sort_df.Other_Expenses.to_list()[0]
    total_cost_var = StringVar()
    total_cost_var.set(total_cost_1)
    total_cost_var_label = Label(f1, text='Total Cost: ', bg='#001020', fg='#edcd64', font=('Berlin Sans FB Demi',15)).grid(row=9, column=1)
    total_cost_var_entry = Label(f1, textvariable=total_cost_var, bg='#001020', fg='#ed9664', font=('Berlin Sans FB Demi',15)).grid(row=9, column=2)

    insurance_issue_date_var = IntVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    insurance_issue_date_var.set(ref_sort_df.Insurance_issue_date.to_list()[0])
    insurance_issue_date_label = Label(f1, text='Insurance Issue Date: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=10, column=1)
    insurance_issue_date_entry = Label(f1, textvariable=insurance_issue_date_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=10, column=2)

    insurance_expiry_date_var = IntVar()
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    insurance_expiry_date_var.set(ref_sort_df.Insurance_expiry_date.to_list()[0])
    insurance_expiry_date_label = Label(f1, text='Insurance Expiry Date: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=11, column=1)
    insurance_expiry_date_entry = Label(f1, textvariable=insurance_expiry_date_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=11, column=2)
    
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    issue_date_str = str(ref_sort_df.Insurance_issue_date.to_list()[0])
    day_1 = int(issue_date_str[0:2])
    month_1 = int(issue_date_str[3:5])
    year_1 = int(issue_date_str[6:10])
    date_1 = date(year_1, month_1, day_1)

    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    expiry_date_str = str(ref_sort_df.Insurance_expiry_date.to_list()[0])
    day_2 = int(expiry_date_str[0:2])
    month_2 = int(expiry_date_str[3:5])
    year_2 = int(expiry_date_str[6:10])
    date_2 = date(year_2, month_2, day_2)

    today = date.today()
    date_today = today.strftime("%d/%m/%Y")
    day_3 = int(date_today[0:2])
    month_3 = int(date_today[3:5])
    year_3 = int(date_today[6:10])
    date_3 = date(year_3, month_3, day_3)


    days_left = (date_2 - date_3 ).days

    days_left_var = StringVar()

    if days_left>0:
        days_left_var.set(f"{days_left} Day(s) Left")
    else:
        days_left_var.set(f" Expired {str(days_left)[1::]} Day(s) Ago")

    days_left_label = Label(f1, text='Insurance License: ', bg='#001020', fg='#edcd64', font=('Berlin Sans FB Demi',15)).grid(row=12, column=1)
    days_left_entry = Label(f1, textvariable=days_left_var, bg='#001020', fg='#ed9664', font=('Berlin Sans FB Demi',15)).grid(row=12, column=2)

    def back_but_func():
        view_car_details_root.destroy()
        show_car_details()

    def delete_car():
        ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Delete Car Record/Details ??")
        if ans==True:
            view_car_details_root.destroy()
            delete_car_details_login()
        else:
            pass
    
    def back_but_func():
        view_car_details_root.destroy()
        show_car_details()
    
    def edit_car_details_func():
        ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Edit Car Record/Details ??")
        if ans==True:
            view_car_details_root.destroy()
            edit_car_details_window()
        else:
            pass
    
    f4 = Frame(view_car_details_root, borderwidth=1, bg='#001020')
    f4.pack(pady=20)

    delete_but = Button(f4, text="Delete Car", font=('Arial Black', 13), bg='#fa968e', command=delete_car).grid(row=1, column=1)
    edit_car_but = Button(f4, text="Edit Car Details", font=('Arial Black', 13), bg='#8efacd', command=edit_car_details_func).grid(row=1, column=2, padx=50)
    back_but = Button(f4, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).grid(row=1, column=3)

    view_car_details_root.mainloop()


def delete_car_details_login():

    def authentication():
        if username_var.get()==user_id and password_var.get()==password:
            ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Delete Car Record/Details ??")
            if ans==True:
                # Deletion Code Here
                car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

                index_names = car_details_df[car_details_df['Ref_No'] == int(selected_ref_no)].index
                
                car_details_df.drop(index_names, inplace = True)
                car_details_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

                tkinter.messagebox.showinfo("Car Details Deleted Successfully", "Car Details Deleted Successfully ...")

                login_root.destroy()
                show_car_details()
            else:
                tkinter.messagebox.showinfo("Car Details Not Deleted", "Car Details Not Deleted !!!!!!")
                login_root.destroy()
                show_car_details()
        else:
            tkinter.messagebox.showerror("Authentication Unsuccessful", "Incorrect User ID or Password")

    def authentication_bind(event):
        authentication()

    def back_but_func():
        login_root.destroy()
        show_car_details()

    login_root = Tk()
    login_root.geometry("1366x695-0+0")
    login_root.title("Login - Speed Up Billing Software")
    login_root.configure(bg="#315b82")
    login_root.iconbitmap('speed_up_logo.ico')

    # Adding Create Account Image
    f1 = Frame(login_root, borderwidth=1, bg="#315b82")
    f1.pack(pady=50)

    login_photo = PhotoImage(file='login_logo.png')
    login_image = Label(f1, image=login_photo, bg="#315b82").pack(pady=10)
    login_text = Label(f1, text="Login to Delete Car Details", font=('Arial Black', 25), bg="#315b82", fg="#ebde4d").pack(padx=50)

    f2 = Frame(login_root, borderwidth=1, bg="#315b82")
    f2.pack(pady=20)

    username_var = StringVar()
    password_var = StringVar()

    user_label = Label(f2, text="User ID : ", font=('Arial Black', 20), bg="#315b82", fg="white").grid(row=1, column=1, padx=10)
    pass_label = Label(f2, text="Password : ", font=('Arial Black', 20), bg="#315b82", fg="white").grid(row=2, column=1)


    user_entry = Entry(f2, textvariable=username_var, font=('comicsansms', 15))
    user_entry.grid(row=1, column=2)
    pass_entry = Entry(f2, textvariable=password_var, font=('comicsansms', 15), show="*").grid(row=2, column=2)

    user_entry.focus()
    
    case_sensitive_label = Label(f2, text="  (Case Sensitive)", font=('Arial', 13), bg="#315b82", fg="yellow").grid(row=1, column=3)
    case_sensitive_label = Label(f2, text="  (Case Sensitive)", font=('Arial', 13), bg="#315b82", fg="yellow").grid(row=2, column=3)

    f3 = Frame(login_root, borderwidth=1, bg="#315b82")
    f3.pack(pady=40)

    login_but = Button(f3, text="Login", font=('Arial Black', 15), bg='#9df760', command=authentication)
    login_but.pack(pady=20)

    back_but = Button(f3, text="Back", font=('Arial Black', 15), bg='#fae88e', command=back_but_func)
    back_but.pack(pady=20)

    # Binding Enter Key
    login_root.bind('<Return>',authentication_bind)

    login_root.mainloop()


def edit_car_details_window():
    global selected_issue_date, selected_expiry_date

    def insurance_issue_func():
        selected_issue_date = insurance_calendar.get_date()
        insurance_issue_var.set(selected_issue_date)
    
    def insurance_expiry_func():
        selected_expiry_date = insurance_calendar.get_date()
        insurance_expiry_var.set(selected_expiry_date)
    
    def edit_car_func():

        # Appending Car Details to Csv
        car_name =  car_name_var.get()
        model = model_var.get()
        year = year_var.get()
        basic_cost =  basic_cost_var.get()
        tire =  tire_var.get()
        battery = battery_var.get()
        denting_painting = denting_painting_var.get()
        other_expenses = other_expenses_var.get()
        insurance_issue_date = insurance_issue_var.get()
        insurance_expiry_date = insurance_expiry_var.get()

        today = date.today()
        date_of_entry = today.strftime("%d/%m/%Y")

        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Car_Name'] = car_name
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Model'] = model
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Year'] = year
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Basic_Cost'] = basic_cost
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Tire_Cost'] = tire
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Battery'] = battery
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Denting_Painting_Cost'] = denting_painting
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Other_Expenses'] = other_expenses
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Insurance_issue_date'] = insurance_issue_date
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Insurance_expiry_date'] = insurance_expiry_date
        car_details_df.loc[car_details_df['Ref_No'] == int(selected_ref_no), 'Date_of_Entry'] = date_of_entry
        
        car_details_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        tkinter.messagebox.showinfo("Car Details Edited Successfully", "Car Details Edited Successfully")
        edit_car_root.destroy()
        show_car_details()

    def back_but_func():
        edit_car_root.destroy()
        show_car_details()

    edit_car_root = Tk()
    edit_car_root.geometry("1366x695-0+0")
    edit_car_root.title("Login - Speed Up Billing Software")
    edit_car_root.configure(bg="#001020")
    edit_car_root.iconbitmap('speed_up_logo.ico')

    f0 = Frame(edit_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Edit Car Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")
    ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
    
    f1 = Frame(edit_car_root, borderwidth=1, bg='#001020')
    f1.pack(pady=40)

    car_name_var = StringVar()
    car_name_var.set(ref_sort_df.Car_Name.to_list()[0])
    car_name_label = Label(f1, text='Car Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    car_name_entry = Entry(f1, textvariable=car_name_var, font=('comicsansms', 15))
    car_name_entry.grid(row=1, column=2)

    f2 = Frame(f1, borderwidth=1, bg='#001020')
    f2.grid(row=1, column=3, padx=20)
    
    model_var = StringVar()
    model_var.set(ref_sort_df.Model.to_list()[0])
    model_label = Label(f2, text='Model: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    model_entry = Entry(f2, textvariable=model_var, font=('comicsansms', 15))
    model_entry.grid(row=1, column=2)
    
    year_var = StringVar()
    year_var.set(ref_sort_df.Year.to_list()[0])
    year_label = Label(f1, text='Year: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=5)
    year_entry = Entry(f1, textvariable=year_var, font=('comicsansms', 15))
    year_entry.grid(row=1, column=6)
    
    basic_cost_var = StringVar()
    basic_cost_var.set(ref_sort_df.Basic_Cost.to_list()[0])
    basic_cost_label = Label(f1, text='Basic Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    basic_cost_entry = Entry(f1, textvariable=basic_cost_var, font=('comicsansms', 15))
    basic_cost_entry.grid(row=4, column=2)
    
    tire_var = IntVar()
    tire_var.set(ref_sort_df.Tire_Cost.to_list()[0])
    tire_label = Label(f1, text='Tire Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    tire_entry = Entry(f1, textvariable=tire_var, font=('comicsansms', 15))
    tire_entry.grid(row=5, column=2)
    
    battery_var = IntVar()
    battery_var.set(ref_sort_df.Battery.to_list()[0])
    battery_label = Label(f1, text='Battery Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    battery_entry = Entry(f1, textvariable=battery_var, font=('comicsansms', 15))
    battery_entry.grid(row=6, column=2)
    
    denting_painting_var = IntVar()
    denting_painting_var.set(ref_sort_df.Denting_Painting_Cost.to_list()[0])
    denting_painting_label = Label(f1, text='Denting Painting Cost: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    denting_painting_entry = Entry(f1, textvariable=denting_painting_var, font=('comicsansms', 15))
    denting_painting_entry.grid(row=7, column=2)
    
    other_expenses_var = IntVar()
    other_expenses_var.set(ref_sort_df.Other_Expenses.to_list()[0])
    other_expenses_label = Label(f1, text='Other Expenses: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=8, column=1)
    other_expenses_entry = Entry(f1, textvariable=other_expenses_var, font=('comicsansms', 15))
    other_expenses_entry.grid(row=8, column=2)

    f3 = Frame(edit_car_root, borderwidth=1, bg='#001020')
    f3.pack()

    # Add Calendar
    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    insurance_calendar = Calendar(f3, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    insurance_calendar.grid(row=1, column=1)
    
    f5 = Frame(f3, borderwidth=1, bg='#001020')
    f5.grid(row=1, column=2, padx=10)

    insurance_issue_var = StringVar()
    insurance_issue_var.set(ref_sort_df.Insurance_issue_date.to_list()[0])
    insurance_expiry_var = StringVar()
    insurance_expiry_var.set(ref_sort_df.Insurance_expiry_date.to_list()[0])
    
    insurance_issue_but = Button(f5, text="Insurance Issue", font=('Arial Black', 10), bg='#fcca5d', command=insurance_issue_func).grid(row=1, column=1, pady=10)
    insurance_expiry_but = Button(f5, text="Insurance Expiry", font=('Arial Black', 10), bg='#fcca5d', command=insurance_expiry_func).grid(row=2, column=1, pady=10)
    
    insurance_issue_label = Label(f5, textvariable=insurance_issue_var, bg='#001020', fg='white', font=('Arial Black',10)).grid(row=1, column=2)
    insurance_expiry_label = Label(f5, textvariable=insurance_expiry_var, bg='#001020', fg='white', font=('Arial Black',10)).grid(row=2, column=2)
    
    f4 = Frame(edit_car_root, borderwidth=1, bg='#001020')
    f4.pack(pady=20)

    edit_but = Button(f4, text="Edit & Save", font=('Arial Black', 13), bg='#5eff8c', command=edit_car_func).grid(row=1, column=1, padx=30)
    back_but = Button(f4, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).grid(row=1, column=2)
    
    car_name_entry.focus()

    edit_car_root.mainloop()


def add_client_details():
    global selected_issue_date, selected_expiry_date


    def date_of_inquiry_func():
        selected_date_of_inquiry = date_of_inquiry_calendar.get_date()
        date_of_inquiry_var.set(selected_date_of_inquiry)

    def add_car_func():


        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

        # Appending Car Details to Csv
        car_name =  car_name_var.get()
        model = model_var.get()
        year = year_var.get()
        client_name = client_name_var.get()
        address = address_var.get()
        mobile_no = mobile_no_var.get()
        email = email_var.get()
        date_of_inquiry = date_of_inquiry_var.get()

        today = date.today()
        date_of_entry = today.strftime("%d/%m/%Y")

        client_details_df_len = len(client_details_df)
        try:
            pre_ref_no = int(client_details_df.Ref_No.to_list()[client_details_df_len-1])
        except Exception as Error:
            pre_ref_no = 0

        # print("Pre Ref No: ", pre_ref_no)

        if car_name!='Select Car' and model!='Select Model' and year!='Select Year' and date_of_inquiry!="" and client_name!="" and address!="" and mobile_no!="" and email!="":
            # Checking All Entry Values are Filled
            if car_name=="" or model=="" or year=="":
                tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")
            else:

                shutil.copy(aadhar_card_filename_path, filepath_1)
                shutil.copy(pan_card_filename_path, filepath_2)

                split_tup_1 = os.path.splitext(aadhar_card_filename_path)
                aadhar_file_ext = split_tup_1[1]
                aadhar_dst_file = os.path.join(filepath_1, aadhar_card_filename)
                aadhar_new_dst_file_name = os.path.join(filepath_1, f'ref_{pre_ref_no+1}{aadhar_file_ext}')
                os.rename(aadhar_dst_file, aadhar_new_dst_file_name)

                split_tup_2 = os.path.splitext(pan_card_filename_path)
                pan_file_ext = split_tup_2[1]
                pan_dst_file = os.path.join(filepath_2, pan_card_filename)
                pan_new_dst_file_name = os.path.join(filepath_2, f'ref_{pre_ref_no+1}{pan_file_ext}')
                os.rename(pan_dst_file, pan_new_dst_file_name)

                aadhar_card_filename_1 = os.path.split(aadhar_new_dst_file_name)[1]
                pan_card_filename_1 = os.path.split(pan_new_dst_file_name)[1]
                dict3 = {
                    "Car_Name": [car_name],
                    "Model": [model],
                    "Year": [year],
                    "Client_Name":[client_name],
                    "Address":[address],
                    "Mobile_No":[mobile_no],
                    "Email":[email],
                    "Date_of_Inquiry":[date_of_inquiry],
                    "Ref_No":[pre_ref_no + 1],
                    "Aadhar_Card":[aadhar_new_dst_file_name],
                    "Pan_Card":[pan_new_dst_file_name],
                    "Aadhar_File_Name":[aadhar_card_filename_1],
                    "Pan_File_Name":[pan_card_filename_1]
                    }
                add_client_details_df = pd.DataFrame(dict3)

                df2 = pd.concat([client_details_df, add_client_details_df], ignore_index=True)
                df2.to_csv("D:\Soham_Motors\Software_Files\client_details_file.csv")
                
                

                print(aadhar_new_dst_file_name)
                print(pan_new_dst_file_name)
                


                if int(clear_entry_content_var_1.get())==1:
                    client_name_entry.delete(0, END)
                    address_entry.delete(0, END)
                    mobile_no_entry.delete(0, END)
                    email_entry.delete(0, END)
                    date_of_inquiry_var.set("")
                else:
                    pass
                
                tkinter.messagebox.showinfo("Car Details Added Successfully", "Car Details Added Successfully")
        else:
            tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")

    def back_but_func():
        add_car_root.destroy()
        main_menu_window()


    add_car_root = Tk()
    add_car_root.geometry("1366x695-0+0")
    add_car_root.title("Login - Speed Up Billing Software")
    add_car_root.configure(bg="#001020")
    add_car_root.iconbitmap('speed_up_logo.ico')

    # Loading Client Details Df
    try:
        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Client_Name":[],
            "Address":[],
            "Mobile_No":[],
            "Email":[],
            "Date_of_Inquiry":[],
            "Ref_No":[],
            "Aadhar_Card":[],
            "Pan_Card":[],
            "Aadhar_File_Name":[],
            "Pan_File_Name":[]
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\client_details_file.csv")

        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    f0 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Add Client Inquiry', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    f1 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f1.pack(pady=40)

    def car_box_update(event):
        global model_list, car2_selected

        car_selected = event.widget.get()
        car2_selected = car_selected
        if car_selected!="Select Car":
            model_list = car_details_df[car_details_df.Car_Name==car_selected].drop_duplicates(subset = ["Model"]).Model.to_list()
            model_list.insert(0, "Select Model")
            model_box['values'] = model_list
    
    def model_box_update(event):
        global year_list

        model_selected = event.widget.get()
        if model_selected!="Select Model":
            year_list = car_details_df[car_details_df.Car_Name==car2_selected][car_details_df.Model==model_selected].drop_duplicates(subset = ["Year"]).Year.to_list()
            year_list.insert(0, "Select Year")
            year_box['values'] = year_list


    # Adding Search Options -------- Starts Here

    # ------ Car Name Combobox --------------
    f10 = Frame(f1, borderwidth=1, bg="#001020")
    f10.pack(fill=BOTH, padx=100)

    f3 = Frame(f10, borderwidth=1, bg="#001020")
    f3.grid(row=1, column=1)

    car_name_label = Label(f3, text='Car Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)

    car_name_list = car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()
    car_name_list.insert(0, "Select Car")

    car_name_var = StringVar()
    car_name_var.set(car_name_list[0])

    car_box = ttk.Combobox(f3, width=20, textvariable=car_name_var)
    car_box['values'] = car_name_list
    car_box.grid(row=1, column=2)
    car_box.current(0)
    car_box.bind("<<ComboboxSelected>>", car_box_update)

    # ------ Model Combobox ----------------
    f4 = Frame(f3, borderwidth=1, bg="#001020")
    f4.grid(row=1, column=3, padx=20)

    model_label = Label(f4, text='Model: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)

    model_list = []
    model_list.insert(0, "Select Model")

    model_var = StringVar()
    model_var.set(model_list[0])

    model_box = ttk.Combobox(f4, width=20, textvariable=model_var)
    model_box['values'] = model_list
    model_box.grid(row=1, column=2)
    model_box.current(0)
    model_box.bind("<<ComboboxSelected>>", model_box_update)


    # ------ Year Combobox ----------------
    f5 = Frame(f3, borderwidth=1, bg="#001020")
    f5.grid(row=1, column=4)

    year_label = Label(f5, text='Year: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)

    year_list = []
    year_list.insert(0, "Select Year")

    year_var = StringVar()
    year_var.set(year_list[0])

    year_box = ttk.Combobox(f5, width=20, textvariable=year_var)
    year_box['values'] = year_list
    year_box.grid(row=1, column=2)
    year_box.current(0)

    f2 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f2.pack()

    client_name_var = StringVar()
    client_name_label = Label(f2, text='Client Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    client_name_entry = Entry(f2, textvariable=client_name_var, font=('comicsansms', 15))
    client_name_entry.grid(row=4, column=2)
    
    address_var = StringVar()
    address_label = Label(f2, text='Address: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    address_entry = Entry(f2, textvariable=address_var, font=('comicsansms', 15))
    address_entry.grid(row=5, column=2)
    
    mobile_no_var = StringVar()
    mobile_no_label = Label(f2, text='Mobile No: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    mobile_no_entry = Entry(f2, textvariable=mobile_no_var, font=('comicsansms', 15))
    mobile_no_entry.grid(row=6, column=2)
    
    email_var = StringVar()
    email_label = Label(f2, text='Email: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    email_entry = Entry(f2, textvariable=email_var, font=('comicsansms', 15))
    email_entry.grid(row=7, column=2)
    
    clear_entry_content_var_1 = StringVar()
    clear_entry_content_button = Checkbutton(f2, text = "Clear Entry Content", bg='#f7ea36', font=('Comicsansms', 10, 'bold') , variable = clear_entry_content_var_1, onvalue = 1, offvalue = 0, height = 2, width = 20)
    clear_entry_content_button.select()
    clear_entry_content_button.grid(row=7, column=3, padx=30)

    def upload_aadhar_card():
        global aadhar_card_filename, pan_card_filename, filepath_1, aadhar_card_filename_path

        filepath_1 = "D:\Soham_Motors\Aadhar_Card"
        aadhar_card_filename_path = filedialog.askopenfilename()
        aadhar_card_filename = os.path.split(aadhar_card_filename_path)[1]
        aadhar_card_path.set(aadhar_card_filename)
    
    def upload_pan_card():
        global aadhar_card_filename, pan_card_filename, filepath_2, pan_card_filename_path

        filepath = "D:\Soham_Motors\Pan_Card"
        pan_card_filename_path = filedialog.askopenfilename()
        pan_card_filename = os.path.split(pan_card_filename_path)[1]
        pan_card_path.set(pan_card_filename)
    
    
    filepath_1 = "D:\Soham_Motors\Aadhar_Card"
    filepath_2 = "D:\Soham_Motors\Pan_Card"

    aadhar_card_path = StringVar()
    pan_card_path = StringVar()

    upload_aadhar_card_but = Button(f2, text="Upload Aadhar Card", font=('Arial Black', 10), bg='#fcca5d', command=upload_aadhar_card).grid(row=8, column=1, pady=10)
    upload_Pan_card_but = Button(f2, text="Upload Pan Card", font=('Arial Black', 10), bg='#fcca5d', command=upload_pan_card).grid(row=8, column=2, pady=10)
    


    f3 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f3.pack()

    # Add Calendar
    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    date_of_inquiry_calendar = Calendar(f3, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    date_of_inquiry_calendar.grid(row=1, column=1)
    
    f5 = Frame(f3, borderwidth=1, bg='#001020')
    f5.grid(row=1, column=2, padx=10)

    date_of_inquiry_var = StringVar()
    
    date_of_inquiry_but = Button(f5, text="Date of Inquiry", font=('Arial Black', 10), bg='#fcca5d', command=date_of_inquiry_func).grid(row=1, column=1, pady=10)
    
    date_of_inquiry_label = Label(f5, textvariable=date_of_inquiry_var, bg='#001020', fg='white', font=('Arial Black',10)).grid(row=1, column=2)
    


    f4 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f4.pack(pady=20)

    add_but = Button(f4, text="Add", font=('Arial Black', 13), bg='#5eff8c', command=add_car_func).grid(row=1, column=1, padx=30)
    back_but = Button(f4, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).grid(row=1, column=2)
    
    add_car_root.mainloop()


def show_client_details():

    show_client_root = Tk()
    show_client_root.geometry("1366x695-0+0")
    show_client_root.title("Login - Speed Up Billing Software")
    show_client_root.configure(bg="#001020")
    show_client_root.iconbitmap('speed_up_logo.ico')

    # Loading Car Details Df
    try:
        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Client_Name":[],
            "Address":[],
            "Mobile_No":[],
            "Email":[],
            "Date_of_Inquiry":[],
            "Ref_No":[],
            "Aadhar_Card":[],
            "Pan_Card":[],
            "Aadhar_File_Name":[],
            "Pan_File_Name":[]
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\client_details_file.csv")

        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")


    f0 = Frame(show_client_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Show Client Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    # Adding Filter Search Title
    f2 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f2.pack(fill=BOTH, padx=100, pady=0)

    title1_label = Label(f2, text='Filter Search:', bg='#001020', fg='#f0b754', font=('Berlin Sans FB Demi',20)).grid(row=1, column=1, padx=0, pady=20)
    title2_label = Label(f2, text='', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',10)).grid(row=1, column=2)
    

    def car_box_update(event):
        global model_list, car1_selected

        car_selected = event.widget.get()
        car1_selected = car_selected
        if car_selected!="Select Car":

            # car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()

            model_list = client_details_df[client_details_df.Car_Name==car_selected].drop_duplicates(subset = ["Model"]).Model.to_list()
            model_list.insert(0, "Select Model")
            model_box['values'] = model_list
    
    def model_box_update(event):
        global year_list, model1_selected

        model_selected = event.widget.get()
        model1_selected = model_selected
        if model_selected!="Select Model":
            year_list = client_details_df[client_details_df.Car_Name==car1_selected][client_details_df.Model==model1_selected].drop_duplicates(subset = ["Year"]).Year.to_list()
            year_list.insert(0, "Select Year")
            year_box['values'] = year_list

    def year_box_update(event):
        global client_name_list

        year_selected = event.widget.get()
        if year_selected!="Select Model":
            required_client_name_df = client_details_df[client_details_df.Car_Name==car1_selected][client_details_df.Model==model1_selected]
            client_name_list = required_client_name_df[client_details_df.Year==int(year_selected)].drop_duplicates(subset = ["Client_Name"]).Client_Name.to_list()

            client_name_list.insert(0, "Select Client")
            client_box['values'] = client_name_list


    # Adding Search Options -------- Starts Here

    # ------ Car Name Combobox --------------
    f10 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f10.pack(fill=BOTH, padx=100)

    f3 = Frame(f10, borderwidth=1, bg="#001020")
    f3.grid(row=1, column=1)

    car_name_label = Label(f3, text='Car Name: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    car_name_list = client_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()
    car_name_list.insert(0, "Select Car")

    car_name_var = StringVar()
    car_name_var.set(car_name_list[0])

    car_box = ttk.Combobox(f3, width=20, textvariable=car_name_var)
    car_box['values'] = car_name_list
    car_box.grid(row=1, column=2)
    car_box.current(0)
    car_box.bind("<<ComboboxSelected>>", car_box_update)

    # ------ Model Combobox ----------------
    f4 = Frame(f3, borderwidth=1, bg="#001020")
    f4.grid(row=1, column=3, padx=20)

    model_label = Label(f4, text='Model: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    model_list = []
    model_list.insert(0, "Select Model")

    model_var = StringVar()
    model_var.set(model_list[0])

    model_box = ttk.Combobox(f4, width=20, textvariable=model_var)
    model_box['values'] = model_list
    model_box.grid(row=1, column=2)
    model_box.current(0)
    model_box.bind("<<ComboboxSelected>>", model_box_update)


    # ------ Year Combobox ----------------
    f5 = Frame(f3, borderwidth=1, bg="#001020")
    f5.grid(row=1, column=4)

    year_label = Label(f5, text='Year: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    year_list = []
    year_list.insert(0, "Select Year")

    year_var = StringVar()
    year_var.set(year_list[0])

    year_box = ttk.Combobox(f5, width=20, textvariable=year_var)
    year_box['values'] = year_list
    year_box.grid(row=1, column=2)
    year_box.current(0)
    year_box.bind("<<ComboboxSelected>>", year_box_update)

    # ------ Car Name Combobox --------------
    f12 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f12.pack(fill=BOTH, padx=100)

    f13 = Frame(f12, borderwidth=1, bg="#001020")
    f13.grid(row=2, column=1)

    client_name_label = Label(f13, text='Client Name: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=2, column=1)

    client_name_list = []
    client_name_list.insert(0, "Select Client")

    client_name_var = StringVar()
    client_name_var.set(client_name_list[0])

    client_box = ttk.Combobox(f13, width=20, textvariable=client_name_var)
    client_box['values'] = client_name_list
    client_box.grid(row=2, column=2)
    client_box.current(0) 


    def date_of_entry_func():
        selected_entry_date = date_of_entry_calendar.get_date()
        date_of_inquiry_var.set(selected_entry_date)

        required_car_result = client_details_df[client_details_df.Date_of_Inquiry == date_of_inquiry_var.get()]

        iid_number1 =1
        sr_no1 = 1

        for i in tree1.get_children():
            tree1.delete(i)
        for i in range(0, len(required_car_result)):
            tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_car_result.Client_Name.to_list()[i], required_car_result.Car_Name.to_list()[i], required_car_result.Model.to_list()[i], required_car_result.Year.to_list()[i], required_car_result.Date_of_Inquiry.to_list()[i], required_car_result.Ref_No.to_list()[i]))
            iid_number1+=1
            sr_no1+=1        


    f6 = Frame(show_client_root, borderwidth=1, bg='#001020')
    f6.place(x=820, y=100)

    # Add Calendar
    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    date_of_entry_calendar = Calendar(f6, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    date_of_entry_calendar.grid(row=1, column=1)

    date_of_inquiry_var = StringVar()

    date_of_entry_but = Button(show_client_root, text="Date of Inquiry", font=('Arial Black', 10), bg='#fcca5d', command=date_of_entry_func).place(x=1110, y=140)
    date_of_entry_label = Label(show_client_root, textvariable=date_of_inquiry_var, bg='#001020', fg='white', font=('Arial Black',10)).place(x=1120, y=180)


    # Adding Search Options -------- Ends Here

    f1 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f1.pack(fill=BOTH, padx=100, pady=50)

    # ------------Treeview for Displaying Cart Items and its Details---------------------

    tree1 = ttk.Treeview(f1, selectmode="extended", height=10)
    # Column names of Treeview
    tree1['columns'] = ('Sr', "Name", 'Car', 'Model', 'Year', 'Date of Inquiry', 'Ref No')

    # Adding Columns
    tree1.column('#0', width=0, stretch=NO)
    tree1.column('Sr', anchor=W, width=30, minwidth=0, stretch=NO)
    tree1.column('Name', anchor=W, width=50, minwidth=50)
    tree1.column('Car', anchor=W, width=50, minwidth=50)
    tree1.column('Model', anchor=W, width=50, minwidth=50)
    tree1.column('Year', anchor=W, width=50, minwidth=50)
    tree1.column('Date of Inquiry', anchor=W, width=50, minwidth=50)
    tree1.column('Ref No', anchor=W, width=50, minwidth=50)
    

    # Adding Heading of Columns
    tree1.heading('#0', text='', anchor=W)
    tree1.heading('Sr', text='Sr', anchor=W)
    tree1.heading('Name', text='Name', anchor=W)
    tree1.heading('Car', text='Car', anchor=W)
    tree1.heading('Model', text='Model', anchor=W)
    tree1.heading('Year', text='Year', anchor=W)
    tree1.heading('Date of Inquiry', text='Date of Inquiry', anchor=W)
    tree1.heading('Ref No', text='Ref No', anchor=W)
    
    tree1.pack(fill=X, pady=20, expand=YES)

    # Adding Scrollbar
    scrollbar = Scrollbar()
    scrollbar.config(command=tree1.yview)

    iid_number1 = 1
    sr_no1 = 1
    client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")
    for i in range(0, len(client_details_df)):
        tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, client_details_df.Client_Name.to_list()[i], client_details_df.Car_Name.to_list()[i], client_details_df.Model.to_list()[i], client_details_df.Year.to_list()[i], client_details_df.Date_of_Inquiry.to_list()[i], client_details_df.Ref_No.to_list()[i]))
        iid_number1+=1
        sr_no1+=1
    
    f11 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f11.pack(padx=100)

    def search_but_func():
        car_name = car_name_var.get()
        model = model_var.get()

        try:
            if car_name=='Select Car' and model=='Select Model' and year_var.get()=='Select Year' and client_name_var.get()=='Select Client':
                iid_number1 = 1
                sr_no1 = 1

                for i in range(0, len(client_details_df)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, client_details_df.Client_Name.to_list()[i], client_details_df.Car_Name.to_list()[i], client_details_df.Model.to_list()[i], client_details_df.Year.to_list()[i], client_details_df.Date_of_Inquiry.to_list()[i], client_details_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                # tkinter.messagebox.showerror("Please Select Car/Model/Year", "Please Select Car/Model/Year")

            elif model=='Select Model' and year_var.get()=='Select Year' and client_name_var.get()=='Select Client':
                required_client_result = client_details_df[client_details_df.Car_Name == car_name]

                iid_number1 =1
                sr_no1 = 1

                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_client_result)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_client_result.Client_Name.to_list()[i], required_client_result.Car_Name.to_list()[i], required_client_result.Model.to_list()[i], required_client_result.Year.to_list()[i], required_client_result.Date_of_Inquiry.to_list()[i], required_client_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                
            elif year_var.get()=='Select Year' and client_name_var.get()=='Select Client':

                required_car_result = client_details_df[client_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_model_result)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_model_result.Client_Name.to_list()[i], required_model_result.Car_Name.to_list()[i], required_model_result.Model.to_list()[i], required_model_result.Year.to_list()[i], required_model_result.Date_of_Inquiry.to_list()[i], required_model_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1

            elif client_name_var.get()=='Select Client':

                year = int(year_var.get())

                required_car_result = client_details_df[client_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]
                search_result_df = required_model_result[required_model_result.Year == year]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(search_result_df)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, search_result_df.Client_Name.to_list()[i], search_result_df.Car_Name.to_list()[i], search_result_df.Model.to_list()[i], search_result_df.Year.to_list()[i], search_result_df.Date_of_Inquiry.to_list()[i], search_result_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1

            else:
                year = int(year_var.get())

                required_car_result = client_details_df[client_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]
                required_year_result = required_model_result[required_model_result.Year == year]
                search_result_df = required_year_result[required_year_result.Client_Name == client_name_var.get()]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(search_result_df)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, search_result_df.Client_Name.to_list()[i], search_result_df.Car_Name.to_list()[i], search_result_df.Model.to_list()[i], search_result_df.Year.to_list()[i], search_result_df.Date_of_Inquiry.to_list()[i], search_result_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                
        except Exception as error:
            pass


    def view_but_func():
        global selected_ref_no

        try:

            selected = tree1.focus()
            selected_item = tree1.item(selected)

            selected_ref_no = int(selected_item['values'][6])

            show_client_root.destroy()

            view_client_details()

        except Exception as error:
            # print(selected_item['values'])
            # print(error)
            tkinter.messagebox.showerror("Please Select Car from the Table", "Please Select Car from the Table")

    def back_but_func():
        show_client_root.destroy()
        main_menu_window()

    search_but = Button(f11, text="Search Results", font=('Arial Black', 10), bg='#fc7ced', command=search_but_func).grid(row=1, column=1)
    view_but = Button(f11, text="View Client Details", font=('Arial Black', 10), bg='#8fd149', command=view_but_func).grid(row=1, column=2, padx=50)
    back_but = Button(f11, text="Back", font=('Arial Black', 10), bg='#fcca5d', command=back_but_func).grid(row=1, column=3)
    

    show_client_root.mainloop()


def view_client_details():

    view_client_details_root = Tk()
    view_client_details_root.geometry("1366x695-0+0")
    view_client_details_root.title("Login - Speed Up Billing Software")
    view_client_details_root.configure(bg="#001020")
    view_client_details_root.iconbitmap('speed_up_logo.ico')

    # Loading Car Details Df
    try:
        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Client_Name":[],
            "Address":[],
            "Mobile_No":[],
            "Email":[],
            "Date_of_Inquiry":[],
            "Ref_No":[],
            "Aadhar_Card":[],
            "Pan_Card":[],
            "Aadhar_File_Name":[],
            "Pan_File_Name":[]
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\client_details_file.csv")

        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")


    f0 = Frame(view_client_details_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Client Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)


    f1 = Frame(view_client_details_root, borderwidth=1, bg='#001020')
    f1.pack(pady=40)

    car_name_var = StringVar()
    ref_sort_df = client_details_df[client_details_df.Ref_No == selected_ref_no]
    car_name_var.set(ref_sort_df.Car_Name.to_list()[0])
    
    car_name_label = Label(f1, text='Car Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    car_name_entry = Label(f1, textvariable=car_name_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=2)

    f2 = Frame(f1, borderwidth=1, bg='#001020')
    f2.grid(row=1, column=3, padx=20)
    
    model_var = StringVar()
    model_var.set(ref_sort_df.Model.to_list()[0])

    model_label = Label(f2, text='Model: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    model_entry = Label(f2, textvariable=model_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=2)
    
    year_var = StringVar()
    year_var.set(ref_sort_df.Year.to_list()[0])
    year_label = Label(f1, text='Year: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=5)
    year_entry = Label(f1, textvariable=year_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=6)
    
    client_name_var = StringVar()
    client_name_var.set(ref_sort_df.Client_Name.to_list()[0])
    client_name_label = Label(f1, text='Client Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    client_name_entry = Label(f1, textvariable=client_name_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=4, column=2)
    
    address_var = StringVar()
    address_var.set(ref_sort_df.Address.to_list()[0])
    address_label = Label(f1, text='Address: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    address_entry = Label(f1, textvariable=address_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=5, column=2)
    
    mobile_no_var = StringVar()
    mobile_no_var.set(ref_sort_df.Mobile_No.to_list()[0])
    mobile_no_label = Label(f1, text='Mobile No: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    mobile_no_entry = Label(f1, textvariable=mobile_no_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=6, column=2)
    
    email_var = StringVar()
    email_var.set(ref_sort_df.Email.to_list()[0])
    email_label = Label(f1, text='Email: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    email_entry = Label(f1, textvariable=email_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=7, column=2)
    
    def view_aadhar_card():
        aadhar_card_view_path = ref_sort_df.Aadhar_Card.to_list()[0]
        print(ref_sort_df.Aadhar_Card.to_list())
        startfile(aadhar_card_view_path)

    def view_pan_card():
        pan_card_view_path = ref_sort_df.Pan_Card.to_list()[0]
        startfile(pan_card_view_path)
    

    f5 = Frame(view_client_details_root, borderwidth=1, bg='#001020')
    f5.pack(pady=20)

    aadhar_card_but = Button(f5, text="View Aadhar Card", font=('Arial Black', 12), bg='#ff82ae', command=view_aadhar_card).grid(row=1, column=1)
    pan_card_but = Button(f5, text="View Pan Card", font=('Arial Black', 12), bg='#f982ff', command=view_pan_card).grid(row=1, column=2, padx=50)
    
    def back_but_func():
        view_client_details_root.destroy()
        show_client_details()

    def delete_car():
        ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Delete Client Record/Details ??")
        if ans==True:
            view_client_details_root.destroy()
            delete_client_details_login()
        else:
            pass

    def edit_car_details_func():
        ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Edit Client Record/Details ??")
        if ans==True:
            view_client_details_root.destroy()
            edit_client_details_window()
        else:
            pass

    f4 = Frame(view_client_details_root, borderwidth=1, bg='#001020')
    f4.pack(pady=20)

    delete_but = Button(f4, text="Delete Client Details", font=('Arial Black', 13), bg='#fa968e', command=delete_car).grid(row=1, column=1)
    edit_car_but = Button(f4, text="Edit Client Details", font=('Arial Black', 13), bg='#8efacd', command=edit_car_details_func).grid(row=1, column=2, padx=50)
    back_but = Button(f4, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).grid(row=1, column=3)

    view_client_details_root.mainloop()


def delete_client_details_login():

    def authentication():
        if username_var.get()==user_id and password_var.get()==password:
            ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Delete Client Record/Details ??")
            if ans==True:
                # Deletion Code Here
                client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

                ref_sort_df = client_details_df[client_details_df.Ref_No == selected_ref_no]
                aadhar_card_view_path = ref_sort_df.Aadhar_Card.to_list()[0]
                pan_card_view_path = ref_sort_df.Pan_Card.to_list()[0]

                try:
                    os.remove(aadhar_card_view_path)
                    os.remove(pan_card_view_path)
                except Exception as error:
                    pass
                
                index_names = client_details_df[client_details_df['Ref_No'] == int(selected_ref_no)].index
                
                client_details_df.drop(index_names, inplace = True)
                client_details_df.to_csv("D:\Soham_Motors\Software_Files\client_details_file.csv")

                tkinter.messagebox.showinfo("Client Details Deleted Successfully", "Client Details Deleted Successfully ...")

                login_root.destroy()
                show_client_details()
            else:
                tkinter.messagebox.showinfo("Client Details Not Deleted", "Client Details Not Deleted !!!!!!")
                login_root.destroy()
                show_client_details()
        else:
            tkinter.messagebox.showerror("Authentication Unsuccessful", "Incorrect User ID or Password")

    def authentication_bind(event):
        authentication()

    def back_but_func():
        login_root.destroy()
        show_client_details()

    login_root = Tk()
    login_root.geometry("1366x695-0+0")
    login_root.title("Login - Speed Up Billing Software")
    login_root.configure(bg="#315b82")
    login_root.iconbitmap('speed_up_logo.ico')

    # Adding Create Account Image
    f1 = Frame(login_root, borderwidth=1, bg="#315b82")
    f1.pack(pady=50)

    login_photo = PhotoImage(file='login_logo.png')
    login_image = Label(f1, image=login_photo, bg="#315b82").pack(pady=10)
    login_text = Label(f1, text="Login to Delete Client Details", font=('Arial Black', 25), bg="#315b82", fg="#ebde4d").pack(padx=50)

    f2 = Frame(login_root, borderwidth=1, bg="#315b82")
    f2.pack(pady=20)

    username_var = StringVar()
    password_var = StringVar()

    user_label = Label(f2, text="User ID : ", font=('Arial Black', 20), bg="#315b82", fg="white").grid(row=1, column=1, padx=10)
    pass_label = Label(f2, text="Password : ", font=('Arial Black', 20), bg="#315b82", fg="white").grid(row=2, column=1)


    user_entry = Entry(f2, textvariable=username_var, font=('comicsansms', 15))
    user_entry.grid(row=1, column=2)
    pass_entry = Entry(f2, textvariable=password_var, font=('comicsansms', 15), show="*").grid(row=2, column=2)

    user_entry.focus()
    
    case_sensitive_label = Label(f2, text="  (Case Sensitive)", font=('Arial', 13), bg="#315b82", fg="yellow").grid(row=1, column=3)
    case_sensitive_label = Label(f2, text="  (Case Sensitive)", font=('Arial', 13), bg="#315b82", fg="yellow").grid(row=2, column=3)

    f3 = Frame(login_root, borderwidth=1, bg="#315b82")
    f3.pack(pady=40)

    login_but = Button(f3, text="Login", font=('Arial Black', 15), bg='#9df760', command=authentication)
    login_but.pack(pady=20)

    back_but = Button(f3, text="Back", font=('Arial Black', 15), bg='#fae88e', command=back_but_func)
    back_but.pack(pady=20)

    # Binding Enter Key
    login_root.bind('<Return>',authentication_bind)

    login_root.mainloop()


def edit_client_details_window():
    global selected_issue_date, selected_expiry_date


    def date_of_inquiry_func():
        selected_date_of_inquiry = date_of_inquiry_calendar.get_date()
        date_of_inquiry_var.set(selected_date_of_inquiry)

    def add_car_func():


        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

        # Appending Car Details to Csv
        car_name =  car_name_var.get()
        model = model_var.get()
        year = year_var.get()
        client_name = client_name_var.get()
        address = address_var.get()
        mobile_no = mobile_no_var.get()
        email = email_var.get()
        date_of_inquiry = date_of_inquiry_var.get()

        today = date.today()
        date_of_entry = today.strftime("%d/%m/%Y")

        client_details_df_len = len(client_details_df)
        
        pre_ref_no = ref_sort_df.Ref_No.to_list()[0]

        # print("Pre Ref No: ", pre_ref_no)

        if car_name!='Select Car' and model!='Select Model' and year!='Select Year' and date_of_inquiry!="" and client_name!="" and address!="" and mobile_no!="" and email!="":
            # Checking All Entry Values are Filled
            if car_name=="" or model=="" or year=="":
                tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")
            else:
                
                new_aadhar_path = pre_aadhar_path
                new_pan_path = pre_pan_path

                try:
                    if pre_aadhar_path!=aadhar_card_filename_path:
                        
                        os.remove(pre_aadhar_path)
                        shutil.copy(aadhar_card_filename_path, filepath_1)

                        split_tup_1 = os.path.splitext(aadhar_card_filename_path)
                        aadhar_file_ext = split_tup_1[1]
                        aadhar_dst_file = os.path.join(filepath_1, aadhar_card_filename)
                        aadhar_new_dst_file_name = os.path.join(filepath_1, f'ref_{pre_ref_no}{aadhar_file_ext}')
                        new_aadhar_path = aadhar_new_dst_file_name
                        os.rename(aadhar_dst_file, aadhar_new_dst_file_name)
                except Exception as error:
                    pass    

                        
                try:
                    if pre_pan_path!=pan_card_filename_path:                            
                        
                        os.remove(pre_pan_path)
                        shutil.copy(pan_card_filename_path, filepath_2)

                        split_tup_2 = os.path.splitext(pan_card_filename_path)
                        pan_file_ext = split_tup_2[1]
                        pan_dst_file = os.path.join(filepath_2, pan_card_filename)
                        pan_new_dst_file_name = os.path.join(filepath_2, f'ref_{pre_ref_no}{pan_file_ext}')
                        new_pan_path = pan_new_dst_file_name
                        os.rename(pan_dst_file, pan_new_dst_file_name)
                except Exception as error:
                    pass



                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Car_Name'] = car_name
                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Model'] = model
                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Year'] = year
                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Client_Name'] = client_name
                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Address'] = address
                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Mobile_No'] = mobile_no
                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Date_of_Inquiry'] = date_of_inquiry_var.get()
                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Aadhar_Card'] = new_aadhar_path
                client_details_df.loc[client_details_df['Ref_No'] == int(selected_ref_no), 'Pan_Card'] = new_pan_path
                
                client_details_df.to_csv("D:\Soham_Motors\Software_Files\client_details_file.csv")

                tkinter.messagebox.showinfo("Client Details Edited Successfully", "Client Details Edited Successfully")
                add_car_root.destroy()
                show_client_details()

        else:
            tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")

    def back_but_func():
        add_car_root.destroy()
        show_client_details()


    add_car_root = Tk()
    add_car_root.geometry("1366x695-0+0")
    add_car_root.title("Login - Speed Up Billing Software")
    add_car_root.configure(bg="#001020")
    add_car_root.iconbitmap('speed_up_logo.ico')

    # Loading Client Details Df
    try:
        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Client_Name":[],
            "Address":[],
            "Mobile_No":[],
            "Email":[],
            "Date_of_Inquiry":[],
            "Ref_No":[],
            "Aadhar_Card":[],
            "Pan_Card":[],
            "Aadhar_File_Name":[],
            "Pan_File_Name":[]
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\client_details_file.csv")

        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    f0 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Edit Client Inquiry', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    f1 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f1.pack(pady=40)

    def car_box_update(event):
        global model_list, car2_selected

        model_var.set(ref_sort_df.Model.to_list()[0])

        car_selected = event.widget.get()
        car2_selected = car_selected
        if car_selected!="Select Car":
            model_list = car_details_df[car_details_df.Car_Name==car_selected].drop_duplicates(subset = ["Model"]).Model.to_list()
            model_list.insert(0, "Select Model")
            model_box['values'] = model_list
    
    def model_box_update(event):
        global year_list
        
        year_var.set(ref_sort_df.Year.to_list()[0])

        model_selected = event.widget.get()
        if model_selected!="Select Model":
            year_list = car_details_df[car_details_df.Car_Name==car2_selected][car_details_df.Model==model_selected].drop_duplicates(subset = ["Year"]).Year.to_list()
            year_list.insert(0, "Select Year")
            year_box['values'] = year_list


    # Adding Search Options -------- Starts Here

    # ------ Car Name Combobox --------------
    f10 = Frame(f1, borderwidth=1, bg="#001020")
    f10.pack(fill=BOTH, padx=100)

    f3 = Frame(f10, borderwidth=1, bg="#001020")
    f3.grid(row=1, column=1)

    ref_sort_df = client_details_df[client_details_df.Ref_No == selected_ref_no]
    



    car_name_label = Label(f3, text='Car Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)

    car_name_list = car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()
    car_name_list.insert(0, ref_sort_df.Car_Name.to_list()[0])

    car_name_var = StringVar()
    car_name_var.set(ref_sort_df.Car_Name.to_list()[0])

    car_box = ttk.Combobox(f3, width=20, textvariable=car_name_var)
    car_box['values'] = car_name_list
    car_box.grid(row=1, column=2)
    car_box.current(0)
    car_box.bind("<<ComboboxSelected>>", car_box_update)

    # ------ Model Combobox ----------------
    f4 = Frame(f3, borderwidth=1, bg="#001020")
    f4.grid(row=1, column=3, padx=20)

    model_label = Label(f4, text='Model: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)

    model_list = []
    model_list.insert(0, ref_sort_df.Model.to_list()[0])

    model_var = StringVar()
    model_var.set(ref_sort_df.Model.to_list()[0])

    model_box = ttk.Combobox(f4, width=20, textvariable=model_var)
    model_box['values'] = model_list
    model_box.grid(row=1, column=2)
    model_box.current(0)
    model_box.bind("<<ComboboxSelected>>", model_box_update)


    # ------ Year Combobox ----------------
    f5 = Frame(f3, borderwidth=1, bg="#001020")
    f5.grid(row=1, column=4)

    year_label = Label(f5, text='Year: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)

    year_list = []
    year_list.insert(0, ref_sort_df.Year.to_list()[0])

    year_var = StringVar()
    year_var.set(ref_sort_df.Year.to_list()[0])

    year_box = ttk.Combobox(f5, width=20, textvariable=year_var)
    year_box['values'] = year_list
    year_box.grid(row=1, column=2)
    year_box.current(0)

    f2 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f2.pack()

    client_name_var = StringVar()
    client_name_var.set(ref_sort_df.Client_Name.to_list()[0])
    client_name_label = Label(f2, text='Client Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    client_name_entry = Entry(f2, textvariable=client_name_var, font=('comicsansms', 15))
    client_name_entry.grid(row=4, column=2)
    
    address_var = StringVar()
    address_var.set(ref_sort_df.Address.to_list()[0])
    address_label = Label(f2, text='Address: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    address_entry = Entry(f2, textvariable=address_var, font=('comicsansms', 15))
    address_entry.grid(row=5, column=2)
    
    mobile_no_var = StringVar()
    mobile_no_var.set(ref_sort_df.Mobile_No.to_list()[0])
    mobile_no_label = Label(f2, text='Mobile No: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    mobile_no_entry = Entry(f2, textvariable=mobile_no_var, font=('comicsansms', 15))
    mobile_no_entry.grid(row=6, column=2)
    
    email_var = StringVar()
    email_var.set(ref_sort_df.Email.to_list()[0])
    email_label = Label(f2, text='Email: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    email_entry = Entry(f2, textvariable=email_var, font=('comicsansms', 15))
    email_entry.grid(row=7, column=2)
    
    clear_entry_content_var_1 = StringVar()
    clear_entry_content_button = Checkbutton(f2, text = "Clear Entry Content", bg='#f7ea36', font=('Comicsansms', 10, 'bold') , variable = clear_entry_content_var_1, onvalue = 1, offvalue = 0, height = 2, width = 20)
    clear_entry_content_button.select()
    clear_entry_content_button.grid(row=7, column=3, padx=30)

    pre_aadhar_path = ref_sort_df.Aadhar_Card.to_list()[0]
    pre_pan_path = ref_sort_df.Pan_Card.to_list()[0]


    def upload_aadhar_card():
        global aadhar_card_filename, pan_card_filename, filepath_1, aadhar_card_filename_path

        filepath_1 = "D:\Soham_Motors\Aadhar_Card"
        aadhar_card_filename_path = filedialog.askopenfilename()
        aadhar_card_filename = os.path.split(aadhar_card_filename_path)[1]
        aadhar_card_path.set(aadhar_card_filename)
    
    def upload_pan_card():
        global aadhar_card_filename, pan_card_filename, filepath_2, pan_card_filename_path

        filepath = "D:\Soham_Motors\Pan_Card"
        pan_card_filename_path = filedialog.askopenfilename()
        pan_card_filename = os.path.split(pan_card_filename_path)[1]
        pan_card_path.set(pan_card_filename)
    
    
    filepath_1 = "D:\Soham_Motors\Aadhar_Card"
    filepath_2 = "D:\Soham_Motors\Pan_Card"

    aadhar_card_path = StringVar()
    pan_card_path = StringVar()

    upload_aadhar_card_but = Button(f2, text="Upload Aadhar Card", font=('Arial Black', 10), bg='#fcca5d', command=upload_aadhar_card).grid(row=8, column=1, pady=10)
    upload_Pan_card_but = Button(f2, text="Upload Pan Card", font=('Arial Black', 10), bg='#fcca5d', command=upload_pan_card).grid(row=8, column=2, pady=10)
    


    f3 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f3.pack()

    # Add Calendar
    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    date_of_inquiry_calendar = Calendar(f3, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    date_of_inquiry_calendar.grid(row=1, column=1)
    
    f5 = Frame(f3, borderwidth=1, bg='#001020')
    f5.grid(row=1, column=2, padx=10)

    date_of_inquiry_var = StringVar()
    date_of_inquiry_var.set(ref_sort_df.Date_of_Inquiry.to_list()[0])
    date_of_inquiry_but = Button(f5, text="Date of Inquiry", font=('Arial Black', 10), bg='#fcca5d', command=date_of_inquiry_func).grid(row=1, column=1, pady=10)
    
    date_of_inquiry_label = Label(f5, textvariable=date_of_inquiry_var, bg='#001020', fg='white', font=('Arial Black',10)).grid(row=1, column=2)
    


    f4 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f4.pack(pady=20)

    add_but = Button(f4, text="Edit & Save", font=('Arial Black', 13), bg='#5eff8c', command=add_car_func).grid(row=1, column=1, padx=30)
    back_but = Button(f4, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).grid(row=1, column=2)
    
    add_car_root.mainloop()


def add_buyer_details():

    show_car_root = Tk()
    show_car_root.geometry("1366x695-0+0")
    show_car_root.title("Login - Speed Up Billing Software")
    show_car_root.configure(bg="#001020")
    show_car_root.iconbitmap('speed_up_logo.ico')

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Basic_Cost": [],
            "Tire_Cost": [],
            "Battery": [],
            "Denting_Painting_Cost": [],
            "Other_Expenses": [],
            "Insurance_issue_date": [],
            "Insurance_expiry_date": [],
            "Date_of_Entry": [],
            "Ref_No": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    f0 = Frame(show_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Select Car', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    # Adding Filter Search Title
    f2 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f2.pack(fill=BOTH, padx=100, pady=0)

    title1_label = Label(f2, text='Filter Search:', bg='#001020', fg='#f0b754', font=('Berlin Sans FB Demi',20)).grid(row=1, column=1, padx=0, pady=20)
    title2_label = Label(f2, text='', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',10)).grid(row=1, column=2)
    

    def car_box_update(event):
        global model_list, car1_selected

        car_selected = event.widget.get()
        car1_selected = car_selected
        if car_selected!="Select Car":

            # car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()

            model_list = car_details_df[car_details_df.Car_Name==car_selected].drop_duplicates(subset = ["Model"]).Model.to_list()
            model_list.insert(0, "Select Model")
            model_box['values'] = model_list
    
    def model_box_update(event):
        global year_list

        model_selected = event.widget.get()
        if model_selected!="Select Model":
            year_list = car_details_df[car_details_df.Car_Name==car1_selected][car_details_df.Model==model_selected].drop_duplicates(subset = ["Year"]).Year.to_list()
            year_list.insert(0, "Select Year")
            year_box['values'] = year_list


    # Adding Search Options -------- Starts Here

    # ------ Car Name Combobox --------------
    f10 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f10.pack(fill=BOTH, padx=100)

    f3 = Frame(f10, borderwidth=1, bg="#001020")
    f3.grid(row=1, column=1)

    car_name_label = Label(f3, text='Car Name: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    car_name_list = car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()
    car_name_list.insert(0, "Select Car")

    car_name_var = StringVar()
    car_name_var.set(car_name_list[0])

    car_box = ttk.Combobox(f3, width=20, textvariable=car_name_var)
    car_box['values'] = car_name_list
    car_box.grid(row=1, column=2)
    car_box.current(0)
    car_box.bind("<<ComboboxSelected>>", car_box_update)

    # ------ Model Combobox ----------------
    f4 = Frame(f3, borderwidth=1, bg="#001020")
    f4.grid(row=1, column=3, padx=20)

    model_label = Label(f4, text='Model: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    model_list = []
    model_list.insert(0, "Select Model")

    model_var = StringVar()
    model_var.set(model_list[0])

    model_box = ttk.Combobox(f4, width=20, textvariable=model_var)
    model_box['values'] = model_list
    model_box.grid(row=1, column=2)
    model_box.current(0)
    model_box.bind("<<ComboboxSelected>>", model_box_update)


    # ------ Year Combobox ----------------
    f5 = Frame(f3, borderwidth=1, bg="#001020")
    f5.grid(row=1, column=4)

    year_label = Label(f5, text='Year: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    year_list = []
    year_list.insert(0, "Select Year")

    year_var = StringVar()
    year_var.set(year_list[0])

    year_box = ttk.Combobox(f5, width=20, textvariable=year_var)
    year_box['values'] = year_list
    year_box.grid(row=1, column=2)
    year_box.current(0)
    

    # Adding Search Options -------- Ends Here

    f1 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f1.pack(fill=BOTH, padx=100, pady=50)

    # ------------Treeview for Displaying Cart Items and its Details---------------------

    tree1 = ttk.Treeview(f1, selectmode="extended", height=10)
    # Column names of Treeview
    tree1['columns'] = ('Sr', 'Name', 'Model', 'Year', 'Total Cost', 'Insurance Issue Date', 'Insurance Expiry Date', 'Date of Entry', 'Ref_No')

    # Adding Columns
    tree1.column('#0', width=0, stretch=NO)
    tree1.column('Sr', anchor=W, width=30, minwidth=0, stretch=NO)
    tree1.column('Name', anchor=W, width=50, minwidth=50)
    tree1.column('Model', anchor=W, width=50, minwidth=50)
    tree1.column('Year', anchor=W, width=50, minwidth=50)
    tree1.column('Total Cost', anchor=W, width=50, minwidth=50)
    tree1.column('Insurance Issue Date', anchor=W, width=50, minwidth=50)
    tree1.column('Insurance Expiry Date', anchor=W, width=50, minwidth=50)
    tree1.column('Date of Entry', anchor=W, width=50, minwidth=50)
    tree1.column('Ref_No', anchor=W, width=50, minwidth=50)
    
    
    # Adding Heading of Columns
    tree1.heading('#0', text='', anchor=W)
    tree1.heading('Sr', text='Sr', anchor=W)
    tree1.heading('Name', text='Name', anchor=W)
    tree1.heading('Model', text='Model', anchor=W)
    tree1.heading('Year', text='Year', anchor=W)
    tree1.heading('Total Cost', text='Total Cost', anchor=W)
    tree1.heading('Insurance Issue Date', text='Insurance Issue Date', anchor=W)
    tree1.heading('Insurance Expiry Date', text='Insurance Expiry Date', anchor=W)
    tree1.heading('Date of Entry', text='Date of Entry', anchor=W)
    tree1.heading('Ref_No', text='Ref_No', anchor=W)
    
    tree1.pack(fill=X, pady=20, expand=YES)

    # Adding Scrollbar
    scrollbar = Scrollbar()
    scrollbar.config(command=tree1.yview)

    iid_number1 = 1
    sr_no1 = 1
    car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")
    for i in range(0, len(car_details_df)):
        total_cost_1 = int(car_details_df.Basic_Cost.to_list()[i]) + car_details_df.Tire_Cost.to_list()[i] + car_details_df.Battery.to_list()[i]+ car_details_df.Denting_Painting_Cost.to_list()[i] + car_details_df.Other_Expenses.to_list()[i]
        tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, car_details_df.Car_Name.to_list()[i], car_details_df.Model.to_list()[i], car_details_df.Year.to_list()[i], total_cost_1, car_details_df.Insurance_issue_date.to_list()[i], car_details_df.Insurance_expiry_date.to_list()[i], car_details_df.Date_of_Entry.to_list()[i], car_details_df.Ref_No.to_list()[i]))
        iid_number1+=1
        sr_no1+=1
    
    f11 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f11.pack(padx=100)

    def search_but_func():
        car_name = car_name_var.get()
        model = model_var.get()

        try:
            if car_name=='Select Car' and model=='Select Model' and year_var.get()=='Select Year':
                iid_number1 = 1
                sr_no1 = 1

                for i in range(0, len(car_details_df)):
                    total_cost_1 = int(car_details_df.Basic_Cost.to_list()[i]) + car_details_df.Tire_Cost.to_list()[i] + car_details_df.Battery.to_list()[i]+ car_details_df.Denting_Painting_Cost.to_list()[i] + car_details_df.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, car_details_df.Car_Name.to_list()[i], car_details_df.Model.to_list()[i], car_details_df.Year.to_list()[i], total_cost_1, car_details_df.Insurance_issue_date.to_list()[i], car_details_df.Insurance_expiry_date.to_list()[i], car_details_df.Date_of_Entry.to_list()[i], car_details_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                # tkinter.messagebox.showerror("Please Select Car/Model/Year", "Please Select Car/Model/Year")

            elif model=='Select Model' and year_var.get()=='Select Year':
                required_car_result = car_details_df[car_details_df.Car_Name == car_name]

                iid_number1 =1
                sr_no1 = 1

                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_car_result)):
                    total_cost_1 = int(required_car_result.Basic_Cost.to_list()[i]) + required_car_result.Tire_Cost.to_list()[i] + required_car_result.Battery.to_list()[i]+ required_car_result.Denting_Painting_Cost.to_list()[i] + required_car_result.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_car_result.Car_Name.to_list()[i], required_car_result.Model.to_list()[i], required_car_result.Year.to_list()[i], total_cost_1, required_car_result.Insurance_issue_date.to_list()[i], required_car_result.Insurance_expiry_date.to_list()[i], required_car_result.Date_of_Entry.to_list()[i], required_car_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                
            elif year_var.get()=='Select Year':

                required_car_result = car_details_df[car_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_model_result)):
                    total_cost_1 = int(required_model_result.Basic_Cost.to_list()[i]) + required_model_result.Tire_Cost.to_list()[i] + required_model_result.Battery.to_list()[i]+ required_model_result.Denting_Painting_Cost.to_list()[i] + required_model_result.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_model_result.Car_Name.to_list()[i], required_model_result.Model.to_list()[i], required_model_result.Year.to_list()[i], total_cost_1, required_model_result.Insurance_issue_date.to_list()[i], required_model_result.Insurance_expiry_date.to_list()[i], required_model_result.Date_of_Entry.to_list()[i], required_model_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
            else:
                year = int(year_var.get())

                required_car_result = car_details_df[car_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]
                search_result_df = required_model_result[required_model_result.Year == year]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(search_result_df)):
                    total_cost_1 = int(search_result_df.Basic_Cost.to_list()[i]) + search_result_df.Tire_Cost.to_list()[i] + search_result_df.Battery.to_list()[i]+ search_result_df.Denting_Painting_Cost.to_list()[i] + search_result_df.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, search_result_df.Car_Name.to_list()[i], search_result_df.Model.to_list()[i], search_result_df.Year.to_list()[i], total_cost_1, search_result_df.Insurance_issue_date.to_list()[i], search_result_df.Insurance_expiry_date.to_list()[i], search_result_df.Date_of_Entry.to_list()[i], search_result_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
        except Exception as error:
            pass


    def next_func():
        global selected_ref_no

        try:

            selected = tree1.focus()
            selected_item = tree1.item(selected)

            selected_ref_no = int(selected_item['values'][8])

            show_car_root.destroy()

            add_buyer_details_window()

        except Exception as error:
            tkinter.messagebox.showerror("Please Select Car from the Table", "Please Select Car from the Table")

    def back_but_func():
        show_car_root.destroy()
        main_menu_window()

    search_but = Button(f11, text="Search Results", font=('Arial Black', 10), bg='#fc7ced', command=search_but_func).grid(row=1, column=1)
    next_but = Button(f11, text="Next", font=('Arial Black', 10), bg='#8fd149', command=next_func).grid(row=1, column=2, padx=50)
    back_but = Button(f11, text="Back", font=('Arial Black', 10), bg='#fcca5d', command=back_but_func).grid(row=1, column=3)
    

    show_car_root.mainloop()


def add_buyer_details_window():
    global selected_issue_date, selected_expiry_date


    def date_of_inquiry_func():
        selected_date_of_inquiry = date_of_inquiry_calendar.get_date()
        date_of_inquiry_var.set(selected_date_of_inquiry)

    def add_car_func():


        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

        ref_sort_df = car_details_df[car_details_df.Ref_No == selected_ref_no]
        

        # Appending Car Details to Csv
        car_name =  ref_sort_df.Car_Name.to_list()[0]
        model = ref_sort_df.Model.to_list()[0]
        year = ref_sort_df.Year.to_list()[0]
        buyer_name = buyer_name_var.get()
        address = address_var.get()
        mobile_no = mobile_no_var.get()
        email = email_var.get()
        cost_price = int(ref_sort_df.Basic_Cost.to_list()[0]) + ref_sort_df.Tire_Cost.to_list()[0] + ref_sort_df.Battery.to_list()[0]+ ref_sort_df.Denting_Painting_Cost.to_list()[0] + ref_sort_df.Other_Expenses.to_list()[0]
        selling_price = int(selling_price_var.get())
        amount_paid = int(amount_paid_var.get())
        profit = int(selling_price - cost_price)
        mode_of_payment = mode_of_payment_var.get()
        date_of_buying = date_of_inquiry_var.get()
        insurance_issue_date = ref_sort_df.Insurance_issue_date.to_list()[0]
        insurance_expiry_date = ref_sort_df.Insurance_expiry_date.to_list()[0]

        buyer_details_df_len = len(buyer_details_df)
        try:
            pre_ref_no = int(buyer_details_df.Ref_No.to_list()[buyer_details_df_len-1])
        except Exception as Error:
            pre_ref_no = 0

        if buyer_name!="" and address!="" and mobile_no!="" and amount_paid_var.get()!="" and selling_price_var.get()!="" and mode_of_payment!="" and date_of_buying!="":
            # Checking All Entry Values are Filled
            if buyer_name=="" and address=="" and mobile_no=="" and amount_paid_var.get()=="" and selling_price_var.get()=="" and mode_of_payment=="" and date_of_buying=="":
                tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")
            else:

                try:
                    shutil.copy(aadhar_card_filename_path, filepath_1)
                    split_tup_1 = os.path.splitext(aadhar_card_filename_path)
                    aadhar_file_ext = split_tup_1[1]
                    aadhar_dst_file = os.path.join(filepath_1, aadhar_card_filename)
                    aadhar_new_dst_file_name = os.path.join(filepath_1, f'ref_{pre_ref_no+1}{aadhar_file_ext}')
                    os.rename(aadhar_dst_file, aadhar_new_dst_file_name)
                except Exception as error:
                    aadhar_new_dst_file_name = ""
                
                try:
                    shutil.copy(pan_card_filename_path, filepath_2)
                    split_tup_2 = os.path.splitext(pan_card_filename_path)
                    pan_file_ext = split_tup_2[1]
                    pan_dst_file = os.path.join(filepath_2, pan_card_filename)
                    pan_new_dst_file_name = os.path.join(filepath_2, f'ref_{pre_ref_no+1}{pan_file_ext}')
                    os.rename(pan_dst_file, pan_new_dst_file_name)
                except Exception as error:
                    pan_new_dst_file_name = ""
                
                try:
                    shutil.copy(car_insurance_filename_path, filepath_3)
                    split_tup_3 = os.path.splitext(car_insurance_filename_path)
                    car_insurance_file_ext = split_tup_3[1]
                    car_insurance_dst_file = os.path.join(filepath_3, car_insurance_filename)
                    car_insurance_new_dst_file_name = os.path.join(filepath_3, f'ref_{pre_ref_no+1}{car_insurance_file_ext}')
                    os.rename(car_insurance_dst_file, car_insurance_new_dst_file_name)
                except Exception as error:
                    car_insurance_new_dst_file_name = ""
                
                try:
                    shutil.copy(reciept_filename_path, filepath_4)
                    split_tup_4 = os.path.splitext(reciept_filename_path)
                    reciept_file_ext = split_tup_4[1]
                    reciept_dst_file = os.path.join(filepath_4, reciept_filename)
                    reciept_new_dst_file_name = os.path.join(filepath_4, f'ref_{pre_ref_no+1}{reciept_file_ext}')
                    os.rename(reciept_dst_file, reciept_new_dst_file_name)
                except Exception as error:
                    reciept_new_dst_file_name = ""

                dict3 = {
                    "Car_Name": [car_name],
                    "Model": [model],
                    "Year": [year],
                    "Buyer_Name":[buyer_name],
                    "Address":[address],
                    "Mobile_No":[mobile_no],
                    "Email":[email],
                    "Cost_Price":[cost_price],
                    "Selling_Price":[selling_price],
                    "Amount_Paid":[amount_paid],
                    "Profit":[profit],
                    "Mode_of_Payment":[mode_of_payment],
                    "Date_of_Buying":[date_of_buying],
                    "Ref_No":[pre_ref_no+1],
                    "Aadhar_Card":[aadhar_new_dst_file_name],
                    "Pan_Card":[pan_new_dst_file_name],
                    "Car_Insurance":[car_insurance_new_dst_file_name],
                    "Reciept":[reciept_new_dst_file_name],
                    "Insurance_issue_date":[insurance_issue_date],
                    "Insurance_expiry_date":[insurance_expiry_date]
            }
                add_buyer_details_df = pd.DataFrame(dict3)

                df2 = pd.concat([buyer_details_df, add_buyer_details_df], ignore_index=True)
                df2.to_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv")
                
                
                
                print(aadhar_new_dst_file_name)
                print(pan_new_dst_file_name)

                # "Ref_No":[pre_ref_no + 1],
                # "Aadhar_Card":[aadhar_new_dst_file_name],
                # "Pan_Card":[pan_new_dst_file_name]
                
                tkinter.messagebox.showinfo("Buyer Details Added Successfully", "Buyer Details Added Successfully")
                add_car_root.destroy()
                add_buyer_details()
        else:
            tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")

    def back_but_func():
        add_car_root.destroy()
        add_buyer_details()


    add_car_root = Tk()
    add_car_root.geometry("1366x695-0+0")
    add_car_root.title("Login - Speed Up Billing Software")
    add_car_root.configure(bg="#001020")
    add_car_root.iconbitmap('speed_up_logo.ico')

    # Loading Buyer Details Df
    try:
        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Buyer_Name":[],
            "Address":[],
            "Mobile_No":[],
            "Email":[],
            "Cost_Price":[],
            "Selling_Price":[],
            "Amount_Paid":[],
            "Profit":[],
            "Mode_of_Payment":[],
            "Date_of_Buying":[],
            "Ref_No":[],
            "Aadhar_Card":[],
            "Pan_Card":[],
            "Car_Insurance":[],
            "Reciept":[],
            "Insurance_issue_date":[],
            "Insurance_expiry_date":[]
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv")

        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    f0 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Add Buyer Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    f1 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f1.pack(pady=10)

    f2 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f2.pack()

    buyer_name_var = StringVar()
    buyer_name_label = Label(f2, text='Buyer Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    buyer_name_entry = Entry(f2, textvariable=buyer_name_var, font=('comicsansms', 15))
    buyer_name_entry.grid(row=1, column=2)
    
    address_var = StringVar()
    address_label = Label(f2, text='Address: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=2, column=1)
    address_entry = Entry(f2, textvariable=address_var, font=('comicsansms', 15))
    address_entry.grid(row=2, column=2)
    
    mobile_no_var = StringVar()
    mobile_no_label = Label(f2, text='Mobile No: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=3, column=1)
    mobile_no_entry = Entry(f2, textvariable=mobile_no_var, font=('comicsansms', 15))
    mobile_no_entry.grid(row=3, column=2)
    
    email_var = StringVar()
    email_label = Label(f2, text='Email: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    email_entry = Entry(f2, textvariable=email_var, font=('comicsansms', 15))
    email_entry.grid(row=4, column=2)
    
    selling_price_var = StringVar()
    selling_price_label = Label(f2, text='Selling Price: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    selling_price_entry = Entry(f2, textvariable=selling_price_var, font=('comicsansms', 15))
    selling_price_entry.grid(row=5, column=2)
    
    amount_paid_var = StringVar()
    amount_paid_label = Label(f2, text='Amount Paid: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    amount_paid_entry = Entry(f2, textvariable=amount_paid_var, font=('comicsansms', 15))
    amount_paid_entry.grid(row=6, column=2)
    
    mode_of_payment_var = StringVar()
    mode_of_payment_label = Label(f2, text='Mode of Payment: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    mode_of_payment_entry = Entry(f2, textvariable=mode_of_payment_var, font=('comicsansms', 15))
    mode_of_payment_entry.grid(row=7, column=2)
    
    def upload_aadhar_card():
        global aadhar_card_filename, pan_card_filename, filepath_1, aadhar_card_filename_path

        filepath_1 = "D:\Soham_Motors\Buyer_Aadhar_Card"
        aadhar_card_filename_path = filedialog.askopenfilename()
        aadhar_card_filename = os.path.split(aadhar_card_filename_path)[1]
        aadhar_card_path.set(aadhar_card_filename)
    
    def upload_pan_card():
        global aadhar_card_filename, pan_card_filename, filepath_2, pan_card_filename_path

        filepath = "D:\Soham_Motors\Buyer_Pan_Card"
        pan_card_filename_path = filedialog.askopenfilename()
        pan_card_filename = os.path.split(pan_card_filename_path)[1]
        pan_card_path.set(pan_card_filename)
    
    def upload_car_insurance():
        global  car_insurance_filename, filepath_2, car_insurance_filename_path

        filepath = "D:\Soham_Motors\Car_Insurance"
        car_insurance_filename_path = filedialog.askopenfilename()
        car_insurance_filename = os.path.split(car_insurance_filename_path)[1]
        car_insurance_path.set(car_insurance_filename)
    
    def upload_reciept():
        global reciept_filename, filepath_2, reciept_filename_path

        filepath = "D:\Soham_Motors\Reciept"
        reciept_filename_path = filedialog.askopenfilename()
        reciept_filename = os.path.split(reciept_filename_path)[1]
        reciept_path.set(reciept_filename)
    
    filepath_1 = "D:\Soham_Motors\Buyer_Aadhar_Card"
    filepath_2 = "D:\Soham_Motors\Buyer_Pan_Card"
    filepath_3 = "D:\Soham_Motors\Car_Insurance"
    filepath_4 = "D:\Soham_Motors\Reciept"
    
    aadhar_card_path = StringVar()
    pan_card_path = StringVar()
    car_insurance_path = StringVar()
    reciept_path = StringVar()
    
    upload_aadhar_card_but = Button(f2, text="Upload Aadhar Card", font=('Arial Black', 10), bg='#fcca5d', command=upload_aadhar_card).grid(row=8, column=1, pady=10)
    upload_Pan_card_but = Button(f2, text="Upload Pan Card", font=('Arial Black', 10), bg='#fcca5d', command=upload_pan_card).grid(row=8, column=2, pady=10)
    upload_car_insurance_but = Button(f2, text="Upload Car Insurance", font=('Arial Black', 10), bg='#fcca5d', command=upload_car_insurance).grid(row=8, column=3, pady=10)
    upload_reciept_but = Button(f2, text="Upload Payment Proof/Reciept", font=('Arial Black', 10), bg='#fcca5d', command=upload_reciept).grid(row=8, column=4, pady=10, padx=40)
    
    f3 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f3.pack()

    # Add Calendar
    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    date_of_inquiry_calendar = Calendar(f3, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    date_of_inquiry_calendar.grid(row=1, column=1)
    
    f5 = Frame(f3, borderwidth=1, bg='#001020')
    f5.grid(row=1, column=2, padx=10)

    date_of_inquiry_var = StringVar()
    
    date_of_inquiry_but = Button(f5, text="Date of Buying Car", font=('Arial Black', 10), bg='#fcca5d', command=date_of_inquiry_func).grid(row=1, column=1, pady=10)
    
    date_of_inquiry_label = Label(f5, textvariable=date_of_inquiry_var, bg='#001020', fg='white', font=('Arial Black',10)).grid(row=1, column=2)
    
    f4 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f4.pack(pady=20)

    add_but = Button(f4, text="Add", font=('Arial Black', 13), bg='#5eff8c', command=add_car_func).grid(row=1, column=1, padx=30)
    back_but = Button(f4, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).grid(row=1, column=2)
    
    add_car_root.mainloop()


def show_buyer_details():

    show_client_root = Tk()
    show_client_root.geometry("1366x695-0+0")
    show_client_root.title("Login - Speed Up Billing Software")
    show_client_root.configure(bg="#001020")
    show_client_root.iconbitmap('speed_up_logo.ico')

    # Loading Car Details Df
    try:
        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Buyer_Name":[],
            "Address":[],
            "Mobile_No":[],
            "Email":[],
            "Cost_Price":[],
            "Selling_Price":[],
            "Amount_Paid":[],
            "Profit":[],
            "Mode_of_Payment":[],
            "Date_of_Buying":[],
            "Ref_No":[],
            "Aadhar_Card":[],
            "Pan_Card":[],
            "Car_Insurance":[],
            "Reciept":[],
            "Insurance_issue_date":[],
            "Insurance_expiry_date":[]
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv")

        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")


    f0 = Frame(show_client_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Show Buyer Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    # Adding Filter Search Title
    f2 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f2.pack(fill=BOTH, padx=100, pady=0)

    title1_label = Label(f2, text='Filter Search:', bg='#001020', fg='#f0b754', font=('Berlin Sans FB Demi',20)).grid(row=1, column=1, padx=0, pady=20)
    title2_label = Label(f2, text='', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',10)).grid(row=1, column=2)
    

    def car_box_update(event):
        global model_list, car1_selected

        car_selected = event.widget.get()
        car1_selected = car_selected
        if car_selected!="Select Car":

            # car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()

            model_list = buyer_details_df[buyer_details_df.Car_Name==car_selected].drop_duplicates(subset = ["Model"]).Model.to_list()
            model_list.insert(0, "Select Model")
            model_box['values'] = model_list
    
    def model_box_update(event):
        global year_list, model1_selected

        model_selected = event.widget.get()
        model1_selected = model_selected
        if model_selected!="Select Model":
            year_list = buyer_details_df[buyer_details_df.Car_Name==car1_selected][buyer_details_df.Model==model1_selected].drop_duplicates(subset = ["Year"]).Year.to_list()
            year_list.insert(0, "Select Year")
            year_box['values'] = year_list

    def year_box_update(event):
        global client_name_list

        year_selected = event.widget.get()
        if year_selected!="Select Model":
            required_client_name_df = buyer_details_df[buyer_details_df.Car_Name==car1_selected][buyer_details_df.Model==model1_selected]
            client_name_list = required_client_name_df[buyer_details_df.Year==int(year_selected)].drop_duplicates(subset = ["Buyer_Name"]).Buyer_Name.to_list()

            client_name_list.insert(0, "Select Buyer")
            client_box['values'] = client_name_list


    # Adding Search Options -------- Starts Here

    # ------ Car Name Combobox --------------
    f10 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f10.pack(fill=BOTH, padx=100)

    f3 = Frame(f10, borderwidth=1, bg="#001020")
    f3.grid(row=1, column=1)

    car_name_label = Label(f3, text='Car Name: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    car_name_list = buyer_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()
    car_name_list.insert(0, "Select Car")

    car_name_var = StringVar()
    car_name_var.set(car_name_list[0])

    car_box = ttk.Combobox(f3, width=20, textvariable=car_name_var)
    car_box['values'] = car_name_list
    car_box.grid(row=1, column=2)
    car_box.current(0)
    car_box.bind("<<ComboboxSelected>>", car_box_update)

    # ------ Model Combobox ----------------
    f4 = Frame(f3, borderwidth=1, bg="#001020")
    f4.grid(row=1, column=3, padx=20)

    model_label = Label(f4, text='Model: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    model_list = []
    model_list.insert(0, "Select Model")

    model_var = StringVar()
    model_var.set(model_list[0])

    model_box = ttk.Combobox(f4, width=20, textvariable=model_var)
    model_box['values'] = model_list
    model_box.grid(row=1, column=2)
    model_box.current(0)
    model_box.bind("<<ComboboxSelected>>", model_box_update)


    # ------ Year Combobox ----------------
    f5 = Frame(f3, borderwidth=1, bg="#001020")
    f5.grid(row=1, column=4)

    year_label = Label(f5, text='Year: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    year_list = []
    year_list.insert(0, "Select Year")

    year_var = StringVar()
    year_var.set(year_list[0])

    year_box = ttk.Combobox(f5, width=20, textvariable=year_var)
    year_box['values'] = year_list
    year_box.grid(row=1, column=2)
    year_box.current(0)
    year_box.bind("<<ComboboxSelected>>", year_box_update)

    # ------ Car Name Combobox --------------
    f12 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f12.pack(fill=BOTH, padx=100)

    f13 = Frame(f12, borderwidth=1, bg="#001020")
    f13.grid(row=2, column=1)

    client_name_label = Label(f13, text='Client Name: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=2, column=1)

    client_name_list = []
    client_name_list.insert(0, "Select Buyer")

    client_name_var = StringVar()
    client_name_var.set(client_name_list[0])

    client_box = ttk.Combobox(f13, width=20, textvariable=client_name_var)
    client_box['values'] = client_name_list
    client_box.grid(row=2, column=2)
    client_box.current(0) 


    def date_of_entry_func():
        selected_entry_date = date_of_entry_calendar.get_date()
        date_of_inquiry_var.set(selected_entry_date)

        required_buyer_result = buyer_details_df[buyer_details_df.Date_of_Buying == date_of_inquiry_var.get()]

        iid_number1 =1
        sr_no1 = 1

        for i in tree1.get_children():
            tree1.delete(i)
        for i in range(0, len(required_buyer_result)):
            tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_buyer_result.Buyer_Name.to_list()[i], required_buyer_result.Car_Name.to_list()[i], required_buyer_result.Model.to_list()[i], required_buyer_result.Year.to_list()[i], required_buyer_result.Cost_Price.to_list()[i], required_buyer_result.Selling_Price.to_list()[i], required_buyer_result.Amount_Paid.to_list()[i], required_buyer_result.Date_of_Buying.to_list()[i], required_buyer_result.Ref_No.to_list()[i]))
            iid_number1+=1
            sr_no1+=1        


    f6 = Frame(show_client_root, borderwidth=1, bg='#001020')
    f6.place(x=820, y=100)

    # Add Calendar
    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    date_of_entry_calendar = Calendar(f6, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    date_of_entry_calendar.grid(row=1, column=1)

    date_of_inquiry_var = StringVar()

    date_of_entry_but = Button(show_client_root, text="Date of Inquiry", font=('Arial Black', 10), bg='#fcca5d', command=date_of_entry_func).place(x=1110, y=140)
    date_of_entry_label = Label(show_client_root, textvariable=date_of_inquiry_var, bg='#001020', fg='white', font=('Arial Black',10)).place(x=1120, y=180)


    # Adding Search Options -------- Ends Here

    f1 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f1.pack(fill=BOTH, padx=100, pady=50)

    # ------------Treeview for Displaying Cart Items and its Details---------------------

    tree1 = ttk.Treeview(f1, selectmode="extended", height=10)
    # Column names of Treeview
    tree1['columns'] = ('Sr', "Name", 'Car', 'Model', 'Year', 'Cost Price', 'Selling Price', 'Amount Paid', 'Date of Buying', 'Ref No')

    # Adding Columns
    tree1.column('#0', width=0, stretch=NO)
    tree1.column('Sr', anchor=W, width=30, minwidth=0, stretch=NO)
    tree1.column('Name', anchor=W, width=50, minwidth=50)
    tree1.column('Car', anchor=W, width=50, minwidth=50)
    tree1.column('Model', anchor=W, width=50, minwidth=50)
    tree1.column('Year', anchor=W, width=50, minwidth=50)
    tree1.column('Cost Price', anchor=W, width=50, minwidth=50)
    tree1.column('Selling Price', anchor=W, width=50, minwidth=50)
    tree1.column('Amount Paid', anchor=W, width=50, minwidth=50)
    tree1.column('Date of Buying', anchor=W, width=50, minwidth=50)
    tree1.column('Ref No', anchor=W, width=50, minwidth=50)
    

    # Adding Heading of Columns
    tree1.heading('#0', text='', anchor=W)
    tree1.heading('Sr', text='Sr', anchor=W)
    tree1.heading('Name', text='Name', anchor=W)
    tree1.heading('Car', text='Car', anchor=W)
    tree1.heading('Model', text='Model', anchor=W)
    tree1.heading('Year', text='Year', anchor=W)
    tree1.heading('Cost Price', text='Cost Price', anchor=W)
    tree1.heading('Selling Price', text='Selling Price', anchor=W)
    tree1.heading('Amount Paid', text='Amount Paid', anchor=W)
    tree1.heading('Date of Buying', text='Date of Buying', anchor=W)
    tree1.heading('Ref No', text='Ref No', anchor=W)
    
    tree1.pack(fill=X, pady=20, expand=YES)

    # Adding Scrollbar
    scrollbar = Scrollbar()
    scrollbar.config(command=tree1.yview)

    iid_number1 = 1
    sr_no1 = 1
    buying_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")
    for i in range(0, len(buying_details_df)):
        tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, buying_details_df.Buyer_Name.to_list()[i], buying_details_df.Car_Name.to_list()[i], buying_details_df.Model.to_list()[i], buying_details_df.Year.to_list()[i], buying_details_df.Cost_Price.to_list()[i], buying_details_df.Selling_Price.to_list()[i], buying_details_df.Amount_Paid.to_list()[i], buying_details_df.Date_of_Buying.to_list()[i], buying_details_df.Ref_No.to_list()[i]))
        iid_number1+=1
        sr_no1+=1
    
    f11 = Frame(show_client_root, borderwidth=1, bg="#001020")
    f11.pack(padx=100)

    def search_but_func():
        car_name = car_name_var.get()
        model = model_var.get()

        try:
            if car_name=='Select Car' and model=='Select Model' and year_var.get()=='Select Year' and client_name_var.get()=='Select Buyer':
                iid_number1 = 1
                sr_no1 = 1

                for i in range(0, len(buyer_details_df)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, buyer_details_df.Buyer_Name.to_list()[i], buyer_details_df.Car_Name.to_list()[i], buyer_details_df.Model.to_list()[i], buyer_details_df.Year.to_list()[i], buyer_details_df.Cost_Price.to_list()[i], buyer_details_df.Selling_Price.to_list()[i], buyer_details_df.Amount_Paid.to_list()[i], buyer_details_df.Date_of_Buying.to_list()[i], buyer_details_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                # tkinter.messagebox.showerror("Please Select Car/Model/Year", "Please Select Car/Model/Year")

            elif model=='Select Model' and year_var.get()=='Select Year' and client_name_var.get()=='Select Buyer':
                required_buyer_result = buyer_details_df[buyer_details_df.Car_Name == car_name]

                iid_number1 =1
                sr_no1 = 1

                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_buyer_result)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_buyer_result.Buyer_Name.to_list()[i], required_buyer_result.Car_Name.to_list()[i], required_buyer_result.Model.to_list()[i], required_buyer_result.Year.to_list()[i], required_buyer_result.Cost_Price.to_list()[i], required_buyer_result.Selling_Price.to_list()[i], required_buyer_result.Amount_Paid.to_list()[i], required_buyer_result.Date_of_Buying.to_list()[i], required_buyer_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                
            elif year_var.get()=='Select Year' and client_name_var.get()=='Select Buyer':

                required_car_result = buyer_details_df[buyer_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_model_result)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_model_result.Buyer_Name.to_list()[i], required_model_result.Car_Name.to_list()[i], required_model_result.Model.to_list()[i], required_model_result.Year.to_list()[i], required_model_result.Cost_Price.to_list()[i], required_model_result.Selling_Price.to_list()[i], required_model_result.Amount_Paid.to_list()[i], required_model_result.Date_of_Buying.to_list()[i], required_model_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1

            elif client_name_var.get()=='Select Buyer':

                year = int(year_var.get())

                required_car_result = buyer_details_df[buyer_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]
                search_result_df = required_model_result[required_model_result.Year == year]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(search_result_df)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, search_result_df.Buyer_Name.to_list()[i], search_result_df.Car_Name.to_list()[i], search_result_df.Model.to_list()[i], search_result_df.Year.to_list()[i], search_result_df.Cost_Price.to_list()[i], search_result_df.Selling_Price.to_list()[i], search_result_df.Amount_Paid.to_list()[i], search_result_df.Date_of_Buying.to_list()[i], search_result_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1

            else:
                year = int(year_var.get())

                required_car_result = buyer_details_df[buyer_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]
                required_year_result = required_model_result[required_model_result.Year == year]
                search_result_df = required_year_result[required_year_result.Buyer_Name == client_name_var.get()]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(search_result_df)):
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, search_result_df.Buyer_Name.to_list()[i], search_result_df.Car_Name.to_list()[i], search_result_df.Model.to_list()[i], search_result_df.Year.to_list()[i], search_result_df.Cost_Price.to_list()[i], search_result_df.Selling_Price.to_list()[i], search_result_df.Amount_Paid.to_list()[i], search_result_df.Date_of_Buying.to_list()[i], search_result_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                
        except Exception as error:
            iid_number1 = 1
            sr_no1 = 1
            buying_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")
            for i in tree1.get_children():
                    tree1.delete(i)
            for i in range(0, len(buying_details_df)):
                tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, buying_details_df.Buyer_Name.to_list()[i], buying_details_df.Car_Name.to_list()[i], buying_details_df.Model.to_list()[i], buying_details_df.Year.to_list()[i], buying_details_df.Cost_Price.to_list()[i], buying_details_df.Selling_Price.to_list()[i], buying_details_df.Amount_Paid.to_list()[i], buying_details_df.Date_of_Buying.to_list()[i], buying_details_df.Ref_No.to_list()[i]))
                iid_number1+=1
                sr_no1+=1


    def view_but_func():
        global selected_ref_no

        try:

            selected = tree1.focus()
            selected_item = tree1.item(selected)

            selected_ref_no = int(selected_item['values'][9])

            show_client_root.destroy()

            view_buyer_details()

        except Exception as error:
            tkinter.messagebox.showerror("Please Select Car from the Table", "Please Select Car from the Table")

    def pending_payment_func():
        
        iid_number1 =1
        sr_no1 = 1

        for i in tree1.get_children():
            tree1.delete(i)
        for i in range(0, len(buyer_details_df)):
            pending_amount = int(buyer_details_df.Selling_Price.to_list()[i]) - int(buyer_details_df.Amount_Paid.to_list()[i])
            if pending_amount!=0:
                tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, buyer_details_df.Buyer_Name.to_list()[i], buyer_details_df.Car_Name.to_list()[i], buyer_details_df.Model.to_list()[i], buyer_details_df.Year.to_list()[i], buyer_details_df.Cost_Price.to_list()[i], buyer_details_df.Selling_Price.to_list()[i], buyer_details_df.Amount_Paid.to_list()[i], buyer_details_df.Date_of_Buying.to_list()[i], buyer_details_df.Ref_No.to_list()[i]))
                iid_number1+=1
                sr_no1+=1

    def back_but_func():
        show_client_root.destroy()
        main_menu_window()

    search_but = Button(f11, text="Search Results", font=('Arial Black', 10), bg='#fc7ced', command=search_but_func).grid(row=1, column=1)
    view_but = Button(f11, text="View Buyer Details", font=('Arial Black', 10), bg='#8fd149', command=view_but_func).grid(row=1, column=2, padx=50)
    pending_payment_but = Button(f11, text="Pending Payment", font=('Arial Black', 10), bg='#00fff2', command=pending_payment_func).grid(row=1, column=3)
    back_but = Button(f11, text="Back", font=('Arial Black', 10), bg='#fcca5d', command=back_but_func).grid(row=1, column=4, padx=50)
    

    show_client_root.mainloop()


def view_buyer_details():

    view_client_details_root = Tk()
    view_client_details_root.geometry("1366x695-0+0")
    view_client_details_root.title("Login - Speed Up Billing Software")
    view_client_details_root.configure(bg="#001020")
    view_client_details_root.iconbitmap('speed_up_logo.ico')

    # Loading Car Details Df
    try:
        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Buyer_Name":[],
            "Address":[],
            "Mobile_No":[],
            "Email":[],
            "Cost_Price":[],
            "Selling_Price":[],
            "Amount_Paid":[],
            "Profit":[],
            "Mode_of_Payment":[],
            "Date_of_Buying":[],
            "Ref_No":[],
            "Aadhar_Card":[],
            "Pan_Card":[],
            "Car_Insurance":[],
            "Reciept":[],
            "Insurance_issue_date":[],
            "Insurance_expiry_date":[]
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv")

        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")


    f0 = Frame(view_client_details_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Buyer Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)


    f1 = Frame(view_client_details_root, borderwidth=1, bg='#001020')
    f1.pack(pady=40)

    car_name_var = StringVar()
    ref_sort_df = buyer_details_df[buyer_details_df.Ref_No == selected_ref_no]
    car_name_var.set(ref_sort_df.Car_Name.to_list()[0])
    
    car_name_label = Label(f1, text='Car Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    car_name_entry = Label(f1, textvariable=car_name_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=2)

    f2 = Frame(f1, borderwidth=1, bg='#001020')
    f2.grid(row=1, column=3, padx=20)
    
    model_var = StringVar()
    model_var.set(ref_sort_df.Model.to_list()[0])

    model_label = Label(f2, text='Model: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    model_entry = Label(f2, textvariable=model_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=2)
    
    year_var = StringVar()
    year_var.set(ref_sort_df.Year.to_list()[0])
    year_label = Label(f1, text='Year: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=5)
    year_entry = Label(f1, textvariable=year_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=1, column=6)
    
    client_name_var = StringVar()
    client_name_var.set(ref_sort_df.Buyer_Name.to_list()[0])
    client_name_label = Label(f1, text='Client Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    client_name_entry = Label(f1, textvariable=client_name_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=4, column=2)
    
    address_var = StringVar()
    address_var.set(ref_sort_df.Address.to_list()[0])
    address_label = Label(f1, text='Address: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    address_entry = Label(f1, textvariable=address_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=5, column=2)
    
    mobile_no_var = StringVar()
    mobile_no_var.set(ref_sort_df.Mobile_No.to_list()[0])
    mobile_no_label = Label(f1, text='Mobile No: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    mobile_no_entry = Label(f1, textvariable=mobile_no_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=6, column=2)
    
    email_var = StringVar()
    email_var.set(ref_sort_df.Email.to_list()[0])
    email_label = Label(f1, text='Email: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    email_entry = Label(f1, textvariable=email_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=7, column=2)
    
    cost_price_var = StringVar()
    cost_price_var.set(ref_sort_df.Cost_Price.to_list()[0])
    cost_price_label = Label(f1, text='Cost Price: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=8, column=1)
    cost_price_entry = Label(f1, textvariable=cost_price_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=8, column=2)
    
    selling_price_var = StringVar()
    selling_price_var.set(ref_sort_df.Selling_Price.to_list()[0])
    selling_price_label = Label(f1, text='Selling Price: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=9, column=1)
    selling_price_entry = Label(f1, textvariable=selling_price_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=9, column=2)
    
    profit_var = StringVar()
    profit_var.set(ref_sort_df.Profit.to_list()[0])
    profit_label = Label(f1, text='Profit: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=10, column=1)
    profit_entry = Label(f1, textvariable=profit_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=10, column=2)
    
    amount_paid_var = StringVar()
    amount_paid_var.set(ref_sort_df.Amount_Paid.to_list()[0])
    amount_paid_label = Label(f1, text='Amount Paid: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=11, column=1)
    amount_paid_entry = Label(f1, textvariable=amount_paid_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=11, column=2)
    
    mode_of_payment_var = StringVar()
    mode_of_payment_var.set(ref_sort_df.Mode_of_Payment.to_list()[0])
    mode_of_payment_label = Label(f1, text='Mode of Payment: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=12, column=1)
    mode_of_payment_entry = Label(f1, textvariable=mode_of_payment_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=12, column=2)
    
    pending_amount = int(ref_sort_df.Selling_Price.to_list()[0]) - int(ref_sort_df.Amount_Paid.to_list()[0])
    pending_amount_var = StringVar()
    pending_amount_var.set(pending_amount)
    pending_amount_label = Label(f1, text='Pending Amount: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=13, column=1)
    pending_amount_entry = Label(f1, textvariable=pending_amount_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=13, column=2)
    
    date_of_buying_var = StringVar()
    date_of_buying_var.set(ref_sort_df.Date_of_Buying.to_list()[0])
    date_of_buying_label = Label(f1, text='Date of Buying: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=14, column=1)
    date_of_buying_entry = Label(f1, textvariable=date_of_buying_var, bg='#001020', fg='#56f585', font=('Berlin Sans FB Demi',15)).grid(row=14, column=2)
    
    def view_aadhar_card():
        try:
            aadhar_card_view_path = ref_sort_df.Aadhar_Card.to_list()[0]
            startfile(aadhar_card_view_path)
        except Exception as error:
            tkinter.messagebox.showerror("Aadhar Card Not Uploaded", "Aadhar Card Not Uploaded")

    def view_pan_card():
        try:
            pan_card_view_path = ref_sort_df.Pan_Card.to_list()[0]
            startfile(pan_card_view_path)
        except Exception as error:
            tkinter.messagebox.showerror("Pan Card Not Uploaded", "Pan Card Not Uploaded")

    def view_car_insurance():
        try:
            car_insurance_view_path = ref_sort_df.Car_Insurance.to_list()[0]
            startfile(car_insurance_view_path)
        except Exception as error:
            tkinter.messagebox.showerror("Car Insurance Not Uploaded", "Car Insurance Not Uploaded")

    def view_reciept():
        try:
            reciept_view_path = ref_sort_df.Reciept.to_list()[0]
            startfile(reciept_view_path)
        except Exception as error:
            tkinter.messagebox.showerror("Payment Proof/Reciept Not Uploaded", "Payment Proof/Reciept Not Uploaded")

    f5 = Frame(view_client_details_root, borderwidth=1, bg='#001020')
    f5.pack(pady=10)

    aadhar_card_but = Button(f5, text="View Aadhar Card", font=('Arial Black', 10), bg='#ff82ae', command=view_aadhar_card).grid(row=1, column=1)
    pan_card_but = Button(f5, text="View Pan Card", font=('Arial Black', 10), bg='#f982ff', command=view_pan_card).grid(row=1, column=2, padx=50)
    car_insurance_card_but = Button(f5, text="View Car Insurance", font=('Arial Black', 10), bg='#f982ff', command=view_car_insurance).grid(row=1, column=3, padx=50)
    reciept_but = Button(f5, text="View Payment Proof/Reciept", font=('Arial Black', 10), bg='#f982ff', command=view_reciept).grid(row=1, column=4, padx=50)
    
    def back_but_func():
        view_client_details_root.destroy()
        show_buyer_details()

    def delete_car():
        ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Delete Buyer Record/Details ??")
        if ans==True:
            view_client_details_root.destroy()
            delete_buyer_details_login()
        else:
            pass

    def edit_car_details_func():
        ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Edit Buyer Record/Details ??")
        if ans==True:
            view_client_details_root.destroy()
            edit_buyer_details()
        else:
            pass

    f4 = Frame(view_client_details_root, borderwidth=1, bg='#001020')
    f4.pack(pady=10)

    delete_but = Button(f4, text="Delete Buyer Details", font=('Arial Black', 10), bg='#fa968e', command=delete_car).grid(row=1, column=1)
    edit_car_but = Button(f4, text="Edit Buyer Details", font=('Arial Black', 10), bg='#8efacd', command=edit_car_details_func).grid(row=1, column=2, padx=50)
    back_but = Button(f4, text="Back", font=('Arial Black', 10), bg='#fcca5d', command=back_but_func).grid(row=1, column=3)

    view_client_details_root.mainloop()


def delete_buyer_details_login():

    def authentication():
        if username_var.get()==user_id and password_var.get()==password:
            ans = tkinter.messagebox.askyesno("Are You Sure??", "Are you sure you want to Delete Buyer Record/Details ??")
            if ans==True:
                # Deletion Code Here
                buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")

                ref_sort_df = buyer_details_df[buyer_details_df.Ref_No == selected_ref_no]
                aadhar_card_view_path = ref_sort_df.Aadhar_Card.to_list()[0]
                pan_card_view_path = ref_sort_df.Pan_Card.to_list()[0]
                car_insurance_view_path = ref_sort_df.Car_Insurance.to_list()[0]
                reciept_view_path = ref_sort_df.Reciept.to_list()[0]
                

                try:
                    os.remove(aadhar_card_view_path)
                except Exception as error:
                    pass
                
                try:
                    os.remove(pan_card_view_path)
                except Exception as error:
                    pass
                
                try:
                    os.remove(car_insurance_view_path)
                except Exception as error:
                    pass
                
                try:
                    os.remove(reciept_view_path)
                except Exception as error:
                    pass
                
                index_names = buyer_details_df[buyer_details_df['Ref_No'] == int(selected_ref_no)].index
                
                buyer_details_df.drop(index_names, inplace = True)
                buyer_details_df.to_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv")

                tkinter.messagebox.showinfo("Buyer Details Deleted Successfully", "Buyer Details Deleted Successfully ...")

                login_root.destroy()
                show_buyer_details()
            else:
                tkinter.messagebox.showinfo("Client Details Not Deleted", "Client Details Not Deleted !!!!!!")
                login_root.destroy()
                show_client_details()
        else:
            tkinter.messagebox.showerror("Authentication Unsuccessful", "Incorrect User ID or Password")

    def authentication_bind(event):
        authentication()

    def back_but_func():
        login_root.destroy()
        show_buyer_details()

    login_root = Tk()
    login_root.geometry("1366x695-0+0")
    login_root.title("Login - Speed Up Billing Software")
    login_root.configure(bg="#315b82")
    login_root.iconbitmap('speed_up_logo.ico')

    # Adding Create Account Image
    f1 = Frame(login_root, borderwidth=1, bg="#315b82")
    f1.pack(pady=50)

    login_photo = PhotoImage(file='login_logo.png')
    login_image = Label(f1, image=login_photo, bg="#315b82").pack(pady=10)
    login_text = Label(f1, text="Login to Delete Buyer Details", font=('Arial Black', 25), bg="#315b82", fg="#ebde4d").pack(padx=50)

    f2 = Frame(login_root, borderwidth=1, bg="#315b82")
    f2.pack(pady=20)

    username_var = StringVar()
    password_var = StringVar()

    user_label = Label(f2, text="User ID : ", font=('Arial Black', 20), bg="#315b82", fg="white").grid(row=1, column=1, padx=10)
    pass_label = Label(f2, text="Password : ", font=('Arial Black', 20), bg="#315b82", fg="white").grid(row=2, column=1)


    user_entry = Entry(f2, textvariable=username_var, font=('comicsansms', 15))
    user_entry.grid(row=1, column=2)
    pass_entry = Entry(f2, textvariable=password_var, font=('comicsansms', 15), show="*").grid(row=2, column=2)

    user_entry.focus()
    
    case_sensitive_label = Label(f2, text="  (Case Sensitive)", font=('Arial', 13), bg="#315b82", fg="yellow").grid(row=1, column=3)
    case_sensitive_label = Label(f2, text="  (Case Sensitive)", font=('Arial', 13), bg="#315b82", fg="yellow").grid(row=2, column=3)

    f3 = Frame(login_root, borderwidth=1, bg="#315b82")
    f3.pack(pady=40)

    login_but = Button(f3, text="Login", font=('Arial Black', 15), bg='#9df760', command=authentication)
    login_but.pack(pady=20)

    back_but = Button(f3, text="Back", font=('Arial Black', 15), bg='#fae88e', command=back_but_func)
    back_but.pack(pady=20)

    # Binding Enter Key
    login_root.bind('<Return>',authentication_bind)

    login_root.mainloop()


def edit_buyer_details():

    show_car_root = Tk()
    show_car_root.geometry("1366x695-0+0")
    show_car_root.title("Login - Speed Up Billing Software")
    show_car_root.configure(bg="#001020")
    show_car_root.iconbitmap('speed_up_logo.ico')

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Basic_Cost": [],
            "Tire_Cost": [],
            "Battery": [],
            "Denting_Painting_Cost": [],
            "Other_Expenses": [],
            "Insurance_issue_date": [],
            "Insurance_expiry_date": [],
            "Date_of_Entry": [],
            "Ref_No": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    f0 = Frame(show_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Select Car', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    # Adding Filter Search Title
    f2 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f2.pack(fill=BOTH, padx=100, pady=0)

    title1_label = Label(f2, text='Filter Search:', bg='#001020', fg='#f0b754', font=('Berlin Sans FB Demi',20)).grid(row=1, column=1, padx=0, pady=20)
    title2_label = Label(f2, text='', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',10)).grid(row=1, column=2)
    

    def car_box_update(event):
        global model_list, car1_selected

        car_selected = event.widget.get()
        car1_selected = car_selected
        if car_selected!="Select Car":

            # car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()

            model_list = car_details_df[car_details_df.Car_Name==car_selected].drop_duplicates(subset = ["Model"]).Model.to_list()
            model_list.insert(0, "Select Model")
            model_box['values'] = model_list
    
    def model_box_update(event):
        global year_list

        model_selected = event.widget.get()
        if model_selected!="Select Model":
            year_list = car_details_df[car_details_df.Car_Name==car1_selected][car_details_df.Model==model_selected].drop_duplicates(subset = ["Year"]).Year.to_list()
            year_list.insert(0, "Select Year")
            year_box['values'] = year_list


    # Adding Search Options -------- Starts Here

    # ------ Car Name Combobox --------------
    f10 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f10.pack(fill=BOTH, padx=100)

    f3 = Frame(f10, borderwidth=1, bg="#001020")
    f3.grid(row=1, column=1)

    car_name_label = Label(f3, text='Car Name: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    car_name_list = car_details_df.drop_duplicates(subset = ["Car_Name"]).Car_Name.to_list()
    car_name_list.insert(0, "Select Car")

    car_name_var = StringVar()
    car_name_var.set(car_name_list[0])

    car_box = ttk.Combobox(f3, width=20, textvariable=car_name_var)
    car_box['values'] = car_name_list
    car_box.grid(row=1, column=2)
    car_box.current(0)
    car_box.bind("<<ComboboxSelected>>", car_box_update)

    # ------ Model Combobox ----------------
    f4 = Frame(f3, borderwidth=1, bg="#001020")
    f4.grid(row=1, column=3, padx=20)

    model_label = Label(f4, text='Model: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    model_list = []
    model_list.insert(0, "Select Model")

    model_var = StringVar()
    model_var.set(model_list[0])

    model_box = ttk.Combobox(f4, width=20, textvariable=model_var)
    model_box['values'] = model_list
    model_box.grid(row=1, column=2)
    model_box.current(0)
    model_box.bind("<<ComboboxSelected>>", model_box_update)


    # ------ Year Combobox ----------------
    f5 = Frame(f3, borderwidth=1, bg="#001020")
    f5.grid(row=1, column=4)

    year_label = Label(f5, text='Year: ', font='comicsansms 13 bold', bg='#001020', fg='white').grid(row=1, column=1)

    year_list = []
    year_list.insert(0, "Select Year")

    year_var = StringVar()
    year_var.set(year_list[0])

    year_box = ttk.Combobox(f5, width=20, textvariable=year_var)
    year_box['values'] = year_list
    year_box.grid(row=1, column=2)
    year_box.current(0)
    

    # Adding Search Options -------- Ends Here

    f1 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f1.pack(fill=BOTH, padx=100, pady=50)

    # ------------Treeview for Displaying Cart Items and its Details---------------------

    tree1 = ttk.Treeview(f1, selectmode="extended", height=10)
    # Column names of Treeview
    tree1['columns'] = ('Sr', 'Name', 'Model', 'Year', 'Total Cost', 'Insurance Issue Date', 'Insurance Expiry Date', 'Date of Entry', 'Ref_No')

    # Adding Columns
    tree1.column('#0', width=0, stretch=NO)
    tree1.column('Sr', anchor=W, width=30, minwidth=0, stretch=NO)
    tree1.column('Name', anchor=W, width=50, minwidth=50)
    tree1.column('Model', anchor=W, width=50, minwidth=50)
    tree1.column('Year', anchor=W, width=50, minwidth=50)
    tree1.column('Total Cost', anchor=W, width=50, minwidth=50)
    tree1.column('Insurance Issue Date', anchor=W, width=50, minwidth=50)
    tree1.column('Insurance Expiry Date', anchor=W, width=50, minwidth=50)
    tree1.column('Date of Entry', anchor=W, width=50, minwidth=50)
    tree1.column('Ref_No', anchor=W, width=50, minwidth=50)
    
    
    # Adding Heading of Columns
    tree1.heading('#0', text='', anchor=W)
    tree1.heading('Sr', text='Sr', anchor=W)
    tree1.heading('Name', text='Name', anchor=W)
    tree1.heading('Model', text='Model', anchor=W)
    tree1.heading('Year', text='Year', anchor=W)
    tree1.heading('Total Cost', text='Total Cost', anchor=W)
    tree1.heading('Insurance Issue Date', text='Insurance Issue Date', anchor=W)
    tree1.heading('Insurance Expiry Date', text='Insurance Expiry Date', anchor=W)
    tree1.heading('Date of Entry', text='Date of Entry', anchor=W)
    tree1.heading('Ref_No', text='Ref_No', anchor=W)
    
    tree1.pack(fill=X, pady=20, expand=YES)

    # Adding Scrollbar
    scrollbar = Scrollbar()
    scrollbar.config(command=tree1.yview)

    iid_number1 = 1
    sr_no1 = 1
    car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")
    for i in range(0, len(car_details_df)):
        total_cost_1 = int(car_details_df.Basic_Cost.to_list()[i]) + car_details_df.Tire_Cost.to_list()[i] + car_details_df.Battery.to_list()[i]+ car_details_df.Denting_Painting_Cost.to_list()[i] + car_details_df.Other_Expenses.to_list()[i]
        tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, car_details_df.Car_Name.to_list()[i], car_details_df.Model.to_list()[i], car_details_df.Year.to_list()[i], total_cost_1, car_details_df.Insurance_issue_date.to_list()[i], car_details_df.Insurance_expiry_date.to_list()[i], car_details_df.Date_of_Entry.to_list()[i], car_details_df.Ref_No.to_list()[i]))
        iid_number1+=1
        sr_no1+=1
    
    f11 = Frame(show_car_root, borderwidth=1, bg="#001020")
    f11.pack(padx=100)

    def search_but_func():
        car_name = car_name_var.get()
        model = model_var.get()

        try:
            if car_name=='Select Car' and model=='Select Model' and year_var.get()=='Select Year':
                iid_number1 = 1
                sr_no1 = 1

                for i in range(0, len(car_details_df)):
                    total_cost_1 = int(car_details_df.Basic_Cost.to_list()[i]) + car_details_df.Tire_Cost.to_list()[i] + car_details_df.Battery.to_list()[i]+ car_details_df.Denting_Painting_Cost.to_list()[i] + car_details_df.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, car_details_df.Car_Name.to_list()[i], car_details_df.Model.to_list()[i], car_details_df.Year.to_list()[i], total_cost_1, car_details_df.Insurance_issue_date.to_list()[i], car_details_df.Insurance_expiry_date.to_list()[i], car_details_df.Date_of_Entry.to_list()[i], car_details_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                # tkinter.messagebox.showerror("Please Select Car/Model/Year", "Please Select Car/Model/Year")

            elif model=='Select Model' and year_var.get()=='Select Year':
                required_car_result = car_details_df[car_details_df.Car_Name == car_name]

                iid_number1 =1
                sr_no1 = 1

                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_car_result)):
                    total_cost_1 = int(required_car_result.Basic_Cost.to_list()[i]) + required_car_result.Tire_Cost.to_list()[i] + required_car_result.Battery.to_list()[i]+ required_car_result.Denting_Painting_Cost.to_list()[i] + required_car_result.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_car_result.Car_Name.to_list()[i], required_car_result.Model.to_list()[i], required_car_result.Year.to_list()[i], total_cost_1, required_car_result.Insurance_issue_date.to_list()[i], required_car_result.Insurance_expiry_date.to_list()[i], required_car_result.Date_of_Entry.to_list()[i], required_car_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
                
            elif year_var.get()=='Select Year':

                required_car_result = car_details_df[car_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(required_model_result)):
                    total_cost_1 = int(required_model_result.Basic_Cost.to_list()[i]) + required_model_result.Tire_Cost.to_list()[i] + required_model_result.Battery.to_list()[i]+ required_model_result.Denting_Painting_Cost.to_list()[i] + required_model_result.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, required_model_result.Car_Name.to_list()[i], required_model_result.Model.to_list()[i], required_model_result.Year.to_list()[i], total_cost_1, required_model_result.Insurance_issue_date.to_list()[i], required_model_result.Insurance_expiry_date.to_list()[i], required_model_result.Date_of_Entry.to_list()[i], required_model_result.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
            else:
                year = int(year_var.get())

                required_car_result = car_details_df[car_details_df.Car_Name == car_name]
                required_model_result = required_car_result[required_car_result.Model == model]
                search_result_df = required_model_result[required_model_result.Year == year]

                iid_number1 =1
                sr_no1 = 1
                for i in tree1.get_children():
                    tree1.delete(i)
                for i in range(0, len(search_result_df)):
                    total_cost_1 = int(search_result_df.Basic_Cost.to_list()[i]) + search_result_df.Tire_Cost.to_list()[i] + search_result_df.Battery.to_list()[i]+ search_result_df.Denting_Painting_Cost.to_list()[i] + search_result_df.Other_Expenses.to_list()[i]
                    tree1.insert(parent='', index='end', iid=iid_number1, text='', values=(sr_no1, search_result_df.Car_Name.to_list()[i], search_result_df.Model.to_list()[i], search_result_df.Year.to_list()[i], total_cost_1, search_result_df.Insurance_issue_date.to_list()[i], search_result_df.Insurance_expiry_date.to_list()[i], search_result_df.Date_of_Entry.to_list()[i], search_result_df.Ref_No.to_list()[i]))
                    iid_number1+=1
                    sr_no1+=1
        except Exception as error:
            pass


    def next_func():
        global selected_ref_no_1

        # try:
        selected = tree1.focus()
        selected_item = tree1.item(selected)

        selected_ref_no_1 = int(selected_item['values'][8])
        show_car_root.destroy()

        edit_buyer_details_window()
        # except Exception as error:
        #     print(error)
        #     tkinter.messagebox.showerror("Please Select Car from the Table", "Please Select Car from the Table")

    def back_but_func():
        show_car_root.destroy()
        main_menu_window()

    search_but = Button(f11, text="Search Results", font=('Arial Black', 10), bg='#fc7ced', command=search_but_func).grid(row=1, column=1)
    next_but = Button(f11, text="Next", font=('Arial Black', 10), bg='#8fd149', command=next_func).grid(row=1, column=2, padx=50)
    back_but = Button(f11, text="Back", font=('Arial Black', 10), bg='#fcca5d', command=back_but_func).grid(row=1, column=3)
    

    show_car_root.mainloop()


def edit_buyer_details_window():
    global selected_issue_date, selected_expiry_date


    def date_of_inquiry_func():
        selected_date_of_inquiry = date_of_inquiry_calendar.get_date()
        date_of_inquiry_var.set(selected_date_of_inquiry)

    def edit_buyer_func():


        client_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\client_details_file.csv", index_col="Unnamed: 0")

        ref_sort_df_1 = car_details_df[car_details_df.Ref_No == selected_ref_no_1]

        car_name =  ref_sort_df_1.Car_Name.to_list()[0]
        model = ref_sort_df_1.Model.to_list()[0]
        year = ref_sort_df_1.Year.to_list()[0]
        buyer_name = buyer_name_var.get()
        address = address_var.get()
        mobile_no = mobile_no_var.get()
        email = email_var.get()
        cost_price = int(ref_sort_df_1.Basic_Cost.to_list()[0]) + ref_sort_df_1.Tire_Cost.to_list()[0] + ref_sort_df_1.Battery.to_list()[0]+ ref_sort_df_1.Denting_Painting_Cost.to_list()[0] + ref_sort_df_1.Other_Expenses.to_list()[0]
        selling_price = int(selling_price_var.get())
        amount_paid = int(amount_paid_var.get())
        profit = int(selling_price - cost_price)
        mode_of_payment = mode_of_payment_var.get()
        date_of_buying = date_of_inquiry_var.get()
        insurance_issue_date = ref_sort_df.Insurance_issue_date.to_list()[0]
        insurance_expiry_date = ref_sort_df.Insurance_expiry_date.to_list()[0]

        
        pre_ref_no = ref_sort_df.Ref_No.to_list()[0]

        # print("Pre Ref No: ", pre_ref_no)

        if buyer_name!="" and address!="" and mobile_no!="" and amount_paid_var.get()!="" and selling_price_var.get()!="" and mode_of_payment!="" and date_of_buying!="":
            # Checking All Entry Values are Filled
            if buyer_name=="" and address=="" and mobile_no=="" and amount_paid_var.get()=="" and selling_price_var.get()=="" and mode_of_payment=="" and date_of_buying=="":
                tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")
            else:
                
                new_aadhar_path = pre_aadhar_path
                new_pan_path = pre_pan_path
                new_car_insurance_path = pre_car_insurance_path
                new_reciept_path = pre_reciept_path
                try:
                    if pre_aadhar_path!=aadhar_card_filename_path:
                        
                        os.remove(pre_aadhar_path)
                        shutil.copy(aadhar_card_filename_path, filepath_1)

                        split_tup_1 = os.path.splitext(aadhar_card_filename_path)
                        aadhar_file_ext = split_tup_1[1]
                        aadhar_dst_file = os.path.join(filepath_1, aadhar_card_filename)
                        aadhar_new_dst_file_name = os.path.join(filepath_1, f'ref_{pre_ref_no}{aadhar_file_ext}')
                        new_aadhar_path = aadhar_new_dst_file_name
                        os.rename(aadhar_dst_file, aadhar_new_dst_file_name)
                except Exception as error:
                    pass    

                        
                try:
                    if pre_pan_path!=pan_card_filename_path:                            
                        
                        os.remove(pre_pan_path)
                        shutil.copy(pan_card_filename_path, filepath_2)

                        split_tup_2 = os.path.splitext(pan_card_filename_path)
                        pan_file_ext = split_tup_2[1]
                        pan_dst_file = os.path.join(filepath_2, pan_card_filename)
                        pan_new_dst_file_name = os.path.join(filepath_2, f'ref_{pre_ref_no}{pan_file_ext}')
                        new_pan_path = pan_new_dst_file_name
                        os.rename(pan_dst_file, pan_new_dst_file_name)
                except Exception as error:
                    pass
                
                try:
                    if pre_car_insurance_path!=car_insurance_filename_path:                            
                        
                        os.remove(pre_car_insurance_path)
                        shutil.copy(car_insurance_filename_path, filepath_2)

                        split_tup_2 = os.path.splitext(car_insurance_filename_path)
                        car_insurance_file_ext = split_tup_2[1]
                        car_insurance_dst_file = os.path.join(filepath_2, car_insurance_filename)
                        car_insurance_new_dst_file_name = os.path.join(filepath_2, f'ref_{pre_ref_no}{car_insurance_file_ext}')
                        new_car_insurance_path = car_insurance_new_dst_file_name
                        os.rename(car_insurance_dst_file, car_insurance_new_dst_file_name)
                except Exception as error:
                    pass

                try:
                    if pre_reciept_path!=reciept_filename_path:                            
                        
                        os.remove(pre_pan_path)
                        shutil.copy(reciept_filename_path, filepath_2)

                        split_tup_4 = os.path.splitext(reciept_filename_path)
                        reciept_file_ext = split_tup_4[1]
                        reciept_dst_file = os.path.join(filepath_4, reciept_filename)
                        reciept_new_dst_file_name = os.path.join(filepath_4, f'ref_{pre_ref_no}{reciept_file_ext}')
                        new_reciept_path = reciept_new_dst_file_name
                        os.rename(reciept_dst_file, reciept_new_dst_file_name)
                except Exception as error:
                    pass

                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Car_Name'] = car_name
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Model'] = model
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Year'] = year
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Buyer_Name'] = buyer_name
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Address'] = address
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Mobile_No'] = mobile_no
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Email'] = email
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Cost_Price'] = cost_price
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Selling_Price'] = selling_price
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Amount_Paid'] = amount_paid
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Profit'] = profit
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Mode_of_Payment'] = mode_of_payment
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Date_of_Buying'] = date_of_buying
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Ref_No'] = pre_ref_no
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Aadhar_Card'] = new_aadhar_path
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Pan_Card'] = new_pan_path
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Car_Insurance'] = new_car_insurance_path
                buyer_details_df.loc[buyer_details_df['Ref_No'] == int(selected_ref_no), 'Reciept'] = new_reciept_path

                
                buyer_details_df.to_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv")

                tkinter.messagebox.showinfo("Buyer Details Edited Successfully", "Buyer Details Edited Successfully")
                add_car_root.destroy()
                show_buyer_details()

        else:
            tkinter.messagebox.showerror("Please Fill All Details", "Please Fill All Details")

    def back_but_func():
        add_car_root.destroy()
        show_client_details()


    add_car_root = Tk()
    add_car_root.geometry("1366x695-0+0")
    add_car_root.title("Login - Speed Up Billing Software")
    add_car_root.configure(bg="#001020")
    add_car_root.iconbitmap('speed_up_logo.ico')

    # Loading Buyer Details Df
    try:
        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": [],
            "Buyer_Name":[],
            "Address":[],
            "Mobile_No":[],
            "Email":[],
            "Cost_Price":[],
            "Selling_Price":[],
            "Amount_Paid":[],
            "Profit":[],
            "Mode_of_Payment":[],
            "Date_of_Buying":[],
            "Ref_No":[],
            "Aadhar_Card":[],
            "Pan_Card":[],
            "Car_Insurance":[],
            "Reciept":[],
            "Insurance_issue_date":[],
            "Insurance_expiry_date":[]
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv")

        buyer_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\\buyer_details_file.csv", index_col="Unnamed: 0")

    # Loading Car Details Df
    try:
        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    except Exception as error:
        dict2 = {
            "Car_Name": [],
            "Model": [],
            "Year": []
            }
        empty_csv_df = pd.DataFrame(dict2)
        empty_csv_df.to_csv("D:\Soham_Motors\Software_Files\car_details_file.csv")

        car_details_df = pd.read_csv("D:\Soham_Motors\Software_Files\car_details_file.csv", index_col="Unnamed: 0")

    f0 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f0.pack(pady=10)

    title_label = Label(f0, text='Edit Buyer Details', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=15)

    ref_sort_df = buyer_details_df[buyer_details_df.Ref_No == selected_ref_no]

    f1 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f1.pack(pady=10)
    
    f2 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f2.pack()

    buyer_name_var = StringVar()
    buyer_name_var.set(ref_sort_df.Buyer_Name.to_list()[0])
    buyer_name_label = Label(f2, text='Buyer Name: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=1, column=1)
    buyer_name_entry = Entry(f2, textvariable=buyer_name_var, font=('comicsansms', 15))
    buyer_name_entry.grid(row=1, column=2)
    
    address_var = StringVar()
    address_var.set(ref_sort_df.Address.to_list()[0])
    address_label = Label(f2, text='Address: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=2, column=1)
    address_entry = Entry(f2, textvariable=address_var, font=('comicsansms', 15))
    address_entry.grid(row=2, column=2)
    
    mobile_no_var = StringVar()
    mobile_no_var.set(ref_sort_df.Mobile_No.to_list()[0])
    mobile_no_label = Label(f2, text='Mobile No: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=3, column=1)
    mobile_no_entry = Entry(f2, textvariable=mobile_no_var, font=('comicsansms', 15))
    mobile_no_entry.grid(row=3, column=2)
    
    email_var = StringVar()
    email_var.set(ref_sort_df.Email.to_list()[0])
    email_label = Label(f2, text='Email: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=4, column=1)
    email_entry = Entry(f2, textvariable=email_var, font=('comicsansms', 15))
    email_entry.grid(row=4, column=2)
    
    selling_price_var = StringVar()
    selling_price_var.set(ref_sort_df.Selling_Price.to_list()[0])
    selling_price_label = Label(f2, text='Selling Price: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=5, column=1)
    selling_price_entry = Entry(f2, textvariable=selling_price_var, font=('comicsansms', 15))
    selling_price_entry.grid(row=5, column=2)
    
    amount_paid_var = StringVar()
    amount_paid_var.set(ref_sort_df.Amount_Paid.to_list()[0])
    amount_paid_label = Label(f2, text='Amount Paid: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=6, column=1)
    amount_paid_entry = Entry(f2, textvariable=amount_paid_var, font=('comicsansms', 15))
    amount_paid_entry.grid(row=6, column=2)
    
    mode_of_payment_var = StringVar()
    mode_of_payment_var.set(ref_sort_df.Mode_of_Payment.to_list()[0])
    mode_of_payment_label = Label(f2, text='Mode of Payment: ', bg='#001020', fg='white', font=('Berlin Sans FB Demi',15)).grid(row=7, column=1)
    mode_of_payment_entry = Entry(f2, textvariable=mode_of_payment_var, font=('comicsansms', 15))
    mode_of_payment_entry.grid(row=7, column=2)
    
    def upload_aadhar_card():
        global aadhar_card_filename, pan_card_filename, filepath_1, aadhar_card_filename_path

        filepath_1 = "D:\Soham_Motors\Buyer_Aadhar_Card"
        aadhar_card_filename_path = filedialog.askopenfilename()
        aadhar_card_filename = os.path.split(aadhar_card_filename_path)[1]
        aadhar_card_path.set(aadhar_card_filename)
    
    def upload_pan_card():
        global aadhar_card_filename, pan_card_filename, filepath_2, pan_card_filename_path

        filepath = "D:\Soham_Motors\Buyer_Pan_Card"
        pan_card_filename_path = filedialog.askopenfilename()
        pan_card_filename = os.path.split(pan_card_filename_path)[1]
        pan_card_path.set(pan_card_filename)
    
    def upload_car_insurance():
        global  car_insurance_filename, filepath_2, car_insurance_filename_path

        filepath = "D:\Soham_Motors\Car_Insurance"
        car_insurance_filename_path = filedialog.askopenfilename()
        car_insurance_filename = os.path.split(car_insurance_filename_path)[1]
        car_insurance_path.set(car_insurance_filename)
    
    def upload_reciept():
        global reciept_filename, filepath_2, reciept_filename_path

        filepath = "D:\Soham_Motors\Reciept"
        reciept_filename_path = filedialog.askopenfilename()
        reciept_filename = os.path.split(reciept_filename_path)[1]
        reciept_path.set(reciept_filename)
    
    filepath_1 = "D:\Soham_Motors\Buyer_Aadhar_Card"
    filepath_2 = "D:\Soham_Motors\Buyer_Pan_Card"
    filepath_3 = "D:\Soham_Motors\Car_Insurance"
    filepath_4 = "D:\Soham_Motors\Reciept"
    
    aadhar_card_path = StringVar()
    pan_card_path = StringVar()
    car_insurance_path = StringVar()
    reciept_path = StringVar()
    
    aadhar_card_path.set(ref_sort_df.Aadhar_Card.to_list()[0])
    pan_card_path.set(ref_sort_df.Pan_Card.to_list()[0])
    car_insurance_path.set(ref_sort_df.Car_Insurance.to_list()[0])
    reciept_path.set(ref_sort_df.Reciept.to_list()[0])
    
    pre_aadhar_path = ref_sort_df.Aadhar_Card.to_list()[0]
    pre_pan_path = ref_sort_df.Pan_Card.to_list()[0]
    pre_car_insurance_path = ref_sort_df.Car_Insurance.to_list()[0]
    pre_reciept_path = ref_sort_df.Reciept.to_list()[0]

    upload_aadhar_card_but = Button(f2, text="Upload Aadhar Card", font=('Arial Black', 10), bg='#fcca5d', command=upload_aadhar_card).grid(row=8, column=1, pady=10)
    upload_Pan_card_but = Button(f2, text="Upload Pan Card", font=('Arial Black', 10), bg='#fcca5d', command=upload_pan_card).grid(row=8, column=2, pady=10)
    upload_car_insurance_but = Button(f2, text="Upload Car Insurance", font=('Arial Black', 10), bg='#fcca5d', command=upload_car_insurance).grid(row=8, column=3, pady=10)
    upload_reciept_but = Button(f2, text="Upload Payment Proof/Reciept", font=('Arial Black', 10), bg='#fcca5d', command=upload_reciept).grid(row=8, column=4, pady=10, padx=40)
    
    f3 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f3.pack()

    # Add Calendar
    today = date.today()
    date_of_entry = today.strftime("%d/%m/%Y")
    day_3 = int(date_of_entry[0:2])
    month_3 = int(date_of_entry[3:5])
    year_3 = int(date_of_entry[6:10])

    date_of_inquiry_calendar = Calendar(f3, selectmode = 'day', year = year_3, month = month_3, day = day_3, date_pattern="dd/mm/y")
    date_of_inquiry_calendar.grid(row=1, column=1)
    
    f5 = Frame(f3, borderwidth=1, bg='#001020')
    f5.grid(row=1, column=2, padx=10)

    date_of_inquiry_var = StringVar()
    date_of_inquiry_var.set(ref_sort_df.Date_of_Buying.to_list()[0])
    date_of_inquiry_but = Button(f5, text="Date of Buying Car", font=('Arial Black', 10), bg='#fcca5d', command=date_of_inquiry_func).grid(row=1, column=1, pady=10)
    
    date_of_inquiry_label = Label(f5, textvariable=date_of_inquiry_var, bg='#001020', fg='white', font=('Arial Black',10)).grid(row=1, column=2)
    
    f4 = Frame(add_car_root, borderwidth=1, bg='#001020')
    f4.pack(pady=20)

    add_but = Button(f4, text="Add", font=('Arial Black', 13), bg='#5eff8c', command=edit_buyer_func).grid(row=1, column=1, padx=30)
    back_but = Button(f4, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).grid(row=1, column=2)
    
    add_car_root.mainloop()


def about_us():
    about_us_root = Tk()
    about_us_root.geometry("1366x695-0+0")
    about_us_root.title("Login - Speed Up Billing Software")
    about_us_root.configure(bg="#001020")
    about_us_root.iconbitmap('speed_up_logo.ico')

    l1 = Label(about_us_root, text='About Us', bg='#001020', fg='#e7ff5e', font=('Berlin Sans FB Demi',30)).pack(pady=50)

    f1 = Frame(about_us_root, borderwidth=1, bg='#001020')
    f1.pack(pady=100)

    l2 = Label(f1, text='This Software is Made By Soham Mahesh Tamhane', bg='#001020', fg='#00ff88', font=('Berlin Sans FB Demi',20)).pack(pady=10)

    def back_but_func():
        about_us_root.destroy()
        main_menu_window()

    back_but = Button(f1, text="Back", font=('Arial Black', 13), bg='#fcca5d', command=back_but_func).pack(pady=90)
    about_us_root.mainloop()

login_window()
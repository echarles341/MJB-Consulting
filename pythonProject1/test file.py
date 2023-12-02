from tkinter import *
import datetime
X = datetime.datetime.now()
print(X.strftime("%m/%d/%y    %H:%M"))
main = Tk()
main.geometry("700x600")
main.title("Reservation Desk")


#Heading
Label(main,text= "Registration form", bg= "blue",font="ar 12 bold").pack()


def click_book():
    print("Your reservation is confirmed")


def click_submit():
    # Validation
    if Credit_card_number_text == "":
        error0()
    elif Credit_card_number_text < 16:
        error8()
    elif Credit_card_number_text > 16:
        error8()
    else:
        print("Enter your your first name")

    if any(ch.isdigit() for ch in First_name_text):
        error()
    elif First_name_text == "":
        error2()
    elif First_name_text < 2:
        error3()
    elif len(First_name_text) > 32:
        error4()
    else:
        print("Enter your last name")
#    else:
#        Label(main, text="Proceed").place(x=15, y=230)
    if  any(ch.isdigit() for ch in Last_name_text):
        error()
    elif Last_name_text == "":
        error()
    elif Last_name_text < 2:
        error2()
    elif Last_name_text > 32:
        error3()
    else:
        print("Enter your email")
#    else:
#        Label(main, text="Proceed").place(x=15, y=230)
    if Email_address_text == "":
        error5()
    else:
        print("Enter your phone number")
    if Phone_number_text == "":
        error6()
    elif Phone_number_text < 9:
        error3()
    elif Phone_number_text > 10:
        error4()
#    else:
    if len(Reseversation_date_text) == "":
        error7()
    else:
        print("Submitted. you will receive a confirmation of your reservation")

def error0():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="Card cannot be empty", fg="red").pack()

def error():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="Name cannot contain numeric character", fg="red").pack()
def error2():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="Name cannot empty", fg="red").pack()
def error3():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="minimum 3 characters are required", fg="red").pack()
def error4():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="Name cannot contain more than 32 characters", fg="red").pack()

def error5():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="Email address cannot empty", fg="red").pack()

def error6():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="Phone number cannot empty", fg="red").pack()

def error7():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="Appointment cannot empty", fg="red").pack()

def error8():
    screen1 = Toplevel(main)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text="Verify your credit card number", fg="red").pack()

#To obtain entries from customers
Credit_card_Value = IntVar()
First_name_value = StringVar()
Last_name_value = StringVar()
Email_address_value = StringVar()
Phone_number_value = IntVar()
Reservation_date_value = IntVar()
check_value = IntVar()
check_value_2 = IntVar()

Credit_card_number_text = Credit_card_Value.get()
First_name_text = First_name_value.get()
Last_name_text = Last_name_value.get()
Email_address_text = Email_address_value.get()
Phone_number_text = Phone_number_value.get()
Reseversation_date_text = Reservation_date_value.get()

#Display the fields on the screen

#Customer info (Entry fields labels)
Credit_card = Label(main, text="Credit card number ").place(x=15, y=30)
First_name = Label(main, text="First name ").place(x=15, y= 50)
Last_name = Label(main, text="last name ").place(x=15, y= 70)
Email_address = Label(main, text="Email address ").place(x=15, y= 90)
Phone_number = Label(main, text="Phone number ").place(x=15, y= 110)
Reservation_date = Label(main, text="Reservation date ").place(x=15, y= 130)
checkbutton = Label(main, text="").place(x=15, y= 150)
checkbutton1 = Label(main, text="").place(x=15, y= 170)

#Creating entry fields (Enter data from customers)
Credit_card_entry = Entry(main,textvariable= Credit_card).place(x=+200, y=30)
First_name_entry = Entry(main,textvariable = First_name).place(x=+200, y= 50)
Last_name_entry = Entry(main,textvariable = Last_name).place(x=200, y=70)
Email_address_entry = Entry(main,textvariable = Email_address).place(x=+200, y=90)
Phone_number_entry = Entry(main,textvariable = Phone_number).place(x=+200, y=110)
Reservation_date_entry = Entry(main, textvariable= Reservation_date).place(x=+200, y=130)


#packing entry fields
Entry(main, textvariable= Credit_card_Value)
Entry(main, textvariable= First_name_value)
Entry(main, textvariable= Last_name_value)
Entry(main, textvariable= Email_address_value)
Entry(main, textvariable= Phone_number_value)
Entry(main, textvariable= Reservation_date_value)


#create a check boxes
checkbtn_book = Checkbutton(text="Book", command=click_book,variable=check_value).place(x=+200, y=150)

#Submit_button
Button(text="Submit Reservation", width="15",command = click_submit).place(x=+220, y=180)



mainloop()


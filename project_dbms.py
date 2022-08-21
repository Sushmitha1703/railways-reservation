import sqlite3
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkcalendar import DateEntry

conn = sqlite3.connect('trains.db')
c = conn.cursor()
mydb = sqlite3.connect('trains.db')
cursor = mydb.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS trains_info(
            train_num INT Primary key,
            Name Text,
            src Text,
            src_time Text,
            dest text,
            dest_time Text,
            fare INT)
            """)

'''
c.execute("""Insert into trains_info values
          (12124,'Deccan Queen','Pune','07:15','Mumbai','10:25',385),
          (02702,'HYB CSMT SPL','Pune','13:15','Mumbai','16:55',500),
          (02208,'Latur CSMT Special','Pune','04:15','Mumbai','07:55',455),
          
          (02779,'Goa Express','Pune','04:30','Delhi','06:25',2838),
         (02629,'Sampark Kranti','Pune','09:10','Delhi','11:25',2504),
          (07305,'NZM Link Express','Pune','04:30','Delhi','06:05',2100),
          (12493,'Darshan Express','Pune','05:15','Delhi','05:35',3850),
         (12147,'Nizamuddin Express','Pune','04:10','Delhi','05:10',2038),
          
          (12163,'LTT Chennai Express','Pune','12:10','Chennai','19:45',2383),
          (19420,'ADI Chennai Express','Pune','21:15','Chennai','17:10',2132),
          (11017,'LTT Karaikal Express','Pune','15:35','Chennai','11:38',2300),
         (11014,'CSMT Chennai Express','Pune','18:10','Chennai','16:20',1999),
          (06502,'ADI MAS SPL','Pune','21:15','Chennai','17:10',2085),         
          
          (11091,'Bhuj Pune Express','Mumbai','12:10','Pune','04:35',495),
          (11043,'LTT Madurai Express','Mumbai','12:15','Pune','03:50',495),
          (11049,'Kolhapur Express','Mumbai','03:35','Pune','07:40',565),
          (02297,'Pune Duronto','Mumbai','03:50','Pune','07:10',625),         
          
         (19019,'Dehradun Express','Mumbai','02:17','Delhi','05:25',1440),
          (22655,'Tvc Nzm Express','Mumbai','19:25','Delhi','15:55',1490),
         (12471,'Swaraj Express','Mumbai','19:55','Delhi','16:35',1735),
          (12499,'Darshan Express','Mumbai','21:00','Delhi','17:35',1490),
          (02617,'Mangaldweep Express','Mumbai','12:40','Delhi','13:25',1735),        
          
         (12136,'LTT Chennai Exp','Mumbai','20:30','Chennai','19:45',2383),
         (19400,'ADI Chennai Exp','Mumbai','17:15','Chennai','17:10',2132),
         (11077,'LTT Karaikal Exp','Mumbai','12:35','Chennai','11:38',2300),
         (11041,'CSMT Chennai Exp','Mumbai','14:10','Chennai','16:20',1999),
         (06052,'ADI MAS SPL','Mumbai','17:05','Chennai','17:10',2085),          
          
         (11078,'Jhelum Express','Delhi','10:15','Pune','15:15',1450),
          (12782,'Swarna Jayanthi','Delhi','05:50','Pune','09:15',1930),
         (12148,'NZM KOP Express','Delhi','05:50','Pune','09:15',1625),
          (12780,'Goa Express','Delhi','15:00','Pune','16:20',1400),
          (12494,'Darshan Express','Delhi','21:35','Pune','21:25',1395),       
          
          (22222,'CSMT Rajdhani','Delhi','17:15','Mumbai','11:50',2100),
          (12432,'Trivandrum Rajdhani','Delhi','10:55','Mumbai','04:25',1950),
          (12264,'Pune Duranto Express','Delhi','10:55','Mumbai','05:50',2200),
          (12910,'BDTS Garib Rath','Delhi','15:35','Mumbai','08:10',1890),
          (12952,'Mumbai Rajdhani','Delhi','16:25','Mumbai','08:15',1789),
          
          (16032,'Andaman Express','Delhi','14:15','Chennai','10:10',2900),
          (12462,'Thirukkural Express','Delhi','07:10','Chennai','18:53',3850),
          (12616,'Grand Trunk Express','Delhi','18:40','Chennai','06:20',2850),
          (12622,'Tamil Nadu Express','Delhi','22:30','Chennai','07:10',2910),
          (12434,'Chennai Rajdhani','Delhi','15:55','Chennai','20:40',4210),
          
         (11042,'Mumbai Express','Chennai','12:20','Pune','09:30',1700),
          (11018,'KIK LTT Express','Chennai','21:05','Pune','19:50',1789),
          (11074,'Chennai LTT Express','Chennai','15:50','Pune','11:55',2100),
         (22919,'Mas ADI Humsafar','Chennai','20:30','Pune','16:30',1970),
         (12164,'MAS LTT Express','Chennai','06:45','Pune','02:20',1890),
          
         (19042,'Mumbai Express','Chennai','12:20','Mumbai','12:35',1790),
         (19018,'KIK LTT Express','Chennai','21:05','Mumbai','11:45',1689),
         (19074,'Chennai LTT Express','Chennai','15:50','Mumbai','16:00',2150),
         (29919,'Mas ADI Humsafar','Chennai','20:30','Mumbai','21:05',1938),
         (19164,'MAS LTT Express','Chennai','06:45','Mumbai','06:00',1890),
          
         (16031,'Andaman Express','Chennai','05:15','Delhi','11:00',1910),
         (12615,'Grand Trunk Express','Chennai','19:15','Delhi','06:30',2050),
         (12687,'Dehradun Express','Chennai','10:00','Delhi','20:40',1890),
         (12651,'Sampark Kranti','Chennai','08:05','Delhi','18:00',2200),
         (12621,'Tamil Nadu Express','Chennai','22:00','Delhi','07:05',1990)
           
          """)

'''
c.execute("""CREATE TABLE IF NOT EXISTS Passenger_info(
             train_num Int,
             Name Text,
             Age Int,
             Gender Text,
             Email Text,
             PNR int Primary key
              
           )
            """)


#Main window to enter source, destination
def enter_train_details():
    root = Tk()
    root.title("TRAIN DETAILS")
    traindetail_width = 400
    traindetail_height = 400
 
    # get the screen dimension
    screen2_width = root.winfo_screenwidth()
    screen2_height = root.winfo_screenheight()

    # find the center point
    center2_x = int(screen2_width/2 - traindetail_width / 2)
    center2_y = int(screen2_height/2 - traindetail_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{traindetail_width}x{traindetail_height}+{center2_x}+{center2_y}')

    #Checking values entered
    def check():
        if cmb.get() == cmb1.get():
            messagebox.showinfo(
                "Error", "Source and Destination cannot be same")
        else:
            cmb_value = cmb.get()
            cmb1_value = cmb1.get()
            root.destroy()
            trains10(cmb_value, cmb1_value)

    def goHome():
        root.destroy()
        homepage()

    # Heading
    Heading = Label(root, text="Railway Reservation System",
                    font=30, fg='pink', bg='green', justify='center')
    Heading.place(x=60, y=25)

    # Source
    source = Label(root, text='Source')
    source.place(x=90, y=130)
    # Combobox-Source
    cmb = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    cmb.place(x=180,y=130)

    # Destination
    dest = Label(root, text='Destination')
    dest.place(x=90,y=190)
    # Combobox-Dest
    cmb1 = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    cmb1.place(x=180,y=190)

    # Submit Button
    submit = Button(root, text='Show Trains', command=check,bg="mint cream")
    submit.place(x=80,y=300)

    # Home Button
    homebtn = Button(root, text='Home', command = goHome,bg="mint cream")
    homebtn.place(x=270,y=300)

    root.mainloop()



# Displaying trains for selected src, dest
def trains10(src, dest):
    r= Tk()
    r.geometry('720x455')
    r.title('Train Details')
    treev = ttk.Treeview(r, selectmode ='browse')
  
    # Calling pack method w.r.to treeview
    treev.pack(side ='left')
  
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(r, 
                           orient ="vertical", 
                           command = treev.yview)
  
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')
  
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
  
    # Defining number of columns
    treev["columns"] = ("1", "2", "3", "4","5","6","7")
  
    # Defining heading
    treev['show'] = 'headings'
  
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 120, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    treev.column("4", width = 90, anchor ='c')
    treev.column("5", width = 90, anchor ='c')
    treev.column("6", width = 110, anchor ='c')
    treev.column("7", width = 90, anchor ='c')
  
    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="Train number")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Source")
    treev.heading("4", text ="Source Time")
    treev.heading("5", text ="Destination")
    treev.heading("6", text ="Destination Time")
    treev.heading("7", text ="Fare")
    sql = "Select * from trains_info where src='{}' and dest='{}'".format(src, dest)
    sql1 = "Select count(*) from trains_info where src='{}' and dest='{}'".format(src, dest)
    no = c.execute(sql1)
    for j in no:
        num=j
    Label(r,text="Number of trains available: ").place(x=100,y=50)
    Label(r,text=num).place(x=260,y=50)
    result = c.execute(sql)
    for i in result:
        treev.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4],i[5],i[6]))
    #GO back to main window from train details window
    def goback():
        #print("Return Button clicked")
        r.destroy()
        enter_train_details()

    def bookTicket():
        r.destroy()
        book_a_ticket()

    

    # Return Back Button
    backBtn = Button(r, text="Back", command=goback,bg="mint cream")
    backBtn.place(x=200,y=400)

    #Book Button
    bookBtn = Button(r, text="Book", command=bookTicket,bg="mint cream")
    bookBtn.place(x=400,y=400)
    r.mainloop()
 

def printt():
        messagebox.showinfo('Printed','Print Successfull!')



# Booking a ticket 
def book_a_ticket():

    def cancel():
        root1.destroy()
        
        homepage()
    #Inserting values in Passenger db
    def into_pass():
        def generate_pnr():
            low= 10**(8-1)
            high = (10**8)-1
            return random.randint(low,high)
        name=name_entry.get()
        age=age_entry.get()
        gender=cmb.get()
        email=email_entry.get()
        train_num=train_no_label.get()
        email= email_entry.get()
        date = cal.get_date()
        if len(name)==0 or  age=='0' or gender=='' or email=='' or train_num=='':
            messagebox.showinfo('Error',"Please fill all details!")
        elif name!='' and age=='' and gender=='' and email=='' and train_num=='':
             messagebox.showinfo('Error',"Please fill all details!")
        elif name!='' and age!='' and gender=='' and email=='' and train_num=='':
             messagebox.showinfo('Error',"Please fill all details!")
        elif name!='' and age!='' and gender!='' and email=='' and train_num=='':
            messagebox.showinfo('Error',"Please fill all details!")
        elif name!='' and age!='' and gender!='' and email!='' and train_num=='':
             messagebox.showinfo('Error',"Please enter train number!") 
        elif '@' not in email:
            messagebox.showinfo('Error',"Please enter valid email id!") 
        elif int(age) not in range(1,100):
            messagebox.showinfo('Error','Enter valid Age!')
        
        else: 
            pnr = generate_pnr()
            sql= '''Insert Into Passenger_info Values(%d,'%s',%d,'%s','%s',%d)''' % (int(train_num),name,int(age),gender,email,int(pnr))
            #print(sql)
            c.execute(sql)
            info = c.execute('select * from Passenger_info')
            conn.commit()
            p=[]
            l=[]
            pnr1=int(pnr)
            for i in info:
                p.insert(0,i)
            r3 = Tk()
            r3.geometry('500x600')
            r3.title('Ticket Details')

            def tkt_det_main():
                  r3.destroy()
                  root1.destroy()
                  main_page()

            res=c.execute("select a.PNR,a.Name,b.train_num,b.Name,b.src,b.src_time,b.dest_time,b.dest,b.fare from Passenger_info as a join trains_info as b on a.train_num=b.train_num where a.PNR=('%d')"%(int(pnr)))
            Heading2 = Label(r3, text="Ticket Details",
                    font=30, fg='pink', bg='green', justify='center')
            Heading2.place(x=220, y=25)
            for i in res:
                l.append(i)
        
                Label(r3, text='PNR            :   '+str(i[0])).place(x=180, y=50)
                Label(r3, text='Passenger Name :   '+str(i[1])).place(x=180, y=100)
                Label(r3, text='Train Number   :   '+str(i[2])).place(x=180, y=150)
                Label(r3, text='Train Name     :   '+str(i[3])).place(x=180, y=200)
                Label(r3, text='Source         :   '+str(i[4])).place(x=180, y=250)
                Label(r3, text='Departure Time :   '+str(i[5])).place(x=180, y=300)
                Label(r3, text='Arrival Time   :   '+str(i[6])).place(x=180, y=350)
                Label(r3, text='Destination    :   '+str(i[7])).place(x=180, y=400)
                Label(r3, text='Fare           :   '+str(i[8])).place(x=180, y=450)
                b3=Button(r3,text="Print",command=printt,bg="mint cream")
                b3.place(x=100,y=500)
                b4=Button(r3,text="Main",command=tkt_det_main,bg="mint cream")
                b4.place(x=280,y=500)

            r3.mainloop()

            conn.commit()
            #print(p)
            #ticket.ticket_display(pnr,int(train_num),p,email,date)
            #messagebox.showinfo('Ticket Details','Your PNR:'+str(pnr))
    
    root1 = Tk()
    
    root1.title('Book Ticket')

    window_width = 600
    window_height = 400

    # get the screen dimension
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root1.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Heading
    Heading = Label(root1, text="Book Ticket",font=30, fg='pink', bg='green', justify='center')
    Heading.place(x=235, y=10)

    # Store name, age, gender, email address
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    email = tk.StringVar()
    train_no = tk.StringVar()

    # Name
    Label(root1, text='Name :').place(x=180, y=60)
    name_entry = Entry(root1, textvariable=name)
    name_entry.place(x=270,y=60)
    name_entry.focus()

    # Age
    Label(root1, text='Age : ').place(x=180, y=100)
    age_entry = Entry(root1, textvariable=age)
    age_entry.place(x=270, y=100)
    age_entry.focus()

    # Email
    Label(root1, text='Email : ').place(x=180, y=140)
    email_entry = Entry(root1, textvariable=email)
    email_entry.place(x=270, y=140)
    email_entry.focus()

    # Gender
    Label(root1, text='Gender : ').place(x=180,y=180)
    # Combobox
    cmb = ttk.Combobox(root1, width="10", values=("M", "F", "Other"), textvariable=gender)
    cmb.place(x=270, y=180)

    #datetime
    Label(root1, text='Choose date').place(x=180, y=220)
 
    cal = DateEntry(root1, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.place(x=270,y=220) 

    # Train No
    Label(root1, text='Train No : ').place(x=180, y=260)
    train_no_label = Entry(root1, textvariable=train_no)
    train_no_label.place(x=270, y=260)
    train_no_label.focus()

    #Confirm Ticket Button
    b1=Button(root1,text="Confirm Ticket",command=into_pass,bg="mint cream")
    b1.place(x=180,y=330)

    #Cancel  Button
    b2=Button(root1,text="Cancel", command=cancel,bg="mint cream")
    b2.place(x=390,y=330)
    root1.mainloop()
    


# Cancel a ticket
def cancel_a_ticket():
    def cancel_ticket():
        p = pnr.get()
        s = 'select pnr from passenger_info'
        pnr_list=[]
        pnr_l = c.execute(s)
        for i in pnr_l:
            pnr_list.append(i[0])
        if int(p) not in pnr_list:
            messagebox.showerror('Error','PNR number invalid!')
        else:
            st = 'Delete from passenger_info where pnr=%d' % int(p)
            c.execute(st)
            conn.commit()
            pnr.set('')
            messagebox.showinfo('Success','Ticket Cancellation Successful!')
    root = Tk()
    root.geometry('300x200')
    root.title('Cancel Ticket')

    pnr = tk.StringVar()

    

    def home():
        root.destroy()
        homepage()

    # Enter PNR
    Label(root, text='Enter PNR No :').grid(row=1, column=0, padx=10)
    input_pnr = Entry(root, textvariable=pnr)
    input_pnr.grid(row=2, column=0, padx=10, pady=10)

    # Buttons
    but1 = Button(root, text='Cancel Ticket', command=cancel_ticket)
    but1.grid(row=4, column=0)

    but2 = Button(root, text='Home', command=home)
    but2.grid(row=4, column=2)

    root.mainloop()


# Homepage
def homepage():
    home = Tk()

    home.title("HOME")
    window_width = 500
    window_height = 500
    home.title('Home')
    # get the screen dimension
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    home.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def showTrains():
        #print("Show trains pressed")
        home.destroy()
        enter_train_details()
    
    def bookTicket():
        #print("Book Ticket pressed")
        home.destroy()
        book_a_ticket()

    def cancelTicket():
        home.destroy()
        cancel_a_ticket()

    def exitBtn():
        home.destroy()
        main_page()
    """
    bg = PhotoImage( file = "./images/welcomepage1.png")
    #Show image using label
    label1 = Label( home, image = bg)
    label1.place(x = 0,y = 0, relwidth=1,relheight=1)    
     """
    # Welcome Message and Styling To Do
    Heading = Label(home, text="Welcome to Indian Railways Booking",
                    font=30, fg='misty rose', bg='green4', justify='center')
    Heading.grid(row=0, column=0,padx=70,pady=40)

    # Show Trains
    show_trains = Button(home, text='Show Trains', command=showTrains, bg='gold', fg="red4")
    show_trains.grid(row=3, column=0,pady=15)
  
    # Book a Ticket
    book_ticket = Button(home, text='Book Ticket', command=bookTicket, bg="gold", fg="red4")
    book_ticket.grid(row=5, column=0,pady=15)

    # Cancel a Ticket
    cancel_ticket = Button(home, text='Cancel Ticket', command=cancelTicket, bg="gold", fg="red4")
    cancel_ticket.grid(row=7, column=0, pady=15)

    # Exit
    exit_btn = Button(home, text='Exit', command=exitBtn, width=9, bg="gold", fg="red4")
    exit_btn.grid(row=9, column=0,pady=15)

    home.mainloop()



# MAIN PAGE
def main_page():
    root = Tk()
    root.title('LOGIN')

    login_width = 400
    login_height = 400

    # get the screen dimension
    screen1_width = root.winfo_screenwidth()
    screen1_height = root.winfo_screenheight()

    # find the center point
    center1_x = int(screen1_width/2 - login_width / 2)
    center1_y = int(screen1_height/2 - login_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{login_width}x{login_height}+{center1_x}+{center1_y}')

    # Button functions
    def guest():
        root.destroy()
        homepage()
    
    def admin():
        root.destroy()
        verification()
    """
    # Image using Label
    bg = PhotoImage( file = "./images/homepage.png")
    #Show image using label
    label1 = Label( root, image = bg)
    label1.place(x = 0,y = 0, relwidth=1,relheight=1)
    """
    # Heading
    Head = Label(root, text="Login As",
                    font=30, fg='pink', bg='green', justify='center')
    Head.grid(row=0, column=3,padx=150,pady=40)

    # Guest Button
    Guest = Button(root, text='GUEST', command=guest,bg="gold",fg="red4")
    Guest.place(x=170,y=130)

    # Admin Button
    Admin = Button(root, text='ADMIN', command=admin,bg="gold",fg="red4")
    Admin.place(x=166,y=200)

    root.mainloop()



# ADMIN PART

mydb = sqlite3.connect('trains.db')
cursor = mydb.cursor()
# Verify Email and password wala function
def verification():
    root = Tk()
    root.title("VERIFICATON")
    window_width = 300
    window_height = 200

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    root.resizable(False, False)
    root.title('Sign In')

    # store email address and password
    user = tk.StringVar()
    passw = tk.StringVar()

    def login_clicked():

        if (username.get()=='Adminit' or username.get()=='adminit' and password.get()=='ssn'):
            root.destroy()
            admin_main()
        else:
            username.delete(0, 'end')
            password.delete(0, 'end')
            messagebox.showinfo("Error", "Incorrect Username or Password")

    def back_clicked():
        root.destroy()
        main_page()


    # Sign in frame
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=True)

    # Username
    username_label = ttk.Label(signin, text="Username:")
    username_label.pack(fill='x', expand=True)

    username = ttk.Entry(signin, textvariable=user)
    username.pack(fill='x', expand=True)
    username.focus()

    # password
    password_label = ttk.Label(signin, text="Password:")
    password_label.pack(fill='x', expand=True)

    password = ttk.Entry(signin, textvariable=passw, show="*")
    password.pack(fill='x', expand=True)

    # login button
    login_button = ttk.Button(signin, text="Login", command=login_clicked)
    login_button.pack(fill='x', expand=True, pady=10)

    # Back Button
    back_button = ttk.Button(signin, text="Back", command=back_clicked)
    back_button.pack(fill='x', expand=True, pady=10)

    root.mainloop()




def show_passengers():
    print('Show Passengers')
    st = 'select * from Passenger_info'
    a= c.execute(st)
    r = Tk()
    r.title("PASSENGERS INFO")
    window_width = 655
    window_height = 455

    # get the screen dimension
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    r.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    treev = ttk.Treeview(r, selectmode ='browse')
  
    # Calling pack method w.r.to treeview
    treev.pack(side ='left')
  
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(r, 
                           orient ="vertical", 
                           command = treev.yview)
  
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')
  
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
  
    # Defining number of columns
    treev["columns"] = ("1", "2", "3", "4" , "5" ,"6")
  
    # Defining heading
    treev['show'] = 'headings'
  
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 120, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    treev.column("4", width = 90, anchor ='c')
    treev.column("5", width = 150, anchor ='c')
    treev.column("6", width = 90, anchor ='c')
  
    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="Train no.")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Age")
    treev.heading("4", text ="Gender")
    treev.heading("5", text ="Email")
    treev.heading("6", text ="PNR")
    st1= 'Select distinct count(pnr) from passenger_info'
    b= c.execute(st1)
    for i in b:
        num=i
    Label(r, text="Number of Passengers :").place(x=200,y=30)
    Label(r, text=num).place(x=330,y=30)
    a= conn.execute('select * from passenger_info')
    
    result = a.fetchall()
    for i in result:
        treev.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4],i[5]))

    # Back Button
    def btn_back():
        r.destroy()
        admin_main()
    """
    def download():
            df = pd.read_sql_query('select * from passenger_info',mydb)
            writer = ExcelWriter('Passenger_info.xlsx')
            df.to_excel(writer,'Sheet1',index=False)
            writer.save()
    """
    Button(r, text='BACK', command = btn_back).place(x=450, y=350)
    #Button(r, text='GET EXCEL SHEET', command = download).place(x=180, y=350)
    r.mainloop()
    r.mainloop()


def show_trains():
    st = 'Select * from trains_info'
    a= c.execute(st)
    r = Tk()

    r.title("TRAINS")
    window_width = 755
    window_height = 455

    # get the screen dimension
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    r.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    b = "select count(*) from trains_info"
    m= c.execute(b)
    # for num in m:
    #     pass
    n= m.fetchone()
    treev = ttk.Treeview(r, selectmode ='browse')
    
    Label(r, text=f"Number of Trains : {int(str(n[0]))}").place(x=100,y=50)
    
    # Calling pack method w.r.to treeview
    treev.pack(side ='left')
  
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(r, orient ="vertical", command = treev.yview)
  
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')
  
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
  
    # Defining number of columns
    treev["columns"] = ("1", "2", "3","4","5","6","7")
  
    # Defining heading
    treev['show'] = 'headings'
  
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 140, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    treev.column("4", width = 90, anchor ='c')
    treev.column("5", width = 90, anchor ='c')
    treev.column("6", width = 98, anchor ='c')
    treev.column("7", width = 90, anchor ='c')
  
    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="Train no.")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Source")
    treev.heading("4", text ="Source Time")
    treev.heading("5", text ="Destination")
    treev.heading("6", text ="Destination Time")
    treev.heading("7", text ="Fare")

    a= conn.execute('select * from trains_info')
    
    result = a.fetchall()
    for i in result:
        treev.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4],i[5],i[6]))
    # Back Button
    def btn_back():
        r.destroy()
        admin_main()

    Button(r, text='BACK', command = btn_back).place(x=400, y=350)
    r.mainloop()
        


def add_trains():
    root = Tk()
    root.title("ADD TRAINS")
    window_width = 500
    window_height = 500

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Defining Inputs
    t_number = tk.StringVar()
    t_name = tk.StringVar()
    t_srctime = tk.StringVar()
    t_desttime = tk.StringVar()
    t_fare = tk.StringVar()

    # Button functions
    def add_train():
        tnum= t_number.get()
        tname= t_name.get()
        tsrc = src.get()
        tsrct= t_srctime.get()
        tdest = dest.get()
        tdestt = t_desttime.get()
        tfare= t_fare.get()
        print("Added")
        st= "insert into trains_info values (%d,'%s','%s','%s','%s','%s',%d)" % (int(tnum),tname,tsrc,tsrct,tdest,tdestt,int(tfare))
        #print(st)
        c.execute(st)
        conn.commit()
        messagebox.showinfo('Success','Train record added successfully!')
         
        

    def cancel():
        root.destroy()
        admin_main()

    def reset():
        num.delete(0, 'end')
        name.delete(0, 'end')
        src.delete(0, 'end')
        dest.delete(0, 'end')
        stime.delete(0, 'end')
        dtime.delete(0, 'end')

    # Heading
    Heading = Label(root, text="Add Trains",
                    font=30, fg='pink', bg='green', justify='center')
    Heading.place(x=180, y=20)

    # Add Train Details
    Label(root, text='Train Number: ').place(x=100, y=80)
    num = Entry(root, textvariable=t_number)
    num.place(x=250, y=80)
    num.focus()

    Label(root, text='Train Name: ').place(x=100, y=120)
    name = Entry(root, textvariable=t_name)
    name.place(x=250, y=120)
    name.focus()

    Label(root, text='Source: ').place(x=100, y=160)
    src = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    src.place(x=250, y=160)

    Label(root, text='Destination: ').place(x=100, y=200)
    dest = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    dest.place(x=250, y=200)
    
    Label(root, text='Source Time: ').place(x=100, y=240)
    stime = Entry(root, textvariable=t_srctime)
    stime.place(x=250, y=240)
    stime.focus()

    Label(root, text='Destination Time: ').place(x=100,y=280)
    dtime = Entry(root, textvariable=t_desttime)
    dtime.place(x=250, y=280)
    dtime.focus()

    Label(root, text='Fare: ').place(x=100, y=320)
    fare = Entry(root, textvariable=t_fare)
    fare.place(x=250, y=320)
    fare.focus()

    # Add Train Button
    btnAdd = Button(root, text='Add Train', command=add_train)
    btnAdd.place(x=120,y=380)

    # Cancel Button
    btnCancel = Button(root, text='BACK', command=cancel)
    btnCancel.place(x=230,y=380)
    
    # Reset Button
    btnReset = Button(root, text='Reset', command=reset)
    btnReset.place(x=320,y=380)

    root.mainloop()



def cancel_trains():
    def cancel():
        tno1 = tnum.get()
        st1 = 'Select train_num from trains_info'
        n = c.execute(st1)
        num_list=[]
        for i in n:
            num_list.append(i[0])
        if int(tno1) not in num_list:
            messagebox.showerror('Error','Train number does not exist')
        else:
            st = 'Delete from trains_info where train_num=%d' % int(tno1)
            #print(st)
            c.execute(st)
            conn.commit()
            messagebox.showinfo('Success','Train record deleted!')
            
    def cancel_tback():
        r.destroy()
        admin_main()        
       
    print('Cancel Trains')
    r = Tk()
    r.title("CANCEL TRAINS")
    tnum = tk.StringVar()
    window_width = 255
    window_height = 255

    # get the screen dimension
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    r.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    Label(r, text="Enter Train number").pack()
    Entry(r, textvariable=tnum).pack()
    Button(r,text="Cancel", command=cancel).pack()
    Button(r,text="Back", command=cancel_tback).pack()
    
    r.mainloop()
    

def admin_main():
    root = Tk()
    window_width = 300
    window_height = 300

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    root.resizable(True, True)
    root.title('Admin')

    def s_passengers():
        root.destroy()
        show_passengers()

    def s_trains():
        root.destroy()
        show_trains()
    
    def a_trains():
        root.destroy()
        add_trains()

    def c_trains():
        root.destroy()
        cancel_trains()

    def logout():
        root.destroy()
        main_page()
        # We need to make a call to the Login Page
        
    # Making buttons
    btn1 = Button(root, text='Show Passengers', command=s_passengers)
    btn1.place(x=100, y=30)
    btn2 = Button(root, text='Show Trains', command=s_trains)
    btn2.place(x=110, y=70)
    btn3 = Button(root, text='Add Trains', command=a_trains)
    btn3.place(x=110, y=110)
    btn4 = Button(root, text='Cancel Trains', command=c_trains)
    btn4.place(x=105, y=150)
    btn5 = Button(root, text='Logout', command=logout)
    btn5.place(x=120, y=190)


main_page()

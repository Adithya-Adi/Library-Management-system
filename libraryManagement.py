from contextlib import nullcontext
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from datetime import date
import random
image1='LibraryHome.jpg'
image2='library.jpg'
image3='LibraryLogin.jpg'

users ={'admin' : 'admin'}

class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data; self.next = None

class LinkedListBook:
  def __init__(self):  
    self.head = None

  # insert book
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

#delete book
  def deleteNode(self, bookid):
    if self.head is None:
        return
    temp = self.head
    if bookid in temp.data:
        self.head = temp.next
    else:
        while(bookid not in temp.data):
            prevtemp = temp
            temp = temp.next
        prevtemp.next = temp.next

#bookid already exists
  def alreadyexists(self,bookid):
      current = self.head
      flag = 1
      while(current):
          if bookid in current.data:
              flag = 0
          else:
            flag = 1
          current = current.next
      if flag == 1:
        return 1
      else:
          return 0

  # display all books
  def printLL(self):
    current = self.head
    data = []
    while(current):
        data.append(current.data)
        current = current.next
    return data

#display searched book
  def printSearch(self,search):
    current = self.head
    data = []
    while(current):
        if search in current.data:
            # print(current.data)
            data.append(current.data)
        current = current.next
    return data

#add and delete copies
  def Lcopies(self,bookid,num,ch):
    current = self.head
    while(current):
        if bookid in current.data:
            if ch == 1:
                current.data[4] = current.data[4] + num
            elif ch == 2:
                current.data[4] = current.data[4] - num
        current = current.next

  def avlcopies(self,bookid):
        current = self.head
        flag = 1
        while(current):
            if bookid in current.data:
                if current.data[4] > 0:
                    flag = 1
                    current.data[4] = current.data[4] - 1
                else:
                    flag = 0
            current = current.next
        if flag == 1:
            return 1
        else:
            return 0

class LinkedListIssue:
  def __init__(self):  
    self.head = None

  # insert book
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode


  # display all books
  def printLL(self):
    current = self.head
    data = []
    while(current):
        data.append(current.data)
        current = current.next
    return data

#display searched book
  def printSearch(self,search):
    current = self.head
    data = []
    while(current):
        if search in current.data:
            # print(current.data)
            data.append(current.data)
        current = current.next
    return data

  def returnbook(self,bookid,studentid,datetoday):
    current = self.head
    flag = 1
    while(current):
        if bookid in current.data and studentid in current.data:
           current.data[3] = datetoday
           linkedlist.Lcopies(bookid,1,1)
           return 1
        current = current.next

if __name__=='__main__':

	# Start with the empty list
    linkedlist = LinkedListBook()
    linkedlistissue = LinkedListIssue()

class menu:
    def __init__(self):
        self.root=Tk()
        self.root.title('Menu')
        self.root.state('zoomed')
        self.a=self.canvases(image1)
        fr1 = Frame(self.a, bg="white")
        fr1.place(x=300, y=85, width=700, height=100)
        liblabel=Label(self.a, text="NMAMIT Library", font=("Calibri", 40, "bold"), bg="white", fg="green").place(x=480, y=100)
        l1=Button(self.a,text='BOOK DATA',font='Papyrus 22 bold',fg='black',bg='white',width=19,padx=10,borderwidth=0,command=self.book).place(x=480,y=250)
        l2=Button(self.a,text='STUDENT DATA',font='Papyrus 22 bold',fg='black',bg='white',width=19,padx=10,borderwidth=0,command=self.student).place(x=480,y=330)
        self.root.mainloop()
    def canvases(self,images):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        photo=Image.open(images)
        photo1=photo.resize((w,h),Image.ANTIALIAS)
        photo2=ImageTk.PhotoImage(photo1)

        self.canvas = Canvas(self.root, width='%d'%w, height='%d'%h)
        self.canvas.grid(row = 0, column = 0)
        self.canvas.grid_propagate(0)
        self.canvas.create_image(0, 0, anchor = NW, image=photo2)
        self.canvas.image=photo2
        return self.canvas
    def book(self):
        self.a.destroy()
        self.a=self.canvases(image2)
        self.all()
        l1=Button(self.a,text='All Books',font='Papyrus 22 bold',fg='black',bg='lightgray',width=15,padx=10,command=self.all).place(x=12,y=100)
        l2=Button(self.a,text='Search Books',font='Papyrus 22 bold',fg='black',bg='lightgray',width=15,padx=10,command=self.search).place(x=12,y=200)
        l4=Button(self.a,text='Add Books',font='Papyrus 22 bold',fg='black',bg='lightgray',width=15,padx=10,command=self.addbook).place(x=12,y=300)
        l4=Button(self.a,text='<< Main Menu',font='Papyrus 22 bold',fg='black',bg='lightgray',width=15,padx=10,command=self.mainmenu).place(x=12,y=500)


    def addbook(self):
        self.aid=StringVar()
        self.aauthor=StringVar()
        self.aname=StringVar()
        self.acopies=IntVar()
        self.agenre=StringVar()
        self.aloc=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='white')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Papyrus 12 bold',fg='black',bg='white',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=45,bg='lightgray',fg='black',textvariable=self.aid).place(x=150,y=50)
        l2=Label(self.f1,text='Title : ',font='Papyrus 12 bold',fg='black',bg='white',pady=1).place(x=50,y=100)
        e2=Entry(self.f1,width=45,bg='lightgray',fg='black',textvariable=self.aname).place(x=150,y=100)
        l3=Label(self.f1,text='Author : ',font='Papyrus 12 bold',fg='black',bg='white',pady=1).place(x=50,y=150)
        e3=Entry(self.f1,width=45,bg='lightgray',fg='black',textvariable=self.aauthor).place(x=150,y=150)
        l4=Label(self.f1,text='Genre : ',font='Papyrus 12 bold',fg='black',bg='white',pady=1).place(x=50,y=200)
        e2=Entry(self.f1,width=45,bg='lightgray',fg='black',textvariable=self.agenre).place(x=150,y=200)
        l4=Label(self.f1,text='Copies : ',font='Papyrus 12 bold',fg='black',bg='white',pady=1).place(x=50,y=250)
        e2=Entry(self.f1,width=45,bg='lightgray',fg='black',textvariable=self.acopies).place(x=150,y=250)
        l5=Label(self.f1,text='Location : ',font='Papyrus 12 bold',fg='black',bg='white',pady=1).place(x=50,y=300)
        e3=Entry(self.f1,width=45,bg='lightgray',fg='black',textvariable=self.aloc).place(x=150,y=300)
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Add',font='Papyrus 10 bold',fg='black',bg='green',width=15,bd=3,command=self.adddata).place(x=150,y=400)
        b2=Button(self.f1,text='Back',font='Papyrus 10 bold',fg='black',bg='red',width=15,bd=3,command=self.rm).place(x=350,y=400)

    def rm(self):
        self.f1.destroy()
    def mainmenu(self):
        self.root.destroy()
        a=menu()

#add book function
    def adddata(self):
        bookid=self.aid.get()
        title=self.aname.get()
        author=self.aauthor.get()
        genre=self.agenre.get()
        copies=self.acopies.get()
        location=self.aloc.get()
    #checking input fields empty
        if (bookid and title and author and genre  and copies and location)=="":
            messagebox.showinfo("Error","Fields cannot be empty")
        else:
            data = [bookid, title, author, genre, copies,location]
            if linkedlist.alreadyexists(bookid):
                linkedlist.insert(data)
                messagebox.showinfo("Inserted","Book inserted successfully")
            else:
                messagebox.showinfo("Inserted","Book ID already exists")


    def search(self):
        #self.search.state('zoomed')
        self.sid=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='lightgray')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID/Title/Author/Genre: ',font=('Papyrus 10 bold'),bd=2, fg='black',bg='lightgray').place(x=20,y=40)
        e1=Entry(self.f1,width=25,bd=5,bg='white',fg='black',textvariable=self.sid).place(x=260,y=40)
        b1=Button(self.f1,text='Search',bg='green',fg="white",font='Papyrus 10 bold',width=9,bd=2,command=self.serch1).place(x=500,y=37)
        b1=Button(self.f1,text='Back',bg='red',fg="white",font='Papyrus 10 bold',width=10,bd=2,command=self.rm).place(x=250,y=450)

    def create_tree(self,plc,lists):
        self.tree=ttk.Treeview(plc,height=13,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=100)
            n=n+1
        return self.tree


    def serch1(self):
        k=self.sid.get()
        if k!="":
            self.list4=("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
            self.trees=self.create_tree(self.f1,self.list4)
            self.trees.place(x=25,y=150)
            #search linked list
            data = linkedlist.printSearch(k)
            i=0
            lent = len(data)
            while(i<lent):
                self.trees.insert('',END,values=data[i])
                i = i+1 
                
            self.trees.bind('<<TreeviewSelect>>')
            self.variable = StringVar(self.f1)
            self.variable.set("Select Action:")

            self.cm =ttk.Combobox(self.f1,textvariable=self.variable ,state='readonly',font='Papyrus 15 bold',height=50,width=15,)
            self.cm.config(values =('Add Copies', 'Delete Copies', 'Delete Book'))

            self.cm.place(x=50,y=100)
            self.cm.pack_propagate(0)


            self.cm.bind("<<ComboboxSelected>>",self.combo)
            self.cm.selection_clear()

        else:
            messagebox.showinfo("Error","Search field cannot be empty.")


    def combo(self,event):
        self.var_Selected = self.cm.current()
        #l7=Label(self.f1,text='copies to update: ',font='Papyrus 10 bold',bd=1).place(x=250,y=700)
        if self.var_Selected==0:
            self.copies(self.var_Selected)
        elif self.var_Selected==1:
            self.copies(self.var_Selected)
        elif self.var_Selected==2:
            self.deleteitem()
    def deleteitem(self):
        try:
            self.curItem = self.trees.focus()
            self.c1=self.trees.item(self.curItem,"values")[0]
            b1=Button(self.f1,text='Update',bg="blue",fg="white",font='Papyrus 10 bold',width=9,bd=3,command=self.delete2).place(x=500,y=97)
        except:
            messagebox.showinfo("Empty","Please select something.")
    def delete2(self):
        linkedlist.deleteNode(self.c1)
        messagebox.showinfo("Successful","Book Deleted sucessfully.")

    def copies(self,varr):
        try:
            curItem = self.trees.focus()
            self.c1=self.trees.item(curItem,"values")[0]
            self.c2=self.trees.item(curItem,"values")[4]
            self.scop=IntVar()
            self.e5=Entry(self.f1,width=20,textvariable=self.scop)
            self.e5.place(x=310,y=100)
            if varr==0:
                b5=Button(self.f1,text='Update',font='Papyrus 10 bold',bg="blue",fg="white",width=9,bd=3,command=self.copiesadd).place(x=500,y=97)
            if varr==1:
                b6=Button(self.f1,text='Update',font='Papyrus 10 bold',bg="blue",fg="white",width=9,bd=3,command=self.copiesdelete).place(x=500,y=97)
        except:
            messagebox.showinfo("Empty","Please select something.")

    def copiesadd(self):
        no=self.e5.get()
        if int(no)>=0:
            data = linkedlist.Lcopies(self.c1,int(no),1)
            messagebox.showinfo("Updated","Copies added sucessfully.")
            self.serch1()
        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

    def copiesdelete(self):
        no1=self.e5.get()
        if int(no1)>=0:
            if int(no1)<=int(self.c2):
               data = linkedlist.Lcopies(self.c1,int(no1),2)
               messagebox.showinfo("Updated","Copies deleted sucessfully.")
               self.serch1()
            else:
                messagebox.showinfo("Maximum","No. of copies to delete exceed available copies.")
        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

    def all(self):
        self.f1=Frame(self.a,height=500,width=650,bg='lightgray')
        self.f1.place(x=500,y=100)
        self.list3=("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
        self.treess=self.create_tree(self.f1,self.list3)
        self.treess.place(x=25,y=100)
        data = linkedlist.printLL()
        i=0
        lent = len(data)
        while(i<lent):
            self.treess.insert('',END,values=data[i])
            i = i+1 

    def student(self):
        self.a.destroy()
        self.a=self.canvases(image2)
        self.issue()
        l1=Button(self.a,text='Issue book',font='Papyrus 22 bold', fg='black',bg='lightgray',width=15,padx=10,command=self.issue).place(x=12,y=300)
        l2=Button(self.a,text='Return Book',font='Papyrus 22 bold', fg='black',bg='lightgray',width=15,padx=10,command=self.returnn).place(x=12,y=200)
        l3=Button(self.a,text='Student Activity',font='Papyrus 22 bold', fg='black',bg='lightgray',width=15,padx=10,command=self.activity).place(x=12,y=100)
        l4=Button(self.a,text='<< Main Menu',font='Papyrus 22 bold', fg='black',bg='lightgray',width=15,padx=10,command=self.mainmenu).place(x=12,y=600)


    def issue(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=500,bg='lightgrey')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='papyrus 15 bold',bg='lightgrey',fg='black').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='papyrus 15 bold',bg='lightgrey',fg='black').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Papyrus 10 bold',fg='white',bg='red',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Issue',font='Papyrus 10 bold',fg='white',bg='blue',width=10,bd=3,command=self.issuedbook).place(x=200,y=250)

    def issuedbook(self):
        bookid=self.aidd.get()
        studentid=self.astudentt.get()
        # print(date.today())
        datetoday = str(date.today())
        # print(datetoday)
        if (self.aidd.get() =='' or self.astudentt.get() == ""):
            messagebox.showinfo("Error","Fields cannot be blank.")
        else:
            data = [bookid, studentid, datetoday, '']
            if(linkedlist.alreadyexists(bookid) == 0):
                if(linkedlist.avlcopies(bookid) == 1):
                    linkedlistissue.insert(data)
                    messagebox.showinfo("Updated","Book Issued sucessfully.")
                else:
                    messagebox.showinfo("Unavailable","Book unavailable.There are 0 copies of the book.")
            else:
                messagebox.showinfo("Unavailable","Book unavailable.")
     
    def returnn(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=500,bg='lightgrey')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='papyrus 15 bold',fg='black', bg='lightgrey').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='papyrus 15 bold',fg='black', bg='lightgrey').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Papyrus 10 bold',bg='red',fg='white',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Return',font='Papyrus 10 bold',bg='green',fg='white',width=10,bd=3,command=self.returnbook).place(x=200,y=250)
        self.f1.grid_propagate(0)

    def returnbook(self):
        bookid=self.aidd.get()
        studentid=self.astudentt.get()
        datetoday = str(date.today())
        if linkedlistissue.returnbook(bookid,studentid,datetoday):
            messagebox.showinfo("Updated","Book returned")
        else:
            messagebox.showinfo("Error","Invalid Book Id or Student ID")



    def activity(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=500,bg='lightgrey')
        self.f1.place(x=500,y=80)
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)
        self.searchall()
        l1=Label(self.f1,text='Book/Student ID : ',font='Papyrus 15 bold',fg='black',bg='lightgrey').place(x=50,y=30)
        e1=Entry(self.f1,width=20,bd=4,bg='white',fg='black',textvariable=self.aidd).place(x=280,y=35)
        #l2=Label(self.f1,text='Student Id : ',font='papyrus 15 bold',fg='orange',bg='black').place(x=50,y=80)
        #e2=Entry(self.f1,width=20,bd=4,bg='orange',textvariable=self.astudentt).place(x=180,y=80)
        b1=Button(self.f1,text='Back',bg='red',font='Papyrus 10 bold',width=10,bd=3,command=self.rm).place(x=340,y=450)
        b1=Button(self.f1,text='Search',bg='green',font='Papyrus 10 bold',width=10,bd=3,command=self.searchact).place(x=40,y=450)
        b1=Button(self.f1,text='All',bg='blue',font='Papyrus 10 bold',width=10,bd=3,command=self.searchall).place(x=190,y=450)
        self.f1.grid_propagate(0)

    def searchact(self):
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)
        bid=self.aidd.get()
        data = linkedlistissue.printSearch(bid)
        i=0
        lent = len(data)
        while(i<lent):
            self.trees.insert('',END,values=data[i])
            i = i+1 
       
    def searchall(self):
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)
        data = linkedlistissue.printLL()
        i=0
        lent = len(data)
        while(i<lent):
            self.trees.insert('',END,values=data[i])
            i = i+1 
       

#===================START=======================
def canvases(images,w,h):
    photo=Image.open(images)
    photo1=photo.resize((w,h),Image.ANTIALIAS)
    photo2=ImageTk.PhotoImage(photo1)

    canvas = Canvas(root, width='%d'%w, height='%d'%h)
    canvas.grid(row = 0, column = 0)
    canvas.grid_propagate(0)
    canvas.create_image(0, 0, anchor = NW, image=photo2)
    canvas.image=photo2
    return canvas
root = Tk()
root.title("LOGIN")
"""width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)"""

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
canvas=canvases(image3,w,h)


USERNAME = StringVar()
PASSWORD = StringVar()
CPASSWORD = StringVar()

def Login(event=None): 
    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("Error","Please fill the required field!")
        lbl_text.config(text="Please fill the required field!", fg="red")
    else:
        if USERNAME.get() in users and PASSWORD.get() == users[USERNAME.get()]:
                root.destroy()  
                a=menu()
        else:
            messagebox.showinfo("Error","Invalid username")
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")

  
#signup
def Signup(event=None):
     if USERNAME.get() == "" or PASSWORD.get() == "" or CPASSWORD.get() == "":
        messagebox.showinfo("Error","Please fill the required field!")
        USERNAME.set('')
        PASSWORD.set('')
        CPASSWORD.set('')
     elif USERNAME.get() in users:
        messagebox.showinfo("Error","UserName Already exists!")
        USERNAME.set('')
        PASSWORD.set('')
        CPASSWORD.set('')
     elif PASSWORD.get() != CPASSWORD.get():
        messagebox.showinfo("Error","Password and confirm password doesnot match")
        USERNAME.set('')
        PASSWORD.set('')
        CPASSWORD.set('')

     else:
            users[USERNAME.get()] = PASSWORD.get()
            messagebox.showinfo("Register","Register Successfull")
            USERNAME.set('')
            PASSWORD.set('')
            CPASSWORD.set('')
            loginpage()


#registration form
def Register(event=None):
    aidd=StringVar()
    astudentt=StringVar()
    f1 = Frame(root, bg="white")
    f1.place(x=300, y=85, width=700, height=550)
    #regiter label
    l_title = Label(f1, text="REGISTER", font=("Calibri", 30, "bold"), bg="white", fg="green").place(x=275, y=55)
    Label(f1, text="Enter the credential", font=("Calibri", 15, "bold"), bg="white", fg="blue").place(x=272, y=100)
    #uname
    u_name = Label(f1, text="User Name:", font=("Calibri", 20, "bold"), bg="white", fg="black").place(x=50, y=170)
    username = Entry(f1,textvariable=USERNAME, font=("Calibri", 15), bg="lightgray")
    username.place(x=270, y=175, width=250)
    #password
    u_password = Label(f1, text="Password:", font=("Calibri", 20, "bold"), bg="white", fg="black").place(x=50, y=210)
    password = Entry(f1,textvariable=PASSWORD,show="*", font=("Calibri", 15), bg="lightgray")
    password.place(x=270, y=215, width=250)
    #confirm password
    c_password = Label(f1, text="Confirm Password:", font=("Calibri", 20, "bold"), bg="white", fg="black").place(x=50, y=250)
    cpassword = Entry(f1,textvariable=CPASSWORD,show="*", font=("Calibri", 15), bg="lightgray")
    cpassword.place(x=270, y=255, width=250)
    #button
    btn_register = Button(f1, text="Sign Up", command=Signup,bg="green",fg="white", font=("Calibri", 20), bd=0, cursor="hand2").place(x=295, y=290)
    #back
    btn_login = Button(f1, text="Back", command=loginpage,bg="red",fg="white", font=("Calibri", 20), bd=0, cursor="hand2").place(x=400, y=290)

def loginpage():
      
    frame1 = Frame(root, bg="white")
    frame1.place(x=300, y=85, width=700, height=550)
    #login label
    l_title = Label(frame1, text="LOGIN", font=("Calibri", 30, "bold"), bg="white", fg="green").place(x=275, y=55)
    Label(frame1, text="Enter login credentials", font=("Calibri", 15, "bold"), bg="white", fg="blue").place(x=240, y=100)
    #username
    u_name = Label(frame1, text="User Name:", font=("Calibri", 20, "bold"), bg="white", fg="black").place(x=50, y=170)
    username = Entry(frame1,textvariable=USERNAME, font=("Calibri", 15), bg="lightgray")
    username.place(x=270, y=175, width=250)
    #password
    u_password = Label(frame1, text="Password:", font=("Calibri", 20, "bold"), bg="white", fg="black").place(x=50, y=230)
    password = Entry(frame1,textvariable=PASSWORD,show="*", font=("Calibri", 15), bg="lightgray")
    password.place(x=270, y=235, width=250)
    #validation
    global lbl_text
    lbl_text = Label(frame1)
    lbl_text.place(x=270,y=210)
    lbl_text.grid_propagate(0)
    #login button
    btn_login = Button(frame1, text="Login", command=Login,bg="green",fg="white", font=("Calibri", 20), bd=0, cursor="hand2").place(x=270, y=300,width=200)
    #register button
    btn_register = Button(frame1, text="Register", command=Register, bg="blue",fg="white", font=("Calibri", 20), bd=0, cursor="hand2").place(x=270, y=360,width=200)


#==============================FRAMES=========================================
'''Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=BOTTOM, pady=20)'''

loginpage()
root.mainloop()

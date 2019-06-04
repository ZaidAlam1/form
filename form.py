from tkinter import *
from mysql import connector
from tkinter import messagebox
top=Tk()
mydb=connector.connect(host="localhost",user="root",passwd="",database="RegistrationForm")
top.geometry("600x600")
cur=mydb.cursor()

top.title("Registration Form")
top.configure(bg='black')
Label(top,text='Items marked with * are compulsory',bg='Black',fg='light green').grid(row=0,sticky=E)
l1=Label(top,text='ID  ',bg='Black',fg='light green')
l1.grid(row=2,sticky=E)
l8=Label(top,text='Set_Password ',bg='Black',fg='light green')
l8.grid(row=3,sticky=E)
l9=Label(top,text='Confirm Password ',bg='Black',fg='light green')
l9.grid(row=4,sticky=E)
l2=Label(top,text='Name ',bg='Black',fg='light green')
l2.grid(row=5,sticky=E)
l3=Label(top,text='Address ',bg='Black',fg='light green')
l3.grid(row=6,sticky=E)
l4=Label(top,text='Course ',bg='Black',fg='light green')
l4.grid(row=7,sticky=E)
l5=Label(top,text='Contact No ',bg='Black',fg='light green')
l5.grid(row=8,sticky=E)
l6=Label(top,text='Alternate Contact No',bg='black',fg='light green')
l6.grid(row=9,sticky=E)
l7=Label(top,text='Fees',bg='black',fg='light green')
l7.grid(row=10,sticky=E)
e1=Entry(top)
e1.grid(row=2,column=1)
e8=Entry(top, show="*")
e8.grid(row=3, column=1)
e9=Entry(top, show="*")
e9.grid(row=4, column=1)
e2=Entry(top)
e2.grid(row=5,column=1)
e3=Entry(top)
e3.grid(row=6,column=1)
e4=Entry(top)
e4.grid(row=7,column=1)
e5=Entry(top)
e5.grid(row=8,column=1)
e6=Entry(top)
e6.grid(row=9,column=1)
e7=Entry(top)
e7.grid(row=10,column=1)


Checkbutton(top,text='I have read terms and conditions',bg='black',fg='light green').grid(columnspan=10)
def save():
        id1 = e1.get()
        pw1 = e8.get()
        cpw1 = e9.get()
        name1 = e2.get()
        addr1 = e3.get()
        crse1 = e4.get()
        cont1 = e5.get()
        alt_cont1 = e6.get()
        fees1 = e7.get()
        #if(id1==0 or pw1=="" or cpw1=="" or name1=="" or addr1=="" or crse1=="" or cont1==0):
               # messagebox.showwarning("Warning", "Fill the text box")
        if(pw1!=cpw1):
                messagebox.showerror("Warning","Password Mismatch")
        else:
                sql="insert into Entries(id,passwd,conf_passwd,name,address,course,cont,alt_cont,fees) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(int(id1),pw1,cpw1,name1,addr1,crse1,cont1,alt_cont1,int(fees1))
                cur.execute(sql,val)
                mydb.commit()

                messagebox.showinfo("Save", "1 Record Saved")
                id1.delete(0, END)
                pw1.delete(0, END)
                cpw1.delete(0, END)
                name1.delete(0, END)
                addr1.delete(0, END)
                crse1.delete(0, END)
                cont1.delete(0, END)
                alt_cont1.delete(0, END)
                fees1.delete(0, END)
                id1.insert(0, "")


def search():
        if(e1.get()==""):
                messagebox.showwarning("Fill Box","Fill the textbox")
                e1.insert(0,"")
        else:
                sql_select_Query="select * from Entries where id=%s"
                cur.execute(sql_select_Query,(e1.get(),))
                #messagebox.showinfo(": Note :", "Searching....")
                for data in cur:
                        e1.insert(0,str(data[0]))
                        e2.insert(0, str(data[1]))
                        e3.insert(0, str(data[2]))
                        e4.insert(0, str(data[3]))
                        e5.insert(0,str(data[4]))
                        e6.insert(0, str(data[5]))
                        e7.insert(0,str(data[6]))
                        e8.insert(0, str(data[7]))
                        e9.insert(0, str(data[8]))



def update():
        sql_update_Query="update Entries set passwd=%s,conf_passwd=%s,name=%s,address=%s,course=%s,cont=%s,alt_cont=%s,fees=%s where id=%s"
        data=[e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e1.get()]
        cur.execute(sql_update_Query,data)
        mydb.commit()
        messagebox.showinfo("Update","Record update Successfully")



def delete():
       sql_delete_query="delete from Entries where id=%s"
       cur.execute(sql_delete_query, (e1.get(),))
       mydb.commit()
       messagebox.showinfo("Delete", "Record Delete Successfully")


bt1=Button(top,text='Save',activeforeground='light green',command=save,activebackground='light green')
bt2=Button(top,text='Search',activeforeground='light green',command=search,activebackground='light green')
bt3=Button(top,text='Update',activeforeground='light green',command=update,activebackground='light green')
bt4=Button(top,text='Delete',activeforeground='light green',command=delete,activebackground='red')
bt5=Button(top,text='Cancel',activeforeground='light green',command=top.quit,activebackground='red')

bt1.place(x=50,y=250)
bt2.place(x=150,y=250)
bt3.place(x=250,y=250)
bt4.place(x=350,y=250)
bt5.place(x=450,y=250)

top.mainloop()

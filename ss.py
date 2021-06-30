from tkinter import Label,Button,Entry,Tk,StringVar
from instabot import Bot
from shutil import rmtree
from time import sleep
from os import getcwd
from threading import Thread
#execution starts from line 9
#To delete config folder
try:
        a = getcwd() + "\config"
        rmtree(a)
except FileNotFoundError:
        pass
#if file not exists the except block will execute
# excution tranfers to 78 line
#button command function
def ss():
 try:
    e14 =Label(text="Loging...!!!", bg="#161A27", fg="#5D9DFF", font="Normal 15 bold", padx=20).place(x=270, y=270,width=60)
    bot = Bot(unfollow_delay=4)
    def k():
        #getting username and password entry from entry box
        USERNAME = u2.get()
        PASSWORD = p2.get()
        #if login fails the login failed is shown on interface
        e14 =Label(text="Login Failed 1.Enter  correct Username and password \n      2.Disable 2fa autification(if enabled)", bg="#161A27", fg="#5D9DFF", font="Normal 15 bold", padx=20).place(x=50,y=270)
        #cheking login
        login = bot.login(username=USERNAME, password=PASSWORD)
        #if login failed line 26 shown if it is successfull then on line 26 label login succesfull is shown
        e15 =Label(text="Login Successfully\n",bg="#161A27", fg="#5D9DFF", font="Normal 15 bold").place(width=600,x=50, y=270)
        #control transfers to line 58
        def unf():
          #gathering following anf followers id's
          unfollowers = set(bot.following) - set(bot.followers)   
          #counting no. of unfollowes user and showing on interface 
          count = 0
          e16 =Label(text="Unfollowed %i/%i" %(count,len(unfollowers)),bg="#161A27", fg="#5D9DFF", font="Normal 15 bold").place(x=270,y=300)
          for i in unfollowers:
            bot.unfollow(i)
            count = count + 1
            e16 =Label(text="Unfollowed %i/%i   " % (count, len(unfollowers)), bg="#161A27", fg="#5D9DFF",font="Normal 15 bold").place(x=250, y=300)
            e17 =Label(text="Unfollowed %s"%bot.get_username_from_user_id(i), bg="#161A27", fg="#5D9DFF",font="Normal 15 bold").place(x=140, y=330,width=400)     
            if count == 49:
                    # if unfollowed users is equal to 49 and line 45 is show on interface
                    l00=Label(text="Sucessfully unfollowed 49 followers \n  excution stops for 5min to avoid action block",bg="#161A27",fg="#e64545",font="Normal 15 bold").place(x=50,y=370,width=600)
                    sleep(300)
                    #line 47 is used to disappear line 44 after 5minutes
                    l00 =Label(text=" \n  ",bg="#161A27", fg="#5D9DFF", font="Normal 15 bold").place(x=50, y=370, width=600)
                    
            if count == 98:
                #if no. of unfollwers 98 then this line excutets and loop is stoped
                l00=Label(text="Sucessfully unfollowed 98 followers \n  excution stops to avoid action block",bg="#161A27",fg="#5D9DFF",font="Normal 15 bold").place(x=26,y=370,width=600)
                l=Label(text="To avoid action block activity message from Instagram\n avoid use of this software more than 4-5 times within 24hr",bg="#161A27",fg="#e64545",font="Normal 15 bold").place(x=15,y=440,width=600)
                break
          sleep(10)
          exit(0)
        #to avoid not responding message on interface thread is used which excuteds further instructions
        t = Thread(target=unf).start()
        #control is tranfered to line 34
    #verifying username is given or not
    if u2.get()=="":
        e11 =Label(text="Insert Username", bg="#161A27", fg="#5D9DFF", font="Normal 15 bold",padx=20).place(width=400,x=150, y=270)
    #verifying password is given or not
    if p2.get()=="":
        e12 =Label(text="Insert  Password", bg="#161A27", fg="#5D9DFF", font="Normal 15 bold",padx=20).place(width=400,x=150,y=270)
    ##verifying both username and password is given or not
    if u2.get()=="" and p2.get()=="":
        e13 =Label(text="Insert Username and Passwoed Again", bg="#161A27", fg="#5D9DFF", font="Normal 15 bold",padx=20).place(width=400,
            x=130, y=270)
    #After verfiying both entries the control is pass to k() function line 21
    if u2.get()!="" and p2.get()!="":
        k()
    #except is block is used for safety to not terminate excution abnormally
 except:
     pass

#python gui
root=Tk()
# title,geometry,resizable
root.title("MS : Instagram Unfollower")
root.geometry("650x500")
root.resizable(0,0)
#background colour
back=Label(bg="#161A27")
back.place(x=0,y=0,height=500,width=650)
#headline
text=Label(text="INSTA AUTO UNFOLLOWER",fg="#42FF62",font=("Normal",25,"bold"),bg="#161A27")
text.place(x=100,y=26)
#username
u1=Label(text="Username :-",fg='white',font=("Normal",15),bg="#161A27")
u1.place(x=140,y=100)
u2=Entry(fg="white",insertbackground='white',bg="black",borderwidth=2,relief="groove",font=("Normal",13))
u2.place(x=260,y=100,height=30,width=200)
#password
p1=Label(text="Password :-",fg='white',font=("Normal",15),bg="#161A27")
p1.place(x=140,y=150)
p2=StringVar()
p22=Entry(fg="white",bg="black",insertbackground='white',textvariable=p2,borderwidth=2,relief="groove",font=('Normal',13),show="*")
p22.place(x=260,y=150,height=30,width=200)
#show hide button
def hide():
    p22=Entry(fg="white",textvariable=p2,bg="black",insertbackground='white',borderwidth=2,relief="groove",font=('Normal',13),show="*").place(x=260,y=150,height=30,width=200)
    p3=Button(fg="white",bg="#161A27",borderwidth=3,relief="groove",text="show",command=show).place(x=470,y=153,height=25)
def show():
    p22=Entry(fg="white",bg="black",insertbackground='white',borderwidth=2,relief="groove",font=('Normal',13),textvariable=p2).place(x=260,y=150,height=30,width=200)
    p3=Button(fg="white",bg="#161A27",borderwidth=3,relief="groove",text=" hide",command=hide).place(x=470,y=153,height=25)
p3=Button(fg="white",bg="#161A27",borderwidth=2,relief="groove",text="show",command=show).place(x=470,y=153,height=25)

#confirm button
b1=Button(text="Confirm",bg="black",fg="white",font=("Normal",13),borderwidth=2,relief="groove",command=ss)
b1.place(x=270,y=200,height=40,width=130)
#excution tranferes to line 17
e113 =Label(text="Wait 1min after pressing confirm button", bg="#161A27", fg="#5D9DFF", font="Normal 15 bold",padx=20).place(width=400, x=130, y=270)

root.mainloop()
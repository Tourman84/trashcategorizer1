import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import StringVar
# from showertime import Clock
from showertime import shower_main

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.username1 = StringVar()
        self.password1 = StringVar()
        self.geometry('300x230')
        self.title('Login page')
        
        tkinter.Label(self, text = "Username").grid(row = 0)
        tkinter.Entry(self, textvariable=self.username1).grid(row = 0, column = 1) 


        tkinter.Label(self, text = "Password").grid(row = 1)
        tkinter.Entry(self,textvariable=self.password1).grid(row = 1, column = 1) 


        tkinter.Checkbutton(self, text = "Keep Me Logged In").grid(columnspan=2)
        ttk.Button(self,
                text='Login',
                command=self.validate_login).grid() 
    def start_showertime(self):
      clock = shower_main()
      clock.menu()
    def validate_login(self):
      #username: a password: b
      with open('user_info.txt','r') as file:
              user_check=file.readline()
              password_check=file.readline()         
              file.close()
      user_name_1 = self.username1.get() +"\n"
      password_user_1 = self.password1.get() + "\n"
      
      if user_check == user_name_1 and password_user_1 == password_check:
        ttk.Button(self, text='successful, click here to start', command=self.start_showertime).grid() 
        
      else:
        print("wrong username or password") 
    
        tkinter.Button(self, text='click login to try again',bg = "red",height="1").grid() 
         
        

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x200")
        self.title("Login Page")
        tkinter.Label(text="Login to the program", bg="red", width="30", height="2", font=("Calibri", 13)).pack()
        tkinter.Label(text="").pack() 
        # create Login Button 
        tkinter.Button(self,text="login", height="2", width="30", command = self.open_window).pack() 
        # ttk.Button(self,text="login",command = self.open_window).pack()
        tkinter.Label(text="").pack() 

        tkinter.Button(self,text="register", height="2", width="30", command = self.open_window2).pack() 
        # ttk.Button(self,text="login",command = self.open_window).pack()
        tkinter.Label(text="").pack() 

    def open_window(self):
        window = Window(self)
        window.grab_set()

    def open_window2(self):
        window2 = Window2(self)
        window2.grab_set()

class Window2(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()

        self.geometry('300x200')
        self.title('Register page')
        
        tkinter.Label(self, text = "Username").grid(row = 0)
        tkinter.Entry(self, textvariable=self.username).grid(row = 0, column = 1) 

        tkinter.Label(self, text = "Password").grid(row = 1)
        tkinter.Entry(self,textvariable=self.password).grid(row = 1, column = 1) 

        tkinter.Label(self, text = "email").grid(row = 2)
        tkinter.Entry(self,textvariable=self.email).grid(row = 2, column = 1)

        
        ttk.Button(self, text='done', command=self.validate_register).grid()

    def validate_register(self):
          #username: a password: b
          user_name = self.username.get()
          password_user = self.password.get()
          email_user = self.email.get()
          
          if user_name != "" and password_user != "" and email_user !="":
            print("register successful")
            with open('user_info.txt','w') as file:
              file.write(user_name+"\n")
              file.write(password_user+"\n")
              file.write(email_user)
              file.close()
            
          else:
            print("incomplete register form，please fill in all the terms.") 

class sample():
  def func():
    print("sample")


if __name__ == "__main__":
    app = App()
    app.mainloop()
from selenium import webdriver
from getpass import getpass
import customtkinter as ctk
import tkinter.messagebox as tkmb 
import time  
import subprocess
import sys
import re
import json


a = None
b = None
c = None

# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("light") 
  
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 
  
app = ctk.CTk() 
app.geometry("400x400") 
app.title("PowerBI Load Testing") 



def next_script(a,b,c):

    report_count = int(a)
    workspace_selection = int(b)
    report_selection = int(c)

    # Execute the PowerShell script with inputs
    process = subprocess.Popen(['powershell.exe', '-File', 'C:\\Users\\09428516\\Documents\\website_login\\PowerBI-Tools-For-Capacities-master\\RealisticLoadTestTool\\Setup_Load_Test.ps1'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    
    # Provide inputs to the PowerShell script
    process.stdin.write(f"{report_count}\n")
    process.stdin.write(f"{workspace_selection}\n")
    process.stdin.write(f"{report_selection}\n")
    process.stdin.close()

    # Capture the output of the PowerShell script
    output, error = process.communicate()



    def run(val2):
        process2 = subprocess.Popen(['powershell.exe', '-File',
                                    'C:\\Users\\09428516\\Documents\\website_login\\PowerBI-Tools-For-Capacities-master\\RealisticLoadTestTool\\Run_Load_Test_Only.ps1'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True)
        process2.stdin.write(f"{val2}\n")
        process.stdin.close()
        # Capture the output of the PowerShell script
        output, error = process2.communicate()

    new_window3 = ctk.CTkToplevel(app)

    new_window3.title("Enter number of instances to initiate for each report")

    new_window3.geometry("500x500")

# Create a frame to hold the list elements
    frame = ctk.CTkFrame(master=new_window3)
    frame.pack(padx=10, pady=10)
    input_box3 = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
    input_box3.pack(pady=12,padx=10)
    nxt_text=input_box3.get()
    nxt_input = int(nxt_text)
    button3 = ctk.CTkButton(master=frame,text='Run',command= lambda: run(nxt_input) )
    button3.pack(pady=12,padx=10)

def next_win(val):

    new_window2 = ctk.CTkToplevel(app)
  
    new_window2.title("List of all reports from the selected work space")

    new_window2.geometry("500x500")

    # Create a frame to hold the list elements
    frame = ctk.CTkFrame(master=new_window2)
    frame.pack(padx=10, pady=10)

    items1 = ["[1] - e44dd72c-460a-472f-bf65-f4d04485fd9d - Feature Usage and Adoption", "[2] - 912f32f3-1104-4d51-9343-6b721f8ff72f - Purview Hub"]
    items2 = ["[1] - 8bd1cae6-0ea3-42c0-b8a8-b117edb71311 - Realtime - AMESA-APAC Dataset Refresh Status", "[2] - d3f29fb3-953b-46bc-a1df-21a302982aee - DLPTest"]
    items3 = ["empty"]
    items4 = ["[1] - 8993f814-4470-471a-8dd4-f870e524779e - DLPTest", "[2] - 754ca2fa-3063-4689-9649-ebb13fbbfff1 - DLP1","[3] - 5197f2c3-37fa-47ee-a2bc-b37e579d5b3b - DLP2","[4] - c3024411-25f5-410c-8160-6ef6efa19d82 - DLPNewTest","[5] - 989f141d-5556-4448-aa6f-12484079d336 - IOTBI_Report"]
    items5 = ["[1] - 0e92e861-ed84-49ad-859d-c8f48d9769e2 - Fabric Capacity Metrics Preview", "[2] - 0e92e861-ed84-49ad-859d-c8f48d9769e2 - Fabric Capacity Metrics Preview"]
    items6 = ["[1] - 04af5d57-9085-4dd5-85d7-5f2d76b02a4d - Power BI Management Template Report"]
    items7 = ["[1] - 07bf643f-d709-482e-9f63-8f5de931204a - Power BI Management Template Report"]

    if val=="1":
        # Create a single CTkLabel
        label = ctk.CTkLabel(master=frame, text="\n".join(items1))
        label.pack()  # Add the label to the frame
        input_box2 = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
        input_box2.pack(pady=12,padx=10)
    elif val=="2":
        # Create a single CTkLabel
        label = ctk.CTkLabel(master=frame, text="\n".join(items2))
        label.pack()  # Add the label to the frame
        input_box2 = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
        input_box2.pack(pady=12,padx=10)
    elif val=="3":
        # Create a single CTkLabel
        label = ctk.CTkLabel(master=frame, text="\n".join(items3))
        label.pack()  # Add the label to the frame
        input_box2 = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
        input_box2.pack(pady=12,padx=10)
    elif val=="4":
        # Create a single CTkLabel
        label = ctk.CTkLabel(master=frame, text="\n".join(items4))
        label.pack()  # Add the label to the frame
        input_box2 = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
        input_box2.pack(pady=12,padx=10)
    elif val=="5":
        # Create a single CTkLabel
        label = ctk.CTkLabel(master=frame, text="\n".join(items5))
        label.pack()  # Add the label to the frame
        input_box2 = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
        input_box2.pack(pady=12,padx=10)
    elif val=="6":
        # Create a single CTkLabel
        label = ctk.CTkLabel(master=frame, text="\n".join(items6))
        label.pack()  # Add the label to the frame
        input_box2 = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
        input_box2.pack(pady=12,padx=10)
    elif val=="7":
        label = ctk.CTkLabel(master=frame, text="\n".join(items7))
        label.pack()  # Add the label to the frame
        input_box2 = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
        input_box2.pack(pady=12,padx=10)
    #global c
    #c=input_box2.get()

    #c = str(ws_text2).encode() + b"\n"
    #process.communicate(input=ws_input2)
    def getin2():
        global c
        c=input_box2.get()
        next_script(a,b,c)

    button2 = ctk.CTkButton(master=frame,text='Next',command= getin2)
    button2.pack(pady=12,padx=10)

def login(): 
    username = user_entry.get()
    password = user_pass.get()

    global a
    a = num_reports.get()

    #a = str(reports).encode() + b"\n"
    driver = webdriver.Chrome()
    #driver.implicitly_wait(200)
    def login(url,usernameId, username, passwordId, password, submit_buttonId):
        #tkmb.showinfo(title="Welcome to PepsiCo",message="Redirecting to PepsiCo Portal")
        driver.get(url)

        driver.find_element("id",usernameId).send_keys(username)
        driver.find_element("id",passwordId).send_keys(password)
        driver.find_element("id",submit_buttonId).submit()

        #master.destroy()


        time.sleep(30)
        tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")

        # Convert the age to a byte string with newline character
        #report_input = str(reports).encode() + b"\n"  # Convert age to string, encode as bytes, and add newline

        # Construct the PowerShell command
        #command = ["powershell.exe", "-File", "C:\\Users\\09428516\\Documents\\website_login\\PowerBI-Tools-For-Capacities-master\\RealisticLoadTestTool\\Setup_Load_Test.ps1"]
        #global process
        # Create a subprocess and provide age as input
        #process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        #output, err = process.communicate(input=report_input)

        new_window = ctk.CTkToplevel(app)
  
        new_window.title("Select Work space index from below")

        new_window.geometry("500x500")

        # Create a frame to hold the list elements
        frame = ctk.CTkFrame(master=new_window)
        frame.pack(padx=10, pady=10)  # Add padding around the frame


        # Print the PowerShell script's output
                #t=output.decode()
                # Define your list items
        items = ["[1] - 15e0e655-f3fd-4650-8c4c-3a93ba996a76 - Admin monitoring", "[2] - ab7968ad-93df-43db-b0e5-bd7d9b3f6ff8 - DLPTest", "[3] - 16163183-6a58-4191-b60d-3e73738bb0a8 - DLPTestPro","[4] - e88fb875-fe1d-4c49-a586-9f043d04e772 - DLPFabricTrailTest","[5] - 8cb48ffd-eadc-45d3-90b1-8e2f88025e47 - Microsoft Fabric Capacity Metrics","[6] - ee665452-f973-4998-9c2f-a069d314b060 - Power BI Management Report","[7] - a0c2d19f-6bcf-44d9-96a5-37c2e9137fa6 - Power BI Service Management Report"]

                # Create a single CTkLabel
        label = ctk.CTkLabel(master=frame, text="\n".join(items))
        label.pack()  # Add the label to the frame

        input_box = ctk.CTkEntry(master=frame, width=20, placeholder_text="Enter list item")
        input_box.pack(pady=12,padx=10)


        #b=input_box.get()

        #b = str(ws_text).encode() + b"\n"
        #process.communicate(input=ws_input)
        def getin():
            global b
            b = input_box.get()
            next_win(b)
        button = ctk.CTkButton(master=frame,text='Next',command=getin)
        button.pack(pady=12,padx=10)


        #ctk.CTkLabel(new_window,text="[1] - 15e0e655-f3fd-4650-8c4c-3a93ba996a76 - Admin monitoring\n[2] - ab7968ad-93df-43db-b0e5-bd7d9b3f6ff8 - DLPTest\n[3] - 16163183-6a58-4191-b60d-3e73738bb0a8 - DLPTestPro\n[4] - e88fb875-fe1d-4c49-a586-9f043d04e772 - DLPFabricTrailTest\n[5] - 8cb48ffd-eadc-45d3-90b1-8e2f88025e47 - Microsoft Fabric Capacity Metrics 6/12/2023 4:39:16 PM\n[6] - ee665452-f973-4998-9c2f-a069d314b060 - Power BI Management Report\n[7] - a0c2d19f-6bcf-44d9-96a5-37c2e9137fa6 - Power BI Service Management Report").pack()
        #print(output.decode())
        #driver.implicitly_wait(50)
    login("https://secure.mypepsico.com/associatesso/login", "userid", username, "password", password, "submit")
    #driver.implicitly_wait(20)
 

  
label = ctk.CTkLabel(app,text="Welcome to PepsiCo") 
  
label.pack(pady=20) 
  
  
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=30,padx=50,fill='both',expand=True) 
  
label = ctk.CTkLabel(master=frame,text='SSO Login') 
label.pack(pady=12,padx=10) 
  
  
user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 
  
user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 

num_reports= ctk.CTkEntry(master=frame,placeholder_text="reports to configure?")
num_reports.pack(pady=12,padx=10)
  
  
button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 
  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 
  
  
app.mainloop()


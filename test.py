import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading
import json

powershell_process = None
additional_input_entry_2 = None
output_text = None

def read_output(output_text):
    global powershell_process

    # Read and display the output continuously
    for line in powershell_process.stdout:
        output_text.insert(tk.END, line)
        output_text.see(tk.END)  # Scroll to the end of the text widget

def run_powershell_script(report_count_entry):
    global powershell_process, output_text

    # Get report count input
    report_count = report_count_entry.get()

    try:
        # Start the PowerShell script with report count input
        powershell_process = subprocess.Popen(['powershell.exe', '-File', 'C:\\Users\\09428516\\Documents\\website_login\\PowerBI-Tools-For-Capacities-master\\RealisticLoadTestTool\\Setup_Load_Test.ps1'],
                                               stdin=subprocess.PIPE,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE,
                                               universal_newlines=True)

        # Send the report count input to the PowerShell script
        powershell_process.stdin.write(f"{report_count}\n")
        powershell_process.stdin.flush()

        # Launch the second screen for output and additional input
        launch_output_screen()

    except Exception as e:
        # Display error message in the UI
        output_text.insert(tk.END, f"Error: {e}\n")

def send_additional_input(additional_input_entry, send_input_button):
    global powershell_process, output_text

    try:
        if powershell_process is None:
            raise RuntimeError("No PowerShell process is currently running")

        # Get additional input from the user
        additional_input = additional_input_entry.get() + '\n'

        # Send the additional input to the running PowerShell script
        powershell_process.stdin.write(additional_input)
        powershell_process.stdin.flush()

        # Disable input fields after sending additional input
        additional_input_entry.delete(0, tk.END)
        additional_input_entry.config(state=tk.DISABLED)
        send_input_button.config(state=tk.DISABLED)

    except Exception as e:
        # Display error message in the UI
        output_text.insert(tk.END, f"Error: {e}\n")

def getin():
    global additional_input_entry_2
    def write_json():
        # Get user inputs
        # report_url = report_url_entry.get()
        page_name = page_name_entry.get()
        bookmark_list = bookmark_list_entry.get().split(',')
        session_restart = int(session_restart_entry.get())
        think_time_seconds = int(think_time_seconds_entry.get())

        # Get filters inputs
        filters = []
        for i in range(len(filter_entries)):
            filter_table = filter_entries[i]['table_entry'].get()
            filter_column = filter_entries[i]['column_entry'].get()
            is_slicer = filter_entries[i]['is_slicer_var'].get()
            filters_list = filter_entries[i]['list_entry'].get().split(',')
            filters.append({
                "filterTable": filter_table,
                "filterColumn": filter_column,
                "isSlicer": is_slicer,
                "filtersList": filters_list
            })

        # Create reportParameters dictionary
        report_parameters = {
            "reportUrl": "",
            "pageName": page_name,
            "bookmarkList": bookmark_list,
            "sessionRestart": session_restart,
            "filters": filters,
            "thinkTimeSeconds": think_time_seconds
        }

        # Write to JSON file with variable assignment
        with open('PBIReport.json', 'w') as json_file:
            json_file.write("reportParameters = ")
            json.dump(report_parameters, json_file, indent=4)

        send_additional_input_2(additional_input_entry_2)

    # Create Tkinter window
    window = tk.Tk()
    window.title("Create JSON File")
    window.geometry("400x500")

    # Add input fields for keys in the JSON file
    page_name_label = tk.Label(window, text="Page Name:")
    page_name_label.pack()
    page_name_entry = tk.Entry(window)
    page_name_entry.pack()

    bookmark_list_label = tk.Label(window, text="Bookmark List (comma-separated):")
    bookmark_list_label.pack()
    bookmark_list_entry = tk.Entry(window)
    bookmark_list_entry.pack()

    session_restart_label = tk.Label(window, text="Session Restart:")
    session_restart_label.pack()
    session_restart_entry = tk.Entry(window)
    session_restart_entry.pack()

    think_time_seconds_label = tk.Label(window, text="Think Time (seconds):")
    think_time_seconds_label.pack()
    think_time_seconds_entry = tk.Entry(window)
    think_time_seconds_entry.pack()

    # Add input fields for 'filters'
    filter_frame = tk.Frame(window)
    filter_frame.pack(pady=10, padx=10)

    filter_entries = []

    # Add a button to add new filter entry
    def add_filter_entry():
        filter_entry = {}

        table_label = tk.Label(filter_frame, text="Filter Table:")
        table_label.grid(row=len(filter_entries), column=0)
        filter_entry['table_entry'] = tk.Entry(filter_frame)
        filter_entry['table_entry'].grid(row=len(filter_entries), column=1)

        column_label = tk.Label(filter_frame, text="Filter Column:")
        column_label.grid(row=len(filter_entries), column=2)
        filter_entry['column_entry'] = tk.Entry(filter_frame)
        filter_entry['column_entry'].grid(row=len(filter_entries), column=3)

        is_slicer_label = tk.Label(filter_frame, text="Is Slicer:")
        is_slicer_label.grid(row=len(filter_entries), column=4)
        filter_entry['is_slicer_var'] = tk.BooleanVar()
        filter_entry['is_slicer_checkbox'] = tk.Checkbutton(filter_frame, variable=filter_entry['is_slicer_var'])
        filter_entry['is_slicer_checkbox'].grid(row=len(filter_entries), column=5)

        list_label = tk.Label(filter_frame, text="Filters List (comma-separated):")
        list_label.grid(row=len(filter_entries), column=6)
        filter_entry['list_entry'] = tk.Entry(filter_frame)
        filter_entry['list_entry'].grid(row=len(filter_entries), column=7)

        filter_entries.append(filter_entry)

    add_filter_entry_button = tk.Button(window, text="Add Filter", command=add_filter_entry)
    add_filter_entry_button.pack()

    # Button to create the JSON file
    create_button = tk.Button(window, text="Create JSON File", command=write_json)
    create_button.pack()

def send_additional_input_2(additional_input_entry_2):
    global powershell_process

    try:
        if powershell_process is None:
            raise RuntimeError("No PowerShell process is currently running")

        # Get Additional Input 2 from the user
        additional_input_2 = additional_input_entry_2.get() + '\n'

        # Send Additional Input 2 to the running PowerShell script
        powershell_process.stdin.write(additional_input_2)
        powershell_process.stdin.flush()

        # Disable input fields after sending Additional Input 2
        additional_input_entry_2.delete(0, tk.END)
        additional_input_entry_2.config(state=tk.DISABLED)

        def run(d):
            instance_num = int(d)
            process2 = subprocess.Popen(['powershell.exe', '-File',
                                         'C:\\Users\\09428516\\Documents\\website_login\\PowerBI-Tools-For-Capacities-master\\RealisticLoadTestTool\\Run_Load_Test_Only.ps1'],
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        universal_newlines=True)
            process2.stdin.write(f"{instance_num}\n")
            process2.stdin.close()
            # Capture the output of the PowerShell script
            output, error = process2.communicate()

        new_window3 = tk.Toplevel(window)

        new_window3.title("Enter number of instances to initiate for each report")

        new_window3.geometry("500x500")

        # Create a frame to hold the list elements
        frame = tk.Label(new_window3, text="Enter Additional Input:")
        frame.pack(padx=10, pady=10)
        input_box3 = tk.Entry(new_window3)
        input_box3.pack(pady=12, padx=10)

        # global d
        def get3():
            d = input_box3.get()
            run(d)

        # print(d)
        # nxt_input = int(nxt_text)
        button3 = tk.Button(new_window3, text='Run', command=get3)
        button3.pack(pady=12, padx=10)

    except Exception as e:
        # Display error message in the UI
        output_text.insert(tk.END, f"Error: {e}\n")

def launch_output_screen():
    global output_text

    output_screen = tk.Toplevel(window)
    output_screen.title("PowerShell Output")
    output_screen.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    # Text widget to display the output
    output_text = scrolledtext.ScrolledText(output_screen, width=50, height=10)
    output_text.pack(expand=True, fill='both')

    # Start a thread to continuously read the output
    output_thread = threading.Thread(target=read_output, args=(output_text,))
    output_thread.start()

    # Entry field for additional input
    additional_input_label = tk.Label(output_screen, text="Enter Additional Input:")
    additional_input_label.pack()
    additional_input_entry = tk.Entry(output_screen)
    additional_input_entry.pack()

    # Button to send additional input to the running PowerShell script
    send_input_button = tk.Button(output_screen, text="Send Additional Input", command=lambda: send_additional_input(additional_input_entry, send_input_button))
    send_input_button.pack()

    # Entry field for additional input 2
    additional_input_label_2 = tk.Label(output_screen, text="Enter Additional Input 2:")
    additional_input_label_2.pack()
    global additional_input_entry_2
    additional_input_entry_2 = tk.Entry(output_screen)
    additional_input_entry_2.pack()

    # Button to trigger getin function
    getin_button = tk.Button(output_screen, text="Open Additional Input 2", command=getin)
    getin_button.pack()

# Create Tkinter window
window = tk.Tk()
window.title("PowerShell Script Runner")
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

# Entry field for report count input
report_count_label = tk.Label(window, text="Enter Report Count:")
report_count_label.grid(row=0, column=0)
report_count_entry = tk.Entry(window)
report_count_entry.grid(row=0, column=1)

# Button to run the PowerShell script with report count input
run_button = tk.Button(window, text="Run PowerShell Script", command=lambda: run_powershell_script(report_count_entry))
run_button.grid(row=0, column=2)

# Run Tkinter event loop
window.mainloop()
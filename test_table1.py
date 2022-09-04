import PySimpleGUI as sg

#  CRUD example, showing how to Add entries to a Table
#  When the user selects a table row, show the values in the Top row 
#  How to update Table when the user edits the values and clicks on the check box "Update Table "
#  How to Refresh Table after adding or updating a record 

col_headings = ['President', 'Date of Birth']

data = [
    ['Ronald Reagan', 'February 6'],
    ['Abraham Lincoln', 'February 12'],
    ['George Washington', 'February 22'],
    ['Andrew Jackson', 'March 15'],
    ['Thomas Jefferson', 'April 13'],
    ['Harry Truman', 'May 8'],
    ['John F. Kennedy', 'May 29'],
    ['George H. W. Bush', 'June 12'],
    ['George W. Bush', 'July 6'],
    ['John Quincy Adams', 'July 11'],
    ['Garrett Walker', 'July 18'],
    ['Bill Clinton', 'August 19'],
    ['Jimmy Carter', 'October 1'],
    ['John Adams', 'October 30'],
    ['Theodore Roosevelt', 'October 27'],
    ['Frank Underwood', 'November 5'],
    ['Woodrow Wilson', 'December 28'],
]

layout = [[sg.Text('President Name : '),sg.Input(key='-president-')],
          [sg.Text('Date of Birth  : '),sg.Input(key='-dob-')], 
          [sg.Checkbox('Update Table', default=False,enable_events=True, key='-update_table_checked-')],
          [sg.Button('Add',key='-add_click-'),sg.Button('Update',disabled = True,key='-update_click-'), sg.Cancel(key='-cancel_click-')],
          [sg.Table(data, headings=col_headings, 
           justification='left', 
           max_col_width=25,
           auto_size_columns=True,
           enable_events=True,
           display_row_numbers=True,     
           select_mode=sg.TABLE_SELECT_MODE_BROWSE, # remove this for multi row select     
           alternating_row_color='lightblue',
           num_rows=min(len(data), 6),
           key='-TABLE-')],
           ]
window = sg.Window("Title", layout, finalize=True)
president_list=[]
#window.bind('<Prior>', "PgUp")
#window.bind('<Next>', "PgDn")

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "-cancel_click-":
        break
    elif event == "-update_table_checked-":
        if values['-update_table_checked-'] == False:
           window['-update_click-'].Update(disabled = True)
        elif values['-update_table_checked-'] == True:    
           window['-update_click-'].Update(disabled = False) 
    elif event == "-TABLE-":   
        window['-update_click-'].Update(disabled = True)        
        window['-update_table_checked-'].Update(value = False)                
        selected_row = values["-TABLE-"][0]
        print(selected_row)
        data_selected = [data[row] for row in values[event]] 
        president_list= data_selected[0]      
        window['-president-'].update(president_list[0])
        window['-dob-'].update(president_list[1])        
        #window.Element('-president-').update(president_list[0])
        #window.Element('-dob-').update(president_list[1])        
    elif event == "-add_click-":  
       president_list = []   
       president_list.append(values["-president-"])
       president_list.append(values["-dob-"])
       data.append(president_list)
       window['-TABLE-'].Update(values=data) # this will refresh the table
    elif event == "-update_click-":           
       data[selected_row][0] =  values["-president-"]
       data[selected_row][1] =  values["-dob-"]       
       window['-TABLE-'].Update(values=data) # this will refresh the table      
window.close()

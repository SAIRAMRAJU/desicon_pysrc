import PySimpleGUI as sg

#  CRUD example, showing how to Add entries to a Table
#  Also updates to SQL Server Database 
#  When the user selects a table row, show the values in the Top row 
#  How to update Table when the user edits the values and clicks on the check box "Update Table "
#  How to Refresh Table after adding or updating a record 

def clear_form(window):
    window['-president-'].update("")
    window['-dob-'].update("")     

def disable_update_button(window):
    window['-update_click-'].Update(disabled = True)  # Disabled
    window['-error-'].update(" "*50)   

def enable_update_button(window):
    window['-update_click-'].Update(disabled = False)  # Enabled
    window['-error-'].update(" "*50)   

def disable_delete_button(window):
    window['-delete_click-'].Update(disabled = True)  # Disabled
    window['-error-'].update(" "*50)   

def enable_delete_button(window):
    window['-delete_click-'].Update(disabled = False)  # Enabled
    window['-error-'].update(" "*50)   

def post_update_delete_tasks(window):
    window['-delete_click-'].Update(disabled = True) # disabling after Update/Deletion,wait for row click to enable
    window['-update_click-'].Update(disabled = True) # disabling after Update/Deletion,wait for row click to enable
    window['-update_table_checked-'].Update(disabled = True) # disabling after Update/Deletion,wait for row click to enable
    clear_form(window)
def check_and_enable_update_button(window,row_data_list,values):
    if row_data_list[0] != values["-president-"] or \
       row_data_list[1] != values["-dob-"]:           
       enable_update_button(window)
    else:
       window['-error-'].update("Values same as in Table row - Nothing to update...")        
       window['-update_table_checked-'].Update(value = False)


def display_selected_row_in_form(window,event,values,data):
    disable_update_button(window)    # Disabled - Wait for update checkbox to Enable
    window['-update_table_checked-'].Update(disabled = False) # Enabled now               
    window['-update_table_checked-'].Update(value = False)  # The check box should be un-checked    
    enable_delete_button(window)    # Disabled - Wait for delete checkbox to Enable        
    data_selected = [data[row] for row in values[event]] 
    row_data_list= data_selected[0]      
    window['-president-'].update(row_data_list[0])
    window['-dob-'].update(row_data_list[1])      
    return row_data_list

def add_click_event(window,values,data):
    row_data_list = []   
    # We have to add validations field wise here with elif logic if required....
    if values["-president-"]: # Main field is not empty 
       row_data_list.append(values["-president-"])
       row_data_list.append(values["-dob-"])
       data.append(row_data_list)
       window['-TABLE-'].Update(values=data) # this will refresh the table
       clear_form(window)    
       disable_delete_button(window)
    else:
       window['-error-'].update("Cannot add empty data - Nothing to Add ...")                
    return data,row_data_list
def update_click_event(window,values,data,selected_row_number):
    # We have to add validations field wise here with if, elif logic if required....    
    data[selected_row_number][0] =  values["-president-"]
    data[selected_row_number][1] =  values["-dob-"]       
    window['-TABLE-'].Update(values=data) # this will refresh the table   
    post_update_delete_tasks(window)
    return data
def delete_click_event(window,values,data,selected_row_number):
    option = sg.PopupOKCancel("Do you want to Delete the Row ? ")
    if option == 'OK': 
       data.pop(selected_row_number)
       window['-TABLE-'].Update(values=data) # this will refresh the table          
       post_update_delete_tasks(window)
    return data

def main():

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
            [sg.Checkbox('Update Table Row', default=False,enable_events=True, key='-update_table_checked-')],
            # [sg.Checkbox('Delete Table Row', default=False,enable_events=True, key='-delete_table_checked-')],
            [sg.Button('Add',key='-add_click-'),
            sg.Button('Update',disabled = True,key='-update_click-'),
            sg.Button('Delete',disabled = True,key='-delete_click-'),
            sg.Button('Quit',key='-quit_click-')],
            [sg.Table(data, headings=col_headings, 
            justification='left', 
            max_col_width=25,
            auto_size_columns=True,
            enable_events=True,
            display_row_numbers=True,     
            select_mode=sg.TABLE_SELECT_MODE_BROWSE, # remove this for multi row select     
            # alternating_row_color='lightblue' ->  not required for CRUD
            num_rows=min(len(data), 6),
            key='-TABLE-')],
            [sg.Text('',text_color='red', key='-error-')],   # To show error message based on validation
            ]
    window = sg.Window("Title", layout, finalize=True)
    row_data_list=[]

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-quit_click-":
            break
        elif event == "-update_table_checked-":       
            if values['-update_table_checked-'] == False:
               disable_update_button(window)
            elif values['-update_table_checked-'] == True: 
                 check_and_enable_update_button(window,row_data_list,values)
        elif event == "-TABLE-":    # User has selected a Row
            if len(values["-TABLE-"]) != 0:
               selected_row_number = values["-TABLE-"][0]  #  This returns the selected row number              
               row_data_list = display_selected_row_in_form(window,event,values,data)         
        elif event == "-add_click-":             
           data,row_data_list=add_click_event(window,values,data)
        elif event == "-update_click-":       
           data=update_click_event(window,values,data,selected_row_number)                
        elif event == "-delete_click-": 
           data=delete_click_event(window,values,data,selected_row_number)                            

    window.close()

if __name__ == "__main__":
    main()

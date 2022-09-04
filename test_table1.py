import PySimpleGUI as sg

headings = ['President', 'Date of Birth']

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
          [sg.Table(data, headings=headings, 
           justification='left', 
           max_col_width=25,
           auto_size_columns=True,
           alternating_row_color='lightblue',
           num_rows=min(len(data), 20),
           key='-TABLE-')],[sg.Output(size=(128, 4))],]
window = sg.Window("Title", layout, finalize=True)
president_list=[]
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(event, values)
    president_list[0] = values["-president-"]
    president_list[1] = values["-dob-"]

window.close()

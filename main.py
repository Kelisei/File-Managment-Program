import PySimpleGUI as sg
import string
import csv, os
actual_directory = os.getcwd()
windows = not '/' in actual_directory
print(windows)
print(actual_directory)
sg.set_options(font='Helvetica 12')
sg.theme('DarkBlack1')
layout =[
            [sg.Text('Choose filepath:',size=(20, 1)), sg.Input(), sg.FileBrowse(initial_folder=actual_directory, button_text='Search files', key='-FILEPATH-')], 
            [sg.Text('Choose shortcut name:',size=(20, 1)), sg.Input(key='-FILENAME-')],
            [sg.Button(button_text='Add'), sg.Text(key='-ERRORTEXT-', text_color='Red')],
            [sg.Text(key='-FILEPATHS-')]
        ]
filepaths = {}
window = sg.Window('File manager', layout, resizable=True)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Add':
        if values['-FILEPATH-'] in filepaths.values():
            window['-ERRORTEXT-'].update('File already added')
        elif values['-FILEPATH-'] == '': 
            window['-ERRORTEXT-'].update('Invalid filepath')
        elif values['-FILENAME-'] == '':
            window['-ERRORTEXT-'].update('Invalid name')
        elif values['-FILENAME-'] in filepaths.keys():
            window['-ERRORTEXT-'].update('Name already added')
        else:
            if windows: 
                filepath = str(values['-FILEPATH-']).replace('/', '\\')
            else:
                filepath = values['-FILEPATH-']
            filepaths[values['-FILENAME-']] = filepath
            text = ''
            for name, path in filepaths.items():
                text+= f'{name}: {path} \n'
            window['-FILEPATHS-'].update(text)
            window['-ERRORTEXT-'].update('')
            os.startfile(filepath)

window.close()
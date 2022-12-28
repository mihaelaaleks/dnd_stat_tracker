import PySimpleGUI as sg
import random

sg.theme('DarkAmber')
def roll_dice(max):
    min = 1
    max = max
    rolled_dice = random.randint(min, max)
        
    return rolled_dice

#each array within first_column represents a row
first_column = [[sg.Text('D&D Dice Helper', font='Courier 54')],
          [sg.Button('D20', font=("", 10, "bold"), size=(10, 5)), sg.Button('D12', font=("", 10, "bold"), size=(10, 5))],
          [sg.Button('D10', font=("", 10, "bold"), size=(10, 5)),sg.Button('D8', font=("", 10, "bold"), size=(10, 5))],
          [sg.Button('D6', font=("", 10, "bold"), size=(10, 5)), sg.Button('D4', font=("", 10, "bold"), size=(10, 5))],
          [sg.Button('D100', font=("", 10, "bold"), size=(10, 5))],
          [sg.Text('Your roll:', font='Courier 54', key= '_text_', visible = True), sg.Text('Dice', font='Courier 54', key= '_text2_', visible = True)]
          ]

second_column = [[sg.Button('EXIT', button_color = 'Red', font=("", 10, "bold"), size=(10, 5))]]

layout = [[sg.Column(first_column)],
          [sg.VSeparator()],
          [sg.Column(second_column)]]

window = sg.Window('D&D Tool', layout).Finalize()
window.Maximize()

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'D20':
        window['_text2_'].update(f'{roll_dice(20)}')
    if event == 'D12':
        window['_text2_'].update(f'{roll_dice(12)}')
    if event == 'D10':
        window['_text2_'].update(f'{roll_dice(10)}')
    if event == 'D8':
        window['_text2_'].update(f'{roll_dice(8)}')
    if event == 'D6':
        window['_text2_'].update(f'{roll_dice(6)}')
    if event == 'D4':
        window['_text2_'].update(f'{roll_dice(4)}')
    if event == 'D100':
        window['_text2_'].update(f'{roll_dice(100)}')
window.close()
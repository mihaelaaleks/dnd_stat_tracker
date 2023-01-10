import PySimpleGUI as sg
from dice import Dice
import character_sheet_reader as csr

d20 = Dice(20)
d12 = Dice(12)
d10 = Dice(10)
d8 = Dice(8)
d6 = Dice(6)
d4 = Dice(4)
d100 = Dice(100)

sg.theme('DarkAmber')
font_preset = 'Courier 32'
sg.set_options(font = font_preset)
default = 'a'

base_stat_labels = ['Strength:', 'Dexterity:', 'Constitution:', 'Wisdom:', 'Intelligence:', 'Charisma:']

strength_skills = ['Athletics:']
dexterity_skills = ['Acrobatics:', 'Sleight of Hand:', 'Stealth:']
intelligence_skills = ['Arcana:', 'History:', 'Investigation:', 'Nature:', 'Religion:']
wisdom_skills = ['Animal Handling:', 'Insight:', 'Medicine:', 'Perception:', 'Survival:']
charisma_skills = ['Deception:', 'Intimidation:', 'Performance:', 'Persuasion:']

main_char_labels = ['Character name:','Class:', 'Level:', 'Background:', 'Player name:', 'Race:', 'Alignment:', 'XP points:', 'Hit Points:', 'Armor Class:' ]

skill_labels = strength_skills + dexterity_skills + intelligence_skills + wisdom_skills + charisma_skills

screen_size = sg.Window.get_screen_size()

exit = [[sg.Button('EXIT', button_color = 'Red', font=("", 10, "bold"), key='-exit-', size=(10, 5))]]

char_column = [
    [sg.Text(d), sg.Push(), sg.Input(default, key=d, size=(4,5))]
     for d in main_char_labels
]

dice_column = [
          [sg.Button(d20.text, font=("", 10, "bold"), size=(10, 5)), sg.Button(d12.text, font=("", 10, "bold"), size=(10, 5))],
          [sg.Button(d10.text, font=("", 10, "bold"), size=(10, 5)),sg.Button(d8.text, font=("", 10, "bold"), size=(10, 5))],
          [sg.Button(d6.text, font=("", 10, "bold"), size=(10, 5)), sg.Button(d4.text, font=("", 10, "bold"), size=(10, 5))],
          [sg.Button(d100.text, font=("", 10, "bold"), size=(10, 5))],
          [sg.Text('Your roll:', font=font_preset, key= '_text_', visible = True), sg.Push(),sg.Text('Dice', font=font_preset, key= '_text2_', visible = True)]
          ]

ability_score_column = [
    [sg.Text(i), sg.Push(), sg.Input(j, size=(4,5))]
    for i, j in zip(base_stat_labels, csr.ability_score_list)]


skill_column = []
for d in skill_labels:
    if d in csr.skill_modifier_dict:
        modifier = str(csr.skill_modifier_dict[d])
        row = [sg.Text(d), sg.Push(), sg.Input(modifier, key=d, size=(4,5))]
    else:
        row = [sg.Text(d), sg.Push(), sg.Input(default, key=d, size=(4,5))]
    skill_column.append(row)

character_column = [
    [sg.Text(main_char_labels[0]), sg.Push(), sg.Input(csr.character.ch_name, key=csr.character.ch_name), sg.Text(main_char_labels[1]), sg.Push(), sg.Input(csr.character.ch_name, key=csr.character.ch_class, size=(7,1))],
    [sg.Text(main_char_labels[2]), sg.Push(), sg.Input(csr.character.ch_level, key=csr.character.ch_level, size=(10,1)), sg.Text(main_char_labels[3]), sg.Push(), sg.Input(csr.character.ch_background, key=csr.character.ch_background, size=(10,1))],
    [sg.Text(main_char_labels[4]), sg.Push(), sg.Input(csr.character.ch_pl_name, key=csr.character.ch_pl_name, size=(10,1)), sg.Text(main_char_labels[5]), sg.Push(), sg.Input(csr.character.ch_race, key=csr.character.ch_race, size=(4,1))],
    [sg.Text(main_char_labels[6]), sg.Push(), sg.Input(csr.character.ch_alignment, key=csr.character.ch_alignment, size=(10,1)), sg.Text(main_char_labels[8]), sg.Push(), sg.Input(csr.character.ch_hp, key=csr.character.ch_hp, size=(4,1))],
    [sg.Text(main_char_labels[9]), sg.Push(), sg.Input(csr.character.ch_armor_class, key=csr.character.ch_armor_class, size=(10,1))]
    ]

grouped_layout = [[sg.Frame('Dice', dice_column), sg.Column(skill_column, scrollable=True, vertical_scroll_only=True)],
                #  [sg.TabGroup([[sg.Tab('Dice', first_column, key='-dicetabkey-'),
                #                 sg.Tab('Stats', second_column, key='-statstabkey-')]])],
                 [sg.Frame('Ability Scores', ability_score_column), sg.Frame('Character', character_column)],
                 [exit]]

window = sg.Window('D&D Tool', grouped_layout, size=(screen_size)).Finalize()


while True:  # Event Loop
    event, values = window.read()
    # sg.popup_non_blocking(event, values)
    print(event, values)
    if event == sg.WIN_CLOSED or event == '-exit-':
        break
    if event == 'D20':
        window['_text2_'].update(d20.roll())
    if event == 'D12':
        window['_text2_'].update(d12.roll())
    if event == 'D10':
        window['_text2_'].update(d10.roll())
    if event == 'D8':
        window['_text2_'].update(d8.roll())
    if event == 'D6':
        window['_text2_'].update(d6.roll())
    if event == 'D4':
        window['_text2_'].update(d4.roll())
    if event == 'D100':
        window['_text2_'].update(d100.roll())
window.close()
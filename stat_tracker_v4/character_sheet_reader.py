import utils
from ability_score import AbilityScore
from character import Character

dict_sheet = utils.load_json_sheet('character_sheet.json')

strength = AbilityScore(dict_sheet['ability_scores']['str'])
dexterity = AbilityScore(dict_sheet['ability_scores']['dex'])
constitution = AbilityScore(dict_sheet['ability_scores']['con'])
wisdom = AbilityScore(dict_sheet['ability_scores']['wis'])
intelligence = AbilityScore(dict_sheet['ability_scores']['int'])
charisma = AbilityScore(dict_sheet['ability_scores']['cha'])

ability_score_list = [strength.score, dexterity.score, constitution.score, wisdom.score, intelligence.score, charisma.score]


skill_modifier_dict = {
    'Athletics:' : strength.get_modifier(),
    'Acrobatics:' : strength.get_modifier(),
    'Sleight of Hand:' : strength.get_modifier(),
    'Stealth:' : strength.get_modifier(),
    'Arcana:' : intelligence.get_modifier(),
    'History:' : intelligence.get_modifier(),
    'Investigation:' : intelligence.get_modifier(),
    'Nature:' : intelligence.get_modifier(),
    'Religion:' : intelligence.get_modifier(),
    'Animal Handling:' : wisdom.get_modifier(),
    'Insight:' : wisdom.get_modifier(),
    'Medicine:' : wisdom.get_modifier(),
    'Perception:' : wisdom.get_modifier(),
    'Survival:' : wisdom.get_modifier(),
    'Deception:' : charisma.get_modifier(),
    'Intimidation:' : charisma.get_modifier(),
    'Performance:' : charisma.get_modifier(),
    'Persuasion:' : charisma.get_modifier()
}

character = Character(dict_sheet['character_name'],
                      dict_sheet['class'], 
                      dict_sheet['level'],
                      dict_sheet['background'],
                      dict_sheet['player_name'],
                      dict_sheet['race'],
                      dict_sheet['alignment'],
                      dict_sheet['hp'],
                      dict_sheet['armor_class'])

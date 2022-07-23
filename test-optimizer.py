import copy

POSITION_SLOTS_OFFENSE = {
    "C": 1,
    "1B": 1,
    "2B": 1,
    "3B": 1,
    "SS": 1,
    "OF": 3,
    "UTIL": 1
}

# initial_lineup = {'C': ['Christian Vazquez'], '1B': ['Vladimir Guerrero Jr.'], '2B': ['Whit Merrifield'], '3B': ['Alec Bohm'], 'SS': ['Brandon Crawford'], 'OF': ['Whit Merrifield', 'Robbie Grossman', 'Nick Castellanos'], 'UTIL': ['Vladimir Guerrero Jr.']}

# the OG test
# position_listing = {
#     'C': [{'Christian Vazquez': -82}], 
#     '1B': [{'Vladimir Guerrero Jr.': 350}, {'Jesus Aguilar': -2}], 
#     '2B': [{'Whit Merrifield': 285}, {'Garrett Hampson': 63}, {'Jean Segura': -196}], 
#     '3B': [{'Alec Bohm': -184}, {'Jean Segura': -196}], 
#     'SS': [{'Brandon Crawford': 65}], 
#     'OF': [{'Whit Merrifield': 285}, {'Robbie Grossman': 166}, {'Nick Castellanos': 124}, {'Garrett Hampson': 63}, {'Avisail Garcia': -20}, {'Dylan Carlson': -148}, {'Christian Yelich': -288}], 
#     'UTIL': [{'Vladimir Guerrero Jr.': 350}, {'Whit Merrifield': 285}, {'Robbie Grossman': 166}, {'Nick Castellanos': 124}, {'Brandon Crawford': 65}, {'Garrett Hampson': 63}, {'Jesus Aguilar': -2}, {'Avisail Garcia': -20}, {'Christian Vazquez': -82}, {'Dylan Carlson': -148}, {'Alec Bohm': -184}, {'Jean Segura': -196}, {'Christian Yelich': -288}]
#     }

# test case with fucked up Tommy Edman

position_listing = {'C': [{'Austin Nola': -271}], '1B': [{'Vladimir Guerrero Jr.': 152}, {'C.J. Cron': 67}], '2B': [{'Tommy Edman': 286}, {'Jazz Chisholm Jr.': 161}, {'Thairo Estrada': 25}, {'Whit Merrifield': -10}, {'Jose Iglesias': -224}], '3B': [{'Bobby Witt Jr.': 77}], 'SS': [{'Tommy Edman': 286}, {'Jazz Chisholm Jr.': 161}, {'Bobby Witt Jr.': 77}, {'Thairo Estrada': 25}, {'Jose Iglesias': -224}], 'OF': [{'Tommy Edman': 286}, {'Ian Happ': 104}, {'Harrison Bader': 74}, {'Myles Straw': 42}, {'Whit Merrifield': -10}, {'Marcell Ozuna': -48}, {'Manuel Margot': -83}, {'Hunter Renfroe': -163}, {"Tyler O'Neill": -189}], 'UTIL': [{'Tommy Edman': 286}, {'Jazz Chisholm Jr.': 161}, {'Vladimir Guerrero Jr.': 152}, {'Ian Happ': 104}, {'Bobby Witt Jr.': 77}, {'Harrison Bader': 74}, {'C.J. Cron': 67}, {'Myles Straw': 42}, {'Thairo Estrada': 25}, {'Whit Merrifield': -10}, {'Marcell Ozuna': -48}, {'Manuel Margot': -83}, {'Hunter Renfroe': -163}, {"Tyler O'Neill": -189}, {'Jose Iglesias': -224}, {'Austin Nola': -271}]}

#position_listing = {'C': [], '1B': [], '2B': [{'Tommy Edman': 286}, {'Jazz Chisholm Jr.': 161}, {'Thairo Estrada': 25}, {'Whit Merrifield': -10}, {'Jose Iglesias': -224}], '3B': [], 'OF': [{'Tommy Edman': 286}, {'Ian Happ': 104}, {'Harrison Bader': 74}, {'Myles Straw': 42}, {'Whit Merrifield': -10}, {'Marcell Ozuna': -48}, {'Manuel Margot': -83}, {'Hunter Renfroe': -163}, {"Tyler O'Neill": -189}], 'UTIL': [{'Tommy Edman': 286}, {'Jazz Chisholm Jr.': 161}, {'Vladimir Guerrero Jr.': 152}, {'Ian Happ': 104}, {'Bobby Witt Jr.': 77}, {'Harrison Bader': 74}, {'C.J. Cron': 67}, {'Myles Straw': 42}, {'Thairo Estrada': 25}, {'Whit Merrifield': -10}, {'Marcell Ozuna': -48}, {'Manuel Margot': -83}, {'Hunter Renfroe': -163}, {"Tyler O'Neill": -189}, {'Jose Iglesias': -224}, {'Austin Nola': -271}]}



# test case with not enough players to go around
# position_listing = {'C': [{'Christian Vazquez': -84}], '1B': [{'Jesus Aguilar': 73}], '2B': [{'Whit Merrifield': 425}], '3B': [{'Ha-Seong Kim': -200}], 'SS': [{'Bobby Witt Jr.': 0}, {'Ha-Seong Kim': -200}], 'OF': [{'Whit Merrifield': 425}, {'Tommy Pham': 58}], 'UTIL': [{'Whit Merrifield': 425}, {'Jesus Aguilar': 73}, {'Tommy Pham': 58}, {'Bobby Witt Jr.': 0}, {'Christian Vazquez': -84}, {'Ha-Seong Kim': -200}]}

# position_listing = {
#     'C': [], 
#     '1B': [{'Vladimir Guerrero Jr.': 350}], 
#     '2B': [{'Whit Merrifield': 285}, {'Garrett Hampson': 63}, {'Jean Segura': -196}], 
#     '3B': [{'Alec Bohm': -184}, {'Jean Segura': -196}], 
#     'SS': [{'Brandon Crawford': 65}], 
#     'OF': [{'Whit Merrifield': 285}, {'Robbie Grossman': 166}, {'Garrett Hampson': 63}, {'Nick Castellanos': 124}], 
#     'UTIL': [{'Vladimir Guerrero Jr.': 350}, {'Whit Merrifield': 285}, {'Robbie Grossman': 166}, {'Nick Castellanos': 124}, {'Brandon Crawford': 65}, {'Garrett Hampson': 63}, {'Jesus Aguilar': -2}, {'Avisail Garcia': -20}, {'Christian Vazquez': -82}, {'Dylan Carlson': -148}, {'Alec Bohm': -184}, {'Jean Segura': -196}, {'Christian Yelich': -288}]
#     }



# for position in position_listing:
#     if len(position_listing[position]) <= 1:
#         continue
#     best_player_object = position_listing[position][0]
#     best_player_name = list(position_listing[position][0].keys())[0]
#     for compare_position in position_listing:
#         if compare_position == position:
#             continue
#         if best_player_object in position_listing[compare_position][0:POSITION_SLOTS_OFFENSE[compare_position]]:
#             print("\n\nconflict detected for ", best_player_name)
#             print("current position listing: \n\n", position_listing)
#             first_position_diff = list(position_listing[position][0].values())[0] - list(position_listing[position][1].values())[0]
#             second_position_diff = position_listing[position][0][best_player_name] - list(position_listing[compare_position][POSITION_SLOTS_OFFENSE[compare_position]].values())[0]

#             if first_position_diff >= second_position_diff:
#                 # we'll keep the player at his first position, and remove him as an option from the compare position list
#                 position_listing[compare_position].remove(best_player_object)
#             else:
#                 # we'll keep the player at the compare position, and remove him as an option from the first position
#                 position_listing[position].remove(best_player_object)



def resolve_conflict(position_listing, player_name, player_object, first_position, compare_position):
    print("resolving conflict for {}".format(player_name))
    print("resolving conflict for {}".format(position_listing))


    if len(position_listing[first_position]) <= POSITION_SLOTS_OFFENSE[first_position]:
        # we'll keep the player at the first position, and remove him as an option from the compare position
        print("bad spot ONNNEEEEEEE!!!!!")
        player_object in position_listing[compare_position] and position_listing[compare_position].remove(player_object)
        return detect_conflict(position_listing)

    if len(position_listing[compare_position]) <= POSITION_SLOTS_OFFENSE[compare_position]:
        # we'll keep the player at the compare position, and remove him as an option from the first position
        print("bad spot TWOOOOOOOOOOO!!!!!")
        player_object in position_listing[first_position] and position_listing[first_position].remove(player_object)
        return detect_conflict(position_listing)

    print("Stuck in the middle with you")
    print(position_listing)
    print(first_position, compare_position)
    first_position_diff = list(position_listing[first_position][0].values())[0] - list(position_listing[first_position][1].values())[0]
    second_position_diff = position_listing[first_position][0][player_name] - list(position_listing[compare_position][POSITION_SLOTS_OFFENSE[compare_position]].values())[0]
    if first_position_diff >= second_position_diff:
        # we'll keep the player at his first position, and remove him as an option from the compare position list
        print("Struggle Bus One") 
        position_listing[compare_position].remove(player_object)
    else:
        # we'll keep the player at the compare position, and remove him as an option from the first position
        print("Struggle Bus Two") 
        position_listing[first_position].remove(player_object)

    return detect_conflict(position_listing)

def detect_conflict(pos_list):

    position_listing = copy.deepcopy(pos_list)

    print("---\ncurrent situation \n\t{}\n".format(position_listing))
    for position in position_listing:
        print("---\ncurrent position \n\t{}\n".format(position))

        if len(position_listing[position]) == 0:
            continue
        best_player_object = position_listing[position][0]
        best_player_name = list(position_listing[position][0].keys())[0]
        for compare_position in position_listing:
            print("---\ncurrent position AGAIN\n\t{}\n".format(position))
            fresh_start = position_listing[compare_position][0:POSITION_SLOTS_OFFENSE[compare_position]]
            if compare_position == position:
                print("BOUNCE")
                continue
            if best_player_object in fresh_start:
                print("---\ncurrent position AGAIN AGAIN\n\t{}\n".format(position))
                print("---\nfirst {} and compare\t{}\n".format(position, compare_position))

                print(position_listing)
                print(best_player_object)
                print(position_listing[compare_position][0:POSITION_SLOTS_OFFENSE[compare_position]])
                print("conflict detected for {} between positions {} and {}\n".format(best_player_name, position, compare_position))
                resolve_conflict(position_listing, best_player_name, best_player_object, position, compare_position)

    return position_listing


def final_lineup(position_listing):
    print("")
    lineup = {}
    for position in position_listing:
        if len(position_listing[position]) == 0:
            lineup[position] = []
            continue
        lineup[position] = [list(player_name.keys())[0] for player_name in position_listing[position][0:POSITION_SLOTS_OFFENSE[position]]]
    return lineup


print("=" * 160)
result = detect_conflict(position_listing)
print(result)

print("-" * 80)
lineup = final_lineup(result)
print(lineup)

        

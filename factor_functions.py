#ITEM: 1)name_of_the_card, 
#      2)elixir (int), 
#      3)health (int), 
#      4)target [Ground, Air & Ground, Buildings, Friendly, N/A, Varies - like mirror], 
#      5)speed [Slow, Medium, Fast, Very Fast, N/A - No movement], 
#      6)attack_speed (float), 
#      7)range_value (Melee or float), 
#      8)attack_dmg (int), 
#      9)tower_dmg (int), 
#      10)little_tower_dmg (int),
#      11)win_condition = [0: NO, 1: YES], 
#      12)number of troops



import numpy as np
# Clash Royale cards data structure
clash_royale_cards = {
    # Troops
    "26000000": ["Knight", 3, 1344, "Ground", "Medium", 1.2, "Melee", 162, "N/A", "N/A",0,1],  # Knight
    "26000001": ["Archers", 3, 304, "Air & Ground", "Medium", 1.2, 5.5, 89, "N/A", "N/A",0,2],  # Archers
    "26000002": ["Goblins", 2, 147, "Ground", "Fast", 1.1, "Melee", 89, "N/A", "N/A",0,4],  # Goblins
    "26000003": ["Giant", 5, 3275, "Buildings", "Slow", 1.5, "Melee", 211, "N/A", "N/A",0,1],  # Giant
    "26000004": ["P.E.K.K.A", 7, 3458, "Ground", "Slow", 1.8, "Melee", 816, "N/A", "N/A",0,1],  # P.E.K.K.A
    "26000005": ["Minions", 3, 190, "Air & Ground", "Fast", 1.0, 2.5, 89, "N/A", "N/A",0,3],  # Minions
    "26000006": ["Balloon", 5, 1344, "Buildings", "Medium", 3.0, "Melee", 816, "N/A", "N/A",0,1],  # Balloon
    "26000007": ["Witch", 5, 665, "Air & Ground", "Medium", 0.7, 5.5, 89, "N/A", "N/A",0,1],  # Witch
    "26000008": ["Barbarians", 5, 636, "Ground", "Medium", 1.4, "Melee", 211, "N/A", "N/A",0,5],  # Barbarians
    "26000009": ["Golem", 8, 4256, "Buildings", "Slow", 2.5, "Melee", 259, "N/A", "N/A",1,1],  # Golem
    "26000010": ["Skeletons", 1, 67, "Ground", "Fast", 1.0, "Melee", 67, "N/A", "N/A",0,4],  # Skeletons
    "26000011": ["Valkyrie", 4, 1344, "Ground", "Medium", 1.5, "Melee", 189, "N/A", "N/A",0,1],  # Valkyrie
    "26000012": ["Skeleton Army", 3, 67, "Ground", "Fast", 1.0, "Melee", 67, "N/A", "N/A",0,15],  # Skeleton Army
    "26000013": ["Bomber", 2, 147, "Ground", "Medium", 1.9, 4.5, 162, "N/A", "N/A",0,1],  # Bomber
    "26000014": ["Musketeer", 4, 598, "Air & Ground", "Medium", 1.0, 6.0, 189, "N/A", "N/A",0,1],  # Musketeer
    "26000015": ["Baby Dragon", 4, 800, "Air & Ground", "Fast", 1.8, 3.5, 189, "N/A", "N/A",1,1],  # Baby Dragon
    "26000016": ["Prince", 5, 1344, "Ground", "Medium", 1.4, "Melee", 390, "N/A", "N/A",1,1],  # Prince
    "26000017": ["Wizard", 5, 598, "Air & Ground", "Medium", 1.4, 5.5, 189, "N/A", "N/A",0,1],  # Wizard
    "26000018": ["Mini P.E.K.K.A", 4, 1088, "Ground", "Fast", 1.8, "Melee", 598, "N/A", "N/A",0,1],  # Mini P.E.K.K.A
    "26000019": ["Spear Goblins", 2, 147, "Air & Ground", "Very Fast", 1.3, 5.5, 89, "N/A", "N/A",0,3],  # Spear Goblins
    "26000020": ["Giant Skeleton", 6, 2662, "Ground", "Slow", 1.5, "Melee", 259, "N/A", "N/A",1,1],  # Giant Skeleton
    "26000021": ["Hog Rider", 4, 1408, "Buildings", "Very Fast", 1.6, "Melee", 189, "N/A", "N/A",0,1],  # Hog Rider
    "26000022": ["Minion Horde", 5, 190, "Air & Ground", "Fast", 1.0, 2.5, 89, "N/A", "N/A",0,6],  # Minion Horde
    "26000023": ["Ice Wizard", 3, 665, "Air & Ground", "Medium", 1.5, 5.5, 89, "N/A", "N/A",0,1],  # Ice Wizard
    "26000024": ["Royal Giant", 6, 2544, "Buildings", "Slow", 1.7, 6.5, 259, "N/A", "N/A",0,1],  # Royal Giant
    "26000025": ["Guards", 3, 65, "Ground", "Fast", 1.2, "Melee", 89, "N/A", "N/A",0,3],  # Guards
    "26000026": ["Princess", 3, 216, "Air & Ground", "Medium", 3.0, 9.0, 189, "N/A", "N/A",0,1],  # Princess
    "26000027": ["Dark Prince", 4, 1344, "Ground", "Medium", 1.4, "Melee", 259, "N/A", "N/A",0,1],  # Dark Prince
    "26000028": ["Three Musketeers", 9, 598, "Air & Ground", "Medium", 1.0, 6.0, 189, "N/A", "N/A",0,3],  # Three Musketeers
    "26000029": ["Lava Hound", 7, 3150, "Buildings", "Slow", 1.3, "Melee", 45, "N/A", "N/A",1,1],  # Lava Hound
    "26000030": ["Ice Spirit", 1, 190, "Air & Ground", "Very Fast", 2.5, "Melee", 95, "N/A", "N/A",0,1],  # Ice Spirit
    "26000031": ["Fire Spirits", 2, 91, "Air & Ground", "Very Fast", 1.0, "Melee", 189, "N/A", "N/A",0,1],  # Fire Spirits
    "26000032": ["Miner", 3, 1000, "Ground", "Fast", 1.2, "Melee", 189, "N/A", "N/A",1,1],  # Miner
    "26000033": ["Sparky", 6, 1240, "Ground", "Slow", 4.0, 4.5, 1334, "N/A", "N/A",0,1],  # Sparky
    "26000034": ["Bowler", 5, 1456, "Ground", "Slow", 2.5, 5.0, 293, "N/A", "N/A",0,1],  # Bowler
    "26000035": ["Lumberjack", 4, 1060, "Ground", "Very Fast", 0.7, "Melee", 259, "N/A", "N/A",0,1],  # Lumberjack
    "26000036": ["Battle Ram", 4, 1008, "Buildings", "Fast", 1.4, "Melee", 259, "N/A", "N/A",0,1],  # Battle Ram
    "26000037": ["Inferno Dragon", 4, 1070, "Air & Ground", "Medium", 0.4, 3.5, 1334, "N/A", "N/A",0,1],  # Inferno Dragon (max damage)
    "26000038": ["Ice Golem", 2, 665, "Buildings", "Slow", 2.5, "Melee", 95, "N/A", "N/A",0,1],  # Ice Golem
    "26000039": ["Mega Minion", 3, 395, "Air & Ground", "Medium", 1.5, 2.0, 259, "N/A", "N/A",0,1],  # Mega Minion
    "26000040": ["Dart Goblin", 3, 216, "Air & Ground", "Very Fast", 0.7, 6.5, 162, "N/A", "N/A",0,1],  # Dart Goblin
    "26000041": ["Goblin Gang", 3, 147, "Ground", "Fast", 1.1, "Melee", 89, "N/A", "N/A",0,1],  # Goblin Gang
    "26000042": ["Electro Wizard", 4, 590, "Air & Ground", "Medium", 1.7, 5.5, 189, "N/A", "N/A",0,1],  # Electro Wizard
    "26000043": ["Elite Barbarians", 6, 940, "Ground", "Very Fast", 1.4, "Melee", 293, "N/A", "N/A",0,1],  # Elite Barbarians
    "26000044": ["Hunter", 4, 756, "Air & Ground", "Medium", 2.2, 4.0, 189, "N/A", "N/A",0,1],  # Hunter
    "26000045": ["Executioner", 5, 1238, "Air & Ground", "Medium", 2.4, 4.5, 189, "N/A", "N/A",0,1],  # Executioner
    "26000046": ["Bandit", 3, 749, "Ground", "Fast", 1.1, "Melee", 390, "N/A", "N/A",0,1],  # Bandit (dash damage)
    "26000047": ["Royal Recruits", 7, 530, "Ground", "Slow", 1.3, "Melee", 89, "N/A", "N/A",0,6],  # Royal Recruits
    "26000048": ["Night Witch", 4, 750, "Air & Ground", "Medium", 1.2, "Melee", 189, "N/A", "N/A",0,1],  # Night Witch
    "26000049": ["Bats", 2, 67, "Air & Ground", "Fast", 1.1, "Melee", 67, "N/A", "N/A",0,5],  # Bats
    "26000050": ["Royal Ghost", 3, 1000, "Ground", "Fast", 1.8, "Melee", 259, "N/A", "N/A",0,1],  # Royal Ghost
    "26000051": ["Ram Rider", 5, 1294, "Buildings", "Medium", 1.8, 3.5, 390, "N/A", "N/A",1,1],  # Ram Rider
    "26000052": ["Zappies", 4, 224, "Air & Ground", "Medium", 1.6, 4.5, 89, "N/A", "N/A",0,3],  # Zappies
    "26000053": ["Rascals", 5, 749, "Air & Ground", "Fast", 1.2, 5.5, 189, "N/A", "N/A",0,3],  # Rascals
    "26000054": ["Cannon Cart", 5, 853, "Ground", "Medium", 1.1, 5.5, 293, "N/A", "N/A",0,1],  # Cannon Cart
    "26000055": ["Mega Knight", 7, 3251, "Ground", "Medium", 1.8, "Melee", 390, "N/A", "N/A",1,1],  # Mega Knight
    "26000056": ["Skeleton Barrel", 3, 308, "Ground", "Medium", 3.0, "Melee", 259, "N/A", "N/A",0,1],  # Skeleton Barrel
    "26000057": ["Flying Machine", 4, 600, "Air & Ground", "Fast", 1.0, 6.0, 189, "N/A", "N/A",0,1],  # Flying Machine
    "26000058": ["Wall Breakers", 2, 120, "Buildings", "Fast", 1.0, "Melee", 815, "N/A", "N/A",0,2],  # Wall Breakers
    "26000059": ["Royal Hogs", 5, 415, "Buildings", "Fast", 1.6, "Melee", 111, "N/A", "N/A",0,4],  # Royal Hogs
    "26000060": ["Goblin Giant", 6, 2703, "Buildings", "Medium", 1.7, "Melee", 189, "N/A", "N/A",1,1],  # Goblin Giant
    "26000061": ["Fisherman", 3, 1129, "Ground", "Medium", 1.5, 7.0, 259, "N/A", "N/A",0,1],  # Fisherman
    "26000062": ["Magic Archer", 4, 448, "Air & Ground", "Medium", 1.1, 7.0, 96, "N/A", "N/A",0,1],  # Magic Archer
    "26000063": ["Electro Dragon", 5, 1007, "Air & Ground", "Medium", 2.3, 3.5, 293, "N/A", "N/A",0,1],  # Electro Dragon
    "26000064": ["Firecracker", 3, 464, "Air & Ground", "Fast", 3.0, 6.0, 108, "N/A", "N/A",0,1],  # Firecracker
    "26000067": ["Elixir Golem", 3, 1071, "Buildings", "Slow", 1.2, "Melee", 96, "N/A", "N/A",0,1],  # Elixir Golem
    "26000068": ["Battle Healer", 4, 1343, "Ground", "Medium", 1.6, 3.5, 189, "N/A", "N/A",0,1],  # Battle Healer
    "26000080": ["Skeleton Dragons", 4, 334, "Air & Ground", "Fast", 2.0, 3.5, 108, "N/A", "N/A",0,1],  # Skeleton Dragons
    "26000083": ["Mother Witch", 4, 598, "Ground", "Medium", 1.1, 5.0, 189, "N/A", "N/A",0,1],  # Mother Witch
    "26000084": ["Electro Spirit", 1, 91, "Air & Ground", "Very Fast", 1.0, "Melee", 189, "N/A", "N/A",0,1],  # Electro Spirit
    "26000085": ["Electro Giant", 8, 4008, "Buildings", "Slow", 2.1, "Melee", 259, "N/A", "N/A",1,1],  # Electro Giant
    
    # Buildings
    "27000000": ["Cannon", 3, 858, "Ground", "N/A", 0.8, 5.5, 120, "N/A", "N/A",0,0],  # Cannon
    "27000001": ["Goblin Hut", 5, 1884, "N/A", "N/A", "N/A", "N/A", 0, "N/A", "N/A",0,1],  # Goblin Hut (spawns troops)
    "27000002": ["Mortar", 4, 1188, "Ground", "N/A", 5.0, 12.0, 293, "N/A", "N/A",0,0],  # Mortar
    "27000003": ["Inferno Tower", 5, 1508, "Air & Ground", "N/A", 0.4, 6.0, 1334, "N/A", "N/A",0,0],  # Inferno Tower (max damage)
    "27000004": ["Bomb Tower", 4, 1540, "Ground", "N/A", 1.6, 6.0, 104, "N/A", "N/A",0,0],  # Bomb Tower
    "27000005": ["Barbarian Hut", 7, 2226, "N/A", "N/A", "N/A", "N/A", 0, "N/A", "N/A",0,3],  # Barbarian Hut (spawns troops)
    "27000006": ["Tesla", 4, 1001, "Air & Ground", "N/A", 1.1, 5.5, 150, "N/A", "N/A",0,0],  # Tesla
    "27000007": ["Elixir Collector", 6, 1330, "N/A", "N/A", "N/A", "N/A", 0, "N/A", "N/A",0,0],  # Elixir Collector
    "27000008": ["X-Bow", 6, 1540, "Ground", "N/A", 0.3, 12.0, 20, "N/A", "N/A",1,0],  # X-Bow
    "27000009": ["Tombstone", 3, 415, "N/A", "N/A", "N/A", "N/A", 0, "N/A", "N/A",0,2],  # Tombstone (spawns skeletons)
    "27000010": ["Furnace", 4, 1045, "N/A", "N/A", "N/A", "N/A", 0, "N/A", "N/A",0,1],  # Furnace (spawns fire spirits)
    "27000012": ["Goblin Cage", 4, 2544, "N/A", "N/A", "N/A", "N/A", 0, "N/A", "N/A",0,1],  # Goblin Cage (releases goblin brawler)
    

    # Spells
    "28000000": ["Fireball", 4, "N/A", "Air & Ground", "N/A", "N/A", 2.5, 325, 325, 130,0,0],  # Fireball
    "28000001": ["Arrows", 3, "N/A", "Air & Ground", "N/A", "N/A", 4.0, 144, 144, 58,0,0],  # Arrows
    "28000002": ["Rage", 2, "N/A", "Friendly", "N/A", "N/A", 5.0, 0, "N/A", "N/A",0,0],  # Rage
    "28000003": ["Rocket", 6, "N/A", "Air & Ground", "N/A", "N/A", 2.0, 720, 720, 288,0,0],  # Rocket
    "28000004": ["Goblin Barrel", 3, "N/A", "Buildings", "N/A", "N/A", "Anywhere", 0, "N/A", "N/A",0,3],  # Goblin Barrel (spawns troops)
    "28000005": ["Freeze", 4, "N/A", "Air & Ground", "N/A", "N/A", 3.0, 95, 95, 38,0,0],  # Freeze
    "28000006": ["Mirror", 5, "N/A", "Varies", "N/A", "N/A", "Varies", 0, "Varies", "Varies",0,0],  # Mirror
    "28000007": ["Lightning", 6, "N/A", "Air & Ground", "N/A", "N/A", 3.5, 514, 514, 206,0,0],  # Lightning
    "28000008": ["Zap", 2, "N/A", "Air & Ground", "N/A", "N/A", 2.5, 159, 159, 64,0,0],  # Zap
    "28000009": ["Poison", 4, "N/A", "Air & Ground", "N/A", "N/A", 3.5, 240, 240, 96,0,0],  # Poison
    "28000010": ["Graveyard", 5, "N/A", "Ground", "N/A", "N/A", 4.0, 0, "N/A", "N/A",1,10],  # Graveyard (spawns skeletons)
    "28000011": ["The Log", 2, "N/A", "Ground", "N/A", "N/A", 11.1, 240, 240, 96,0,1],  # The Log
    "28000012": ["Tornado", 3, "N/A", "Air & Ground", "N/A", "N/A", 5.5, 109, 109, 44,0,1],  # Tornado
    "28000013": ["Clone", 3, "N/A", "Friendly", "N/A", "N/A", 3.0, 0, "N/A", "N/A",0,1],  # Clone
    "28000014": ["Earthquake", 3, "N/A", "Ground", "N/A", "N/A", 3.5, 259, 259, 104,0,0],  # Earthquake
    "28000015": ["Barbarian Barrel", 2, "N/A", "Ground", "N/A", "N/A", 4.6, 159, 159, 64,0,0],  # Barbarian Barrel
    "28000016": ["Heal", 1, "N/A", "Friendly", "N/A", "N/A", 2.5, 0, "N/A", "N/A",0,0],  # Heal Spirit
    "28000017": ["Giant Snowball", 2, "N/A", "Air & Ground", "N/A", "N/A", 3.0, 159, 159, 64,0,0],  # Giant Snowball
    "28000018": ["Royal Delivery", 3, "N/A", "Air & Ground", "N/A", "N/A", 3.5, 344, 344, 138,0,1],  # Royal Delivery
}

# string
# deckexample = "2600000126000002260000032700000028000000280000012600000728000016"

def stringtolist(deck_int):
    deck_string = str(deck_int)
    # Check if the input is a string
    if not isinstance(deck_string, str):
        raise ValueError("Input must be a string")
    # Check if the length of the string is correct
    if len(deck_string) != 64:
        raise ValueError(f"Deck string must be exactly 64 characters long, got {len(deck_string)}")
    # Split the string into chunks of 8 characters each

    return [deck_string[i:i+8] for i in range(0, len(str(deck_string)), 8)]


#deck = 8 IDs of card : [ID_1, ID_2, ..., ID_8]

#AVERAGE ELIXIR COST
def factor_1(deck):

    #Check if the deck is given as a list
    if not isinstance(deck, list):
        raise ValueError("Deck must be a list")

    #Check if the size of the deck is right
    if len(deck) != 8:
        raise ValueError(f"Deck must contain exactly 8 cards, got {len(deck)}")
    
    sum = 0

    for id in deck:
        sum += clash_royale_cards[id][1]

        
    return np.float32(sum//8)

#NUMBER OF SPELL IN A DECK
def factor_2(deck):

    #Check if the deck is given as a list
    if not isinstance(deck, list):
        raise ValueError("Deck must be a list")

    #Check if the size of the deck is right
    if len(deck) != 8:
        raise ValueError(f"Deck must contain exactly 8 cards, got {len(deck)}")
    
    sum = 0

    for id in deck:
        #27 is building we try to avoid them
        #id[4] == speed
        if str(id)[:2] != "27" and clash_royale_cards[id][4] == "N/A":
                sum += 1

    return np.float32(sum)

#NUMBER OF BUILDINGS IN A DECK
def factor_3(deck):

    #Check if the deck is given as a list
    if not isinstance(deck, list):
        raise ValueError("Deck must be a list")

    #Check if the size of the deck is right
    if len(deck) != 8:
        raise ValueError(f"Deck must contain exactly 8 cards, got {len(deck)}")
    
    sum = 0

    for id in deck:
        #27 is building 
        if str(id)[:2] == "27":
                sum += 1

    return np.float32(sum)

#NUMBER OF BUILDINGS IN A DECK
def factor_4(deck):

    #Check if the deck is given as a list
    if not isinstance(deck, list):
        raise ValueError("Deck must be a list")

    #Check if the size of the deck is right
    if len(deck) != 8:
        raise ValueError(f"Deck must contain exactly 8 cards, got {len(deck)}")
    
    sum = 0

    for id in deck:
        #27 is building 
        if str(id)[:2] == "27":
                sum += 1

    return np.float32(sum)

#NUMBER OF TROOPS IN A DECK
def factor_5(deck):
    #Check if the deck is given as a list
    if not isinstance(deck, list):
        raise ValueError("Deck must be a list")

    #Check if the size of the deck is right
    if len(deck) != 8:
        raise ValueError(f"Deck must contain exactly 8 cards, got {len(deck)}")
    
    sum = 0

    for id in deck:
        #26 is troop 
        if str(id)[:2] == "26":
                sum += 1

    return np.float32(sum)
     
#WIN CONDITION: TROOPS THAT GO DIRECTLY TO THE TOWER
def factor_6(deck):
    #Check if the deck is given as a list
    if not isinstance(deck, list):
        raise ValueError("Deck must be a list")

    #Check if the size of the deck is right
    if len(deck) != 8:
        raise ValueError(f"Deck must contain exactly 8 cards, got {len(deck)}")
    
    sum = 0

    for id in deck:
         if clash_royale_cards[id][10] == 1:
              sum += 1
    
    return np.float32(sum)

#TOTAL DAMAGE
def factor_7(deck):
    #Check if the deck is given as a list
    if not isinstance(deck, list):
        raise ValueError("Deck must be a list")

    #Check if the size of the deck is right
    if len(deck) != 8:
        raise ValueError(f"Deck must contain exactly 8 cards, got {len(deck)}")
    
    sum = 0

    for id in deck:
        sum += clash_royale_cards[id][7]

    return np.float32(sum)       
        
#TOTAL HEALTH
def factor_8(deck):
    #Check if the deck is given as a list
    if not isinstance(deck, list):
        raise ValueError("Deck must be a list")

    #Check if the size of the deck is right
    if len(deck) != 8:
        raise ValueError(f"Deck must contain exactly 8 cards, got {len(deck)}")
    
    sum = 0

    for id in deck:
        if clash_royale_cards[id][2] != "N/A":
            # If the health is not "N/A", add it to the sum
            # Clash Royale cards health is given as an integer, so we can safely convert it
            sum += clash_royale_cards[id][2]

    return np.float32(sum)

#print(factor_7(["26000001","26000002","26000020","27000000","28000000","28000001","26000007","28000016"]))
#print(clash_royale_cards["26000000"])


# take csv file of 3 columns, first two cols with one deck as a string and last column with the winrate of the deck
# run all the functions on the deck string of the first col and make a numpy array of the results, with factor_1, factor_2, factor_3 as cols
# run all the functions on the deck string of the second col and make a numpy array of the results, with factor_1, factor_2, factor_3 as cols
# then concatenate the two numpy arrays and save it as a csv file with the winrate as the last column
import pandas as pd
def process_deck_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Initialize lists to store the results
    factor_1_deck1 = []
    factor_1_deck2 = []
    factor_2_deck1 = []
    factor_2_deck2 = []
    factor_3_deck2 = []
    factor_3_deck1 = []
    factor_3_deck2 = []
    factor_3_deck2 = []
    factor_4_deck1 = []
    factor_4_deck2 = []
    factor_5_deck1 = []
    factor_5_deck2 = []
    factor_6_deck1 = []
    factor_6_deck2 = []
    factor_7_deck1 = []
    factor_7_deck2 = []
    factor_8_deck1 = []
    factor_8_deck2 = []

    winrate_list = []
    invalidcards = [[], []]  # To store invalid decks for player1 and player2
    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        deck1_string = row['player1.cards.list']
        deck2_string = row['player2.cards.list']
        winrate = row['check']

        # Convert the deck strings to lists
        deck1 = stringtolist(deck1_string)
        deck2 = stringtolist(deck2_string)

        # Check if the decks are valid
        if not all(card_id in clash_royale_cards for card_id in deck1):
            print(f"Invalid card ID in deck 1 at index {index}: {deck1}")
            invalidcards[0].append(deck1)
            continue
        if not all(card_id in clash_royale_cards for card_id in deck2):
            print(f"Invalid card ID in deck 2 at index {index}: {deck2}")
            invalidcards[1].append(deck2)
            continue


        # Calculate the factors for each deck
        factor_1_deck1.append(factor_1(deck1))
        factor_1_deck2.append(factor_1(deck2))
        factor_2_deck1.append(factor_2(deck1))
        factor_2_deck2.append(factor_2(deck2))
        factor_3_deck1.append(factor_3(deck1))
        factor_3_deck2.append(factor_3(deck2))
        factor_4_deck1.append(factor_4(deck1))
        factor_4_deck2.append(factor_4(deck2))
        factor_5_deck1.append(factor_5(deck1))
        factor_5_deck2.append(factor_5(deck2))
        factor_6_deck1.append(factor_6(deck1))
        factor_6_deck2.append(factor_6(deck2))
        factor_7_deck1.append(factor_7(deck1))
        factor_7_deck2.append(factor_7(deck2))
        factor_8_deck1.append(factor_8(deck1))
        factor_8_deck2.append(factor_8(deck2))

        # Append the winrate
        winrate_list.append(winrate)
    result_df = pd.DataFrame({
        'factor_1_deck1': factor_1_deck1,
        'factor_1_deck2': factor_1_deck2,
        'factor_2_deck1': factor_2_deck1,
        'factor_2_deck2': factor_2_deck2,
        'factor_3_deck1': factor_3_deck1,
        'factor_3_deck2': factor_3_deck2,
        'factor_4_deck1': factor_4_deck1,
        'factor_4_deck2': factor_4_deck2,
        'factor_5_deck1': factor_5_deck1,
        'factor_5_deck2': factor_5_deck2,
        'factor_6_deck1': factor_6_deck1,
        'factor_6_deck2': factor_6_deck2,
        'factor_7_deck1': factor_7_deck1,
        'factor_7_deck2': factor_7_deck2,
        'factor_8_deck1': factor_8_deck1,
        'factor_8_deck2': factor_8_deck2,
        'winrate': winrate_list
    })
    # Save the results to a new CSV file
    result_df.to_csv('processed_deck_data.csv', index=False)

process_deck_data('BattlesStaging_01012021_WL_tagged_new.csv')


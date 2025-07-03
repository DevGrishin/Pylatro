
card_indexes = []

def check_straight(card_list):
    # Extract and sort the card values
    values = sorted([int(card[2]) for card in card_list])
    # Check for normal straight
    for i in range(4):
        if values[i+1] != values[i] + 1:
            break
    else:
        return True
    return False
    
def check_flush(card_list):
    card1 = card_list[0]
    card2 = card_list[1]
    card3 = card_list[2]
    card4 = card_list[3]
    card5 = card_list[4]
    if card2[0] == card1[0] and card3[0] == card2[0] and card4[0] == card3[0] and card5[0] == card4[0]:
        return True
    else:
        return False
    
def check_StraightFlush(card_list):
    card1 = card_list[0]
    card2 = card_list[1]
    card3 = card_list[2]
    card4 = card_list[3]
    card5 = card_list[4]
    if check_flush(card_list) and check_straight(card_list):
        return True
    else:
        return False

def check_RoyalFlush(card_list):
    card1 = card_list[0]
    card2 = card_list[1]
    card3 = card_list[2]
    card4 = card_list[3]
    card5 = card_list[4]
    if check_flush(card_list) and card1[2] == "10" and card2[2] == "11" and card3[2] == "12" and card4[2] == "13" and card5[2] == "14":
        return True
    else:
        return False

def HighCard(card_list):
    global card_indexes
    max = 0
    highcard = None
    for card in card_list:
        if int(card[2]) > int(max):
            max = card[2]
            highcard = card
    card_indexes.append(card_list.index(highcard))

def check_pair(card_list):
    global card_indexes
    list = []
    highcard = None
    for i in range(2, 15):
        for card in card_list:
            if int(card[2]) == i:
                list.append(card)
        if len(list) == 2:
            for card in list:
                card_indexes.append(card_list.index(card))
            return True
        else:
            list = []
    return False

def check_TwoPair(card_list):
    global card_indexes
    list = []
    listlist = []
    highcard = None
    pairs = 0
    for i in range(2, 15):
        for card in card_list:
            if int(card[2]) == i:
                list.append(card)
        if len(list) == 2:
            listlist.append(list)
            pairs += 1
            list = []
        else:
            list = []
    if pairs == 2:
        for pair in listlist:
            for card in pair:
                card_indexes.append(card_list.index(card))
        return True
    else:
        return False

def check_three(card_list):
    global card_indexes
    list = []
    highcard = None
    for i in range(2, 15):
        for card in card_list:
            if int(card[2]) == i:
                list.append(card)
        if len(list) == 3:
            for card in list:
                card_indexes.append(card_list.index(card))
            return True
        else:
            list = []
    return False
def check_four(card_list):
    global card_indexes
    list = []
    highcard = None
    for i in range(2, 15):
        for card in card_list:
            if int(card[2]) == i:
                list.append(card)
        if len(list) == 4:
            for card in list:
                card_indexes.append(card_list.index(card))
            return True
        else:
            list = []
    return False

def check_FullHouse(card_list):
    card1 = card_list[0]
    card2 = card_list[1]
    card3 = card_list[2]
    card4 = card_list[3]
    card5 = card_list[4]
    if check_pair(card_list) and check_three(card_list):
        return True
    else:
        return False


def chip_calc(card_list):
    global card_indexes
    mult = 1
    chips = 5
    hand = ""
    
    if len(card_list) == 5 and check_RoyalFlush(card_list):
        mult = 8
        chips = 100
        hand = "Royal Flush"
        card_indexes = list(range(5))
    elif  len(card_list) == 5 and check_StraightFlush(card_list):
        mult = 8
        chips = 100
        hand = "Straight Flush"
        card_indexes = list(range(5))
    elif check_four(card_list):
        mult = 7
        chips = 60
        hand = "Four of a kind"
    elif len(card_list) == 5 and check_FullHouse(card_list):
        mult = 4
        chips = 40
        hand = "Full House"
        card_indexes = list(range(5))
    elif len(card_list) == 5 and check_flush(card_list):
        mult = 4
        chips = 35
        hand = "Flush"
        card_indexes = list(range(5))
    elif len(card_list) == 5 and check_straight(card_list):
        mult = 4
        chips = 30
        hand = "Straight"
        card_indexes = list(range(5))
    elif check_three(card_list):
        mult = 3
        chips = 30
        hand = "Three of a kind"
    elif check_TwoPair(card_list):
        mult = 2
        chips = 20
        hand = "Two Pair"
    elif check_pair(card_list):
        mult = 2
        chips = 10
        hand = "Pair"
    else:
        HighCard(card_list)
        mult = 1
        chips = 5
        hand = "High Card"
    indexes = card_indexes
    card_indexes = []
    print(indexes)
    return [hand, chips, mult, indexes]

            
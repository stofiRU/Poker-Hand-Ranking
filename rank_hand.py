import re

# dictionaries pairing card with value
faceValue = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
aceValue = {'A':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}

def check_straight(h):
    # create a set of first characters in hand (face values)
    # if size of set == 5 then all cards are unique
    # and if difference between highest and lowest card == 4 then they're straight
    # We also need a solution in case A has the value of 1
    aceSort = sorted(h, key=lambda x: aceValue.get(x[0]))
    if ((len(set(map(lambda x: x[0], h))) == 5) and (faceValue.get(h[len(h)-1][:1]) - faceValue.get(h[0][:1]) == 4)):
        return True
    elif ((len(set(map(lambda x: x[0], aceSort))) == 5) and (aceValue.get(aceSort[len(aceSort)-1][:1]) - aceValue.get(aceSort[0][:1]) == 4)):
        return True
    else:
        return False

# check if input is a flush (all cards of the same sort)
def check_flush(h):
    # create a set of second characters in hand (sorts)
    # if size of set == 1 then all cards are of the same sort and therefore a flush
    if len(set(map(lambda x: x[1], h))) == 1:
        return True
    else:
        return False

def check_royal_flush(h):
    if ((check_flush(h)) and (check_straight(h)) and ((re.search('T', h[0])))):
        return True
    else:
        return False

def check_straight_flush(h):
    if((check_flush(h)) and (check_straight(h))):
        return True
    else:
        return False

def check_four_of_a_kind(h):
    counter = 0
    reference = h[2][:1]    
    # regardless of there the hand is a four-of-a-kind or a full house, the reference point will be in the middle
    for i in range(len(h)):
        if (h[i][:1] == reference):
            counter += 1
    if counter > 3:
        return True
    else:
        return False

def check_full_house(h):
    # as check_four_of_a_kind is false, having only two sorts in five cards means a full house
    if len(set(map(lambda x: x[0], h))) == 2:
        return True
    else:
        return False

def check_three_of_a_kind(h):
    sortedBySort = sorted(h, key=lambda x: x[1])
    # hand sorted by sort means a three of a kind has to have its sort in index 2 (card no. 3)
    counter = 0
    reference = sortedBySort[2][-1]    # sort to check for
    for i in range(len(sortedBySort)):
        if sortedBySort[i][-1] == reference:
            counter += 1
    if counter == 3:
        return True
    else:
        return False
def check_two_pairs(h):
    pairChecker = list(set(map(lambda x: x[0], h)))     ### TODO: sorted?
    counter = 0
    pairCounter = 0
    for i in range(0, len(pairChecker)):
        for j in range(0, len(h)):
            if (pairChecker[i] == h[j][:1]):
                counter +=1
            if counter == 2:
                pairCounter += 1
                counter = 0
    if pairCounter == 2:
        return True
    else:
        return False

# we'll check by highest rank first, as some of them also qualify lower ranks 
# (e.g. three of a kind also includes a pair)
def rank_hand(hand):
    rank = 0
    # sorting the cards by value simplifies checking, e.g. pairs and rows
    sortedHand = sorted(hand, key=lambda x: faceValue.get(x[0]))
    if (check_royal_flush(sortedHand)):
        rank = 9
    elif (check_straight_flush(sortedHand)):
        rank = 8
    elif (check_four_of_a_kind(sortedHand)):
        rank = 7
    elif (check_full_house(sortedHand)):
        rank = 6
    elif (check_flush(sortedHand)):
        rank = 5
    elif (check_straight(sortedHand)):
        rank = 4
    elif (check_three_of_a_kind(sortedHand)):
        rank = 3
    elif (check_two_pairs(sortedHand)):
        rank = 2
    else:
        rank = 0
    return rank
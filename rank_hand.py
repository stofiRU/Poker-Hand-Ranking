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


# test

print("9:", rank_hand([ 'TD', 'JD', 'QD', 'KD', 'AD' ]))          # royal flush
print("9:", rank_hand([ 'JD', 'KD', 'TD', 'QD', 'AD' ]))          # royal flush
print("9:", rank_hand([ 'JS', 'KS', 'TS', 'QS', 'AS' ]))          # royal flush
print("9:", rank_hand([ 'JC', 'KC', 'TC', 'QC', 'AC' ]))          # royal flush
print("9:", rank_hand([ 'JH', 'KH', 'TH', 'QH', 'AH' ]))          # royal flush

print("8:", rank_hand([ '2D', '3D', '4D', '5D', '6D' ]))          # straight flush
print("8:", rank_hand([ '6C', '4C', '5C', '2C', '3C' ]))          # straight flush
print("8:", rank_hand([ '7S', 'TS', 'JS', '8S', '9S' ]))          # straight flush
print("8:", rank_hand([ '5H', '4H', '7H', '8H', '6H' ]))          # straight flush

print("8:", rank_hand([ 'AH', '2H', '3H', '4H', '5H' ]))          # straight flush with ace
print("8:", rank_hand([ 'AD', '2D', '3D', '4D', '5D' ]))          # straight flush with ace
print("8:", rank_hand([ 'AS', '2S', '3S', '4S', '5S' ]))          # straight flush with ace
print("0:", rank_hand([ 'AH', '5D', '3S', '4D', 'TC' ]))          # high card

print("7:", rank_hand([ '5H', '5D', '5S', '5C', 'TC' ]))          # four of a kind
print("6:", rank_hand([ '5H', '5D', 'TS', 'TC', 'TH' ]))          # full house

print("7:", rank_hand([ '6D', 'AH', 'AS', 'AD', 'AC' ]))          # four of a kind
print("7:", rank_hand([ 'QD', 'KH', 'KS', 'KC', 'KD' ]))          # four of a kind
print("7:", rank_hand([ 'TH', '7H', '7S', '7D', '7C' ]))          # four of a kind
print("7:", rank_hand([ '9S', '9D', '9C', '9H', 'KD' ]))          # four of a kind

print("6:", rank_hand([ '5H', '5D', 'TS', 'TC', 'TH' ]))         # full house
print("2:", rank_hand([ '5H', '5D', '6S', 'TC', 'TH' ]))         # two pairs
print("6:", rank_hand([ 'KH', 'QD', 'QS', 'QC', 'KS' ]))         # full house
print("6:", rank_hand([ 'TH', 'AD', 'AS', 'TC', 'AH' ]))         # full house

print("6:", rank_hand([ 'AD', '9S', 'AH', 'AC', '9H' ]))         # full house
print("6:", rank_hand([ '4H', '5D', '4S', '4C', '5H' ]))         # full house
print("6:", rank_hand([ 'KH', 'KD', 'QS', 'QC', 'KS' ]))         # full house
print("6:", rank_hand([ 'AH', 'AD', 'AS', 'TC', 'TH' ]))         # full house

print("5:", rank_hand([ '2D', '5D', 'TD', '9D', 'KD' ]))          # flush
print("5:", rank_hand([ 'AC', '2C', '3C', '9C', '5C' ]))          # flush
print("5:", rank_hand([ '4S', 'TS', '8S', '3S', 'QS' ]))          # flush
print("5:", rank_hand([ 'QH', 'KH', '2H', '8H', '9H' ]))          # flush

print("4:", rank_hand([ '3D', '5D', '6C', '2S', '4H' ]))          # straight
print("4:", rank_hand([ 'TD', 'JD', 'QC', 'KS', 'AH' ]))          # straight
print("4:", rank_hand([ '3D', '2H', '4C', '5S', '6D' ]))          # straight
print("4:", rank_hand([ '2S', '3D', '4H', '5D', '6C' ]))          # straight
print("4:", rank_hand([ '6C', '4D', '5C', '2H', '3C' ]))          # straight
print("4:", rank_hand([ '7S', 'TD', 'JD', '8S', '9S' ]))          # straight
print("4:", rank_hand([ '5H', '4C', '7C', '8D', '6S' ]))          # straight

print("3:", rank_hand([ '2D', '5D', 'TD', '9S', 'KC' ]))          # three of a kind
print("3:", rank_hand([ 'AC', '2C', '3D', '9D', '5C' ]))          # three of a kind
print("3:", rank_hand([ '4S', 'TC', '8C', '3S', 'QS' ]))          # three of a kind
print("3:", rank_hand([ 'QH', 'KD', '2S', '8H', '9H' ]))          # three of a kind

print("2:", rank_hand([ 'QH', 'QS', '2S', '2D', '9D' ]))          # two pairs
print("2:", rank_hand([ 'QH', 'KH', 'KS', '8D', '8C' ]))          # two pairs
print("2:", rank_hand([ 'QH', 'KH', '3S', '3D', 'KC' ]))          # two pairs
print("2:", rank_hand([ 'TH', 'AH', '4S', 'AD', 'TC' ]))          # two pairs

'''
# test straight check
print(check_straight([ 'TD', 'TC', 'TS', 'TC', 'AD']))
print(check_straight([ 'TD', 'TC', 'KS', 'TC', 'AD']))
print(check_straight([ 'TD', 'JD', 'QD', 'KD', 'AD' ]))
print(check_straight([ 'TD', 'JD', 'QC', 'KS', 'AH' ]))

# test flush check
# print(check_flush([ 'TD', 'JD', 'QD', 'KD', 'AD' ]))
# print(check_flush([ 'TD', 'JD', 'QC', 'KS', 'AH' ]))
'''
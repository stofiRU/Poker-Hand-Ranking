# tests for rank_hand.py
from rank_hand import rank_hand

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
print(check_flush([ 'TD', 'JD', 'QD', 'KD', 'AD' ]))
print(check_flush([ 'TD', 'JD', 'QC', 'KS', 'AH' ]))
'''
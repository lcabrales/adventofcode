from collections import Counter
from functools import cmp_to_key

file_path = 'day7.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

is_part1 = False
if is_part1:
    card_labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
else:
    card_labels = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_hand_rank(hand):
    label_counts = Counter(hand)
    
    if 5 in label_counts.values():
        rank = 6 # five of a kind
    elif 4 in label_counts.values():
        rank = 5 # four of a kind
    elif 3 in label_counts.values() and 2 in label_counts.values():
        rank = 4 # full house
    elif 3 in label_counts.values():
        rank = 3 # three of a kind
    elif list(label_counts.values()).count(2) == 2:
        rank = 2 # two pair
    elif list(label_counts.values()).count(2) == 1:
        rank = 1 # one pair
    else:
        rank = 0 # high card

    if is_part1:
        return rank
    
    if 'J' in label_counts:
        best_hand_type = 0
        for label in card_labels:
            if label == 'J':
                continue
            hand_with_joker = hand.replace('J', label)
            hand_type = get_hand_rank(hand_with_joker)
            if hand_type > best_hand_type:
                best_hand_type = hand_type
        rank = best_hand_type

    return rank

def compare_hands(hand1, hand2):
    rank1 = get_hand_rank(hand1)
    rank2 = get_hand_rank(hand2)

    if rank1 != rank2:
        return rank1 - rank2
    
    for i in range(len(hand1)):
        index1 = card_labels.index(hand1[i])
        index2 = card_labels.index(hand2[i])

        if index1 != index2:
            return index2 - index1
        
    return 0

hands_dict = {}
for line in lines:
    line = line.strip()

    hand, bid = line.split()
    hands_dict[hand] = bid

hands = sorted(hands_dict.keys(), key=cmp_to_key(compare_hands))
ans = 0
for index, hand in enumerate(hands, start=1):
    bid = int(hands_dict[hand])
    ans += index * bid

print(ans)

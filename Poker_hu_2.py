import random


SUITS = ['Herz', 'Karo', 'Pik', 'Kreuz']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Bube', 'Dame', 'König', 'Ass']
deck = [(rank, suit) for rank in RANKS for suit in SUITS]


def deal_cards(deck):
    random.shuffle(deck)

    player_hand = [deck[i] for i in range(2)]

    community_cards = [deck[i+2] for i in range(3)]
    return player_hand, community_cards

def count_ranks(cards):
    rank_counts = {}
    for card in cards:
        rank = card[0]
        if rank in rank_counts:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        else:
            rank_counts[rank] = 1
    return rank_counts



# Kombinationen erkennen
def evaluate_hand(player_hand, community_cards):

    all_cards = player_hand + community_cards
    rank_counts = count_ranks(all_cards)



    if 4 in rank_counts.values():
        return "Vierling (Four of a Kind)"
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        return "Full House"
    elif 3 in rank_counts.values():
        return "Drilling (Three of a Kind)"
    elif list(rank_counts.values()).count(2) == 2:
        return "Zwei Paare (Two Pairs)"
    elif 2 in rank_counts.values():
        return "Ein Paar (One Pair)"
    else:
        highest_card = max(player_hand + community_cards, key=lambda card: RANKS.index(card[0]))
        return f"High Card: {highest_card[0]}, {highest_card[1]}"


player_hand, community_cards = deal_cards(deck)
print(f"Spielerhand: {player_hand}")
print(f"Gemeinschaftskarten: {community_cards}")


hand_combination = evaluate_hand(player_hand, community_cards)
print(f"Beste Handkombination: {hand_combination}")

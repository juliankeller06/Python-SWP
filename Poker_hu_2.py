import random

# Definieren der Kartenfarben und Kartenwerte
SUITS = ['Herz', 'Karo', 'Pik', 'Kreuz']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Bube', 'Dame', 'König', 'Ass']
deck = [(rank, suit) for rank in RANKS for suit in SUITS]


# Karten austeilen
def deal_cards(deck):
    random.shuffle(deck)
    player_hand = [deck[i] for i in range(2)]
    community_cards = [deck[i + 2] for i in range(3)]
    return player_hand, community_cards


# Ränge der Karten zählen
def count_ranks(cards):
    rank_counts = {}
    for card in cards:
        rank = card[0]
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    return rank_counts


# Farben (Suits) der Karten zählen
def count_suits(cards):
    suit_counts = {}
    for card in cards:
        suit = card[1]
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1
    return suit_counts


# Überprüfen, ob die Karten eine Straße (Straight) bilden
def is_straight(cards):
    values = [card[0] for card in cards]
    indices = sorted([RANKS.index(value) for value in values])
    print(indices)

    # Sonderfall für A, 2, 3, 4, 5
    if indices == [0, 1, 2, 3, 12]:
        return True

    # Prüfen, ob die Indizes aufeinanderfolgend sind
    for i in range(1, len(indices)):
        if indices[i] != indices[i - 1] + 1:
            return False
    return True


# Flush erkennen
def is_flush(cards):
    suit_counts = count_suits(cards)
    # Wenn eine Farbe 5-mal vorkommt, handelt es sich um einen Flush
    return 5 in suit_counts.values()


# Straight Flush erkennen
def is_straight_flush(cards):
    return is_flush(cards) and is_straight(cards)


# Royal Flush erkennen
def is_royal_flush(cards):
    values = [card[0] for card in cards]
    royal_values = [10, 'Bube', 'Dame', 'König', 'Ass']
    return is_flush(cards) and sorted(values) == sorted(royal_values)


# Handkombinationen auswerten
def evaluate_hand(player_hand, community_cards):
    all_cards = player_hand + community_cards
    rank_counts = count_ranks(all_cards)

    # Überprüfen, ob es sich um einen Royal Flush handelt
    if is_royal_flush(all_cards):
        return "Royal Flush"
    # Straight Flush erkennen
    elif is_straight_flush(all_cards):
        return "Straight Flush"
    # Flush erkennen
    elif is_flush(all_cards):
        return "Flush"
    # Straight erkennen
    elif is_straight(all_cards):
        return "Straight"
    # Vierling (Four of a Kind) erkennen
    elif 4 in rank_counts.values():
        return "Vierling (Four of a Kind)"
    # Full House erkennen
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        return "Full House"
    # Drilling (Three of a Kind) erkennen
    elif 3 in rank_counts.values():
        return "Drilling (Three of a Kind)"
    # Zwei Paare erkennen
    elif list(rank_counts.values()).count(2) == 2:
        return "Zwei Paare (Two Pairs)"
    # Ein Paar erkennen
    elif 2 in rank_counts.values():
        return "Ein Paar (One Pair)"
    # Falls keine Kombination vorliegt, die höchste Karte ausgeben
    else:
        highest_card = max(all_cards, key=lambda card: RANKS.index(card[0]))
        return f"High Card: {highest_card[0]}, {highest_card[1]}"


def main():
    # Karten austeilen und Handkombination ermitteln
    player_hand, community_cards = deal_cards(deck)
    print(f"Spielerhand: {player_hand}")
    print(f"Gemeinschaftskarten: {community_cards}")

    hand_combination = evaluate_hand(player_hand, community_cards)
    print(f"Kombination: {hand_combination}")

if __name__ == '__main__':
    main()

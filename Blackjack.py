import random

logo = '''
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                 
'''

CARDS = ['''
 -------
|K      |
|       |
|       |
|       |
|      K|
 ------- ''', '''
 -------
|Q      |
|       |
|       |
|       |
|      Q|
 ------- ''', ''' 
 -------
|J      |
|       |
|       |
|       |
|      J|
 ------- ''', '''
 -------
|10     |
|       |
|       |
|       |
|     10|
 ------- ''', '''
 -------
|9      |
|       |
|       |
|       |
|      9|
 ------- ''', '''
 -------
|8      |
|       |
|       |
|       |
|      8|
 ------- ''', '''
 -------
|7      |
|       |
|       |
|       |
|      7|
 ------- ''', '''
 -------
|6      |
|       |
|       |
|       |
|      6|
 ------- ''', '''
 -------
|5      |
|       |
|       |
|       |
|      5|
 ------- ''', '''
 -------
|4      |
|       |
|       |
|       |
|      4|
 ------- ''', '''
 -------
|3      |
|       |
|       |
|       |
|      3|
 ------- ''', '''
 -------
|2      |
|       |
|       |
|       |
|      2|
 ------- ''', ''' 
 -------
|A      |
|       |
|       |
|       |
|      A|
 ------- '''
]

BLANKCARD = '''
 -------
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
 ------- '''


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck2 = {"K": CARDS[0], "Q": CARDS[1], "J": CARDS[2], 10: CARDS[3], 9: CARDS[4], 8: CARDS[5], 7: CARDS[6], 6: CARDS[7],
         5: CARDS[8], 4: CARDS[9], 3: CARDS[10], 2: CARDS[11], "A": CARDS[12]}

global player_cards
global dealer_cards
global phand_value
global dhand_value


def player_hand(z):
    while z > 0:
        player_cards.append(random.choice(deck))
        for y in deck2:
            if y == (player_cards[len(player_cards) - 1]):
                print(deck2[y])
        z -= 1

    player_check()


def dealer_hand(z):
    while z > 0:
        dealer_cards.append(random.choice(deck))
        for y in deck2:
            if y == (dealer_cards[len(dealer_cards) - 1]):
                print(deck2[y])
        z -= 1

    dealer_check()


def player_check():
    global phand_value
    phand_value = 0
    for a in player_cards:
        if a in deck[9:13]:
            phand_value += 10
        else:
            phand_value += a

    print(f"Player has {phand_value}")

    if phand_value > 21:
        print("Player Bust")


def dealer_check():
    global dhand_value
    dhand_value = 0
    for u in dealer_cards:
        if u in deck[9:13]:
            dhand_value += 10
        else:
            dhand_value += u

    print(f"Dealer has {dhand_value}")

    if dhand_value > 21:
        print("Dealer Bust")


def play_game():
    global player_cards
    player_cards = []
    global dealer_cards
    dealer_cards = []
    global phand_value
    phand_value = 0
    global dhand_value
    dhand_value = 0

    print(logo)
    print("Welcome to Blackjack")

    player_hand(2)
    dealer_hand(1)

    while phand_value < 21:
        if input("Hit or Stand? ").lower() == "hit":
            print("Hit")
            player_hand(1)
        else:
            print("Stand")
            break

    while dhand_value < 21 and phand_value <= 21:
        if dhand_value < phand_value:
            dealer_hand(1)
        elif phand_value < dhand_value < 21:
            print("Dealer Wins")
            break
        else:
            print("Draw")
            break

    if input("Play Again: Y or N").lower() == "y":
        play_game()


play_game()


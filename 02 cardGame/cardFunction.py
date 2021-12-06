import random

def createNewDeck():
    number = list(range(1, 14))
    priority = list(range(1,5))
    court = [0, "J", "Q", "K"]
    deck = list(range(0, 52))

    for i in range(10):
        deck[i] = [number[i], priority[0], court[0]]
    for i in range(10):
        deck[i+13] = [number[i], priority[1], court[0]]
    for i in range(10):
        deck[i+26] = [number[i], priority[2], court[0]]
    for i in range(10):
        deck[i+39] = [number[i], priority[3], court[0]]

    for i in range(3):
        deck[i+10] = [10, priority[0], court[i+1]]
    for i in range(3):
        deck[i+23] = [10, priority[1], court[i+1]]
    for i in range(3):
        deck[i+36] = [10, priority[2], court[i+1]]
    for i in range(3):
        deck[i+49] = [10, priority[3], court[i+1]]

    return deck

def handOut(deck: list):
    player = deck[0:2]
    del deck[0:2]
    
    return player, deck

def drawOne(player: list, deck: list):
    card = deck[0]
    player3card = list(range(0,3))
    player3card[0] = player[0]
    player3card[1] = player[1]
    player3card[2] = card

    del deck[0]

    return player3card, deck

def judge(player1: list, player2: list):
    if len(player1) == 2 and (player1[0][0] + player1[1][0])%10 == 8 or (player1[0][0] + player1[1][0])%10 == 9:
        return "player1 win"
    elif len(player2) == 2 and (player2[0][0] + player2[1][0])%10 == 8 or (player2[0][0] + player2[1][0])%10 == 9:
        return "player2 win"
    else: 
        if len(player1) == 3 and type(player1[0][2]) is str and type(player1[1][2]) is str and type(player1[2][2]) is str:
            return "player1 win"
        elif len(player2) == 3 and type(player2[0][2]) is str and type(player2[1][2]) is str and type(player2[2][2]) is str:
            return "player2 win"
        else:
            score1 = 0
            for i in range(len(player1)):
                score1 = score1 + player1[i][0]
        
                if score1 > 10:
                    score1 = score1 % 10
                else:
                    continue

            score2 = 0
            for i in range(len(player2)):
                score2 = score2 + player2[i][0]

                if score2 > 10:
                    score2 = score2 % 10
                else:
                    continue

            if score1 > score2:
                return "player1 win"
            elif score2 > score1:
                return "player2 win"
            else:
                return "tie"

def  numToSign(hand: list):
    for i in range(len(hand)):
        if hand[i][1] == 1:
            hand[i][1] = "Club"
        elif hand[i][1] == 2:
            hand[i][1] = "Diamond"
        elif hand[i][1] == 3:
            hand[i][1] = "Heart"
        else:
            hand[i][1] = "Spade"
    return hand



import cardFunction
import random

deck1 = cardFunction.createNewDeck()
random.shuffle(deck1)

player, deck1 = cardFunction.handOut(deck1)
enemy, deck1 = cardFunction.handOut(deck1)
playerRe = cardFunction.numToSign(player)
enemyRe = cardFunction.numToSign(enemy)

playerDraw, deck1 = cardFunction.drawOne(playerRe, deck1)
playerDrawRe = cardFunction.numToSign(playerDraw)


if (enemyRe[0][0] + enemyRe[1][0]) % 10 <= 4:
    enemyRe, deck1 = cardFunction.drawOne(enemyRe, deck1)
    enemyRe = cardFunction.numToSign(enemyRe)
else:
    card1 = enemyRe[0]
    card2 = enemyRe[1]
    enemyRe = [card1, card2, 0]

winner = cardFunction.judge(playerDrawRe, enemyRe)
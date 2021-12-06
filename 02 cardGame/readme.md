# My 2nd project for learning Python
This card game's rule
- 52 standard cards
- 2 players game
- each player draw 2 card
- each player don't know their enemy card
- player who has the most last number of card number's sum is the winner (if you get 8 and 7, your score is 5) and **if your score is 8 or 9, you win instanyly**
- if you 2 cards are bad, you can draw the 3rd card and sum your score again **if your 3 card is J, Q or K, you win instantly (except 8-9 from 2 cards)** 
- winning situation summary: 8-9 points from 2 card >> 3 J, Q or K >> compararing sum score

I devided this project into 3 parts:

### cardFunction.py: create fucntion for play this game
- function to create 52 cards deck
- function to give player 2 cards while start the game
- function to draw 3rd card (if you need)
- function to find the winner
- function to change card code to text (firstly, my card is like [4, 2, 0] << this is Diamond 2)

### script.py: compose each stage of playing
- import functions from cardFunction.py
- start the game with create new deck and give 2 cards to each player
- assign user's enemy to draw a 3rd card if sum score is lower than 5
- change card code into text
- find the winner

### playing.py: use tkinter to:
- create grid that contain 3 columns and 4 rows
- row[0] is for user card and 3 columns of this row will show 3 cards
- row[1] is enemy card, their 3 columns contain 2 or 3 cards and will show user after find the winner
- row[2] is display to show who is the winner
- row[3] is for user buttons including: start, draw, done

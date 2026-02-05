"""Rock paper scissors"""

player1 = input('Enter rock, paper or scissors: ')
player2 = input('Enter rock, paper or scissors: ')

if (player1 == 'rock' and player2 == 'scissors'):
    print('Player 1 wins')
elif (player1== 'scissors' and player2 == 'rock'):
    print('Player 2 wins')
elif (player1 == 'paper' and player2 == 'rock'):
    print('Player 1 wins')
elif (player1 == 'rock' and player2 == 'paper'):
    print('Player 2 wins')
elif (player1 == 'scissors' and player2 == 'paper'):
    print('Player 1 wins')
elif (player1 == 'paper' and player2 == 'scissors'):
    print('Player 2 wins')
else:
    print('Tie')

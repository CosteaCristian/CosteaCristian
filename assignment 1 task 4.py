#group 13 984165 and 965396
#we set move on valid for using it in the while loop
move='valid'
while move=='valid':
#inputing the moves
    goat=str(input('Please enter the move of the goat(w/e):'))
    wolf=str(input('Please enter the move of the wolf(w/e):'))
    cabbage=str(input('Please enter the move of the cabbage(w/e):'))
    man=str(input('Please enter the move of the man(w/e):'))  
#putting move invalid if there is made a wrong move so the game is lost
    if goat=='e' and wolf=='e':
        move='invalid'
    if goat=='e' and cabbage=='e':
        move='invalid'
        print('This move is',move) 
#if all the figures are on the other side of the river the game is won and it breaks
    if goat=='w' and wolf=='w' and cabbage=='w' and man=='w':
        print('The game is won')
        break
    if man=='e' and goat=='e' and cabbage=='e'and wolf=='e':
        move='valid'
    if man=='e' and goat=='e' and cabbage=='e':
        move='valid'
    if man=='e' and goat=='e' and wolf=='e':
        move='valid'

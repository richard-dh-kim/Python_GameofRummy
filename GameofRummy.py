import random

def make_deck(num):
    suits=[100,200,300,400]
    for i in range(1,num+1):
        for s in suits:
            deck.append(s+i)

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards_start(deck):
    if len(deck)>=7:
        for i in range(-7,0):
            player.append(deck[i])
            del deck[i]
    elif len(deck)<7:
        print("There is not enough cards in the deck to start")

def deal_new_cards(deck, player, num1):
    if num1 >= 1 and num1 <= 6:
        if len(deck)>=num1:
            for i in range(-num1,0):
                player.append(deck[i])
                del deck[i]
        elif num1>len(deck):
            for i in range(-len(deck),0):
                player.append(deck[i])
                del deck[i]
    else:
        print("The number must be bigger or equal to 1, and smaller or equal to 6.")

def print_deck_twice(hand):
    firstprint=hand
    secondprint=hand
    def secondsorting(i):
        return (abs(i)%100)
    firstprint.sort()
    print(firstprint)
    secondprint.sort(key=secondsorting)
    print(secondprint)

def is_valid(cards,player):
    counter=0
    for x in cards:
        if x not in player:
            print(x," is not in your hand. Invalid input.")
            counter += 1
    if counter>0:
        return False
    elif counter==0:
        return True

def is_discardable_kind(cards):
    lasttwodigitslist=[]
    if len(cards)<2:
        print('Invalid sequence. Discardable set needs to have at least 2 cards.')
        return False
    elif len(cards)>=2:
        for i in cards:
            lasttwodigitslist.append(abs(i)%100)
        if lasttwodigitslist[1:]==lasttwodigitslist[:-1]:
            return True
        elif lasttwodigitslist[1:]!=lasttwodigitslist[:-1]:
            return False

def is_discardable_seq(cards):
    if len(cards)<3:
        print('Invalid sequence. Discardable sequence needs to have at least 3 cards.')
        return False
    elif len(cards)>=3:
        if sorted(cards) == list(range(min(cards), max(cards)+1)):
            return True
        elif sorted(cards) != list(range(min(cards), max(cards)+1)):
            return False 

def rolled_one_round(player):
    a=int(input('Discard any card of your choosing \nWhich card would you like to discard? '))
    while a not in player:
        print(a, '\nNo such card in the deck. Try again.')
        a=int(input('Which card would you like to discard? '))
    if a in player:
        player.remove(a)
        hand=player
        print_deck_twice(hand)

def rolled_nonone_round(player):
    a=input('Yes or no, do you have a sequences of three or more cards of the same suit or two or more of a kind? ')
    if a=="yes":
        raw_input=input('Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by sapce: ').strip().split()
        cards=[int(x) for x in raw_input]
        u=len(cards)
        if is_valid(cards,player)==True:
            if u<2:
                is_discardable_seq (cards)
                is_discardable_kind (cards)
                rolled_nonone_round(player)
            if 2< u <3:
                if is_discardable_kind(cards)==True:
                    player=[z for z in player if z not in cards]
                    hand=player
                    print_deck_twice(hand)
                    rolled_nonone_round(player)
                if is_discardable_kind(cards)==False:
                    for i in cards:
                        lasttwodigitslist.append(abs(i)%100)
                    print('Invalid meld: ', lasttwodigitslist[0], 'is not equal to ', lasttwodigitslist[1])
                    rolled_nonone_round(player)
            if u>=3:
                if is_discardable_kind(cards)==True:
                    player=[z for z in player if z not in cards]
                    hand=player
                    print_deck_twice(hand)
                    rolled_nonone_round(player)
                elif is_discardable_seq(cards)==True:
                    player=[z for z in player if z not in cards]
                    hand=player
                    print_deck_twice(hand)
                    rolled_nonone_round(player)
        else:
            rolled_nonone_round(player)
    elif a=='no':
        return
    else:
        rolled_nonone_round(player)


# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()
if size_change == 'yes':
    b=int(input("Enter a number between 3 and 99, for the number of ranks: "))
    print('You are playing with ', b*4, ' cards')
    print('Here is your starting hand printed in two ways')
    deck=[]
    player=[]
    make_deck(b)
    shuffle_deck(deck)
    deal_cards_start(deck)
    hand=player
    print_deck_twice(hand)
else:
    print('You are playing with 52 cards')
    print('Here is your starting hand printed in two ways')
    deck=[]
    player=[]
    make_deck(13)
    shuffle_deck(deck)
    deal_cards_start(deck)
    hand=player
    print_deck_twice(hand)
rounds=0
while len(deck)>0:
    rounds+=1
    print('Welcome to round ', rounds, '.')
    input('Please roll the dice.')
    num1=random.randint(1,6)
    print('You rolled the dice and it shows: ', num1)
    deal_new_cards(deck, player, num1)
    print('Here is your new hand printed in two ways:')
    print_deck_twice(hand)
    if num1 ==1:
        rolled_one_round(player)
        print('Round ', rounds, ' completed.')
    elif num1!=1:
        rolled_nonone_round(player)
        print('Round ', rounds, ' completed.')

if len(deck)==0:
    rounds+=1
    print('Welcome to round ', rounds, '.')
    print('This game is in empty deck phase.')
    while len(player)>0:
        print('Discard any card of your choosing')
        cards=list(int(input('Which card would you like to discard? ')))
        is_valid(cards,player)
    if len(player)==0:
        print('Round ', rounds,' completed.')
        print('Congratulations, you completed the game in', rounds, 'rounds.')
                   
    
    







  

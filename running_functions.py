# this is where we put all our functions that will be used as the foundation and logic

class Card:
    def __init__(self, color, shade, number, shape):
        self.color = color
        self.shade = shade
        self.number = number
        self.shape = shape
        self.img = 'xyz'

# The main logic of the card, using the philosophy of modulo
def find_third_card(first_card, second_card):
    # first card and second card should be 4-tuples with integer entries {1,2,3}
    third_card = [0,0,0,0]
    for i in range(4):
        if first_card[i] == second_card[i]:
            third_card[i] = first_card[i]
        else:
            third_card[i] = (first_card[i] + second_card[i]) % 4
            if third_card[i] == 0:
                third_card[i] = 2
    return tuple(third_card)


# I expect board to be a list of 12 tuples (or n tuples where n is the value user wants)

# This function is to transform the input trinary integer into the four characters of the card, each are from 1 to 3
# each card is a tuple of (a,b,c,d)
def trinary_transform(input_num):
    d = input_num % 3 + 1
    c = (input_num - (d-1)) // 3 % 3 + 1
    b = (input_num - (d-1) - (c-1)*3) // 9 % 3 + 1
    a = (input_num - (d-1) - (c-1)*3 - (b-1)*9) // 27 + 1
    return (a,b,c,d)

# This function is to generate a cardboard based on user defined number
def generate_cardboard(card_stack, number_of_cards = 12):
    if number_of_cards <= 3:
        raise ValueError("The initial card amount should be more than 3 cards")
    cardboard = []
    for i in range(number_of_cards):
        cardboard.append(card_stack.pop())
    return cardboard

# This function is to store all the scores of each card in one deck and will be used as hint
def hint(cardboard):
    # Score matrix is the matrix used to record the score of the cards and the highest score meaning they are most useful
    global score_matrix
    score_matrix = [0]*len(cardboard)
    # loop through all cards and check if there are any set present
    for i in range(len(cardboard)):
        for j in range(len(cardboard)):
            if i != j:
                if find_third_card(cardboard[i], cardboard[j]) in cardboard:
                    score_matrix[i] += 1
                    score_matrix[j] += 1
    return score_matrix

# This function is to prevent the case when there are no sets in the cards that are presented
# add three cards into the cardboard if none are no sets currently
def check_if_sets_present(cardboard, card_stack):
    is_set = False
    # loop through all cards and check if there are any set present
    for i in range(len(cardboard)):
        for j in range(len(cardboard)):
            if i != j:
                if find_third_card(cardboard[i], cardboard[j]) in cardboard:
                    is_set = True
    # if there are no sets after the loop, then add three cards onto the cardboard
    if not is_set and len(card_stack) >= 3:
        for k in range(3) and is_set is False:
            cardboard.pop()
            cardboard.append(card_stack.pop())
            check_if_sets_present(cardboard, card_stack)
    else:
        return True


# this function is to check if three user-chosen cards are a set
def check_set(cardboard, first_card, second_card, third_card, user_set_list, card_stack):
    # first check if there are sets present
    if check_if_sets_present(cardboard,card_stack):
        is_set = False
        if find_third_card(cardboard[first_card],cardboard[second_card]) == cardboard[third_card]:
            is_set = True
        if is_set and not end(card_stack):
            user_set_list.append((cardboard[first_card],cardboard[second_card],cardboard[third_card]))
            # these three lines are to change the cards that are considered to be a set with three new cards
            if len(card_stack) >= 2:
                cardboard[first_card] = card_stack.pop()
                cardboard[second_card] = card_stack.pop()
                cardboard[third_card] = card_stack.pop()
        elif end(card_stack):
            return False
        else:
            # this need to be programmed with pygame --> blink red if the cards they choose is not a set
            print("not a set")
            #raise ValueError("the three cards chosen is not a set")
        return cardboard

def end(card_stack):
    if len(card_stack) < 3:
        return True

# This file deals with mostly user interface and is responsible for the shown and flow of the entire game

import time
import pygame
import random
from running_functions import trinary_transform, generate_cardboard, check_set, end, hint


display_height = 300
display_width = 500
screen = pygame.display.set_mode([display_width, display_height])

# a color dictionary
colors = {"white":(255,255,255), "black" : (0,0,0), "red":(200,0,0),"green" :(0,200,0),"blue" : (0,0,200),"bright_red " : (255, 0, 0),"bright_green" : (0,255,0),"bright_blue" : (0,0,255)}

# The general button function that detects buttons, the press of bottons an direction to different functions
def button(message,location_x,location_y,width,height,inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # this is to change the color of the block to make the users know that they are over the button
    if location_x + width > mouse[0] > location_x and location_y + height > mouse[1] > location_y:
        pygame.draw.rect(screen, active_color, (location_x, location_y, width, height))
        # these are the directions when user press certain buttons and their message behind
        if click[0] == 1 and action != None:
            if action == "Easymode":
                game_play(20)
            elif action == "Hardmode":
                game_play(16)
            elif action == "Try again":
                game_intro()
            elif action == "Exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, inactive_color, (location_x, location_y, width, height))

    # this is how the instruction on the button will show
    small_text = pygame.font.Font("freesansbold.ttf", 15)
    text_surf, text_rect = text_object(message, small_text)
    text_rect.center = ((location_x+(width/2)), (location_y+(height/2)))
    screen.blit(text_surf, text_rect)

# this is the function of the introduction page to the game
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # make the screen all white
        screen.fill(colors["white"])
        large_text = pygame.font.Font("freesansbold.ttf", 50)
        text_surf, text_rect = text_object("Sets", large_text)
        text_rect.center = ((display_width / 2), (display_height / 3))
        screen.blit(text_surf, text_rect)

        # define the buttons we want on the intro page -- we want to give users
        button("Easy",100,150,80,40,colors["green,bright_green"],"Easymode")
        button("Hard", 320,150,80,40, colors["red,bright_red"], "Hardmode")

        pygame.display.update()


def text_object(text, font):
     text_surface = font.render(text, True, (0,0,0))
     return text_surface, text_surface.get_rect()


def game_play(num):
    screen.fill(colors["white"])

    user_set_list = []

    # card stack is the deck of all 81 possible cards
    card_stack = []

    cards = random.sample(range(0, 81), 81)
    for card_num in cards:
        card_stack.append(trinary_transform(card_num))
    # cardboard is the deck of cards that will appear on the screen that is randomly popped from the all element list
    cardboard = generate_cardboard(card_stack, num)

    #card_stack = card_stack[:6]

    # the implementation of a timer that will give the user a final score of how long they used to finish the deck
    start = time.time()
    time_elapsed_cal = 0

    done = False
    # defining buttons
    button1 = pygame.Rect(0, 0, 100, 50)
    button2 = pygame.Rect(100, 0, 100, 50)
    button3 = pygame.Rect(200, 0, 100, 50)
    button4 = pygame.Rect(300, 0, 100, 50)
    button5 = pygame.Rect(0, 50, 100, 50)
    button6 = pygame.Rect(100, 50, 100, 50)
    button7 = pygame.Rect(200, 50, 100, 50)
    button8 = pygame.Rect(300, 50, 100, 50)
    button9 = pygame.Rect(0, 100, 100, 50)
    button10 = pygame.Rect(100, 100, 100, 50)
    button11 = pygame.Rect(200, 100, 100, 50)
    button12 = pygame.Rect(300, 100, 100, 50)
    button13 = pygame.Rect(0, 150, 100, 50)
    button14 = pygame.Rect(100, 150, 100, 50)
    button15 = pygame.Rect(200, 150, 100, 50)
    button16 = pygame.Rect(300, 150, 100, 50)
    button17 = pygame.Rect(0, 200, 100, 50)
    button18 = pygame.Rect(100, 200, 100, 50)
    button19 = pygame.Rect(200, 200, 100, 50)
    button20 = pygame.Rect(300, 200, 100, 50)
    hint_button = pygame.Rect(410,20,80,40)

    cards_selected = []
    card_dict = {f: i for i, f in enumerate(cardboard)}
    while not done:
        button("Hint", 410, 20, 80, 40, colors["green"], colors["bright_green"])
        button("Quit", 410, 80, 80, 40, colors["red"], colors["bright_red"], "Exit")

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button1.collidepoint(mouse_pos):
                    # prints current location of mouse
                    if cardboard[0] not in cards_selected:
                        cards_selected.append(cardboard[0])
                        pygame.draw.rect(screen, (0, 0, 255), (0, 0, 100, 50), 10)
                    else:
                        cards_selected.remove(cardboard[0])
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif button2.collidepoint(mouse_pos):
                    if cardboard[1] not in cards_selected:
                        cards_selected.append(cardboard[1])
                    else:
                        cards_selected.remove(cardboard[1])
                    print(cards_selected)
                    print('button2 was pressed at {0}'.format(mouse_pos))
                elif button3.collidepoint(mouse_pos):
                    if cardboard[2] not in cards_selected:
                        cards_selected.append(cardboard[2])
                    else:
                        cards_selected.remove(cardboard[2])
                    print(cards_selected)
                    # prints current location of mouse
                    print('button3 was pressed at {0}'.format(mouse_pos))
                elif button4.collidepoint(mouse_pos):
                    if cardboard[3] not in cards_selected:
                        cards_selected.append(cardboard[3])
                    else:
                        cards_selected.remove(cardboard[3])
                    # prints current location of mouse
                    print('button4 was pressed at {0}'.format(mouse_pos))
                elif button5.collidepoint(mouse_pos):
                    if cardboard[4] not in cards_selected:
                        cards_selected.append(cardboard[4])
                    else:
                        cards_selected.remove(cardboard[4])
                    # prints current location of mouse
                    print('button5 was pressed at {0}'.format(mouse_pos))
                elif button6.collidepoint(mouse_pos):
                    if cardboard[5] not in cards_selected:
                        cards_selected.append(cardboard[5])
                    else:
                        cards_selected.remove(cardboard[5])
                    # prints current location of mouse
                    print('button6 was pressed at {0}'.format(mouse_pos))
                elif button7.collidepoint(mouse_pos):
                    if cardboard[6] not in cards_selected:
                        cards_selected.append(cardboard[6])
                    else:
                        cards_selected.remove(cardboard[6])
                    # prints current location of mouse
                    print('button7 was pressed at {0}'.format(mouse_pos))
                elif button8.collidepoint(mouse_pos):
                    if cardboard[7] not in cards_selected:
                        cards_selected.append(cardboard[7])
                    else:
                        cards_selected.remove(cardboard[7])
                    # prints current location of mouse
                    print('button8 was pressed at {0}'.format(mouse_pos))
                elif button9.collidepoint(mouse_pos):
                    if cardboard[8] not in cards_selected:
                        cards_selected.append(cardboard[8])
                    else:
                        cards_selected.remove(cardboard[8])
                    # prints current location of mouse
                    print('button9 was pressed at {0}'.format(mouse_pos))
                elif button10.collidepoint(mouse_pos):
                    if cardboard[9] not in cards_selected:
                        cards_selected.append(cardboard[9])
                    else:
                        cards_selected.remove(cardboard[9])
                    # prints current location of mouse
                    print('button10 was pressed at {0}'.format(mouse_pos))
                elif button11.collidepoint(mouse_pos):
                    if cardboard[10] not in cards_selected:
                        cards_selected.append(cardboard[10])
                    else:
                        cards_selected.remove(cardboard[10])
                    # prints current location of mouse
                    print('button11 was pressed at {0}'.format(mouse_pos))
                elif button12.collidepoint(mouse_pos):
                    if cardboard[11] not in cards_selected:
                        cards_selected.append(cardboard[11])
                    else:
                        cards_selected.remove(cardboard[11])
                    # prints current location of mouse
                    print('button12 was pressed at {0}'.format(mouse_pos))
                elif button13.collidepoint(mouse_pos):
                    if cardboard[12] not in cards_selected:
                        cards_selected.append(cardboard[12])
                    else:
                        cards_selected.remove(cardboard[12])
                    # prints current location of mouse
                    print('button13 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif button14.collidepoint(mouse_pos):
                    # prints current location of mouse
                    if cardboard[13] not in cards_selected:
                        cards_selected.append(cardboard[13])
                    else:
                        cards_selected.remove(cardboard[13])
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif button15.collidepoint(mouse_pos):
                    # prints current location of mouse
                    if cardboard[14] not in cards_selected:
                        cards_selected.append(cardboard[14])
                    else:
                        cards_selected.remove(cardboard[14])
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif button16.collidepoint(mouse_pos):
                    # prints current location of mouse
                    if cardboard[15] not in cards_selected:
                        cards_selected.append(cardboard[15])
                    else:
                        cards_selected.remove(cardboard[15])
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif button17.collidepoint(mouse_pos):
                    # prints current location of mouse
                    if cardboard[16] not in cards_selected:
                        cards_selected.append(cardboard[16])
                    else:
                        cards_selected.remove(cardboard[16])
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif button18.collidepoint(mouse_pos):
                    # prints current location of mouse
                    if cardboard[17] not in cards_selected:
                        cards_selected.append(cardboard[17])
                    else:
                        cards_selected.remove(cardboard[17])
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif button19.collidepoint(mouse_pos):
                    # prints current location of mouse
                    if cardboard[18] not in cards_selected:
                        cards_selected.append(cardboard[18])
                    else:
                        cards_selected.remove(cardboard[18])
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif button20.collidepoint(mouse_pos):
                    # prints current location of mouse
                    if cardboard[19] not in cards_selected:
                        cards_selected.append(cardboard[19])
                    else:
                        cards_selected.remove(cardboard[19])
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    print(cards_selected)
                elif hint_button.collidepoint(mouse_pos):
                    score_matrix = hint(cardboard)
                    if len(cards_selected) == 0:
                        max_val = max(score_matrix)
                        max_index = score_matrix.index(max_val)
                        cards_selected.append(cardboard[max_index])
        # to refill the screen to be white
        screen.fill((255, 255, 255))

        for i in range(len(cardboard)):
            imgtoload = "/Users/sharonwang/PycharmProjects/107project-wang-wang-soemitro/Card_Images/{}{}{}{}.png"
            img = pygame.image.load(
                imgtoload.format(cardboard[i][0], cardboard[i][1], cardboard[i][2], cardboard[i][3]))
            if i == 0:
                screen.blit(img, (0, 0))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (0, 0, 100, 50), 2)
            elif i == 1:
                screen.blit(img, (100, 0))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (100, 0, 100, 50), 2)
            elif i == 2:
                screen.blit(img, (200, 0))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (200, 0, 100, 50), 2)
            elif i == 3:
                screen.blit(img, (300, 0))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (300, 0, 100, 50), 2)
            elif i == 4:
                screen.blit(img, (0, 50))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (0, 50, 100, 50), 2)
            elif i == 5:
                screen.blit(img, (100, 50))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (100, 50, 100, 50), 2)
            elif i == 6:
                screen.blit(img, (200, 50))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (200, 50, 100, 50), 2)
            elif i == 7:
                screen.blit(img, (300, 50))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (300, 50, 100, 50), 2)
            elif i == 8:
                screen.blit(img, (0, 100))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (0, 100, 100, 50), 2)
            elif i == 9:
                screen.blit(img, (100, 100))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (100, 100, 100, 50), 2)
            elif i == 10:
                screen.blit(img, (200, 100))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (200, 100, 100, 50), 2)
            elif i == 11:
                screen.blit(img, (300, 100))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (300, 100, 100, 50), 2)
            elif i == 12:
                screen.blit(img, (0, 150))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (0, 150, 100, 50), 2)
            elif i == 13:
                screen.blit(img, (100, 150))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (100, 150, 100, 50), 2)
            elif i == 14:
                screen.blit(img, (200, 150))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (200, 150, 100, 50), 2)
            elif i == 15:
                screen.blit(img, (300, 150))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (300, 150, 100, 50), 2)
            elif i == 16:
                screen.blit(img, (0, 200))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (0, 200, 100, 50), 2)
            elif i == 17:
                screen.blit(img, (100, 200))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (100, 200, 100, 50), 2)
            elif i == 18:
                screen.blit(img, (200, 200))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (200, 200, 100, 50), 2)
            elif i == 19:
                screen.blit(img, (300, 200))
                if cardboard[i] in cards_selected:
                    pygame.draw.rect(screen, (0, 0, 255), (300, 200, 100, 50), 2)

        if len(cards_selected) >= 3:
            check_set(cardboard, card_dict[cards_selected[0]], card_dict[cards_selected[1]],
                      card_dict[cards_selected[2]], user_set_list, card_stack)
            cards_selected = []
            card_dict = {f: i for i, f in enumerate(cardboard)}

        # check_if_sets_present(cardboard, card_stack)
        pygame.display.flip()
        if end(card_stack) is True and not done:
            final = time.time()
            done = True
            time_elapsed_cal = (final - start)
            time_elapsed_cal = round(time_elapsed_cal, 2)
    message_display("Your time used is {}s".format(str(time_elapsed_cal)))

# display message when game ends
def message_display(text):
    message = True
    while message:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(colors["white"])
        large_text = pygame.font.Font("freesansbold.ttf", 30)
        text_surf, text_rect = text_object(text, large_text)
        text_rect.center = ((display_width / 2), (display_height / 3))
        screen.blit(text_surf, text_rect)

        button("Easy", 80, 150, 80, 40, colors["green"], colors["bright_green"], "Easymode")
        button("Hard", 220, 150, 80, 40, colors["red"], colors["bright_red"], "Hardmode")
        button("Quit", 360, 150, 80, 40, colors["blue"], colors["bright_blue"], "Exit")

        pygame.display.update()
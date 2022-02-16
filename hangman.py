from random import choice
import os                                                                                            #For cleaning screen
import sys                                                                                           #For program exiting

def print_logo(lifes):                                                                               #Hangman printing
    os.system('cls||clear')                                                                          #CLEARING console
    print("\033[36m********************************************************************************")
    print("*------------------------------------------------------------------------------*")
    print("*|                                HANGMAN                                     |*")
    print("*------------------------------------------------------------------------------*")
    print("********************************************************************************\n")
    gibbet(lifes)                                                                                    #PRINTING gibbet

def gibbet(lifes):                                                                                   #PRINTING gibbet with lifes logic
    print("********************************************************************************")        #1(28)
    print("*------------------------------------------------------------------------------*")        #2(27)
    print("*|                                                                            |*")        #3(26)
    print("*|                                                                            |*")        #4(25)
    print("*|                                                                            |*")        #5(24)
    print("*|                                                                            |*")        #6(23)
    print("*|                                                                            |*")        #7(22)
    print("*|                       *******                                              |*")        #8(21)
    print("*|                    ***       ***                                           |*")        #9(20)
    print("*|                 ***             ***                                        |*")        #10(19)
    print("*|              ***                   ***                                     |*")        #11(18)
    print("*|           ***                         ***                                  |*")        #12(17)
    print("*|        ***                               ***                               |*")        #13(16)
    print("*|     ***                                     ***                            |*")        #14(15)
    print("*|  *************************************************                         |*")        #15(14)
    print("*|          *********************************                                 |*")        #16(13)
    print("*|          *                               *                                 |*")        #17(12)
    print("*|          *  *********                    *                                 |*")        #18(11)
    print("*|          *  *   |   *        ********    *                                 |*")        #19(10)
    print("*|          *  *-------*        *      *    *                                 |*")        #20(9)
    print("*|          *  *   |   *        *      *    *                                 |*")        #21(8)
    print("*|          *  *********        *    @ *    *                                 |*")        #22(7)
    print("*|          *                   *      *    *                                 |*")        #23(6)
    print("*|          *                   *      *    *                                 |*")        #24(5)
    print("*|          *********************************                                 |*")        #25(4)
    print("*|                                                                            |*")        #26(3)
    print("*------------------------------------------------------------------------------*")        #27(2)
    print("********************************************************************************")        #28(1)
    if(lifes <= 9):                                                                                  #FIRST module of gibbet(adding first vertical module(6))
        print("\033[4F\033[56C**\033[2D", end='')                                                    #Standing in start position + printing '**'
        for i in range(5):
            print("\033[1A**\033[2D", end='')                                                        #Standing (for upper position, two left) and printing **
        print("\033[9E", end='')                                                                     #Returning to entered position
    if(lifes <= 8):                                                                                  #SECOND module of gibbet(adding middle vertical module(6))
        print("\033[9F\033[56C**\033[2D", end='')                                                    #Standing in start position + printing '**'
        for i in range(5):
            print("\033[1A**\033[2D", end='')                                                        #Standing (for upper position, two left) and printing **
        print("\033[14E", end='')                                                                    #Returning to entered position
    if(lifes <= 7):                                                                                  #THIRD module of gibbet(adding last vertical module(6))
        print("\033[15F\033[56C**\033[2D", end='')                                                   #Standing in start position + printing '**'
        for i in range(5):
            print("\033[1A**\033[2D", end='')                                                        #Standing (for upper position, two left) and printing **
        print("\033[20E", end='')                                                                    #Returning to entered position
    if(lifes <= 6):                                                                                  #FOURTH module of gibbet(adding horizontal plank)
        print("\033[20F\033[58C**************\033[2D", end='')                                       #Standing in start position + printing '**************'
        print("\033[20E", end='')                                                                    #Returning to entered position
    if(lifes <= 5):                                                                                  #FIFTH module of gibbet(adding rope)
        print("\033[19F\033[71C*\033[1D", end='')                                                    #Standing in start position + printing '*'
        for i in range(3):
            print("\033[1B*\033[1D", end='')                                                         #Standing lower and printing *
        print("\033[16E", end='')                                                                    #Returning to entered position
    if(lifes <= 4):                                                                                  #SIXTH module of gibbet(adding face)
        print("\033[15F\033[70C🥲\033[1D", end='')                                                   #Standing in start position + printing '🥲'(face)
        print("\033[15E", end='')                                                                    #Returning to entered position
    if(lifes <= 3):                                                                                  #SEVENTH module of gibbet(body + change face)
        print("\033[15F\033[70C😒\033[1D", end='')                                                   #Standing in start position + printing '😒'(face)
        for i in range(4):
            print("\033[1B|\033[1D", end='')                                                         #Standing (lower and left) and printing |
        print("\033[11E", end='')                                                                    #Returning to entered position
    if(lifes <= 2):                                                                                  #EIGHTS module of gibbet(adding arms + change face)
        print("\033[15F\033[70C😤\033[2D", end='')                                                   #Standing in start position + printing '😤'(face)
        print("\033[1B\\\033[1C/", end='')                                                           #Standing lower and printing \   /
        print("\033[1A\033[4D\\\033[3C/", end='')                                                    #Standing lower and printing \ /
        print("\033[15E", end='')                                                                    #Returning to entered position
    if(lifes <= 1):                                                                                  #NINTH module of gibbet(adding legs + change face)
        print("\033[15F\033[70C😱\033[2D", end='')                                                   #Standing in start position + printing '😱'(face)
        print("\033[5B/\033[1C\\", end='')                                                           #Standing lower and printing / \
        print("\033[1B\033[4D/\033[3C\\", end='')                                                    #Standing lower and printing /   \
        print("\033[9E", end='')                                                                     #Returning to entered position
    if(lifes <= 0):                                                                                  #TENTH(LAST) module of gibbet(dying face)
        print("\033[15F\033[70C😵\033[1D", end='')                                                   #Standing in start position + printing '😵'(face)
        print("\033[15E", end='')                                                                    #Returning to entered position
    print("\033[0m", end = '')                                                                       #SWITCHING color to WHITE

def error(text, lifes):                                                                              #PRINT nice error margin(red)
    print_logo(lifes)                                                                                #PRINTING logo with ten lifes
    print("\033[31m", end='')                                                                        #SWITCHING color to RED
    for i in range(len(text)+4):                                                                     #For upper border(length of text + '| '+' |')
        print('-', end='')                                                                           #PRINTING '-'(upper border)
    print('\n| '+text+' |')                                                                          #PRINTING left and right borders + tabulated text
    for i in range(len(text)+4):                                                                     #for lower border(length of text + '| '+' |')
        print('-', end='')                                                                           #PRINTING '-'(lower border)
    print("\033[0m")                                                                                 #SWITCHING color to WHITE

def print_secret(word, letters):                                                                     #PRINT hidden word + CHECK if word was guessed
    print("\033[35m", end = '')                                                                      #SWITCHING color to VIOLET
    guessed = True                                                                                   #Boolean for checking(if word was guessed)
    for i in word:                                                                                   #Enumeration each letter in word
        if(not(ord(i.lower()) >= 97 and ord(i.lower()) <= 122) and 
        not(ord(i.lower()) >= 1072 and ord(i.lower()) <= 1103)):                                     #CHECK (for being not ENGLISH/RUSSIAN letter)
            print(i, end = ' ')                                                                      #PRINTING SYMBOL(not letter)
            continue                                                                                 #SWITCHING to next symbol
        if(i in letters):                                                                            #CHECK (if such letter was entered)
            print(i, end = ' ')                                                                      #PRINTING guessed letter
        else:                                                                                        #CHECK (else for '_')
            print('_', end = ' ')                                                                    #PRINTING hidden letter
            guessed = False                                                                          #Word is not guessed
    print("\033[0m")                                                                                 #SWITCHING color to WHITE
    return guessed                                                                                   #RETURNING CHECK if word was guessed

categories = ['words', 'vegetables', 'fruits', 'animals']                                            #list of all supported categories(ENGLISH)
categories_russian = ['простые слова', 'овощи', 'фрукты', 'животные']                                #list of all supported categories(RUSSIAN)
languages = ['english', 'russian']                                                                   #list of all supported languages

print_logo(10)                                                                                       #PRINTING logo with ten lifes

while True:                                                                                          #Can be breaked only if user entered something, that is not "yes"
    print('\033[33mSelect language ', end='[')                                                       #SWITCHING color to YELLOW
    for i in languages:                                                                              #PRINTING all languages, splited with '/'
        print(i, end = '/')
    language = input('quit] (quit): ')                                                               #End of print + inputing language
    print("\033[0m", end='')                                                                         #SWITCHING color to WHITE
    if(language.lower() == 'quit' or language.lower() == 'q'):                                       #CHECK if user want's to quit
        sys.exit()                                                                                   #END of program
    if(language.lower() == 'e'):                                                                     #CHECK if user want's to use ENGLISH
        language = 'english'                                                                         #SETTING language(ENGLISH)
    elif(language.lower() == 'r' or language.lower() == 'р' or language.lower() == 'рус'):           #CHECK if user want's to use RUSSIAN
        language = 'russian'                                                                         #SETTING language(RUSSIAN)
    elif(language.lower() not in languages):                                                         #CHECK if there is no such language in list of supported languages
        error('Your input is not in a right form!', 10)                                              #PRINTING ERROR('Your input is not in a right form!')
        continue                                                                                     #RESETING language
    language = language.lower()                                                                      #SETTING language(ENGLISH/RUSSIAN)

    print_logo(10)                                                                                   #PRINTING logo with ten lifes

    if(language == 'english'):                                                                       #ENGLISH version of categorie choosing
        print('\033[34mSelect categorie ', end='[')                                                  #SWITCHING color to BLUE
        for i in categories:                                                                         #PRINTING all categories, splited with '/'
            print(i, end = '/')
        categorie = input('back/quit] (quit): ')                                                     #End of print + inputing categorie
        print("\033[0m", end='')                                                                     #SWITCHING color to WHITE
        if(categorie.lower() == 'quit' or categorie.lower() == 'q'):                                 #CHECK if user want's to quit
            sys.exit()                                                                               #END of program
        if(categorie.lower() == 'back' or categorie.lower() == 'b'):                                 #CHECK if user want's to change language
            continue                                                                                 #RESETING language
        if(categorie.lower() == 'w'):                                                                #CHECK if user want's 'words' categorie
            categorie = 'words'                                                                      #SETTING categorie(words)
        elif(categorie.lower() == 'v'):                                                              #CHECK if user want's 'vegetables' categorie
            categorie = 'vegetables'                                                                 #SETTING categorie(vegetables)
        elif(categorie.lower() == 'f'):                                                              #CHECK if user want's 'fruits' categorie
            categorie = 'fruits'                                                                     #SETTING categorie(fruits)
        elif(categorie.lower() == 'a'):                                                              #CHECK if user want's 'animals' categorie
            categorie = 'animals'                                                                    #SETTING categorie(animals)
        elif(categorie.lower() not in categories):                                                   #CHECK if there is no such categorie in list of supported categories
            error('Your input is not in a right form!', 10)                                          #PRINTING ERROR('Your input is not in a right form!')
            continue                                                                                 #RESETING language
        categorie = categorie.lower()                                                                #SETTING categorie(words/vegetables/fruits/animals)
    else:                                                                                            #RUSSIAN version of categorie choosing
        print('\033[34mВыберите категорию ', end='[')                                                #SWITCHING color to BLUE
        for i in categories_russian:                                                                 #PRINTING all categories
            print(i, end = '/')
        categorie = input('назад/выход] (выход): ')
        print("\033[0m", end='')                                                                     #SWITCHING color to WHITE
        if(categorie.lower() == 'выход' or categorie.lower() == 'выйти' or categorie.lower() == 'в'):#CHECK if user want's to quit
            sys.exit()                                                                               #END of program
        if(categorie.lower() == 'назад' or categorie.lower() == 'н'):                                #CHECK if user want's to change language
            continue                                                                                 #RESETING language
        if(categorie == 'п' or categorie == 'с'):                                                    #CHECK if user want's 'простые слова' categorie
            categorie = 'простые слова'                                                              #SETTING categorie(простые слова)
        elif(categorie == 'о'):                                                                      #CHECK if user want's 'овощи' categorie
            categorie = 'овощи'                                                                      #SETTING categorie(овощи)
        elif(categorie == 'ф'):                                                                      #CHECK if user want's 'фрукты' categorie
            categorie = 'фрукты'                                                                     #SETTING categorie(фрукты)
        elif(categorie == 'ж'):                                                                      #CHECK if user want's 'животные' categorie
            categorie = 'животные'                                                                   #SETTING categorie(животные)
        elif(categorie.lower() not in categories_russian):                                           #CHECK if there is no such categorie in list of supported categories
            error('Вы ввели недопустимое значение!', 10)                                             #PRINTING ERROR('Вы ввели недопустимое значение!')
            continue                                                                                 #RESETING language
        categorie = categories[categories_russian.index(categorie.lower())]                          #SETTING categorie(простые слова/овощи/фрукты/животные)

    if(language == 'english'):                                                                       #CHECK language of file
        file = open(categorie+'.txt')                                                                #OPENING file with (categorie) by adding '.txt' at the end
    else:
        file = open('russian_'+categorie+'.txt')                                                     #OPENING file with (categorie) by adding 'russian_' at the begin and '.txt' at the end
    words = file.read().split('\n')                                                                  #SPLITING file's text with '\n'
    file.close()                                                                                     #CLOSING file

    word = choice(words)                                                                             #CHOSING random word of (categorie)
    letters = []                                                                                     #CREATING array with entered letters
    lifes = 10                                                                                       #CREATING life's counter

    print_logo(lifes)                                                                                #PRINTING logo with lifes

    while lifes > 0:                                                                                 #CHECK if user can play
        if(print_secret(word, letters)):                                                             #WIN
            if(language == 'english'):                                                               #ENGLISH version of WIN
                print('\033[32m You won! Your score is: '+str(len(word)/(11-lifes)*100)+'\033[0m')   #SWITCHING color to GREEN + score output
            else:                                                                                    #RUSSIAN version of WIN
                print('\033[32m Вы победили! У вас '+str(len(word)/(11-lifes)*100)+' очков!\033[0m') #SWITCHING color to GREEN + score output
            break                                                                                    #ASK for new game
        if(language == 'english'):                                                                   #ENGLISH version of lifes PRINT
            print('\033[31m You have '+str(lifes)+' lifes\033[0m', end = ' ')                        #LIFES output(english)
        else:                                                                                        #RUSSIAN version of lifes PRINT
            print('\033[31m У вас есть '+str(lifes)+' жизней\033[0m', end = ' ')                     #LIFES output(russian)
        for i in range(lifes):                                                                       #LIFES output(HEARTS)
            print("❤️‍🔥", end = ' ')                                                                   #PRINTING ❤️‍🔥
        print()                                                                                      #STANDING to lower line
        if(language == 'english'):                                                                   #ENGLISH version of letter's guess
            print("\033[33m Guess a letter ", end = '[')                                             #SWITCHING color to YELLOW
            for i in range(123-97):                                                                  #CHECK to all letters extends entered symbols
                if(not(chr(i+97) in letters)):                                                       #CHECK if letter was not written yet
                    print(chr(97+i), end = '/')                                                      #PRINTING letters, that was not written yet
                else:                                                                                #CHECK else if letter was written yet
                    print(' ', end = '/')                                                            #PRINTING ' ' in place of letters, that was written yet
            user_guess = input("quit] (quit): ")                                                     #INPUT by user(letter)
        else:                                                                                        #RUSSIAN version of letter's guess
            print("\033[33m Угадайте букву ", end = '[')                                             #SWITCHING color to YELLOW
            for i in range(1104-1072):                                                               #CHECK to all letters extends entered symbols(RUSSIAN)
                if(not(chr(i+1072) in letters)):                                                     #CHECK if letter was not written yet(RUSSIAN)
                    print(chr(1072+i), end = '/')                                                    #PRINTING letters, that was not written yet(RUSSIAN)
                else:                                                                                #CHECK else if letter was written yet(RUSSIAN)
                    print(' ', end = '/')                                                            #PRINTING ' ' in place of letters, that was written yet(RUSSIAN)
            user_guess = input("выход] (выход): ")                                                   #INPUT by user(letter)(RUSSIAN)
        print("\033[0m", end='')                                                                     #SWITCHING color to WHITE
        if(user_guess.lower() == 'quit' or user_guess.lower() == 'выход'):                           #QUIT
            break
        if(len(user_guess) > 1 or len(user_guess) == 0):                                             #CHECK to more than one character
            if(language == 'english'):                                                               #ENGLISH case
                error('Your input is not a letter/is not a one letter!', lifes)                      #PRINTING ERROR('Your input is not a letter/is not a one letter!'), lifes - for gibbet draw
            else:                                                                                    #RUSSIAN case
                error('Ваш ввод не являеться буквой/Не являеться одной буквой', lifes)               #PRINTING ERROR('Ваш ввод не являеться буквой/Не являеться одной буквой'), lifes - for gibbet draw
            continue                                                                                 #ASKING for new letter
        if(user_guess.lower() in letters):                                                           #CHECK to double enter
            if(language == 'english'):                                                               #ENGLISH case
                error('You have entered this letter twice!', lifes)                                  #PRINTING ERROR('You have entered this letter twice!'), lifes - for gibbet draw
            else:                                                                                    #RUSSIAN case
                error('Вы ввели эту букву дважды!', lifes)                                           #PRINTING ERROR('Вы ввели эту букву дважды!'), lifes - for gibbet draw
            continue                                                                                 #ASKING for new letter
        elif(not(ord(user_guess.lower()) >= 97 and ord(user_guess.lower()) <= 122) and 
        not(ord(user_guess.lower()) >= 1072 and ord(user_guess.lower()) <= 1103)):                   #CHECK (for being not english/russian letter)
            if(language == 'english'):                                                               #ENGLISH case
                error('Your input is not a letter!', lifes)                                          #PRINTING ERROR('Your input is not a letter!'), lifes - for gibbet draw
            else:                                                                                    #RUSSIAN case
                error('Ваш ввод не являеться буквой!', lifes)                                        #PRINTING ERROR('Ваш ввод не являеться буквой!'), lifes - for gibbet draw
            continue                                                                                 #ASKING letter again
        letters.append(user_guess.lower())                                                           #ADDING user_guess in lowercase to letters(array)
        if(len(letters) == 0 or not(letters[-1] in word)):                                           #CHECK to not such letter in word
            lifes-=1                                                                                 #Minus one life
        print_logo(lifes)                                                                            #PRINTING logo with lifes
    if(lifes == 0):                                                                                  #CHECK if user lost(out of lifes)
        if(language == 'english'):                                                                   #ENGLISH case
            print('\033[31m You lost! Right word was \033[1m\033[4m"'+word+'"\033[0m')               #LOST
        else:                                                                                        #RUSSIAN case
            print('\033[31m Вы проиграли! Правильное слово было \033[1m\033[4m"'+word+'"\033[0m')    #LOST
    answer = input("\033[36m Do you want to play again?(y/n) -> ")                                   #INPUT wish to play again
    print("\033[0m",end='')                                                                          #SWITCHING color to WHITE
    if(answer.lower() == 'y' or answer.lower() == 'yes' or answer.lower() == 'да' or answer == '+'): #play AGAIN
        print_logo(lifes)                                                                            #PRINTING logo with lifes
        continue                                                                                     #STARTING game again(language select)
    break                                                                                            #QUIT

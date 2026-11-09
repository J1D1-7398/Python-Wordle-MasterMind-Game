import random, subprocess, os, time
subprocess.call("cls" if os.name == "nt" else "clear")
while True:
    print("\n ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗███╗   ███╗██╗███╗  ██╗██████╗ \n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝████╗ ████║██║████╗ ██║██╔══██╗\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  ██╔████╔██║██║██╔██╗██║██║  ██║\n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  ██║╚██╔╝██║██║██║╚████║██║  ██║\n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗██║ ╚═╝ ██║██║██║ ╚███║██████╔╝\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚══╝╚═════╝ \n")
    main_menu_selection = input("1. Wordle\n2. MasterMind\n3. Exit\n> ")
    if main_menu_selection == "1":
        subprocess.call("cls" if os.name == "nt" else "clear")
        while True:
            print("\n ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗\n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  \n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  \n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝\n")
            wordle_menu_selection = input("1. New Game\n2. Previous Game Stats\n3. How to play\n4. Add a new word\n5. Remove a word\n6. Clear screen\n7. Main Menu\n> ")
            if wordle_menu_selection == "1":
                subprocess.call("cls" if os.name == "nt" else "clear")
                with open("wordlist.txt", "r") as read_wordlist:
                    words = read_wordlist.read()
                print("\n ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗\n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  \n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  \n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝\n \033[1;33;43m                                                     \033[0m")
                chosen_word = random.choice(words.strip().split())
                written_words = []
                x = 0
                start_time_wordle = time.time()
                while x < 6:
                    answer = [0, 0, 0, 0, 0]
                    chosen_word_list = list(chosen_word)
                    wordle_guess = input("\n Guess word: ")
                    while len(wordle_guess) != 5:
                        wordle_guess = input(" Please enter a 5 letter word\n Guess word: ")
                    while wordle_guess not in words:
                        wordle_guess = input(" Please enter a valid word (Add it to the list if this is an error)\n Guess word: ")
                    for i in range(5):
                        if wordle_guess[i] == chosen_word[i]:
                            answer[i] = 32
                            chosen_word_list.remove(chosen_word[i])
                    for i in range(5):
                        if answer[i] == 0:
                            if wordle_guess[i] in chosen_word_list:
                                answer[i] = 33
                                chosen_word_list.remove(wordle_guess[i])
                            else:
                                answer[i] = 31
                    subprocess.call("cls" if os.name == "nt" else "clear")
                    append_word = ""
                    for i in range(5):
                        append_word += f"\033[1;49;{answer[i]}m{wordle_guess[i]}\033[0m"
                    written_words.append(append_word)
                    print("\n ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗\n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  \n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  \n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")
                    print(" ", end="")
                    for i in range(5 - x):
                        print("\033[1;33;43m         \033[0m", end="")
                    print("\n")
                    for i in written_words:
                        print("   "+i)
                    if wordle_guess == chosen_word:
                        input(f"\n   You won!\n   Time: {(time.time() - start_time_wordle):.0f} seconds\n   Press Enter to return to Wordle menu...")
                        break
                    x += 1
                del words
                if x == 6:
                    input(f"\n   You lost!\n   Time: {(time.time() - start_time_wordle):.0f} seconds\n   The word was: {chosen_word}\n   Press Enter to return to Wordle menu...")
                subprocess.call("cls" if os.name == "nt" else "clear")
            elif wordle_menu_selection == "2":
                if "chosen_word" in locals():
                    subprocess.call("cls" if os.name == "nt" else "clear")
                    print(f"\nPrevious game stats:")
                    print("You Won\n" if written_words[-1].replace("\033[1;49;32m", "").replace("\033[0m", "") == chosen_word else f"You Lost (Answer: {chosen_word})\n")
                    for i in written_words:
                        print(i)
                    print(f"\nTime: {(time.time() - start_time_wordle):.0f} seconds")
                else:
                    subprocess.call("cls" if os.name == "nt" else "clear")
                    print("\nThere is no last game in memory\n")
            elif wordle_menu_selection == "3":
                subprocess.call("cls" if os.name == "nt" else "clear")
                input("\nHow to play:\nSelect \"New Game\" to start playing\nWhen in game:\nEnter a 5 letter word (all lowercase)\nThe program will give back your word but with different colors\n\n\033[1;49;32mGreen or cyan\033[0m (depending on your system): Means that this letter is correct and is in the correct spot\n\033[1;49;33mYellow or Orange\033[0m (depending on your system): Means that letter is in the word but not in that spot\n\033[1;49;31mRed\033[0m: Means that letter is not in the word\n\nYou have \033[1;49;33m6 tries\033[0m\n\nPress enter to return to Wordle menu...")
                subprocess.call("cls" if os.name == "nt" else "clear")
            elif wordle_menu_selection == "4":
                new_entry = input("Type a 5 letter word to add to the list (you can add more than one by spacing them): ")
                new_entry = new_entry.strip().split()
                entry_isok = False
                while entry_isok == False:
                    entry_isok = True
                    for i in new_entry:
                        if len(i) != 5:
                            entry_isok = False
                    if entry_isok == False:
                        new_entry = input("Ensure to type 5 letter words!\nType a 5 letter word to add to the list (you can add more than one by spacing them): ")
                subprocess.call("cls" if os.name == "nt" else "clear")
                print("\nAdded:")
                with open("wordlist.txt", "a") as add_entry_to_wordlist:
                    for i in new_entry:
                        add_entry_to_wordlist.write(" "+i)
                        print(" "+i)
            elif wordle_menu_selection == "5":
                del_entry = input("Type a 5 letter word to remove from the list (you can remove more than one by spacing them): ")
                del_entry = del_entry.strip().split()
                entry_isok = False
                while entry_isok == False:
                    entry_isok = True
                    for i in del_entry:
                        if len(i) != 5:
                            entry_isok = False
                    if entry_isok == False:
                        del_entry = input("Ensure to type 5 letter words!\nType a 5 letter word to remove from the list (you can remove more than one by spacing them): ")
                subprocess.call("cls" if os.name == "nt" else "clear")
                print("\nRemoved:")
                with open("wordlist.txt", "r+") as add_entry_to_wordlist:
                    wordlist_content = add_entry_to_wordlist.read()
                    for i in del_entry:
                        wordlist_content = wordlist_content.replace(f" {i}", "")
                        print(" "+i)
                    add_entry_to_wordlist.write(wordlist_content)
            elif wordle_menu_selection == "6":
                subprocess.call("cls" if os.name == "nt" else "clear")
            elif wordle_menu_selection == "7":
                subprocess.call("cls" if os.name == "nt" else "clear")
                break
    elif main_menu_selection == "2":
        subprocess.call("cls" if os.name == "nt" else "clear")
        while True:
            print("\n███╗   ███╗ █████╗  ██████╗████████╗███████╗██████╗ ███╗   ███╗██╗███╗  ██╗██████╗ \n████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗ ██║██╔══██╗\n██╔████╔██║███████║╚█████╗    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗██║██║  ██║\n██║╚██╔╝██║██╔══██║ ╚═══██╗   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚████║██║  ██║\n██║ ╚═╝ ██║██║  ██║██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚███║██████╔╝\n╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚══╝╚═════╝\n")
            mastermind_menu_selection = input("1. New Game\n2. Previous Game Stats\n3. Color code\n4. How to play\n5. Clear screen\n6. Main Menu\n> ")
            if mastermind_menu_selection == "1":
                mastermind_difficulty = input("\nSelect difficulty:\n1. Easy\n2. Hard\n> ")
                if mastermind_difficulty == "1":
                    subprocess.call("cls" if os.name == "nt" else "clear")
                    print("\033[1;49;32m\n███╗   ███╗ █████╗  ██████╗████████╗███████╗██████╗ ███╗   ███╗██╗███╗  ██╗██████╗ \n████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗ ██║██╔══██╗\n██╔████╔██║███████║╚█████╗    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗██║██║  ██║\n██║╚██╔╝██║██╔══██║ ╚═══██╗   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚████║██║  ██║\n██║ ╚═╝ ██║██║  ██║██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚███║██████╔╝\n╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚══╝╚═════╝\n Easy Mode\033[0m\n \033[1;32;42m                                                                                 \033[0m")
                    colors = ["b", "p", "g", "y", "r", "o", "w", "c"] #blue purple green yellow red orange white cyan ## green if correct, yellow if in but not correct place, red if incorrect
                    chosen_color_pattern = ""
                    for i in range(4):
                        chosen_color_pattern += random.choice(colors)
                    written_colors = []
                    x = 0
                    start_time_mastermind = time.time()
                    while x < 9:
                        mastermind_guess = input("\n Guess color pattern: ")
                        while len(mastermind_guess) != 4:
                            mastermind_guess = input(" Please enter a 4 letter color pattern\n Guess color pattern: ")
                        mastermind_guess_isok = False
                        while mastermind_guess_isok == False:
                            mastermind_guess_isok = True
                            for i in range(4):
                                if mastermind_guess[i] not in colors:
                                    mastermind_guess_isok = False
                            if mastermind_guess_isok == False:
                                mastermind_guess = input(" Please enter a valid 4 letter color pattern (check in \"Color Code\" for valid colors)\n Guess color pattern: ")
                        green = 0
                        yellow = 0
                        red = 0
                        chosen_color_pattern_list = list(chosen_color_pattern)
                        for i in range(4):
                            if mastermind_guess[i] == chosen_color_pattern[i]:
                                green += 1
                                chosen_color_pattern_list.remove(chosen_color_pattern[i])
                        for i in range(4):
                            if mastermind_guess[i] != chosen_color_pattern[i]:
                                if mastermind_guess[i] in chosen_color_pattern_list:
                                    yellow += 1
                        subprocess.call("cls" if os.name == "nt" else "clear")
                        append_colors = ""
                        red = 4 - green - yellow
                        if green != 0:
                            for i in range(green):
                                append_colors += "\033[1;49;32mo\033[0m"
                        if yellow != 0:
                            for i in range(yellow):
                                append_colors += "\033[1;49;33mo\033[0m"
                        if red != 0:
                            for i in range(red):
                                append_colors += "\033[1;49;31mo\033[0m"
                        written_colors.append(f"{mastermind_guess} {append_colors}")
                        print("\033[1;49;32m\n███╗   ███╗ █████╗  ██████╗████████╗███████╗██████╗ ███╗   ███╗██╗███╗  ██╗██████╗ \n████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗ ██║██╔══██╗\n██╔████╔██║███████║╚█████╗    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗██║██║  ██║\n██║╚██╔╝██║██╔══██║ ╚═══██╗   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚████║██║  ██║\n██║ ╚═╝ ██║██║  ██║██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚███║██████╔╝\n╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚══╝╚═════╝\n Easy Mode\033[0m")
                        print(" ", end="")
                        for i in range(8 - x):
                            print("\033[1;32;42m         \033[0m", end="")
                        print("\n")
                        for i in written_colors:
                            print("   "+i)
                        if mastermind_guess == chosen_color_pattern:
                            input(f"\n   You won!\n   Time: {(time.time() - start_time_mastermind):.0f} seconds\n   Press Enter to return to Mastermind menu...")
                            break
                        x += 1
                    if x == 9:
                        input(f"\nYou lost!\nTime: {(time.time() - start_time_mastermind):.0f} seconds\nThe color pattern was: {chosen_color_pattern}\nPress Enter to return to Mastermind menu...")
                    subprocess.call("cls" if os.name == "nt" else "clear")
                elif mastermind_difficulty == "2":
                    subprocess.call("cls" if os.name == "nt" else "clear")
                    print("\033[1;49;31m\n███╗   ███╗ █████╗  ██████╗████████╗███████╗██████╗ ███╗   ███╗██╗███╗  ██╗██████╗ \n████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗ ██║██╔══██╗\n██╔████╔██║███████║╚█████╗    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗██║██║  ██║\n██║╚██╔╝██║██╔══██║ ╚═══██╗   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚████║██║  ██║\n██║ ╚═╝ ██║██║  ██║██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚███║██████╔╝\n╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚══╝╚═════╝\n Hard Mode\033[0m\n \033[1;31;41m                                                                                 \033[0m")
                    colors = ["b", "p", "g", "y", "r", "o", "w", "c"] #blue purple green yellow red orange white cyan ## green if correct, yellow if in but not correct place, red if incorrect
                    chosen_color_pattern = ""
                    for i in range(6):
                        chosen_color_pattern += random.choice(colors)
                    written_colors = []
                    x = 0
                    start_time_mastermind = time.time()
                    while x < 16:
                        mastermind_guess = input("\n Guess color pattern: ")
                        while len(mastermind_guess) != 6:
                            mastermind_guess = input(" Please enter a 6 letter color pattern\n Guess color pattern: ")
                        mastermind_guess_isok = False
                        while mastermind_guess_isok == False:
                            mastermind_guess_isok = True
                            for i in range(6):
                                if mastermind_guess[i] not in colors:
                                    mastermind_guess_isok = False
                            if mastermind_guess_isok == False:
                                mastermind_guess = input(" Please enter a valid 6 letter color pattern (check in \"Color Code\" for valid colors)\n Guess color pattern: ")
                        green = 0
                        yellow = 0
                        red = 0
                        chosen_color_pattern_list = list(chosen_color_pattern)
                        for i in range(6):
                            if mastermind_guess[i] == chosen_color_pattern[i]:
                                green += 1
                                chosen_color_pattern_list.remove(chosen_color_pattern[i])
                        for i in range(6):
                            if mastermind_guess[i] != chosen_color_pattern[i]:
                                if mastermind_guess[i] in chosen_color_pattern_list:
                                    yellow += 1
                        subprocess.call("cls" if os.name == "nt" else "clear")
                        append_colors = ""
                        red = 6 - green - yellow
                        if green != 0:
                            for i in range(green):
                                append_colors += "\033[1;49;32mo\033[0m"
                        if yellow != 0:
                            for i in range(yellow):
                                append_colors += "\033[1;49;33mo\033[0m"
                        if red != 0:
                            for i in range(red):
                                append_colors += "\033[1;49;31mo\033[0m"
                        written_colors.append(f"{mastermind_guess} {append_colors}")
                        print("\033[1;49;31m\n███╗   ███╗ █████╗  ██████╗████████╗███████╗██████╗ ███╗   ███╗██╗███╗  ██╗██████╗ \n████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗ ██║██╔══██╗\n██╔████╔██║███████║╚█████╗    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗██║██║  ██║\n██║╚██╔╝██║██╔══██║ ╚═══██╗   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚████║██║  ██║\n██║ ╚═╝ ██║██║  ██║██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚███║██████╔╝\n╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚══╝╚═════╝\n Hard Mode\033[0m")
                        print(" ", end="")
                        for i in range(15 - x):
                            print("\033[1;31;41m     \033[0m", end="")
                        print("\n")
                        for i in written_colors:
                            print("   "+i)
                        if mastermind_guess == chosen_color_pattern:
                            input(f"\n   You won!\n   Time: {(time.time() - start_time_mastermind):.0f} seconds\n   Press Enter to return to Mastermind menu...")
                            break
                        x += 1
                    if x == 16:
                        input(f"\nYou lost!\nTime: {(time.time() - start_time_mastermind):.0f} seconds\nThe color pattern was: {chosen_color_pattern}\nPress Enter to return to Mastermind menu...")
                    subprocess.call("cls" if os.name == "nt" else "clear")
            elif mastermind_menu_selection == "2":
                if "chosen_color_pattern" in locals():
                    subprocess.call("cls" if os.name == "nt" else "clear")
                    print(f"\nPrevious game stats:")
                    if mastermind_difficulty == "1":
                        print("You Won (Easy Mode)\n" if written_colors[-1][:4] == chosen_color_pattern else f"You Lost (Easy Mode) (Answer: {chosen_color_pattern})\n")
                    elif mastermind_difficulty == "2":
                        print("You Won (Hard Mode)\n" if written_colors[-1][:6] == chosen_color_pattern else f"You Lost (Hard Mode) (Answer: {chosen_color_pattern})\n")
                    for i in written_colors:
                        print(i)
                    print(f"\nTime: {(time.time() - start_time_mastermind):.0f} seconds")
                else:
                    subprocess.call("cls" if os.name == "nt" else "clear")
                    print("\nThere is no last game in memory\n")
            elif mastermind_menu_selection == "3":
                subprocess.call("cls" if os.name == "nt" else "clear")
                print("\n Color code\n b: blue\n p: purple\n g: green\n y: yellow\n r: red\n o: orange\n w: white\n c: cyan")
            elif mastermind_menu_selection == "4":
                subprocess.call("cls" if os.name == "nt" else "clear")
                input("\nHow to play:\nSelect \"New Game\" and select difficulty to start playing\n\nWhen in game:\nType 4 colors (found in the \"Color code\" category) in this format \"xxxx\" (no uppercase, all lowercase) where x is the first letter of the wanted color\nThe game will then give back your color selection with 4 \"o\" after it, these are just for the color, the \"o\" specifically doesn\'t mean anything, look at the colors\n\nThe color \033[1;49;32mgreen or cyan\033[0m (depending on your system), means there is a color in the right spot\n\033[1;49;33mAttention!\033[0m It doesn\'t indicate that the color in that specific spot is correct, it indicates there is a color in the right spot somewhere\n\nThe color \033[1;49;33myellow or orange\033[0m (again, depending on your system) indicates there is a color that is right, but in the wrong spot\n\033[1;49;33mAttention!\033[0m It doesn\'t indicate that the color in that specific spot is correct but not in the right spot, it indicates there is a color that is right but not in the right spot somewhere\n\nFinally there is \033[1;49;31mred\033[0m, which indicates that there is a color that is incorrect\n\033[1;49;33mAttention!\033[0m It doesn\'t indicate that the color in that specific spot is incorrect, it indicates there is an incorrect color somewhere\n\nYou have \033[1;49;33m9 tries\033[0m in Easy Mode and \033[1;49;33m16 tries\033[0m in Hard Mode\n\nPress enter to return to Mastermind menu...")
                subprocess.call("cls" if os.name == "nt" else "clear")
            elif mastermind_menu_selection == "5":
                subprocess.call("cls" if os.name == "nt" else "clear")
            elif mastermind_menu_selection == "6":
                subprocess.call("cls" if os.name == "nt" else "clear")
                break
    elif main_menu_selection == "3":
        subprocess.call("cls" if os.name == "nt" else "clear")
        break

import random  # random module for the random box monster
import turtle # a module to draw graphics
from termcolor import colored
import time

# Ask the player for their name.
player_name = input("What's your name? ")

# Initialize the starting and ending positions
start = (0, 1)
end = (5, 3)
player_pos = list(start)

# Dictionary mapping coordinates to their respective named locations.
locations = {
    (0, 1): "you are at the entrance to maze, south is the only way in, begin your adventure!",
    (1, 1): "you are in a large cave, a boulder falls behind you you are trapped in the" 
            " maze now, only South or East exits are possible",
    (1, 2): "you enter a cave and a small monster is here, he says answer my"
            " riddle to pass!",
    (1, 3): "you enter a new cave, omg its a new monster, he speaks to you"
            " and goes you may pick a box from the 3 here",
    (2, 1): "you enter a room with large monster troll and he grunts towards"
            " a door, do you have they key?", 
    (3, 1): "you enter through the door into cave with a large sign, the door"
            " slams behind you shut and locks! \n Sign says W, S or E", #sign here, not needed
    (3, 0): "you walk into a pretty room with a fortune telling monster",
    (3, 2): "you walk into a room with a guess monster who roars!",
    (4, 1): "you enter a large room with a password monster, he smiles",
    (5, 1): "you stumble upon a very big monster",
    (5, 2): "you found the Treasure Chest. The end!" #not used, end of game
    #add other locations as needed
}

valid_moves = {
    (0, 1): ["S",],  # From Start, you can go South only.
    (1, 1): ["S","E"],  # From Cave 1, you can go South or East.
    (1, 2): ["E", "W"],  # From Riddle cave , you can go East or West.
    (1, 3): ["W",],  # From random box cave, you can go West.
    (2, 1): ["S", "N"], # South through locked door
    (3, 1): ["S","W","E"],  # From Sign cave, you can go West, East, South.
    (3, 0): ["E"],  # From Fortune teller cave, you can go back East.
    (3, 2): ["W"], #Monster guess number for swoard game
    (4, 1): ["S"], #Gate monster password number?
    (5, 1): ["E"] # Monster fight!
    #add other valid location moves as needed
}

# Your quiz riddle code here
def quiz_game():
    questions = [
        ("Riddle 1: I hiss not speak, crawl but no feet. What am I?", "snake"),
        ("Riddle 2: I groan, I moan, I like brainssss. What am I?", "zombie"),
        # Add more questions and answers here if you want
    ]

    score = 0

    print("I am the riddle monster!")
    print("Type your answer to pass or get eaten! Get at least one right!")
    print("Let's get started, I'm hungry!")

    for question, answer in questions:
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer was: {answer}\n")
            print("You got eaten, nom nom nom!")
            return None  # Special return value indicating game over

    if score >= 1:  # Change this threshold as needed
        print(f"You passed the riddles, grrr no food for me! You may pass")
    else:
        print(f"You failed the riddles muahaha!")

    print(f"Your final score is: {score} out of {len(questions)}")
    return score > 0  # True if at least one is correct, False otherwise

def box_game():
    has_key = False  # To keep track of whether found the key or not

    print("I am the Box Monster!")
    print("Pick the right box to find the key or keep guessing!")
  
    while not has_key:
        # Randomly choose a box to contain the key each time through the loop
        correct_box = random.choice(['A', 'B', 'C'])

        # Ask the player to choose a box
        player_choice = input("Choose a box (A, B, C): ").upper()

        if player_choice == correct_box:
            print("Congrats! You found the key!")
            has_key = True  # Player found the key, set has_key to True
        else:
            print("Haha, wrong box! Keep guessing!")

    return has_key  # Return True if the player has the key, False otherwise

def print_monster_maze():
    text = "Monster Maze"
    colors = ['red', 'yellow', 'green', 'blue', 'magenta', 'cyan']
    colorized_text = ""

    for i, char in enumerate(text):
        if char == " ":
            colorized_text += " "
            continue
        color = colors[i % len(colors)]
        colorized_text += colored(char, color)

    print(colorized_text)

def print_sign():
    print(colored("#######################", 'red'))
    print(colored("#", 'red') + "                   " + colored("  #", 'red'))
    print(colored("#", 'red') + colored(" Beware of Monsters! ", 'yellow') + colored("#", 'red'))
    print(colored("#", 'red') + colored("   West - Fortune", 'blue') + colored("    #", 'red'))
    print(colored("#", 'red') + colored("   East - Sword", 'blue') + colored("      #", 'red'))
    print(colored("#", 'red') + colored("   South - Fight!", 'blue') + colored("    #", 'red'))
    print(colored("#", 'red') + "                   " + colored("  #", 'red'))
    print(colored("#######################", 'red'))
    print(colored("           #", 'black') + "                   ")
    print(colored("           #", 'black') + "                   ")
    print(colored("           #", 'black') + "                   ")
    print(colored("           #", 'black') + "                   ")

def fortune_teller():
    global fortunes_given
    if fortunes_given < 3:
        fortune_messages = [
            "I see danger in your future... But here's a hint for you:",
            "Ah, a twisty path awaits you... Here's a piece of guidance:",
            "Mysterious winds whisper to me... Here's a fragment for you:"
        ]
        print(fortune_messages[fortunes_given])
        hint = password_parts[fortunes_given]
        print(hint)
        fortunes_given += 1
        return hint
    else:
        print("I have shared all I can see. The rest is up to you.")
        return None

def number_guessing_game():
    secret_number = random.randint(1, 100)  # Random number between 1 and 100
    max_guesses = 10
    guesses = 0

    print("Burp!!! You have 10 attempts only!")
    print("Guess my secret number between 1 and 100.")

    while guesses < max_guesses:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1
            if guess == secret_number:
                print(f"Correct! It took you {guesses} guesses.")
                print("You have proven your worth. Here's a sword for your bravery.")
                return True
            elif guess < secret_number:
                print("Ha! Higher.")
            else:
                print("Ha! Lower.")
        except ValueError:
            print("Please enter a valid number.")
    # If the player doesn't guess correctly in the allowed attempts.
    if guesses == max_guesses:
        print("You failed, now you are my dinner nom nom nom!")
        return False

def password_monster():
    attempts = 3  # Give the player 3 attempts to guess correctly
    correct_password = "monster"
    global password_completed

    print("The Password Monster blocks your path!")
    for i in range(attempts):
        password_guess = input("Enter the magic password: ")

        if password_guess.lower() == correct_password:
            print("The Password Monster nods approvingly and steps aside.")
            password_completed = True  # Correct password, can proceed further
            return True  # Exit the function early

        else:
            if i < attempts - 1:  # If it's not the last attempt, give a hint
                print("Wrong! Try again.")

    # Will only be printed if 3 failed attempts
    print("The Password Monster growls, 'You're not worthy!' and eats you!")
    return False  # Incorrect password after all attempts

def battle_with_monster(has_sword):
    player_health, monster_health = 100, 100

    if not has_sword:
        print("You are unarmed and stand no chance against the monster!")
        return False  # Player will always lose without the sword

    print("Welcome to Attack of the Monsters!")
    print("You are facing a scary monster. You have 100 health points.")

    while player_health > 0 and monster_health > 0:
        print(f"Health: {player_health} | Monster health: {monster_health}")
        print("1. Attack | 2. Defend")
        choice = input("Enter choice (1 or 2): ")

        if choice == "1":
            player_attack = attack_player(has_sword)
            monster_damage = attack_monster(has_sword)
            player_health -= monster_damage
            monster_health -= player_attack
            print(f"Attacked: -{monster_damage} | You attacked: -{player_attack}")

        elif choice == "2":
            monster_attack = attack_monster(has_sword) // 2
            player_health -= monster_attack
            print(f"Defended: -{monster_attack}")

        else:
            print("Wrong choice. Select 1 or 2.")

    if player_health <= 0:
        print("Oh no! You were defeated by the monster. Game over.")
        return False
    else:
        print("Congratulations! You defeated the monster. You are victorious!")
        return True

def rainbow_message(message):
    colors = ['red', 'yellow', 'green', 'blue', 'magenta', 'cyan']
    
    for color in colors:
        print(colored(message, color))
        time.sleep(0.5)

def print_compass():
    # Function to print colorful ASCII sign
    print()
    print(colored("            N", 'blue'))
    print(colored("            ↑", 'blue'))
    print(colored("      W ←───┼───→ E", 'blue'))
    print(colored("            ↓", 'blue'))
    print(colored("            S", 'blue'))

def print_colored_monster():
    monster_art = (
        colored("    /\\_/\\    ", 'green') + "\n" +
        colored("   / ", 'green') + colored("o", 'yellow') + colored(" ", 'green') + colored("o", 'yellow')
         + colored(" \\   ", 'green') + "\n" +
        colored("  /   ^   \\  ", 'green') + "\n" +
        colored(" /   vvv   \\ ", 'green') + "\n" +
        colored("/_/|     |\\_\\", 'green') + "\n" +
        colored("    \\~*~/     ", 'green') + "\n" +
        colored("    /\\-/\\     ", 'red')
    )
    print(monster_art)

def print_colored_monster2():
    monster_art = (
        colored("     _.-----_   ", 'yellow') + "\n" +
        colored("   /         \\   ", 'yellow') + "\n" +
        colored("  | ", 'yellow') + colored(" O", 'blue') + colored("    ", 'yellow') + colored(" O", 'blue')
        + colored("  |", 'yellow') + "\n" +
        colored("  |  .", 'yellow') + colored("^^^^^", 'red') + colored(".  |", 'yellow') + "\n" +
        colored("  /  |     |  \\", 'yellow') + "\n" +
        colored(" /   `", 'yellow') + colored("^^^^^", 'red') + colored("'   \\", 'yellow') + "\n" +
        colored("/               \\", 'yellow') + "\n" +
        colored("|               | ", 'yellow') + "\n" +
        colored("|               | ", 'yellow') + "\n" +
        colored(" \\             / ", 'yellow') + "\n" +
        colored("  \\___________/ ", 'yellow') + "\n" +
        colored("   //     \\\\   ", 'yellow') + "\n" +
        colored("  //       \\\\  ", 'yellow') + "\n" +
        colored("  ^^       ^^  ", 'yellow')
    )
    print(monster_art)

# Function to update the player's position based on the chosen direction.
def move(direction):
    x, y = player_pos

    # Convert full direction names to abbreviations
    direction_dict = {"NORTH": "N", "EAST": "E", "SOUTH": "S", "WEST": "W"}
    direction = direction_dict.get(direction, direction)
    
    # Check if the move is valid for the current location
    if direction not in valid_moves.get((x, y), []):
        print("You can't move in that direction from here.")
        return

    # Block move to (3, 1) if the player doesn't have the key
    if (x, y) == (2, 1) and direction == "S" and not has_key:
        print("The troll blocks your way. You need a key to proceed!")
        return
        
    # Now we implement the move logic
    if direction == "N" and x > 0:
        player_pos[0] -= 1
    elif direction == "E" and y < 3: # 3 as the boundary, but can change it
        player_pos[1] += 1
    elif direction == "S" and x < 5: # 5 is the boundary here
        player_pos[0] += 1
    elif direction == "W" and y > 0:
        player_pos[1] -= 1

# Instead of always printing the coordinates, we'll check if the current
# position is in our dictionary. 
# If it is, we'll print the associated location name.
def print_location():
    location_name = locations.get(tuple(player_pos), None)
    if location_name:
        if tuple(player_pos) == (1, 2) and quiz_completed:
            print(f"{player_name}, the Riddle Monster says:") 
            print(" Leave me alone and pass!")
        elif tuple(player_pos) == (1, 3) and box_completed:
            print(f"{player_name}, the Box Monster says:") 
            print(" You may pass now, you've earned it!")
        elif tuple(player_pos) == (3, 1):
            print("wow a sign!")
            print_sign()
            # Call the function that draws sign
        elif tuple(player_pos) == (3,0) and fortune_completed:
            print("You have the password fragments, good luck!")  
        elif tuple(player_pos) == (5, 2):  # End location
            rainbow_message(f"Congratulations {player_name}! " 
                            "You completed the monster maze!")
            print("Game Over!")
            # Here you can choose to break out of your main 
            # game loop if you want to end the game.
            exit()
        else: 
            print(f"{player_name}, {location_name}!")
    else:
        print(f"{player_name}, you are in an unnamed location"
              f" at {tuple(player_pos)}.")
#note if we have coded correctly this catch all unamed 
#location is not needed, good to have it though, just in case!

# Display a welcome message to the player.
print(f"Greetings {player_name}, welcome to", end=" ")
print_monster_maze()
print("Beware of the monsters, try to find the treasure!")
print(f"{player_name} use directions N -North E - East  S - South W -West ")
print_compass()

# Main game loop
quiz_completed = False  # Add this variable to track quiz completion
box_completed = False  # Add this variable to track box game completion
has_key = False  # Add this variable to track whether the player has the key
fortune_completed = False # Add this variable to track fortune completion
fortunes_given = 0 # Global variable to keep track of fortunes given
# The secret password parts
password_parts = ["mo", "nst", "er"]
random.shuffle(password_parts)  # Shuffle to make it more interesting
#Note we added this code here to only shuffle the password once
#And not to be reshuffled each time the function is called!
password_fragments = []
sword = False  # Global variable to track if player has the sword
password_completed = False
battle_completed = False

def attack_player(has_sword):
    if has_sword:
        return random.randint(10, 20)  # boosted damage
    else:
        return random.randint(5, 15)

def attack_monster(has_sword):
    damage_to_player = random.randint(10, 20)
    if has_sword:
        damage_to_player //= 2  # half the damage if the player has the sword
    return damage_to_player

while player_pos != list(end):

    if tuple(player_pos) == (1, 2) and not quiz_completed:
        print("You have encountered the Riddle Monster!")
        print_colored_monster()
        passed = quiz_game()  # Call quiz_game and store the result
        quiz_completed = True  #Mark quiz as complete after attempting it

        if not passed:
            print("Tasty, Game Over!")
            break
    elif tuple(player_pos) == (1, 3) and not box_completed:
        print("You have encountered the Box Monster!")
        has_key = box_game()  #Call box_game and store the result
        box_completed = True  #Mark game as completed after attempting it
    elif tuple(player_pos) == (3, 0) and not fortune_completed:
        input("Ask the fortune teller monster for your fortune: ")
        hint = fortune_teller()
        if hint is not None:
            password_fragments.append(hint)
        # Check if all hints have been gathered
        if len(password_fragments) == 3:
            print("You have all the password fragments! Use them wisely.")
            fortune_completed = True
    elif tuple(player_pos) == (3, 2) and not sword: 
        print("You have encountered the Guessing Number Monster!")
        sword_won = number_guessing_game()
        if sword_won:
            sword = True
            print("You have won a rusty sword!")
        else:
            print("Game Over!")
            break
    elif tuple(player_pos) == (4, 1) and not password_completed:
        print("You have encountered the Password Monster!")
        passed = password_monster()
        if passed:
            print("You can proceed further!")
        else:
            print("You cannot proceed further without the correct password.")
            print("Game Over!")
            break
    elif tuple(player_pos) == (5, 1) and not battle_completed:
        print("You have encountered a ferocious monster!")
        print_colored_monster2()
        victory = battle_with_monster(sword)
        if victory:
           print("With the monster defeated, the way forward is clear!")
           battle_completed = True  #If the battle is won, mark as completed
        else:
            print("Game Over!")
            break   
    else:
        direction = input("Enter direction (N/E/S/W or Q to quit): ").upper()
        if direction == "Q":
            print(f"Thanks for playing, {player_name}!")
            break

        move(direction)
        print_location()

# Check if the player reached the end and display a congratulations message.
# Not needed as it ends in treasure room, but useful to know
if player_pos == list(end):
    print(f"Congratulations, {player_name}! You found the Prize! Knowledge :)")

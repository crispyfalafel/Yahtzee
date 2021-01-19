"""
COMP 1510 Finals
Jolin Lin A01080811
"""

import doctest
import random
import re
import time


def NUMBER_OF_YAHTZEE_DICE() -> int:
    """
    Return the number of dice used for the Yahtzee game.
    """
    return 5


def NUMBER_OF_DICE_SIDES() -> int:
    """
    Return the number of sides on a dice used for Yahtzee.
    """
    return 6


def NUMBER_OF_EXTRA_ROLLS() -> int:
    """
    Return the number of extra dice rolls a player is allowed to use during a Yahtzee turn.
    """
    return 2


def LOWER_SCORE_REGEXES() -> dict:
    """
    Return a dictionary of Yahtzee lower section score categories and their regexes.
    """
    score_regexes = {
        "4 of a kind": r'.*(.)\1{3}',
        "3 of a kind": r'.*(.)\1{2}',
        "full house": r'(.)\1{2}(.)\2|(.)\3(.)\4{2}',
        "small straight": r'.?(1234|2345|3456).?',
        "large straight": r'12345|23456',
        "yahtzee!": r'(.)\1{4}'
    }
    return score_regexes


def FIXED_SCORE_VALUES() -> dict:
    """
    Return a dictionary for constant Yahtzee score categories and the corresponding score value.
    """
    constant_scores = {
        'full house': 25,
        'small straight': 30,
        'large straight': 40,
        'yahtzee!': 50
    }
    return constant_scores


def UPPER_SCORE_CATEGORIES() -> dict:
    """
    Return a dictionary of Yahtzee upper score categories and their corresponding numerical value.
    """
    upper_scores = {
        'aces': 1,
        'twos': 2,
        'threes': 3,
        'fours': 4,
        'fives': 5,
        'sixes': 6
    }
    return upper_scores


def LOWER_SCORE_CATEGORIES() -> tuple:
    """
    Return a tuple of Yahtzee lower score categories.
    """
    return '3 of a kind', '4 of a kind', 'full house', 'small straight', 'large straight', 'yahtzee!', 'chance'


def UPPER_SCORE_BONUS() -> int:
    """
    Return the upper score bonus value.
    """
    return 35


def YAHTZEE_BONUS_SCORE() -> int:
    """
    Return the Yahtzee bonus score value.
    """
    return 100


def VALID_MENU_OPTIONS() -> dict:
    """
    Return a dictionary of valid menu options for a player's turn.
    """
    menu_options = {
        1: "keep",
        2: "score"
    }
    return menu_options


def INVALID_SCORE() -> int:
    """
    Return the score value for an invalid score.
    """
    return 0


def get_dice_to_keep(dice_hand: list) -> (list, None):
    """
    Ask the user which dice they would like to keep from the given list.

    :param dice_hand: A list of dice rolls.
    :precondition: dice_hand must be a list of integers from 1 - 6.
    :postcondition: Asks the player to choose which dice to keep and checks the input's validity.
    :return: A sorted list of integers representing dice rolls the user chose, or None if the input is invalid.
    """
    dice_choices = input("Which dice would you like to keep? Enter dice values separated by a space (eg. 1 3 4).\n")
    dice_choices_list = dice_choices.split()

    try:
        dice_to_keep = [int(die) for die in dice_choices_list]
    except ValueError:
        print("Invalid dice format.")
        return

    for die in dice_to_keep:
        if die in dice_hand:
            dice_hand.remove(die)
        else:
            print("You do not have those dice.")
            return
    return sorted(dice_to_keep)


def keep_dice(dice_hand: list) -> list:
    """
    Choose which dice to keep from the given list.

    :param dice_hand: A list of all dice rolls.
    :precondition: dice_hand must be a list of integers from 1 - 6.
    :postcondition: Asks the player to choose which dice to keep.
    :return: A list of dice rolls the player wants to keep.
    """
    dice_to_keep = None

    while dice_to_keep is None:
        dice_to_keep = get_dice_to_keep(dice_hand)

    return dice_to_keep


def roll_dice(number_of_dice: int, number_of_sides: int) -> list:
    """
    Roll dice based on the given number of sides and dice to roll.

    :param number_of_dice: A positive integer.
    :param number_of_sides: A positive integer.
    :precondition: Both parameters must be positive integers.
    :postcondition: Rolls the dice based on the given number of dice and sides, and sorts the values.
    :return: A sorted list of dice rolls.
    """
    dice = random.choices(range(1, number_of_sides + 1), k=number_of_dice)
    return sorted(dice)


def check_for_upper_bonus(player: dict) -> None:
    """
    Check if the player's score is high enough to earn an upper bonus, and record the bonus score if applicable.

    :param player: A dictionary of Yahtzee player information.
    :precondition: player must contain all necessary information required for Yahtzee.
    :postcondition: Checks if the sum of the player's upper scores is at least 63, and records a score of 35 if it is.

    >>> person = {'name': 'Jolin', 'extra_rolls': 0, 'yahtzee bonuses': 2, 'upper bonus': 0, 'scoreboard': {'aces': 3, \
     'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0, '3 of a kind': 17, \
     '4 of a kind': 25, 'small straight': 30, 'large straight': None, 'yahtzee!': 50, 'chance': 17}}
    """
    upper_score_total = 0

    for upper_category in UPPER_SCORE_CATEGORIES():
        try:
            upper_score_total += player['scoreboard'][upper_category]
        except TypeError:
            pass

    if upper_score_total >= 63:
        player['upper bonus'] = UPPER_SCORE_BONUS()


def calculate_yahtzee_score_or_bonus(player: dict, dice_hand: list) -> int:  # maybe decompose
    """
    Calculate a Yahtzee score or a Yahtzee bonus if the player already has a Yahtzee recorded.

    :param player: A dictionary of Yahtzee player information.
    :param dice_hand: A list of dice rolls.
    :precondition: player must contain all necessary information required for Yahtzee.
    :precondition: dice_hand must be a list of 5 integers from 1 - 6.
    :precondition: The player must be allowed to enter a Yahtzee score or bonus according to the Yahtzee rules.
    :postcondition: Calculates a Yahtzee score or Yahtzee bonus if applicable.
    :return: An integer reprsenting what the player scored based on the given hand and scoreboard.

    >>> dice = [5, 5, 5, 5, 5]
    >>> person = {'name': 'Jolin', 'extra_rolls': 0, 'yahtzee bonuses': 2, 'upper bonus': 0, 'scoreboard': {'aces': 3, \
     'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0, '3 of a kind': 17, \
     '4 of a kind': 25, 'small straight': 30, 'large straight': None, 'yahtzee!': 50, 'chance': 17}}
     >>> calculate_yahtzee_score_or_bonus(person, dice)
     100
     >>> dice = [3, 5, 5, 5, 5]
     >>> person = {'name': 'N', 'extra_rolls': 0, 'yahtzee bonuses': 2, 'upper bonus': 0, 'scoreboard': {'aces': 3, \
     'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0, '3 of a kind': 17, \
     '4 of a kind': 25, 'small straight': 30, 'large straight': None, 'yahtzee!': None, 'chance': 17}}
     >>> calculate_yahtzee_score_or_bonus(person, dice)
     0
    """
    yahtzee_recorded = True if player['scoreboard']['yahtzee!'] is not None else False
    valid_yahtzee = check_for_yahtzee(dice_hand)

    if valid_yahtzee and yahtzee_recorded:
        score = YAHTZEE_BONUS_SCORE()

    elif valid_yahtzee and not yahtzee_recorded:
        score = FIXED_SCORE_VALUES()['yahtzee!']

    else:  # Recording invalid first yahtzee
        score = INVALID_SCORE()

    return score


def check_for_yahtzee(dice_hand: list) -> bool:
    """
    Check if the given dice hand is a Yahtzee.

    :param dice_hand: A list of dice rolls.
    :precondition: dice_hand must be a list of 5 integers from 1 - 6.
    :postcondition: Checks if the dice hand is a valid Yahtzee.
    :return: True if the dice hand is a Yahtzee, False otherwise.

    >>> check_for_yahtzee([3, 3, 3, 3, 3])
    True
    >>> check_for_yahtzee([1, 2, 3, 4, 4])
    False
    """
    dice_string_list = [str(die) for die in dice_hand]
    dice_string = ''.join(dice_string_list)

    if re.match(LOWER_SCORE_REGEXES()['yahtzee!'], dice_string):
        return True
    else:
        return False


def get_valid_score_type(scoreboard: dict, dice_hand: list) -> (str, None):
    """
    Ask the user to choose which Yahtzee score category they would like to record.

    :param scoreboard: A dictionary of Yahtzee score information.
    :param dice_hand: A list of dice rolls.
    :precondition: scoreboard must contain keys for every type of Yahtzee score.
    :precondition: dice_hand must be a list of 5 integers from 1 - 6.
    :postcondition: Asks the player to choose a score category that does not have an existing score.
    :return: A string representing the score category the player chose, or None if the string is not a valid category.
    """
    all_categories = list(UPPER_SCORE_CATEGORIES()) + list(LOWER_SCORE_CATEGORIES())
    valid_categories = find_valid_score_categories(scoreboard, dice_hand)

    user_prompt = f"Which score category would you like to record? Enter a number from 1 - {len(all_categories)}: "
    category_choice = input(user_prompt)

    try:
        category_index = int(category_choice) - 1
        category = all_categories[category_index]
    except (ValueError, IndexError):
        print(f"Enter a number from 1 - {len(all_categories)}.")
        return

    if category in valid_categories:
        return category
    else:
        print(f"You already recorded a score for {category.title()}.")
        return


def find_valid_score_categories(scoreboard: dict, dice_hand: list) -> list:
    """
    Determine which Yahtzee score categories a user is eligible to record a score for.

    :param scoreboard: A dictionary of Yahtzee score information.
    :param dice_hand: A list of dice rolls.
    :precondition: scoreboard must contain keys for every type of Yahtzee score.
    :precondition: dice_hand must be a list of 5 integers from 1 - 6.
    :postcondition: Determines the Yahtzee score categories that a user can record a score for.
    :return: A list of categories a user can record a score for.

    >>> test = {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0, '3 of a kind': 17, \
     '4 of a kind': 25, 'full house': 0, 'small straight': 30, 'large straight': None, 'yahtzee!': 50, 'chance': 17}
    >>> find_valid_score_categories(test, [3, 3, 3, 3, 3])
    ['fours', 'large straight', 'yahtzee!']
    """
    all_categories = list(UPPER_SCORE_CATEGORIES()) + list(LOWER_SCORE_CATEGORIES())
    valid_categories = [category for category in all_categories if scoreboard[category] is None]

    # Add yahtzee as an option if user is eligible for bonus
    if scoreboard['yahtzee!'] == 50 and check_for_yahtzee(dice_hand):
        valid_categories.append("yahtzee!")

    return valid_categories


def print_score_recorded(score: int, category: str) -> None:
    """
    Print the recorded score based on the given score value and category.

    :param score: An integer.
    :param category: A string.
    :precondition: score must be 0 or greater.
    :precondition: category must be a valid Yahtzee score category.
    :postcondition: Prints the score result.

    >>> print_score_recorded(30, "full house")
    You recorded 30 pts for Full House.
    >>> print_score_recorded(0, "aces")
    You recorded 0 pts for Aces.
    """
    print(f"You recorded {score} pts for {category.title()}.")


def print_score_categories() -> None:
    """
    Print a numbered list of Yahtzee score categories.

    :postcondition: Prints a numbered list of Yahtzee score categories.

    >>> print_score_categories()
    1. Aces         7. 3 of a Kind
    2. Twos         8. 4 of a Kind
    3. Threes       9. Full House
    4. Fours       10. Small Straight
    5. Fives       11. Large Straight
    6. Sixes       12. Yahtzee!
                   13. Chance
    """
    print(f"{'1. Aces':<16}7. 3 of a Kind")
    print(f"{'2. Twos':<16}8. 4 of a Kind")
    print(f"{'3. Threes':<16}9. Full House")
    print(f"{'4. Fours':<15}10. Small Straight")
    print(f"{'5. Fives':<15}11. Large Straight")
    print(f"{'6. Sixes':<15}12. Yahtzee!")
    print(f"{'':<15}13. Chance")


def update_scoreboard(player: dict, score_category: str, score: int) -> None:
    """
    Update the player's scoreboard based on the given score information.

    :param player: A dictionary of Yahtzee player information.
    :param score_category: A string.
    :param score: An integer.
    :precondition: player must contain all necessary information required for Yahtzee.
    :precondition: category must be a lowercase valid Yahtzee score category.
    :precondition: score must be 0 or greater.
    :precondition: The player must be allowed to record a score in the given score category.
    :postcondition: Updates the player dictionary according to the score given.

    >>> test = {'name': 'Jolin', 'extra_rolls': 0, 'yahtzee bonuses': 2, 'upper bonus': 0, 'scoreboard': {'aces': 3, \
     'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0, '3 of a kind': 17, \
     '4 of a kind': 25, 'small straight': 30, 'large straight': None, 'yahtzee!': 50, 'chance': 17}}
     >>> update_scoreboard(test, "fours", 16)
     >>> test['scoreboard']['fours']
     16
    """
    if score == 100:  # Record Yahtzee bonus
        player['yahtzee bonuses'] += 1
    else:
        player["scoreboard"][score_category] = score


def record_score(player: dict, dice_hand: list) -> None:
    """
    Update the player's scoreboard to add the score based on the given dice hand and the player's chosen category.

    :param player: A dictionary of Yahtzee player information.
    :param dice_hand: A list of dice rolls.
    :precondition: player must contain all necessary information required for Yahtzee.
    :precondition: dice_hand must be a list of 5 integers from 1 - 6.
    :postcondition: Updates the player's scoreboard and prints a score message for the player.
    """
    print_dice_roll(dice_hand)
    print_score_categories()
    score_category = None

    while score_category is None:
        score_category = get_valid_score_type(player['scoreboard'], dice_hand)

    if score_category in UPPER_SCORE_CATEGORIES():
        score = calculate_score_upper_section(dice_hand, score_category)
    elif score_category in ("small straight", "large straight"):
        score = calculate_score_straights(dice_hand, score_category)
    elif score_category == "yahtzee!":
        score = calculate_yahtzee_score_or_bonus(player, dice_hand)
    else:
        score = calculate_score_lower_other(dice_hand, score_category)

    update_scoreboard(player, score_category, score)
    print_score_recorded(score, score_category)


def calculate_score_upper_section(dice_hand: list, score_category: str) -> int:
    """
    Calculate a Yahtzee score for the upper section based on the given dice.

    :param dice_hand: A list of dice rolls.
    :param score_category: A string.
    :precondition: dice_hand must be a list of 5 integers from 1 - 6.
    :precondition: score_category must be a lowercase valid Yahtzee upper score category.
    :postcondition: Calculates the player's score based on the given category.
    :return: An integer representing the player's score.

    >>> calculate_score_upper_section([2, 2, 2, 3, 6], "twos")
    6
    >>> calculate_score_upper_section([3, 4, 5, 5, 6], "aces")
    0
    """
    upper_score_number = UPPER_SCORE_CATEGORIES()[score_category]

    return upper_score_number * dice_hand.count(upper_score_number)


def calculate_score_lower_other(dice_hand: list, score_category: str) -> int:
    """
    Calculate possible Yahtzee scores for the lower section based on the given dice.

    :param dice_hand: A list of dice rolls.
    :param score_category: A string.
    :precondition: dice_hand must be a sorted list of 5 integers from 1 - 6.
    :precondition: score_category must be "full house", "4 of a kind", "3 of a kind", or "chance".
    :postcondition: Calculates the player's score based on the given category.
    :return: An integer representing the player's score.

    >>> calculate_score_lower_other([1, 1, 1, 3, 3], "full house")
    25
    >>> calculate_score_lower_other([1, 2, 2, 3, 4], "3 of a kind")
    0
    """
    dice_string_list = [str(die) for die in dice_hand]
    dice_string = "".join(dice_string_list)

    if score_category == "full house":
        if re.match(LOWER_SCORE_REGEXES()['full house'], dice_string):
            score = FIXED_SCORE_VALUES()['full house']
        else:
            score = INVALID_SCORE()

    elif score_category == "3 of a kind":
        score = sum(dice_hand) if re.match(LOWER_SCORE_REGEXES()['3 of a kind'], dice_string) else INVALID_SCORE()
    elif score_category == "4 of a kind":
        score = sum(dice_hand) if re.match(LOWER_SCORE_REGEXES()['4 of a kind'], dice_string) else INVALID_SCORE()
    else:  # chance
        score = sum(dice_hand)

    return score


def calculate_score_straights(dice_hand: list, straight_category: str) -> int:
    """
    Calculate possible Yahtzee scores for the straight categories based on the given dice.

    :param dice_hand: A list of dice rolls.
    :param straight_category: A string.
    :precondition: dice_hand must be a list of 5 integers from 1 - 6.
    :precondition: straight_category must be "small straight" or "large straight".
    :postcondition: Calculates the player's score based on the given category.
    :return: An integer representing the player's score.

    >>> calculate_score_straights([1, 2, 3, 4, 5], "large straight")
    40
    >>> calculate_score_straights([1, 2, 2, 3, 4], "small straight")
    30
    """
    dice_set = set(dice_hand)
    dice_string_list = [str(die) for die in sorted(list(dice_set))]
    dice_string = ''.join(dice_string_list)

    if re.match(LOWER_SCORE_REGEXES()[straight_category], dice_string):
        score = FIXED_SCORE_VALUES()[straight_category]
    else:
        score = INVALID_SCORE()
    return score


def print_scoreboard(player: dict) -> None:
    """
    Print a player's Yahtzee scoreboard.

    :param player: A dictionary.
    :precondition: player must be a dictionary that contains all necessary information for the player.
    :postcondition: Prints the scoreboard.

    >>> test_player = {'name': 'player', 'extra_rolls': 0, 'yahtzee bonuses': 1, 'upper bonus': 0, \
    'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0, '3 of a kind': 17, \
     '4 of a kind': 25, 'full house': 0, 'small straight': 30, 'large straight': None, 'yahtzee!': 50, 'chance': 17}}
    >>> print_scoreboard(test_player) # doctest: +NORMALIZE_WHITESPACE
    Player's Scoreboard
    Aces           3         3 Of A Kind       17
    Twos           6         4 Of A Kind       25
    Threes         4         Full House        0
    Fours                    Small Straight    30
    Fives          5         Large Straight
    Sixes          0         Yahtzee!          50
    Upper Bonus    0         Chance            17
                             Yahtzee Bonuses   1 x 100
    """
    scores = {category: score if score is not None else "" for category, score in player['scoreboard'].items()}

    print(f"{player['name'].title()}'s Scoreboard")

    for upper_category, lower_category in zip(UPPER_SCORE_CATEGORIES(), LOWER_SCORE_CATEGORIES()):
        print(f"{upper_category.title():<15}{scores[upper_category]:<10}", end="")
        print(f"{lower_category.title():<18}{scores[lower_category]}")

    print(f"{'Upper Bonus':<15}{player['upper bonus']:<10}", end="")
    print(f"{LOWER_SCORE_CATEGORIES()[-1].title():<18}{scores[LOWER_SCORE_CATEGORIES()[-1]]}")

    print(f"{'':<25}{'Yahtzee Bonuses':<18}{player['yahtzee bonuses']} x {YAHTZEE_BONUS_SCORE()}")


def print_dice_roll(list_of_dice: list) -> None:
    """
    Print a player's dice roll.

    :param list_of_dice: A list of dice rolls.
    :precondition: list_of_dice must be a list of 5 integers from 1-6.
    :postcondition: Prints the dice roll values.

    >>> print_dice_roll([1, 3, 3, 4, 5])
    Your dice rolls: 1 3 3 4 5
    """
    list_of_dice.sort()
    dice_string_list = [str(die) for die in list_of_dice]
    dice_string = " ".join(dice_string_list)
    print(f"Your dice rolls: {dice_string}")


def get_menu_choice() -> (int, None):
    """
    Ask the player to choose an option from the Yahtzee turn menu.

    :postcondition: Asks the player to choose to keep dice to roll again, or choose a score.
    :return: An integer representing the number choice, or None if the user entered an invalid choice.
    """
    user_choice = input("What would you like to do? Press 1 to keep dice and roll again, "
                        "press 2 to record a score.\n").strip()

    try:
        if int(user_choice) in VALID_MENU_OPTIONS():
            return int(user_choice)
    except ValueError:
        print("Enter 1 or 2.")
        return


def turn_valid_menu_choice() -> str:
    """
    Get a valid choice from the player to keep dice to roll again, or choose a score.

    :postcondition: Gets a valid user choice to keep dice to roll again, or choose a score.
    :return: "keep" or "score" depending on the player's choice.
    """
    valid_choice = None
    while valid_choice is None:
        valid_choice = get_menu_choice()

    return VALID_MENU_OPTIONS()[valid_choice]


def yahtzee_turn(player: dict) -> None:
    """
    Play a turn of Yahtzee.

    :param player: A dictionary of Yahtzee player information.
    :precondition: player must be a dictionary that contains all necessary information for the player.
    :postcondition: Plays a turn of Yahtzee and updates the dictionary accordingly.
    """
    player['extra_rolls'] = NUMBER_OF_EXTRA_ROLLS()
    player_dice = []

    print(f"{player['name'].title()}'s turn!")
    print_scoreboard(player)

    while player['extra_rolls'] > 0:
        player_dice += roll_dice(NUMBER_OF_YAHTZEE_DICE() - len(player_dice), NUMBER_OF_DICE_SIDES())
        print_dice_roll(player_dice)

        keep_or_score = turn_valid_menu_choice()

        if keep_or_score == "keep":
            player_dice = keep_dice(player_dice)
            print(f"{player['extra_rolls']} roll(s) remaining.")
            player['extra_rolls'] -= 1
        else:  # score
            player['extra_rolls'] = 0

    player_dice += roll_dice(NUMBER_OF_YAHTZEE_DICE() - len(player_dice), NUMBER_OF_DICE_SIDES())
    player_dice.sort()

    record_score(player, player_dice)
    check_for_upper_bonus(player)


def is_scoreboard_full(player: dict) -> bool:
    """
    Check if the player's scoreboard has a value in every spot.

    :param player: A dictionary of Yahtzee player information.
    :precondition: player must be a dictionary that contains all necessary information for the player.
    :postcondition: Check if the player's scoreboard has a value in every spot.
    :return: True if the scoreboard is full, False otherwise.

    >>> value = {'name': 'player', 'extra_rolls': 0, 'yahtzee bonuses': 1, 'upper bonus': 0, \
    'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0, '3 of a kind': 17, \
     '4 of a kind': 25, 'small straight': 30, 'large straight': None, 'yahtzee!': 50, 'chance': 17}}
     >>> is_scoreboard_full(value)
     False
     >>> value = {'name': 'player', 'extra_rolls': 0, 'yahtzee bonuses': 1, 'upper bonus': 0, \
    'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': 0, 'fives': 5, 'sixes': 0, '3 of a kind': 17, \
     '4 of a kind': 25, 'small straight': 30, 'large straight': 0, 'yahtzee!': 50, 'chance': 17}}
     >>> is_scoreboard_full(value)
     True
    """
    for category_score in player['scoreboard'].values():
        if category_score is None:
            return False
    return True


def create_player_information(player_name: str) -> dict:
    """
    Create a dictionary of Yahtzee player information.

    :param player_name: A string.
    :postcondition: Creates a dictionary of player information that sets up values for the an empty scoreboard,
                    dice held, player name, number of Yahtzee bonuses, and total score.
    :return: A dictionary containing Yahtzee player information.

    >>> create_player_information("Jolin") # doctest: +NORMALIZE_WHITESPACE
    {'name': 'Jolin', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 0, 'scoreboard': {'aces': None,
     'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None, '3 of a kind': None,
     '4 of a kind': None, 'full house': None, 'small straight': None, 'large straight': None,
     'yahtzee!': None, 'chance': None}}
    """
    categories = list(UPPER_SCORE_CATEGORIES()) + list(LOWER_SCORE_CATEGORIES())
    scoreboard = {category: None for category in categories}

    player_dictionary = {
        'name': player_name,
        'extra_rolls': NUMBER_OF_EXTRA_ROLLS(),
        'yahtzee bonuses': 0,
        'upper bonus': 0,
        'scoreboard': scoreboard
    }
    return player_dictionary


def calculate_final_score(player: dict) -> int:
    """
    Calculate the player's Yahtzee score.

    :param player: A dictionary of Yahtzee player information.
    :precondition: player must be a dictionary that contains all necessary information for the player.
    :postcondition: Calculates the player's final score
    :return: An integer representing the player's score.

    >>> p1 = {'name': 'p1', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 35, 'scoreboard': {'aces': 10, \
    'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10, 'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, \
    'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}
    >>> calculate_final_score(p1)
    155
    """
    final_score = player['upper bonus'] + player['yahtzee bonuses'] * YAHTZEE_BONUS_SCORE()

    for score in player['scoreboard'].values():
        final_score += score

    return final_score


def determine_winner(player_1: dict, player_2: dict):
    """
    Determine the winner of a 2 player yahtzee game.

    :param player_1: A dictionary of Yahtzee player information.
    :param player_2: A dictionary of Yahtzee player information.
    :precondition: Both dictionaries must contain all necessary information for a Yahtzee player.
    :postcondition: Determines and prints the winner of the yahtzee game.

    >>> p1 = {'name': 'p1', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 35, 'scoreboard': {'aces': 10, \
    'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10, 'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, \
    'full house': 0, 'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}
    >>> p2 = {'name': 'p2', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 0, 'scoreboard': {'aces': 10, \
    'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10, 'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, \
    'full house': 0, 'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}
    >>> determine_winner(p1, p2) # doctest: +NORMALIZE_WHITESPACE
    P1's Scoreboard
    Aces           10        3 Of A Kind       10
    Twos           10        4 Of A Kind       10
    Threes         10        Full House        0
    Fours          10        Small Straight    10
    Fives          10        Large Straight    10
    Sixes          10        Yahtzee!          10
    Upper Bonus    35        Chance            10
                             Yahtzee Bonuses   0 x 100
    P1's final score: 155 pts.
    P2's Scoreboard
    Aces           10        3 Of A Kind       10
    Twos           10        4 Of A Kind       10
    Threes         10        Full House        0
    Fours          10        Small Straight    10
    Fives          10        Large Straight    10
    Sixes          10        Yahtzee!          10
    Upper Bonus    0         Chance            10
                             Yahtzee Bonuses   0 x 100
    P2's final score: 120 pts.
    P1 won!
    """
    player_1_score = calculate_final_score(player_1)
    player_2_score = calculate_final_score(player_2)

    print_scoreboard(player_1)
    print(f"{player_1['name'].title()}'s final score: {player_1_score} pts.")
    print_scoreboard(player_2)
    print(f"{player_2['name'].title()}'s final score: {player_2_score} pts.")

    if player_1_score > player_2_score:
        print(f"{player_1['name'].title()} won!")
    elif player_2_score > player_1_score:
        print(f"{player_2['name'].title()} won!")
    else:
        print("Tie!")


def yahtzee() -> None:
    """
    Run a two-player Yahtzee game.

    :postcondition: Plays a game of two-player Yahtzee.
    """
    player_1 = create_player_information("player 1")
    player_2 = create_player_information("player 2")
    game_ongoing = True

    while game_ongoing:
        if not is_scoreboard_full(player_1):
            yahtzee_turn(player_1)
            time.sleep(1.5)
        if not is_scoreboard_full(player_2):
            yahtzee_turn(player_2)
            time.sleep(2)

        game_ongoing = not is_scoreboard_full(player_1) and not is_scoreboard_full(player_2)

    determine_winner(player_1, player_2)


def main():
    """
    Execute the program.
    """
    doctest.testmod()
    yahtzee()


if __name__ == '__main__':
    main()

dcatef print_scoreboard(player):
    name = player['name']
    scoreboard = player['scoreboard']
    categories = ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes', '3 of a kind', '4 of a kind', 'full house',
                  'small straight', 'large straight', 'yahtzee!', 'chance']

    scores_to_print = {category: score if score else "" for category, score in scoreboard.items()}

    print(f"{name.title()}'s Scoreboard")
    for upper_category, lower_category in zip(categories[:6], categories[6:]):
        print(f"{upper_category.title():<15}{str(scores_to_print[upper_category]):<10}", end="")
        print(f"{lower_category.title():<18}{scores_to_print[lower_category]}")

    print(" " * 24, f"{categories[-1].title():<18}{scores_to_print['chance']}")

    print(f"{'Upper Bonus':<15}{player['upper bonus']:<10}", end="")
    print(f"{'Yahtzee Bonuses':<18}{player['yahtzee bonuses']} x 100")


def main():
    player = {'name': 'Jolin', 'extra_rolls': 0, 'yahtzee bonuses': 1, 'upper bonus': 0,
              'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 15, 'sixes': 0,
                             '3 of a kind': 17, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                             'large straight': None, 'yahtzee!': 50, 'chance': 17}}
    print_scoreboard(player)


if __name__ == '__main__':
    main()
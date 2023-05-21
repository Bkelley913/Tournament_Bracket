import random

def run_bracket():
    # Define Teams
    teams = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6", "Team 7", "Team 8"
             "Team 9", "Team 10", "Team 11", "Team 12", "Team 13", "Team 14", "Team 15", "Team 16"]

    # Splits teams in two different groups
    random.shuffle(teams)
    group_a = teams[:8]
    group_b = teams[8:]

    # Play group match and determine the winner
    group_a_winner = play_group_matches(group_a)
    group_b_winner = play_group_matches(group_b)

    # Play final match between group winner
    winner_a, winner_b = play_final_match(group_a_winner, group_b_winner)

    # Print tourament results
    print("Tournament Results: ")
    print(f"Winner of Group A is: {winner_a}")
    print(f"Winner of group B is: {winner_b}")
import tkinter as tk
import random
import threading

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

# GUI implementation
def play_group_matches(group_teams):
    winners = []
    results_text = "Group Matches:\n"
    #print("Groups Matches: ")
    for i in range(0, len(group_teams), 2):
        team1 = group_teams[i]
        team2 = group_teams[i + 1]
        winner = random.choice([team1, team2])
        winners.append(winner)
        results_text += f"{team1} vs {team2} - Winner: {winner}\n"
        #print(f"{team1} vs {team2} - Winner: {winner}")
    #print()
    results_text += "\n"
    results_label.config(text=results_text)
    return winners

def play_final_match(winner_a, winner_b):
    #print("Final Match: ")
    results_text = "Final Match: \n"
    winner = random.choice([winner_a, winner_b])
    #print(f"{winner_a} vs {winner_b} - Winner: {winner}")
    results_text += f"{winner_a} vs {winner_b} - Winner: {winner}\n\n"
    results_label.config(text=results_text)
    #print()
    return winner

def run_tournament():
    tourament_thread = threading.Thread(target=run_bracket)
    tourament_thread.start()

# Run the tournament
#run_bracket()

window = tk.Tk()
window.title("Tournament Bracket")

title_label = tk.Label(window, text="Tournament Bracket")
title_label.pack()

results_label = tk.Label(window, text="Results will appear here.")
results_label.pack()

play_button = tk.Button(window, text="Run Tournament", command=run_tournament)
play_button.pack()

window.mainloop()
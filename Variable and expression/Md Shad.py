
#taking input from user.
total_time = int(input("How many minutes the player was on the field? :- "))

total_goals = int(input("\nHow many goals the player scored? :- "))

shots_taken = int(input("\nHow many times the player tried to shoot? :- "))

on_target = int(input("\nHow many shots actually went towards the goal? :- "))

distance_ran = int(input("\nHow many kilometers the player ran (decimal number)? :- "))

#Shot Accuracy, that is, the percentage of shots that were on target.

shots_accuracy = (on_target/shots_taken)*100
print(f"\nThe percentage of shots that were on target.: {shots_accuracy}%\n")

#Goal Scoring Rate, that is, the percentage of shots turned into goals.

goal_rate = (total_goals/shots_taken)*100
print(f"The percentage of shots turned into goals: {goal_rate}%\n")

#Running Stats, the average speed of the player in kilometers per minute.

running_stats = (distance_ran/total_time)
print(f"The average speed of the player in kilometers per minute: {running_stats}km per minute")

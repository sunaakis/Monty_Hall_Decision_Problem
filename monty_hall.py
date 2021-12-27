from random import shuffle, choice

# defining door numbers
door_numbers = [1, 2, 3]

# defining prize
wanted_prize = "car"
unwanted_prize = "goat"
prize = [wanted_prize, unwanted_prize, unwanted_prize]


# defining game
def monty_hall_game(initial_door_number, should_switch):
    """
    The result of the one time Monty Hall game.

    args:
    ---
        initial_door_number: int, the chosen door number by the player at first
        should_switch: boolean object, whether the player should switch or not

    """
    shuffle(prize) # shuffling the order - car is randomly located
    doors = dict(zip(door_numbers, prize)) # assigning prize to each door
    # remaining doors among which Monty Hall can chose
    remaining_door_numbers = [x for x in door_numbers if x != initial_door_number]
    for door in remaining_door_numbers:
        if doors[door] == unwanted_prize:
            remaining_door_numbers.remove(door)
            break

    switched_door_number = remaining_door_numbers[0]
    final_door_number = switched_door_number if should_switch else initial_door_number
    won_car = doors[final_door_number] == wanted_prize
    return won_car


monty_hall_game(1,True)
# True


def simulation(trial_number, should_switch):
    winning_times = 0
    for trial in trial_number:
        int_door = choice(door_numbers) # choose a random item from a sequence.
        result = monty_hall_game(int_door, should_switch)
        if result:
            winning_times += 1

    probability_of_win = round(winning_times/len(trial_number),2)
    return probability_of_win


simulation(range(10000), True)
# 0.67
simulation(range(10000), False)
# 0.33





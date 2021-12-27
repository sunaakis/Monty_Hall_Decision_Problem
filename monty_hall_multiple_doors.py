from random import shuffle, choice

# defining door numbers
door_numbers = list(range(10))

# defining prize
wanted_prize = "car"
unwanted_prize = "goat"
prize = [wanted_prize] * 1 + [unwanted_prize] * (len(door_numbers) - 1)

# defining game
def monty_hall_game(initial_door, switch):
    """
    The result of the one time Monty Hall game.

    args:
    ---
    initial_door_number: int, the chosen door number by the player at first
    should_switch: boolean object, whether the player should switch or not

    """
    shuffle(prize) # shuffling the order - car is randomly located
    doors = dict(zip(door_numbers, prize)) # assigning prize to each door
    initial_door = choice(door_numbers)
    # remaining doors among which Monty Hall can chose
    remaining_doors = [door for door in door_numbers if door != initial_door]

    while len(remaining_doors) > 1:
        monty = choice(remaining_doors)
        if doors[monty] != wanted_prize:
            remaining_doors.remove(monty)

    switch_list = [initial_door] + remaining_doors
    final_decision = switch_list[1] if switch else switch_list[0]
    won_car = doors[final_decision] == wanted_prize
    return won_car


monty_hall_game(1, True)
# True
monty_hall_game(1, False)
# False


def simulation(trial_number, switch):
    winning_times = 0
    for trial in trial_number:
        int_door = choice(door_numbers)
        result = monty_hall_game(int_door, switch)
        if result:
            winning_times += 1

    probability_of_win = round(winning_times / len(trial_number), 2)
    return probability_of_win

simulation(range(10000), True)
# 0.9
simulation(range(10000), False)
# 0.1
import random

"""
args:
    budget: the current budget the player has
    num_infected_neighbours: number of infected neighbours 
    is_infected: true if the player is currently infected, false if not
    is_protected: ture if the player choose to protect themselfes

return:
    budget (int): the new total budget for the player
    new_money (int): the amount of new money the player got
    num_infected_neighbours (int): the new number of infected neighbours
    num_neighbours (int): total number of neighbours
    is_infected: true if the player got infected, false if not
    is_protected: true if the player is protected, flase if not

"""
def run_step(budget, num_infected_neighbours, num_neighbours, is_infected, is_protected):

    chance = random.random()
    # get infected by by conditional propability
    is_infected = False if is_protected and chance >= 0.1 or chance > 0.8 else True

    # protection costs 20, infection costs 50
    budget = budget - 20 if is_protected else budget
    budget = budget - 50 if is_infected else budget

    # neighbours get infected by change
    chance = random.random()
    num_infected_neighbours = round(num_neighbours * chance)
    num_healthy_neighbours = num_neighbours - num_infected_neighbours

    # each round, new money is distributed
    total_new_money_per_round = 50 * num_neighbours

    # if you stay healty you get more money
    healthy_group_bias = 10 * num_neighbours


    if num_healthy_neighbours != 0:
        healthy_group_percentage = num_healthy_neighbours / num_neighbours
        healty_group_new_money = healthy_group_percentage * total_new_money_per_round + healthy_group_bias
        money_per_healthy_individual = healty_group_new_money / num_healthy_neighbours

    if num_infected_neighbours != 0:
        sick_group_percentage = num_infected_neighbours / num_neighbours
        sick_group_new_money = sick_group_percentage * total_new_money_per_round
        money_per_sick_individual = sick_group_new_money / num_infected_neighbours

    
    new_money =  money_per_healthy_individual if not is_infected else money_per_sick_individual

    budget += new_money

    total_new_money_distributed = money_per_healthy_individual * num_healthy_neighbours + money_per_sick_individual * num_infected_neighbours
    print("budget: {}, new_money: {}, num_infected_neighbours: {}, is_infected: {}, healty_money: {}, sick_money: {}, total_money_distributed: {}".format(int(budget), int(new_money), int(num_infected_neighbours), is_infected, round(money_per_healthy_individual), round(money_per_sick_individual), round(total_new_money_distributed)))

    return int(budget), int(new_money), int(num_infected_neighbours), int(num_neighbours), is_infected, is_protected



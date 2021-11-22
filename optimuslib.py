"""Optimus trade lib"""
import csv
import math


class Action:
    def __init__(self, name, price, profit):

        self.name = name
        self.price = math.floor(abs(float(price)))
        self.profit = math.floor(float(profit))
        self.benefice = self.price * self.profit / 100

    def __repr__(self):
        return (
            f"Action: '{self.name}' Prix: {self.price}€"
            f" Pourcentage(2ans): {self.profit}% Bénéfice: {self.benefice}€"
        )


def most_benefice_bruteforce(budget, actions, taken_actions = []):
    """Try all cominations from the list of action et return the ones with most benefice based on the budget"""
    if actions:
        """Call the function until there is no one left to check"""
        action_one, val_one = most_benefice_bruteforce(budget, actions[1:], taken_actions)
        action = actions[0]

        """if the price is lower than budget"""
        if action.price <= budget:
            action_two, val_two = most_benefice_bruteforce(budget - action.price, actions[1:], taken_actions + [action])

            """Compare the choosen action with the next one to see which one is better in benefice"""
            if action_one < action_two:
                return action_two, val_two

        return action_one, val_one
    else:
        """return the sum of the most benefice combination and the list of actions you have to buy """
        return sum([i.benefice for i in taken_actions]), taken_actions



def most_benefice_optimized(budget, actions):
    """Create a table with a line for the budget and a line for actions"""
    table = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]

    for i in range(len(actions) + 1):
        for b in range(budget + 1):
            if actions[i-1].price <= b:
                table[i][b] = max(actions[i-1].benefice + table[i-1][b-actions[i-1].price], table[i-1][b])
            else:
                table[i][b] = table[i-1][b]
    
    a = len(actions)
    b = budget
    taken_actions = []

    while b >= 0 and a >= 0:
        e = actions[a-1]
        if table[a][b] == table[a-1][b-e.price] + e.benefice:
            taken_actions.append(e)
            b -= e.price
            

        a -= 1
        
    print(len(taken_actions))
    return table[-1][-1], taken_actions

    
def get_action(file, list):
    """Read a csv file, take the data and transform them in actions to use them after"""
    read = csv.DictReader(file)
    for row in read:
        action = Action(row["name"], row["price"], row["profit"])
        list.append(action)

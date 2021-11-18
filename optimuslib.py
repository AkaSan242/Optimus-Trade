"""Optimus trade lib"""
import csv

class Action:
    def __init__(self, name, price, profit):

        self.name = name
        self.price = float(price)
        self.profit = float(profit)
        self.benefice = (self.price * self.profit) / 100

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
        if action[1] <= budget:
            action_two, val_two = most_benefice_bruteforce(budget - action[1], actions[1:], taken_actions + [action])

            """Compare the choosen action with the next one to see which one is better in benefice"""
            if action_one < action_two:
                return action_two, val_two

        return action_one, val_one
    else:
        return sum([i[2] for i in taken_actions]), taken_actions


def get_action(file, list):
    """Read a csv file, take the data and transform them in actions to use them after"""
    read = csv.DictReader(file)
    for row in read:
        action = Action(row["name"], row["price"], row["profit"])
        tuple_action = (action.name, action.price, action.benefice)
        list.append(tuple_action)

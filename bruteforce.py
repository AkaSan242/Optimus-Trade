import csv
from operator import attrgetter
from time import sleep

"""
récuper les actions du fichier csv
transformer les actions en objets Action
ajouter les actions dans une liste

"""

class Action:
    def __init__(self, name, cost, percentage_after_two_years):

        self.name = name
        self.cost = cost
        self.percentage = percentage_after_two_years
        self.benefice = (self.cost * self.percentage) / 100

    def __repr__(self):
        return (
            f"Action: '{self.name}' Prix: {self.cost}€"
            f" Pourcentage(2ans): {self.percentage}% Bénéfice: {self.benefice}€"
        )


def buy_action(customer, action):
    new_budget = customer.budget - action.cost
    customer.budget = new_budget


customer_budget = 500
actions_list = []


def most_benefice(budget, actions, taken_actions = []):
    if actions:
        action_one, val_one = most_benefice(budget, actions[1:], taken_actions)
        action = actions[0]
        if action[1] <= budget:
            action_two, val_two = most_benefice(budget - action[1], actions[1:], taken_actions + [action])
            if action_one < action_two:
                return action_two, val_two

        return action_one, val_one
    else:
        return sum([i[2] for i in taken_actions]), taken_actions


def get_action(file, list):
    read = csv.DictReader(file)
    for row in read:
        action = Action(row["name"], float(row["price"]), float(row["profit"]))
        tuple_action = (action.name, float(action.cost), float(action.benefice))
        list.append(tuple_action)


f = open(r"actions.csv")
get_action(f, actions_list)
print(most_benefice(customer_budget, actions_list))



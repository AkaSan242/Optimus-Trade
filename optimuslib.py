"""Optimus trade lib"""
import csv
import math


class Action:
    def __init__(self, name, price, profit):

        self.name = name
        self.price = math.ceil(abs(float(price)))
        self.profit = float(profit)
        self.benefice = self.price * self.profit / 100

    def __repr__(self):
        return (
            f"Action: '{self.name}' Prix: {self.price}€"
            f" Pourcentage(2ans): {self.profit}% Bénéfice: {self.benefice}€"
        )

  
def get_action(file, list):
    """Read a csv file, take the data and transform them in actions to use them after"""
    read = csv.DictReader(file)
    for row in read:
        action = Action(row["name"], row["price"], row["profit"])
        list.append(action)

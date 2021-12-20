"""Optimus trade lib"""
import csv
import math


class Action:
    def __init__(self, name, price, profit):

        self.name = name
        self.price = math.ceil(float(price))
        self.real_price = float(price)
        self.profit = float(profit)
        self.percentage = self.price * self.profit / 100
        self.real_percentage = self.real_price * self.profit / 100
        self.benefice = float("{:.2f}".format(self.real_percentage))

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
        if action.price > 1:
            list.append(action)

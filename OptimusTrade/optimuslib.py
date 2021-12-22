"""Optimus trade lib"""
import csv


class Action:
    def __init__(self, name, price, profit):

        self.name = name
        self.price = int(float(price) * 100)
        self.profit = int(float(profit) * 100)
        self.benefice = int(self.price * self.profit / 10000)


    def __repr__(self):
        return (
            f"Action: '{self.name}' Prix: {self.price / 100} €"
            f" Pourcentage(2ans): {self.profit / 100}% Bénéfice: {self.benefice / 100}€"
        )

  
def get_action(file):
    """Read a csv file, take the data and transform them in actions to use them after"""
    actions_list = []
    read = csv.DictReader(file)
    for row in read:
        action = Action(row["name"], row["price"], row["profit"])
        if action.price > 1:
            actions_list.append(action)

    return actions_list

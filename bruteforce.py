from operator import attrgetter
from time import sleep


class Customer:
    def __init__(self, budget):
        self.budget = budget


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


luc = Customer(500)
taken_actions = []

actions = [
    Action("Nike", 20, 5),
    Action("Adidas", 30, 10),
    Action("Ralph Lauren", 50, 15),
    Action("Gucci", 70, 20),
    Action("Fred Perry", 60, 17),
    Action("Zara", 80, 25),
    Action("Gap", 22, 7),
    Action("Courir", 26, 11),
    Action(
        "Foot Locker",
        48,
        13,
    ),
    Action("Burberry", 34, 27),
    Action("Mickael Kors", 42, 17),
    Action("Prada", 110, 9),
    Action("H&M", 38, 23),
    Action("JD", 14, 1),
    Action("Jules", 18, 3),
    Action("Uniqlo", 8, 8),
    Action("Celio", 4, 12),
    Action("Diesel", 10, 14),
    Action("Kiabi", 24, 21),
    Action("Louis Vuitton", 114, 18),
]


def most_benefice(customer, actions, taken_actions):

    """sort the list by percentage to choose the actions with the most percentage of benefice first"""
    actions_ranking = sorted(actions, key=attrgetter("percentage"), reverse=True)
    min = actions_ranking[0].cost

    """Use to define the lowest price of all actions"""
    for i in range(len(actions_ranking)):
        if actions_ranking[i].cost < min:
            min = actions_ranking[i].cost

    # To make sure that we don't spend more than budget
    while customer.budget > min:
        for i in range(len(actions_ranking)):
            if customer.budget > actions_ranking[i].cost:
                buy_action(customer, actions_ranking[i])
                taken_actions.append(actions_ranking[i])

    print(
        "voici la liste des actions qu'il faudrait acheter pour un maximum de bénéfice"
    )
    sleep(1)
    # Check the best combination of actions
    for i in range(len(taken_actions)):
        print(taken_actions[i])

    sleep(2)
    print(
        "Vous prendriez  "
        + str(len(taken_actions))
        + " actions et il vous restera "
        + str(customer.budget)
        + " euros"
    )

    benefice = 0
    for i in range(len(taken_actions)):
        benefice += taken_actions[i].benefice

    sleep(1)
    print("Vous feriez un bénéfice de " + str(benefice) + " euros en 2ans")


most_benefice(luc, actions, taken_actions)

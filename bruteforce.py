from operator import attrgetter


class Customer:
    def __init__(self, budget):
        self.budget = budget


class Action:
    def __init__(self, cost, percentage_after_two_years):

        self.cost = cost
        self.percentage = percentage_after_two_years
        self.benefice = (self.cost * self.percentage) // 100

    def show_benefice(self):
        print("le bénéfice de cette action après 2 ans est de " + str(self.benefice) + " euros")

    def __repr__(self):
        return f"(Prix: {self.cost}€, Pourcentage(2ans): {self.percentage}%, Bénéfice: {self.benefice}€)"


def buy_action(customer, action):
    new_budget = customer.budget - action.cost
    customer.budget = new_budget


luc = Customer(500)
taken_actions = []

actions = [Action(20, 5), Action(30, 10), Action(50, 15), Action(70, 20), Action(60, 17), Action(80, 25),
           Action(22, 7), Action(26, 11), Action(48, 13,), Action(34, 27), Action(42, 17), Action(110, 9),
           Action(38, 23), Action(14, 1), Action(18, 3), Action(8, 8), Action(4, 12), Action(10, 14),
           Action(24, 21), Action(114, 18)]


def most_benefice(customer, actions, taken_actions):

    actions_ranking = sorted(actions, key=attrgetter("benefice"), reverse=True)
    while customer.budget >= 0:
        for i in range(len(actions_ranking)):
            if customer.budget > actions_ranking[i].cost:
                buy_action(customer, actions_ranking[i])
                print(customer.budget)
                taken_actions.append(actions_ranking[i])


    print("vous avez pris " + str(len(taken_actions)) + "actions et il vous reste" + str(customer.budget) + "euros")


most_benefice(luc, actions, taken_actions)



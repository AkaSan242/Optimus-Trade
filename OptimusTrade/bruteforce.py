from optimuslib import get_action
from memory_profiler import profile


def most_benefice_bruteforce(budget, actions, taken_actions = []):
    #Try all cominations from the list of action et return the ones with most benefice based on the budget
    if actions:
        #Call the function until there is no one left to check
        action_one, val_one = most_benefice_bruteforce(budget, actions[1:], taken_actions)
        action = actions[0]

        #if the price of the action is lower than budget
        if action.price <= budget:
            action_two, val_two = most_benefice_bruteforce(budget - action.price, actions[1:], taken_actions + [action])

            #Compare the choosen action with the next one to see which one is better in benefice
            if action_one < action_two:
                return action_two, val_two

        return action_one, val_one
    else:
        #return the sum of the most benefice combination and the list of actions you have to buy
        return (["bénéfice: " + str(sum([i.benefice for i in taken_actions])) + "€", "budget dépensé: " + str( 500 - budget) + "€" ],
                ["Liste des actions à acheter: " + str([i.name for i in taken_actions])]
        )

customer_budget = 500
actions_list = []

if __name__=='__main__':
    f = open(r"actions.csv")
    get_action(f, actions_list)
    print("Voici le meilleur plan d'investissement:")
    print(most_benefice_bruteforce(customer_budget, actions_list))
else:
    print("Veuillez éxécuter la commande 'python bruteforce.py' pour avoir le résultat")



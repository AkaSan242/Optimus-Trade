from optimuslib import get_action, most_benefice_optimized

customer_budget = 500
actions_list = []

if __name__=='__main__':
    f = open(r"actions.csv")
    get_action(f, actions_list)
    print(most_benefice_optimized(customer_budget, actions_list))
else:
    print("Veuillez éxécuter la commande 'python bruteforce.py' pour avoir le résultat")
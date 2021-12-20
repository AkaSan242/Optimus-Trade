import csv
from optimuslib import get_action


def most_benefice_optimized(budget, actions):
    """Create a table with a line for the budget and a line for actions"""
    table = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]
   
   #Create a line for each action and calculate the max value of the benefice if buy

    for i in range(len(actions)):
        for b in range(budget + 1):
            action = actions[i-1]

            #to make sure we don't exceed the budget
            if action.real_price <= b:
                #if the benefice is better than the previous one the new benefice become the max 
                table[i][b] = max(action.benefice + table[i-1][b-action.price], table[i-1][b])
            else:
                #the max don't change and we keep checking the next actions 
                table[i][b] = table[i-1][b]
    
    
    a = len(actions)
    b = budget
    taken_actions = []

    #while we still have money on budget and there is still actions to check 
    while b > 1 and a >= 0:
        e = actions[a-1]

        #if the action is the max benefice in the table for the budget we take it
        if table[a][b] == table[a-1][b-e.price] + e.benefice:
            taken_actions.append(e)
            b -= e.price
            

        a -= 1

    spend_budget = sum([i.real_price for i in taken_actions])
    formated_spend_budget = "{:.2f}".format(spend_budget)
    
    
    most_benefice = table[-2][-2]
    formated_benefice = "{:.2f}".format(most_benefice)

    
    
    create_csv("actionsreport.csv", taken_actions, formated_spend_budget, formated_benefice)
    return (["bénéfice: " + str(formated_benefice) + "€", "Budget dépensé: " + str(formated_spend_budget) + "€"] ,
     ["Liste des actions à acheter: " + str([i.name for i in taken_actions]) + " " + "Nombre d'actions: " +  str(len(taken_actions))]
    )

def create_csv(csvfile, list, budget, benefice):
    
    with open(csvfile, 'w', newline='', encoding='utf-8-sig') as data:
                datawriter = csv.writer(data, delimiter=',', dialect='excel', quoting=csv.QUOTE_ALL)

                datawriter.writerow(['Name', 'Price', 'Bénéfice'])

    for elt in list:
            with open(csvfile, 'a', newline='', encoding='utf-8-sig') as data:
                datawriter = csv.writer(data, delimiter=',', dialect='excel')
                datawriter.writerow([elt.name, str(elt.real_price) + "€", str(elt.benefice) + "%"])

    with open(csvfile, 'a', newline='', encoding='utf-8-sig') as data:
                datawriter = csv.writer(data, delimiter=',', dialect='excel')
                datawriter.writerow(["Total bénéfice: " + str(benefice) + "€","Budget dépensé: " + str(budget) + "€",
                "Nombre d'action: " + str(len(list))])



customer_budget = 500
actions_list = []


if __name__=='__main__':
    f = open(r"actions.csv")
    get_action(f, actions_list)
    print("Voici le meilleur plan d'investissement:")
    print(most_benefice_optimized(customer_budget, actions_list))
else:
    print("Veuillez éxécuter la commande 'python optimized.py' pour avoir le résultat")
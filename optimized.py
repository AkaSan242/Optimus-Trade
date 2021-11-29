from optimuslib import get_action
from memory_profiler import profile


@profile
def most_benefice_optimized(budget, actions):
    """Create a table with a line for the budget and a line for actions"""
    table = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]
   
   #Create a line for each action and calculate the max value of the benefice if buy

    for i in range(len(actions)):
        for b in range(budget + 1):
            action = actions[i-1]

            #to make sure we don't exceed the budget
            if action.price <= b: 
                #if the benefice is better than the previous one the new benefice become the max 
                table[i][b] = max(action.benefice + table[i-1][b-action.price], table[i-1][b])
            else:
                #the max don't change and we keep checking the next actions 
                table[i][b] = table[i-1][b]
    
    
    a = len(actions)
    b = budget
    taken_actions = []

    #while we still have money on budget and there is still actions to check 
    while b >= 0 and a >= 0:
        e = actions[a-1]

        #if the action is the max benefice in the table for the budget we take it
        if table[a][b] == table[a-1][b-e.price] + e.benefice:
            taken_actions.append(e)
            b -= e.price
            

        a -= 1
        
    
    return (["bénéfice: " + str(table[-2][-2]) + "€", "Budget dépensé: " + str(500 - b) + "€"] ,
     ["Liste des actions à acheter: " + str([i.name for i in taken_actions])]
    )


customer_budget = 500
actions_list = []

if __name__=='__main__':
    f = open(r"actions.csv")
    get_action(f, actions_list)
    print("Voici le meilleur plan d'investissement:")
    print(most_benefice_optimized(customer_budget, actions_list))
else:
    print("Veuillez éxécuter la commande 'python optimized.py' pour avoir le résultat")
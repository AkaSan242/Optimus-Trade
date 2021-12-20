# Optimus-Trade
Optimus Trade Application

## Installation

To install Optimus Trade **clone** this repository by run ` git clone https://github.com/Luc-Aka-Evy/Optimus-Trade.git`

## Description

Optimuse Trade is an application who use the **data** of a **csvfile** with some actions and return the best comination of them to get the most benefice return.

## How it works

First of all what is an **action** ? An action is a **piece** of a company you can buy with an investment and get a percentage of **benefice** after some time.
the percentage is based on the **price** of the action and depend of the company.

So to use Optimus Trade you need a csvfile with **'the name of the action, the price and the percentage of benefice'**. Make sure to put the file in the same directory or add the path in the script you'll use.

## Bruteforce or Optimized ?

Whats different ? in the fact both does the same things the difference is the **time** they use to make it if your csvfile got few action (10, 20, 50) and use **bruteforce.py** we talk about seconds but the more you got more time it take and when i said more time we talk about hours to get the results.

**Optimized.py** is better when you got a high number of actions (1000 or more).

## How to use 

**Before** use go in the script define the **budget** you have to buy actions in the variables *'budget'* and at the line *'f = open(r'actions.csv')'* change the name with your csvfile.

run `python3 bruteforce.py` or `python3 optimized.py`

optimized.py create a csvfile with the result.

## Recommandation

Python 3

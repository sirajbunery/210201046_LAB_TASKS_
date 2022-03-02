#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Siraj ahmad khan reg no: 210201046


# In[1]:


##Qno1
product_num = eval(input("Enter Number of products: "))
my_dict ={}
for x in range(product_num):
    productName = input("Enter Product Name: ")
    productPrice = int(input("Enter Product Price"))
    my_dict[productName] = productPrice


while True:
    productName = input("Enter Product name to get Price")
    if productName in my_dict:
        print("The price for your product is ", my_dict[productName])
        break;

    else:
        print("This product is not found in dictionary")


print(my_dict)


# In[4]:


##Qno2
product_num = eval(input("Enter Number of products: "))
my_dict ={}
for x in range(product_num):
    productName = input("Enter Product Name: ")
    productPrice = int(input("Enter Product Price"))
    my_dict[productName] = productPrice

amount =eval(input("Enter Amount: $$"))
for key ,values in my_dict.items():
    if  int(values) < amount:
        print (key ,"->",values)
        break;
    else:
        print("none of the product is less than your enterred amount")
        break;


# In[5]:


##Qno3
import operator

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

#a
user_input= input("Enter Name of a month: ")
for key, values in year.items():
     if user_input == key:  
        print( values)


#b
sorted_year ={key:year[key] for key in sorted(year)}
print(sorted_year.keys())

#c
for keys,values in year.items():
    if int(values) == 31:
        print(keys)

#d


sorted_bymonthdays = dict(sorted(year.items(),key= operator.itemgetter(1)))
print(sorted_bymonthdays)


# In[6]:


##Q4
user_dict ={"Ahmad":"1234","Khan":"Larissa","Hassan":"Gaga"}
def CheckUser_Pass(x,y):
    for keys ,values in user_dict.items():
        if keys == x  and y == user_dict[keys]:
            return ("you are succesfully logged in",keys,user_dict[keys])
        else:
            return  ("Please do check your login details")



x = input("Enter Username: ")    
y = input("Enter Your Password ")
print(CheckUser_Pass(x,y))


# In[8]:


#Q5
def teamWIn():
    no_ofTeams = int(input("Enter Number of Teams: "))
    team_dict={}
    score_list =[]
    winning_record =[]
    percentage_score = 0
    for team in range(no_ofTeams):
        team_name = input("Enter Team Name: ")
        team_winning_score = int(input("Team Winning game: "))
        team_dict.update({team_name:team_winning_score})
        score_list.append(team_winning_score)
        winning_record.append(team_name)

    userinput = input("Enter team to check % of wins: ")
    for  keys,values in team_dict.items():

         if userinput == keys:
            score = team_dict[keys]
            percentage_score = (score/100)* 100

    return "Your teams list is {},Percentage win of team {}%, All team with winning record  {}".format(team_dict,percentage_score,winning_record)






print(teamWIn())


# In[10]:


##Q6
def teamInfo():
    num_team =int(input("Enter Number Of Teams: "))
    team_dict={}
    for team in range(num_team):
        key = input("Enter Team name: ")
        value =[]
        wins = int(input("Enter Win: "))
        losses = int(input("Enter Losses: "))
        value.extend((wins,losses))
        team_dict.update({key:value})
       
    return team_dict


# In[11]:


##Q7
matrix_5= [1,2,3,4,5,
           5,6,7,4,5,
           6,7,8,0,3,
           4,2,1,5,6,
           7,8,9,0,5]

def creatList():
    matrix_dict={}
    for num in range(len(matrix_5)):
        key = matrix_5[num]
        value = matrix_5.count(key)
        matrix_dict.update({key:value})
    return matrix_dict



print(creatList())


# In[12]:


#Q8
import random

all_card ={"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards = 3
player1Card =[]
player2Card =[]
for card in range(cards):
    c1 =random.choice(list(all_card.values()))
    c2= random.choice(list(all_card.values()))
    player1Card.append(c1)
    player2Card.append(c2)
print(player1Card,player2Card)

if sum(player1Card) > sum(player2Card):
    print("Player 1 wins with ",sum(player1Card)," Against Player 2 with",sum(player2Card))
elif sum(player2Card) > sum(player1Card):
    print("Player 2 wins with ",sum(player2Card)," Against Player 1 with",sum(player1Card))


# In[ ]:


#Q10
from enum import Enum
from random import sample

class Cards(Enum):
    DECK = [{'value':i, 'suit':c} 
            for c in ['spades', 'clubs', 'hearts', 'diamonds'] 
            for i in range(2,15)]

def validate_num(message):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input > 0:
                valid = True
            else:
                print('\nEnter a huge number for how many hands to play.')
        except ValueError:
            print('\nEnter a valid integer.')
    return user_input

def flush(COUNT, num):
    for i in range(num):
        hand = get_cards()
        if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit'] == hand[4]['suit']:
            COUNT += 1
        else:
            pass
    return COUNT

def get_cards():
    rand_cards = sample(Cards.DECK.value, 5)
    return rand_cards

def main():
    COUNT = 0
    message = 'Enter the number of hands to play: '
    num = validate_num(message)
    prob = flush(COUNT, num)
    print(f'\n{prob} hand(s) had a flush.\n')
    print(f'The probability to get a flush from {num} hands is {round((prob/num)*100, 3)}%.')

if __name__ == '__main__':
    main()


# In[13]:


#Q14
d=[{'name':'siraj', 'phone':'0336-9277930', 'email':'siraj048@gmail.com'},
{'name':'umair', 'phone':'0333-6689908', 'email':'umair@gmail.com'},
{'name':'raza', 'phone':'0348-1878188', 'email':' '},
{'name':'dawood', 'phone':'0333-9076397', 'email':'dawood@gmail.com'}]


for dict  in  range(len(d)):
     dctnry =d[dict ]
for keys,values in dctnry.items():
     if keys == "phone" and values[-1] == "8":
            print(dctnry)
   
     if keys == "email" and values =='':
            print(dctnry)
# in 1st if codition program will show item of phone no having 8 as last didgit 
# in second if condition program will show item which dont have email means empty email value.


# In[ ]:





# In[ ]:





# In[14]:


#16
def int_to_roman(input):

    if not isinstance(input, type(1)):
        raise (TypeError,"expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise (ValueError, "Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)


print(int_to_roman(22))


# In[ ]:





# In[ ]:





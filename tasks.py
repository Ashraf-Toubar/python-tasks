

#1 Create a Boolean variable named x
x = True
print(x)
#2 Create an integer variable named y

y = 5
print(y)

#3 Create a float variable named z
z = 3.2

#4 Create a string variable names s
s = 'welcome'

#5 Convert the int variable to float

z= float(2)

#6 Can we convert the str to int ?,
# no,only in the input function

#7 Create a list of numbers from 1 to 5
list2 =[1,2,3,4,5]

#8 Create a tuple from 10 to 15
mytuple = ('banana','apple','orange')

#9 Convert the list to tuple

list2 =tuple([1,2,3,4,5])

#10 Create a dict of 3 values

dict1 = {'mohamed':20, 'sasa': 22, 'mahmoud': 25}

#11 Can we use semi colon ; with python
#no we can't

#12 Python is interpreted or compiled ?
#interpreted

#13 What is the differences between low level & high level
#low level: very machine-friendly,Debugging them is very difficult,They are not very easy to understand
#high level : programmer-friendly,It is very easy to debug these languages,One can easily run them on different platforms,very easy to understand,easy maintenance and are thus simple and manageable 

#14 What is the differences between = , == -- =:puts the value in the variable(used for assignation of value), == : is the value equal the variable(comparison of two variable)

#15 What do we mean by using != : is not equal
'''
#16 What is the operator precedence: order of operations. Operators are used to perform operations on variables and values 
 and it is classified into:Arithmetic operators Assignment operators
Comparison operators
Logical/Bitwise operators
Identity operators
Membership operators
'''









#17 Create a variable x with value of 10
x= 10

#18 Increase x value by 15 using assignment operators
x+=15
print(x)

#19 Divide the x value by 5 using assignment operators

x /= 5
print(x)

#20 Multiply the x value by 10 using assignment operator

x *= 10
print(x)

#21 Get module of x on 3 using assignment operators
x %= 3
print(x)

#22 Using python print the module of 11 to 4
print( 11%4 )

#23 Print the exponent of 2,3
E =2**3
print(E)

#24  Divide 11 by 3 using python division
Q = 11 / 3

'''
#25 Can we divide 11 by 3 and get an integer number ?
YES,by converting it to int
'''
x = int(5/2)
print(x)

#26,27  Check if 10 is bigger than 15 or not
if(10 > 15):
    print(True)
else:
    print('x is smaller than 15')    

#28 In which cases we will use all : with more than one condition and they all have to be ture

#29 What is the differences between all , and: syntax also all: saves space if there is more than one condition , and:with with mre than one condition it takes spaces

#30 What is the differences between any , or : in the syntax

#31 If we need all the conditions to be true we will use 'all'

#32 What is the differences between if , elif --
# if: is the first condition,
# elif:if you want to add another condition or more
'''
#33 What is the differences between elif else-- 
# elseif :if you want to put another condition or more,
# else: we put it in the end of the if function  
'''

#34 Can we use more than one elif: yes we can

#35 Can we use more than one else: no we can't --only one inside the nested if and one in the outside if

#36 write s simple ternary operator
x= 200
print('x > 100') if x > 100  else print(x)

'''
#37 in elif , python will check all the conditions no matter what ?
 : if condition elsif is true she will do it and get out the whole if function
'''

#38 in elif we use else for ... ? the last condition(if not any of the other if and elif is ture)

#39 if we have this list [2,4,6,8,10] :
#39-1 check to see if 4 in this list or not
list1 = [2,4,6,8,10]

if 4 in list1:
    print('found')

#39-2 check to see if 4 and 6 in this list on not
if 4 and 6 in list1:
    print('found')

#39-3 check to see if 3 or 6 in this list
if 3 or 6 in list1:
    print('found')

#39-4 check to see if 2 , 4 and 5 in this list
if 2 and 4 and 5 in list1:
    print('found12')
else:
    print('not found')
    
    
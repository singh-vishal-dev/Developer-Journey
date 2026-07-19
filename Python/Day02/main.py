#operators and type casting
# An operator is symbol that perforn a certain operation between operands
# 1. arithametic operator (+,-,*,/,//,%,**)
#example
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print("a+b:",a+b)
print("a-b:",a-b)
print("a*b:",a*b)
print("a/b:",a/b)
print("a//b:",a//b)
print("a%b:",a%b)
print("a**b:",a**b)

# 2. relational operator(==,!=,>,<,>=,<=)
#example
c=50
d=30
print(c==d) #false
print(c!=d) #true
print(c>=d)
print(c<=d)
print(c>d)

# 3. assignment operator(=,+=,-=,*=,/=,%=,**=)
#example
num= 10
num +=5
num2 = 20
num2 -= 5
print("add:",num,"sub:",num2)

#4.logical operator (not, and, or) it is work on boolean value
#example
e=10
f=20
print(not False)
print(not True)
print(not(e>f))
 
val1 = True
val2 = True
print( "and operator ",val1 and val2)
print("or operator",val1 or val2)

#type casting
#example
str1 = "27"
str1 = int(str1)
print(type(str1))
 
g = 5
g = str(g)
print(type(g)) 
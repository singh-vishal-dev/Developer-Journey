
#string- string is a data type that strore a sequence of characters.
#basic operation

# 1. concatination("hello"+"world"--->"helloworld")
#example
str01 = "vishal"
str02 = "singh"
final_str = str01+" "+str02
print(final_str)
print(len(final_str))

# 2.indexing(in indexing only access the index not manupulate)
#example
str03 = "sujay aman"
print(str03[5])
print(str03[6])

# 3. slicing- access the part of string.
#example
str04 = "vinaykumarmaurya"
print(str04[1:4]) #ina
print(str04[:4]) #vina
print(str04[0:15])
print(str04[0:len(str04)])
print(str04[-4:-1]) #ury
print(str04[-6:]) #maurya

# 4 string function 
#example 
str001 = "hello i am Vishal singh."
print(str001.endswith("gh.")) #return true is string ends with gh.
print(str001.capitalize()) #capitalizes first char
print(str001.replace("Vishal","aman"))#replace old vale 
print(str001.find("hello")) #return 1st index of 1st occurrer
print(str001.count("i")) 


#practice question 
# WAP to input user's first name & print its lenght.
name=input("name:")
print(len(name))

# WAP to find the occurrence of 's' in string.
str6=input("enter randomly any string :")
print(str6)
print("the numper of $ in this string are :",str6.count("$"))


#conditional statements------------------------------------------
#examples

#01 WAP to check weather a number is positive, negative, or zero.
num=int(input("enter any num:"))
if(num>0):
    print("the num is positive:")
elif(num<0):
    print("tne num is negative:")
else:
    print("the num is zero:")

#02 WAP to check whether a number even or odd.
a=int(input("enter any number:"))
if(a/2==0):
    print("the number is even")
else:
    print("the number is odd")

#03 WAP to check whether a person is eligible to vote based on age.
age=int(input("enter the age :"))
if(age<=18):
    print("not vote")
else:
    print("vote")

#04 WAP to check whether a student is pass or fail.
marks=int(input("marks obtained"))
mm= int(input("total marks"))
percentage=(marks/mm)*100
print("your percentage is :",percentage)
if(percentage>33):
    print("you are pass")
else:
    print("you are fail")    

#05 WAP to find the greather number bewtween two numbers.
num1=int(input("enter first num:"))
num2=int(input("enter second num:"))
if(num1>num2):
    print("num1 is greater")
else:
    print("num2 is greater")

#06 WAP to find thr greatest number among three numbers.
num01=int(input("enter 1st num:"))
num02=int(input("enter 2nd num:"))
num03=int(input("enter 3rd num:"))
if(num01>num02 and num01>num03):
    print(num01," is greather")
elif(num02>num01 and num02>num03):
    print(num02,"is greather")
else:
    print(num03,"is greather")

#07 WAP to calculate the grade of a student based on marks.
num001=int(input("enter your marks"))
if(num001>=90):
    grade="A"
elif(num001>=80 and num001<90):
    grade="B"
elif(num001>=70 and num001<80):
    grade="C" 
else:
    grade="D"
print("grade of the student is",grade)

#08 WAP to check whether a number is divisible by boths 5 and 11.
num002=int(input())
if(num002/5==0 or num002/11==0):
    print("the number is divisible by boths 5 and 11.")
else:
    print("the number is not divisible by boths 5 and 11. ")

#09 WAP to check whether a given year is a leap year.
year=int(input("enter year:"))
if (year%4==0):
    theyear="leap year"
else:
    theyear="not leap year"
print(theyear)

#10 WAP a program to check whether a character is a vowel or a consonant.
str=input("enter any character:")
if(str=="a","e","i","o","u"):
    print("this is vowel")
else:
    print("this is consonant")





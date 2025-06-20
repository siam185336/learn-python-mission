# Variable:-
        # Variable হলো কন্টেনার বা বাক্স যেখানে ডাটা রাখা হয়।

        # Variable এর নাম শুরু হতে হবে ইংরেজি অক্ষর বা আন্ডারস্কোর দিয়ে।
        # A variable can't start with an number/digit.
        # No while space is allowed in variable names.

        # EXAMPLE: my_variable, myVariable, _myvariable, my_variable1, myvariable1, _myvariable1 etc.

# Data Types:-
        # Data type হলো ডাটার ধরন। Python এ বিভিন্ন ধরনের ডাটা টাইপ আছে। যেমনঃ

        # 1. Integer (int): পূর্ণ সংখ্যা। যেমন: 1, 2, 3, -1, -2, -3 etc.
        # 2. Float: দশমিক সংখ্যা। যেমন: 1.5, 2.5, 3.5, -1.5, -2.5, -3.5 etc.
        # 3. String (str): টেক্সট বা অক্ষরের সমষ্টি। যেমন: "Hello", "World", "Python" etc. string সবসময় quotation এর মধ্যে লেখা হয়।
        # 4. Boolean (bool): সত্য বা মিথ্যা। যেমন: True, False.
        # 5. None: কোন মান নেই। এটি Python এর একটি বিশেষ ডাটা টাইপ। যেমন: None.

        # Python is a fantastic language that automatically identifies the type of data for us.

# Type Method:-
        # Python এ type() মেথড ব্যবহার করে আমরা কোন ভ্যারিয়েবলের ডাটা টাইপ জানতে পারি।

        # EXAMPLE:
name="Syfuddin"                                     # এটি একটি string টাইপের ভ্যারিয়েবল।
print(type(name))                                   # type() মেথড ব্যবহার করে ভ্যারিয়েবলের ডাটা টাইপ প্রিন্ট করা হয়েছে। এটি <class 'str'> রিটার্ন করবে।

age=22                                              # এটি একটি integer টাইপের ভ্যারিয়েবল।
print(type(age))                                    # type() মেথড ব্যবহার করে ভ্যারিয়েবলের ডাটা টাইপ প্রিন্ট করা হয়েছে। এটি <class 'int'> রিটার্ন করবে।

height=5.8                                          # এটি একটি float টাইপের ভ্যারিয়েবল।
print(type(height))                                 # type() মেথড ব্যবহার করে ভ্যারিয়েবলের ডাটা টাইপ প্রিন্ট করা হয়েছে। এটি <class 'float'> রিটার্ন করবে।

is_student=True                                     # এটি একটি boolean টাইপের ভ্যারিয়েবল।
print(type(is_student))                             # type() মেথড ব্যবহার করে ভ্যারিয়েবলের ডাটা টাইপ প্রিন্ট করা হয়েছে। এটি <class 'bool'> রিটার্ন করবে।

none_value=None                                     # এটি একটি None টাইপের ভ্যারিয়েবল।
print(type(none_value))                             # type() মেথড ব্যবহার করে ভ্যারিয়েবলের ডাটা টাইপ প্রিন্ট করা হয়েছে। এটি <class 'NoneType'> রিটার্ন করবে।

# Operators in Python:-
       # Following are some common operators in python:

       # (1). Arithmetic Operators (গানিতিক অপারেটর) : +, -, *, /, // (পূর্নসংখ্যা), %(ভাগশেষ), **(ঘাত) [(Addition, Subtraction, Multiplication, Division, Floor Division, Modulus, Exponentiation)]
       # EXAMPLE:
num1 =10
num2=4

print("Addition:", num1 + num2)                                # Addition.
print("Subtraction:", num1 - num2)                             # Subtraction.
print("Multiplication:", num1 * num2)                          # Multiplication.
print("Division:", num1 / num2)                                # Division.
print("Floor Division:", num1 // num2)                         # Floor Division.
print("Modulus:", num1 % num2)                                 # Modulus.
print("Exponentiation:", num1 ** num2)                         # Exponentiation.

print(f"Addition: {num1 + num2}")                              # f-string ব্যবহার করে Addition.
print(f"Subtraction: {num1 - num2}")                           # f-string ব্যবহার করে Subtraction.
print(f"Multiplication: {num1 * num2}")                        # f-string ব্যবহার করে Multiplication.
print(f"Division: {num1 / num2}")                              # f-string ব্যবহার করে Division.
print(f"Floor Division: {num1 // num2}")                       # f-string ব্যবহার করে Floor Division.
print(f"Modulus: {num1 % num2}")                               # f-string ব্যবহার করে Modulus.
print(f"Exponentiation: {num1 ** num2}")                       # f-string ব্যবহার করে Exponentiation.


       # (2). Comparison Operators (তুলনামূলক অপারেটর) : ==(সমান কিনা), !=(সমান নয় কিনা), >(বড় কিনা), <(ছোট কিনা), >=(বড় ও সমান কিনা), <=(ছোট ও সমান কিনা) [(Equal to, Not equal to, Greater than, Less than, Greater than or equal to, Less than or equal to)]

       # True & False এর মাধ্যমে output দেয়।
       
       # EXAMPLE:
dig1=10
dig2=4

print("Equal to:", dig1==dig2)                                  # Equal to.
print("Not Equal to:", dig1!=dig2)                              # Not Equal to.
print("Greater Than:", dig1>dig2)                               # Greater than.
print("Less Than:", dig1<dig2)                                  # Less than.
print("Greater than or equal to:", dig1>=dig2)                  # Greater than or equal to.
print("Less than or equal to:", dig1<=dig2)                     # Less than or equal to.

print(f"Equal to: {dig1==dig2}")                               # f-string ব্যবহার করে Equal to.
print(f"Not equal to: {dig1!=dig2}")                           # f-string ব্যবহার করে Not equal to.
print(f"Greater than: {dig1>dig2}")                            # f-string ব্যবহার করে Greater than.
print(f"Less than: {dig1<dig2}")                               # f-string ব্যবহার করে Less than.
print(f"Grater than or equal to: {dig1>=dig2}")                # f-string ব্যবহার করে Greater than or equal to.
print(f"Less than or equal to: {dig1<=dig2}")                  # f-string ব্যবহার করে Less than or equal to.

      # (3). Assignment Operators (নির্ধারন অপারেটর) : = (মান নির্ধারন), += (যোগ করে মান নির্ধারন), -= (বিয়োগ করে মান নির্ধারন), *= (গুন করে মান নির্ধারন), /= (ভাগ করে মান নির্ধারন), //= (পূর্নভাগ করে মান নির্ধারন), %= (ভাগশেষ করে মান নির্ধারন), **= (ঘাত করে মান নির্ধারন)

      # EXAMPLE:
x = 10
print("x =", x)                                                                           # x = 10

x += 5
print("x += 5:", x)                                                                       # x = 15

x -= 3
print("x -= 3:", x)                                                                       # x = 12

x *= 2
print("x *= 2:", x)                                                                       # x = 24

x /= 4
print("x /= 4:", x)                                                                       # x = 6.0

x %= 4
print("x %= 4:", x)                                                                       # x = 2.0

x **= 3
print("x **= 3:", x)                                                                      # x = 8.0

x //= 2
print("x //= 2:", x)                                                                      # x = 4.0

     # (4). Logical Operators (যোক্তীক অপারেটর) : and (দুটি সত্য হলে,true অন্যথায় false), or (যেকোন একটি সত্য হলে,true অন্যথায় false), not(সত্যকে মিথ্যা ও মিথ্যাকে সত্য বানায়)

     # True & False এর মাধ্যমে output দেয়।

     # EXAMPLE:
x = 10
print(x > 5 and x < 15)                                                             # True, কারণ দুইটি শর্তই সত্য।
print(x > 5 and x > 20)                                                             # False, কারণ দ্বিতীয় শর্তটি মিথ্যা।

print(x > 5 or x < 5)                                                               # True, কারণ প্রথম শর্তটি সত্য।
print(x > 15 or x < 5)                                                              # False, কারণ দুইটিই মিথ্যা।

print(not (x > 5))                                                                  # False, কারণ x > 5 হলো True, কিন্তু not করলে False.
print(not (x < 5))                                                                  # True, কারণ x < 5 হলো False, not করলে True.

# Input Funcation:-
     # Python এ users এর কাছ থেকে data নেওয়ার জন্য input function ব্যবহার করা হয়।

     # EXAMPLE:
a=input("Enter 1st number:")                   # এটি str টাইপ হবে। কারন input ফাংশন সমসময় string হিসেবেে আউটপুট দেয়।
b=input("Enter 2nd number:")                   # এটি str টাইপ হবে। কারন input ফাংশন সমসময় string হিসেবেে আউটপুট দেয়।

print("Number a is:",a)
print("Number b is:",b)
print("Sum is :",a+b)                     # এখানে যোগ করলে 1414 আসে কারন input function সবসময় string হিসেবেে আউটপুট দেয়। REPL করলে ভালোভাবে বুঝা যায়। এর সমাধান হলো ঃ

a=int(input("Enter 1st number:"))            # যদি input নাম্বার হয়, তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। তা না হলে string হিসেবে আউটপুট আসবে।
b=int(input("Enter 2nd number:"))            # যদি input নাম্বার হয়, তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। তা না হলে string হিসেবে আউটপুট আসবে।

print("Number a is:",a)
print("Number b is:",b)
print("Sum is :",a+b)


                                                                                 # PRATICE PROBLEM!
# PROBLEM 1: Write a python program to add two number?
# উওর:-
a=20
b=9

print("Sum is:", a+b)                          # সাধারন নিয়মে print করা হয়েছে।
print(f"Sum is {a+b}")                         #f-formate ব্যবহার করে print করা হয়েছে।

# PROBLEM 2: Write a python program to find reminder (ভাগশেষ) when a number is divided by b?
#উওর:-
a=int(input("Enter your 1st number:"))         # যদি input নাম্বার, হয় তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। কারন, input funcition সবসময় string হিসেবে output দেয়।
b=int(input("Enter your 2nd number:"))         # যদি input নাম্বার, হয় তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। কারন, input funcition সবসময় string হিসেবে output দেয়।

print("The remainder is:", a%b)                # সাধারন নিয়মে print করা হয়েছে।
print(f"The remainder is: {a%b}")              # f-string ব্যবহার করে print করা হয়েছে।

# PROBLEM 3: Check the type of the variable assigned using input() funcition?
#উওর:-
name=input("Enter your name:")
age=int(input("Enter your age:"))
height=float(input("Enter your height:"))
is_student=True
love=None

print(f"My name is {name} and I am {age} years old. I am a student. I am {height} feet tall. I don't have anyone to love.")                 # f-string ব্যবহার করে print করা হয়েছে।
print(type(name),type(age),type(height),type(is_student),type(love))

#PROBLEM 4: Use comparison operators to find out whether a given variable "a" is grater than "b" or not. a=34 and b=80.
#উওর:-
a=int(input("Enter the value of a:"))                                     # যদি input নাম্বার, হয় তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। কারন, input funcition সবসময় string হিসেবে output দেয়।
b=int(input("Enter the value of b:"))                                     # যদি input নাম্বার, হয় তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। কারন, input funcition সবসময় string হিসেবে output দেয়।

print(f"a থেকে b ছোট হলে True দিবে অন্যথায় False দিবে: {a>b}")             # f-string ব্যবহার করে print করা হয়েছে।

if a > b:
    print("b থেকে a বড়।")
else:
    print("a b থেকে ছোট।")

#PROBLEM 5: Write a python program to find avarage of two numbers entered by the user.
# উওর:-
a1=int(input("Enter your 1st value:"))                                    # যদি input নাম্বার, হয় তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। কারন, input funcition সবসময় string হিসেবে output দেয়।
b1=int(input("Enter your 2nd value:"))                                    # যদি input নাম্বার, হয় তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। কারন, input funcition সবসময় string হিসেবে output দেয়।

print("Here is your avarage calue:", (a1+b1)/2)                           # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print(f"Here is your avarage value: {(a1+b1)/2}")                         # f-string ব্যবহার করে print করা হয়েছে।

#PROBLEM 6: Write a python program to calculate square of a number entered by users.
# উওর:-
a2=int(input("Please sir tell me what is your 1st number:"))              # যদি input নাম্বার, হয় তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। কারন, input funcition সবসময় string হিসেবে output দেয়।
b2=int(input("Please sir tell me what is your 2nd number:"))              # যদি input নাম্বার, হয় তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে। কারন, input funcition সবসময় string হিসেবে output দেয়।

print("Here the value of square is given:",a2**b2)                        # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print(f"Here the value of square is given:{a2**b2}")                      # f-string ব্যবহার করে print করা হয়েছে।

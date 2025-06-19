# 1st program:-
print("Hello World")

# Module:-
import pyjokes  # Module pip এর সাহায্যে install করতে হয়।
joke= pyjokes.get_joke()  # pyjokes মডিউল থেকে get_joke() ফাংশন ব্যবহার করে একটি রেন্ডম জোক পাওয়া যাবে।
print(joke)

# Using python as a calculator:-
        # আমরা windows terminal এ গিয়ে python লিখে enter করলে পাইথন ইন্টারপ্রেটার চালু হবে। সেখানে আমরা পাইথন কোড লিখতে পারব,এবং পাইথন ক্যালকুলেটর হিসেবে কাজ করবে।

# Comments:-
        # Comments are used to explain the code and make it more readable. They are ignored by the Python interpreter.

# Print:-
        # Multi line print করতে হলে """ """/ ''' ''' ব্যাবহার করতে হয়।


                                                             # PRATICE PROBLEMS!

# PROBLEM 1:- Write Twinkle Twinkle, Twinkle, Little Star using print function.
#উওর:-
print("""Song Lyrics
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.""")

# PROBLEM 2:- Use REPL and print the table of 5 using it.
#উওর:-
     # Terminal এ গিয়ে python লিখে enter করলে পাইথন ইন্টারপ্রেটার চালু হবে। সেখানে আমরা ৫ এর টেবিল প্রিন্ট করতে পারি।

# PROBLEM 3:- Install an external module and use it to perform or operation of your interest.
#উওর:-
from joke.jokes import *  # This will import all joke-functions (geek, icanhazdad, chucknorris, icndb). Now you can use them to get some jokes.
for i in range(10):       # For example you can display 10 Chuck Norris jokes.
    print(chucknorris())  # Or get a random joke-function.
from random import choice
print(choice([geek, icanhazdad, chucknorris, icndb]))

# PROBLEM 4:- Write a python program to print the contents of a directory using os module.Search online for the function which does this.
#উওর:-
import os                                                                      # OS module import করে।
directory = "/"                                                                # Directory path সেট করে। এখানে "/" মানে root directory। আপনি আপনার পছন্দের ডিরেক্টরি path দিতে পারেন। যেমন: "c:/Users/YourUsername/Documents" অথবা "/home/yousername/documents"

try:
    contents = os.listdir(directory)                                           # os.listdir()	ডিরেক্টরির কনটেন্ট list আকারে রিটার্ন করে।
    print(f"Contents of directory '{directory}':")
    for item in contents:                                                      # for item in contents	প্রতিটি ফাইল বা ফোল্ডার প্রিন্ট করে।
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")                      # try/except	Error (যেমন path না থাকলে) হ্যান্ডল করে।
except PermissionError:
    print(f"You do not have permission to access '{directory}'.")

# PROBLEM5:- Learn the program written in problem 4 with comments.
#উওর:-
          # উপরের OS মডিউলে কমেন্ট ব্যাবহার করা হয়েছে।
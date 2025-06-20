# String:-
       # String is a datatype in python.
       # String হলো অক্ষর বা ক্যারেক্টারের একটি সিকুয়েন্স বা ধারাবাহিকতা,যা single, double or triple quotes এর মধ্যে লেখা হয়।
       # String একবার তৈরি হলে আর পরিবর্তন করা যায় না।
       # ‍String এর প্রতিটি ক্যারেক্টারের একটি নির্দিষ্ট পজিশন অর্থ্যাৎ INDEXING আছে।
       # ‍String slicing করা অর্থাৎ নির্দিষ্ট অংশ কেটে বের করা যায়।

       # Example:-
             # (1). Single quote string: 'Siam'
             # (2). Double quote string: "Siam"
             # (3). Triple quote string: """Siam"""
             # (4). Single triple quote string:'''Siam'''


# String Slicing:-
        # Slicing হলো string এর নির্দিষ্ট একটি অংশ কেটে বের করা।
        # 3rd bracket use করা হয়।

        # STRING VARIABLE [START:END]                       # Start: কোথা থেকে শুরো হবে index.
        # STRING-VARIABLE [START:END:STEP]                  # End: কোথায় শেষ হবে (এই ইনডেক্সটি ধরা হয় না।) # ‍Step: কয়টা করে লাফ দিয়ে অক্ষর নিবে (অপশনাল)

        # ইনডেক্স চার্ট (Posative and Negative):-
           # Text=Bangladesh::    B    A    N    G    L    A    D    E    S    H
           
           # Posative Indexing:   0    1    2    3    4    5    6    7    8    9         # Posative index শূন্য থেকে শুরু হয়।
           # Negative Indexing:  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1         # Negative index  -1 থেকে শুরু হয়।

        # Example:
text="Bangladesh"
text1="Programming"
text2="PythonProgramming"

print(text[0:5])                           # নির্দিষ্ট অংশ বের করে।
print(text[-5:-1])                         # Negative Slicing.
print(text[:4])                            # শুরু থেকে নির্দিষ্ট জায়গা পর্যন্ত বের করে।
print(text[5:])                            # নির্দিষ্ট জায়গা থেকে শেষ পর্যন্ত বের করে।
print(text[:])                             # সম্পূর্ন স্ট্রিং বের করে।
print(text[::2])                           # প্রতি ২ অক্ষর পর পর বের করে। REPAL করলে ভালোভাবে বুঝা যায়।
print(text[::-1])                          # উল্টো করে প্রিন্ট করা।
print(text1[:3] + text1[8:])               # স্ট্রিং এর মাঝ অংশ বাদ দিয়ে দুই প্রান্তের অংশ নেওয়া।
print(text1[1:-1])                         # ১ম ও শেষ character বাদ দিয়ে মাঝের অংশ নেওয়া।
print(text1[::-2])                         # বীপরিত ‍দিক থেকে প্রতি ২ অক্ষর পর পর নেও।
print(text2[6:16][::-1])                   # মাঝখানের অংশ উল্টানো।


# String Indexing:-
        # Indexing হলো String এর প্রতিটি অক্ষরের অবস্থান বের করা।
        # 3rd bracket use করা হয়।
        # সবকিছু slicing এর মতো। শুধু একটি করে মান দেয় যেমন:২,৩,৪ ইত্যাদি।

        # ইনডেক্স চার্ট (Posative and Negative):-
           # Text=Bangladesh::    B    A    N    G    L    A    D    E    S    H
           
           # Posative Indexing:   0    1    2    3    4    5    6    7    8    9         # Posative index শূন্য থেকে শুরু হয়।
           # Negative Indexing:  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1         # Negative index  -1 থেকে শুরু হয়।

# String Funcition:-
        # Here are some string funcition:

        # 1. len()----                                 #স্ট্রিং এর দৈর্ঘ্য জানায়।
        # 2. lower()--                                 #সব অক্ষর ছোট করে।
        # 3. upper()--                                 #সব অক্ষর বড় করে।
        # 4. strip()--                                 #দুই পাশের ফাকা যায়গা সরায়।
        # 5. replace(old,new)---                       #স্ট্রিং এর অংশ বদলায়।
        # 6. split(separator)--                        #স্ট্রিং এর তালিকা ভেঙে দেয়। string কে list বানায়। output 3rd bracket এ আসে।
        # 7. join(list)--                              #লিস্টকে স্ট্রিং বানায়।
        # 8. find(substring)--                         #substring কোথায় আছে (index দেয়)
        # 9. startswith()--                            #কোন স্ট্রিং দিয়ে শুরু হয়েছে কিনা।
        # 10. endswith()--                             #কোন স্ট্রিং দিয়ে শেষ হয়েছে কিনা।
        # 11. count()--                                #কয়বার substring এসেছে।
        # 12. capitilize()--                           #প্রথম অক্ষর বড় করে।
        # 13. title()--                                #প্রতিটি শব্দের প্রথম অক্ষর বড় করে।
        # 14. isdigite()--                             #শুধু সংখ্যা আছে কিনা।
        # 15. isalpha()--                              #শুধু অক্ষর আছে কিনা।
        # 16. isalnum()--                              #অক্ষর ও সংখ্যা আছে কিনা।
        # 17. islower()--                              #সব ছোট অক্ষর কিনা।
        # 18. isupper()--                              #সব বড় অক্ষর কিনা।

        # EXAMPLE:-
strip1="    Siam    "
replace1="Python"
split1="apple, banana, mango"
join1=["I", "am", "learning"]
count1="apple,banana,Orange"

print(strip1.strip())
print(replace1.replace("Python", "Java"))
print(split1.split(","))                         # এখানে double quote এর মধ্যে কমা (,) দেওয়া হয়েছে কারন string এ কমা (,) আছে। String যদি space দিয়ে লেখা হতো তাহলে double quote এ space আসত।
print(" ".join(join1))                           # এখানে space না দিলে output- Iamlearning আসত।
print(replace1.find("p"))                        # substring এর index দেয়।
# ৯,১০,১৪,১৫,১৬,১৭ ও ১৮ পর্যন্ত True and False এ output দেয়।
print(count1.count("a"))                         # String এ একটা শব্দ কতবার আছে তা দেখায়।

# ‍String Concatenation:-
        # দুই বা ততোধিক string একসাথে জুরে নতুন string তৈরি করে।
        # উদাহরন:-
    # ১. plus(+) দিয়ে কনক্যাটেশন।
first_name="Syfuddin"
last_name="Siam"
print(first_name,last_name)                   # কমা (,) দেওয়ার পরে space দেওয়া লাগে না কমা space এর মতো কাজ করে।
print(first_name+" "+last_name)               # Double quote এ space দিলে space আসবে, না দিলে output হবে syfuddinsiam.
print(f"{first_name} {last_name}")            # f-string ব্যাবহার করলে সবচেয়ে ভালো space এর কোন জামেলা নেই।

    # ২. variable এর সাথে string যোগ করা।
name="Siam"
print("Hello"+" "+ name + "!")
print("Hello", name,"!")                      # কমা(,) space এর মতো কাজ করে।    
print(f"Hello {name}!")

    # ৩. সংখ্যা যোগ করলে কি হয়?
age=20
   #    print("I am"+ age + "years old.")               ###### Error আসবে কারন, variable টা integer. শুধুমাএ string কে string এর সাথে ‍সংযুক্ত করতে পারে।
print("I am "+ str(age)+" years old")                # years এর আগে space না দিলে output আসতোঃ i am 20years old.
print(f"I am {age} years old")                       ### f-string এর মাধ্যমে integer কে string এর সাথে সংযুক্ত করা যায়।

# ৪. গুন চিহ্ন দিয়ে স্ট্রিং বার বার যোগ করা হয়।
tab="Hi!"
print(tab*3)

    # ৫. join() দিয়ে একাধিক string কনক্যাট।
words=["Python","is","fun."]                          # কমা(,) না দিলে list তৈরি হবে না এবং output এ space আসবে না।
sentence=" ".join(words)                              # ‍Double quote এ space না দিলে output এ space আসবে না।
print(sentence) 

# Escape Sequence Character:-
        # Escape Sequence হলো একটি \(ব্যাকস্ল্যাশ) দিয়ে শুরু হওয়া বিশেষ চিহ্ন যা সাধারনত ক্যারেক্টারের মতো ব্যাবহার হয় না-বরং বিশেষ কিছু কাজ করে।
        # Escape Sequence সবসময় string এর ভিতরে ব্যবহার হয়।

                # (১.) \n:- নতুন লাইন। 
                # (২.) \t:- একটি ট্যাব স্পেস।
                # (৩.) \\:- Backslash লেখতে।
                # (৪.) \':- একক কোটেশন লেখতে।
                # (৫.) \":- ডাবল কোটেশন লেখতে।
                # (৬.) \r:- লাইনের শুরুতে ফিরে যেতে (ক্যারেজ রির্টান)।
                # (৭.) \b:- Backspace (একটি অক্ষর delect করতে)।
                # (৮.) \f:- From feed (নতুন পৃষ্ঠা,কম ব্যাবহৃত)।
                # (৯.) \a:- বিপ ‍শব্দ তৈরি করে কিছু সিস্টেমে কাজ করে।
        #Example:-

print("Hello\nworld")
print("Name:\tSiam")
print("c:\\python")                                                          # একটি backslash (\) দিলেও হবে কারন double quote এর মধ্যে আছে।
print("It\'s Nice")
print("He said \"Hello\"")
print("Hello\rHi")
print("Hello\b")                                                            #Windows Command Prompt (CMD) বা PowerShell-এ রান করো: VS Code-এর পরিবর্তে নিচের মত Command Prompt-এ কোডটা চালাও: তাহলে সমস্যা সমাধান হয়ে যাবে এবং ০ ডিলিট হয়ে যাবে।
print("Hello\b!")
print("Hello\fWorld")
print("\a")                                                                 # কিছু সিস্টেমে beep sound দেয়।


                                                                                 # PRATICE PROBLEM!
# PROBLEM 1: Write a python program to display a user entered name followed by Good Afternoon using input() funcition?
# Answer:
name=input("Enter your name:")
print(f"Good Afternoon {name}")
print("Good Afternoon",name)                                                                                                   # এখানে কমা(,) space এর কাজ করছে।
print("Good Afternoon "+name)                                                                                                  # এখানে Afternoon এর পরে Space না দিলে output হতোঃ Good AfternoonSiam.

# PROBLEM 2: Write a python program to fill in a letter templet given below with name and date?
             # letter= '''Dear <|Name|>,                                                                                      #এটাও প্রশ্নর অংশ।
             # you are selected!                                                                                              #এটাও প্রশ্নর অংশ।
             # <|Date|>'''                                                                                                    #এটাও প্রশ্নর অংশ।
# Answer:
letter= '''Dear <|Name|>,
you are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Siam").replace("<|Date|>", "25 september,2025"))                                             # Replace method ব্যবহার করে নাম এবং ডেইট চেঞ্জ করা হয়েছে।

# PROBLEM 3: Write a program to detect double space in a string?
# Answer:
name="Siam is  a good  boy"
print(name.find("  "))                                                                                                        # এখানে প্রথম double space find করতে পারলেও 2nd double space পারে না। 2nd double space খুজে বের করার জন্য loop/ if-else funcition use করতে হবে।

# PROBLEM 4: Replace the double space from problem 3 with single space.
# Answer:
name="Siam is  a good  boy"
print(name.replace("  "," "))                                                                                                # Replace method ব্যবহার করে double space, single space এ পরিবর্তন করা হয়েছে।

# PROBLEM 5: Write a program to format the following letter using escape sequence character.
           # letter="Dear Siam, This python course is nice.Thanks!"                                                           #এটাও প্রশ্নর অংশ।
# Answer:
letter="Dear \"Siam\",\n\tThis python course is nice.\nThanks!"
print(letter)

import math
import string
from collections import Counter
import random

def distance_calc(a1 ,b1 ,a2 ,b2):
    d = math.sqrt((a2 -a1 )**2 + (b2 -b1 )**2)
    print(f"\nDistance: {d}")

def remove_similar(lst):
    uni_set = set()
    uni_set = uni_set.union(set(lst))
    print(list(uni_set))

def string_splitter(s1, s2):
    print(len(s1)//2)
    if len(s1) % 2 == 0:
        front1, back1 = s1[:len(s1)//2],s1[len(s1)//2:]
    else:
        front1, back1 = s1[:len(s1)//2+1], s1[len(s1)//2+1:]
    if len(s2) % 2 == 0:
        front2, back2 = s2[:len(s2)//2] , s2[len(s2)//2:]
    else:
        front2, back2 = s2[:len(s2)//2+1] , s2[len(s2)//2+1:]

    print(front1+front2+back1+back2)
def popular_words(file_name):
    words = open(file_name + '.txt').read().lower().split()
    words_count = Counter(words)
    most_occur = words_count.most_common(20)

    str = ''
    for word in most_occur:
        str += word[0]
        str += ' '

    return str

def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    newtext = ""

    for i in text:
        if i not in vowels:
            newtext += i
    print(newtext)

def find_indexes(str,c):
    indexes = [x for x, cl in enumerate(str) if cl == c]
    print(indexes)
# print("Problem 1")
# x1, y1, x2, y2 = map(float, input().split())
# distance_calc(x1 ,y1 ,x2 ,y2)
# #############################################################
# print("problem 2")
# lst=[]
# lst = [int(x) for x in input().split()]
# remove_similar(lst)
#############################################################
# print("problem 3")
# str1,str2 = map(str,input().split())
# string_splitter(str1,str2)
#############################################################
# print("Problem 4")
# file_name=input("enter file name")
# text=popular_words(file_name)
# f=open('popular_words','w')
# f.write(text)
################################################################
# print("problem 5")
# text = input("enter your string")
# remove_vowels(text)
################################################################
# print("problem 6")
# str=input("enter your string")
# c=input("enter character to find it's locations ")
# find_indexes(str,c)
##############################################################
print("bonus")
num = random.randint(0, 10)
user_tries=7
guessed_numbers=[]
play_again=1
content=open('result.txt','r').read().strip('[]').split(',')
games_count=int(content[0])
won_games=int(content[1])
lost_games=int(content[2])
print(games_count)
while play_again==1:
    games_count+=1
    user_tries=7
    lose_flag = False
    guessed_numbers.clear()
    while user_tries :
        print("user tries",user_tries)
        user_input = int(input('Enter Number: '))
        if user_input == num:
            won_games+=1
            lose_flag=True
            print('You won!')
            num=random.randint(0,10)
            guessed_numbers.clear()
        elif user_input>100:
            print("Number Out of range\n the number should be less than 100 ")
            continue
        elif user_input in guessed_numbers:
            print("you entered this number before")
            continue
        else:
            user_tries-=1
            guessed_numbers.append(user_input)
            print("your num is greater than the NUMBER") if user_input > num else print("your num is smaller than the Number")
            continue
    if lose_flag ==False:
        lost_games+=1
    play_again=int( input("Enter 1 if you wanna play again and 0 if to exit game"))
result=[games_count,won_games,lost_games]
result_file = open('result.txt','w')
result_file.write(str(result))
result_file.close()

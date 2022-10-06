# import random
#
# a = random.randint(1, 5)
# print(a)
# b = random.random() * 10
# print(b)
#
# list = ["hii", "hey", "hie", "heya"]
# choice = random.choice(list)
# print(choice)

# from emoji import emojize
#
# print(emojize(":grin:"))
#
# import emojis
#
# emojified = emojis.encode("There is a :elephant: in my boot !")
# print(emojified)
import emojis
import emoji
print(emoji.emojize(":winking_face_with_tongue:",use_aliases=True))
print(emoji.emojize(":winking_face:",use_aliases=True))
print(emoji.emojize(":kissing_heart:",use_aliases=True))
emojified=emojis.encode("love is :heart:!")
print(emojified)
print(emoji.demojize("😘"))
print(emoji.demojize("😉"))
print(emoji.demojize("😜"))
print(emoji.emojize(":face_blowing_a_kiss:",use_aliases=True))
emojified=emojis.encode("love is :face_blowing_a_kiss: !")
print(emojified)
print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))
print(emoji.emojize("I am :blue_heart:",variant="emoji_type"))
print(emoji.emojize("I am :kissing_smiling_eyes:",variant="emoji_type"))
print(emoji.emojize("I am :angry:",variant="emoji_type"))
print("\U0001F923")
print(emoji.demojize("🤣"))
print(emoji.emojize("I am :rolling_on_the_floor_laughing:",variant="emoji_type"))

#import antigravity


import sys
while True:
    print("type exit to exit")
    response=input()
    if response=="exit":
        print("Exiting the program")
        sys.exit()
        print("you typed",response)
#string concatenation (how to put strings together)
#suppose we want to create a string that says "subscribe to _"
# youtuber = "Kylie Ying"
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# (output -
# Adjective: amazing
# Verb: skydive
# Verb: jump
# Famous person: captain america)

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so exited all the time because \
  I love {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)
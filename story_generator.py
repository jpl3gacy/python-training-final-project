# MVP: Get User input and have a pre determined story print out

# class Character:
#     def __init__(self, name, age, feeling):
#         self.name = name
#         self.age = age
#         self.feeling = feeling

def age_story(name, age):
    if int(age) == 0:
        return "still not born! How are you even typing!!!\n" + name + " is 0 "
    else:
        return age


def storybuilder(name_pronoun, age, feeling):
    print(name_pronoun + " is " + age + " year(s) old and feels " + feeling)



name = input("What is your name?: ")
pronoun = input("What are your pronouns?: ")
name_pronoun = name + "(" + pronoun + ")"

age = input("How old are you?: ")
feeling = input("How are you feeling? (adj.): ")

storybuilder(name_pronoun, age_story(name, age), feeling)





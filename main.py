# import genanki
# # import pandas as pd
# modelID = 8
# # modelID should be random number hardcoded into myModel
# # deckID should be a random number hardcoded into myDeck
#
# myModel=genanki.Model(
#     modelID,
#     "DECK",
#     fields = [
#         {"name": "Question"},
#         {"name": "Answer"},
#             ],
#     templates = [
#         {"name": "Card 1",
#         "qfmt": "{{Question}}",
#         "afmt": "{{Frontside}}<hr id='answer'>{{Answer}}"}
#                 ])
#
#
# note=genanki.Note(
#     model=myModel,
#     fields = ["Amber", "Alaska"]
# )
#
#
# def gen_cards(n):
#     deck=[]
#     data = [
#             ["hello", "answer"],
#             ["fill_in_blank", "answer"]
#             ]
#     for i in range(0,n):
#         card = Card(data)
#         deck += []
#     return deck


sheet= [['Front', 'Back', 'Cloze1', 'Cloze2', '', 'Image1', 'Image2'],
        ['Q1', 'No', 'This', 'Is', 'Patrick'],
        ['Q2', '', 'Yes'],
        ['Q3', 'No', 'Cloze'],
        ['Q4', '', 'Break1'],
        ['Q5', '', '', 'Break2'],
        ['', 'Break3'],
        ['', '', 'Break4'],
        [],
        ['Check Q', 'Check A', 'Check C1', '', '', 'Break']
    ]






# class Card:
#     """
#     Card class inputs ______ returns array len 3 containing question, answer
#
#     """
#
#     def __init__(self, data):
#         self.front = data[0]
#         self.back = self.type(data[1])
#         if self.back == "cloze":
#             self.front = self.cloze(data)
#         self.extras = None
#
#     def type(self, back):
#         '''
#         Determine if a card is a simple one or a cloze card.
#         Returns cloze or standard depending on the contents of the back field.
#         '''
#         if "cloze" in back.lower():
#             return "cloze"
#         return "standard"
#
#     def __repr__(self):
#         return self.front
#
#     def __iter__(self):
#         return itty(self)
#
#     def itty(self):
#
#
#
#     def cloze(self, data):
#         '''
#         should be called if data[1]=="cloze"
#         "string STRING string c1 string c2"
#         return a card
#
#         update for new data frame setup
#         '''
#         cloze_count = 2
#         ret = ""
#         # for n in data[0][1:-1]:
#         # look for numbers if number is found check if it's immediately preceded by "c". Should not be double digit clozes lol wtf
#
#         for n in range(1, len(data[0])):
#             # Check if  start of cloze statement
#             if data[0][n].isnumeric() and data[0][n - 1].lower() is "c":
#                 # First cloze
#                 if ret == "":
#                     ret = data[0][0:n - 1] + data[2]  # call cloze formatter
#                 # Subsequent clozes
#                 else:
#                     ret = ret[0:-1] + data[cloze_count]
#                 cloze_count += 1
#             # Normal chars
#             else:
#                 ret += data[0][n]
#         return ret
#
#     def cloze_it(self, string, replace="..."):
#         '''
#         Formats cloze statements
#         Always with cloze number 1
#         Default replacement is ..., can be changed with an arguement.
#         '''
#         ret = f'{{c1:: {string}::{replace}}}'
#         return ret
#
#
# class CardIter:
#     def __init__(self, card):
#         self._card = card
#         self._index = 0
#
#     def __next__(self):
#         if self._index < len()




"""
use this data frame structure.
df=
[[front, back (or cloze), [cloze 1|replace], [cloze 2, replace]...
]

make count default to 1 

def cloze(data):
    count = 1
    remove used clozes

"""



def cloze(data):
    '''
    should be called if data[1]=="cloze"
    "string STRING string c1 string c2"
    return a card

    update for new data frame setup
    '''
    cloze_count=2
    ret = ""
    # for n in data[0][1:-1]:
    #look for numbers if number is found check if it's immediately preceded by "c". Should not be double digit clozes lol wtf
    print(data)
    c = ["c", "C"]
    for n in range(1, len(data[0])):
        # Check if  start of cloze statement
        if data[0][n].isnumeric() and data[0][n-1] in c:
            # First cloze
            if ret == "":
                ret = data[0][0:n-1] + cloze_it(data[2]) # Calls the cloze formatter
                                                        # Future: pass the index of data[cloze] to get c2 and stuff
            # Subsequent clozes
            else:
                ret = ret[0:-1] + cloze_it(data[cloze_count])
            cloze_count+=1
        # Normal chars
        else:
            ret += data[0][n]
    print("cloze count:", cloze_count)
    return ret


def cloze_it(string, rep="..."):
    '''
    Formats cloze statements
    Always with cloze number 1
    Default replacement is ..., can be changed with an indicator in string.

    "cloze statement|replacement" -> "cn::cloze statement::replacement"
    '''
    if "|" in string:
        rep, string = string.split("|")[1], string.split("|")[0]
        if rep[0] == " ": # Remove unnecessary extra space
            rep = rep[1:]

    ret = f'{{c1::{string}::{rep}}}'
    return ret








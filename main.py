import genanki
# import pandas as pd
modelID = 8
# modelID should be random number hardcoded into myModel
# deckID should be a random number hardcoded into myDeck


df = [
    ['Front', 'back'],
    [],
    [],

]

myModel=genanki.Model(
    modelID,
    "DECK",
    fields = [
        {"name": "Question"},
        {"name": "Answer"},
            ],
    templates = [
        {"name": "Card 1",
        "qfmt": "{{Question}}",
        "afmt": "{{Frontside}}<hr id='answer'>{{Answer}}"}
                ])


note=genanki.Note(
    model=myModel,
    fields = ["Amber", "Alaska"]
)


def gen_cards(n):
    deck=[]
    data = [
            ["hello", "answer"],
            ["fill_in_blank", "answer"]
            ]
    for i in range(0,n):
        card = Card(data)
        deck += []
    return deck

class Card:
    """
    Card class inputs ______ returns array len 3 containing question, answer

    """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.type = self.type(self.question)

    def type(self):
        if "_" in self.question:
            return "fill_blank"
        return "simple"

    def format(self):
        cloze = 1


    pass

file = "filename"

arr = []


"""
use this data frame structure.
df=
[[front, back (or cloze), [cloze 1, replace], [cloze 2, replace]...
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
                ret = data[0][0:n-1] + data[2] # call cloze formatter
            # Subsequent clozes
            else:
                ret = ret[0:-1] + data[cloze_count]
            cloze_count+=1
        # Normal chars
        else:
            ret += data[0][n]
    print("cloze count:", cloze_count)
    return ret


def cloze_it(string, replace="..."):
    '''
    Formats cloze statements
    Always with cloze number 1
    Default replacement is ..., can be changed with an arguement.
    '''
    ret = f'{{c1:: {string}::{replace}}}'
    return ret
print(cloze_it("hi", "poop"),
cloze_it("hi", "help"),
cloze_it("hi"))



dat = ["1 string c 23 string c1 string c2 c3", "clozeeee", "CLOZE1", "aMERICA", "Georgetown"]
# print(cloze(dat))

























def read_from_csv(filename):
    xl = pd.ExcelFile(filename)



    pass





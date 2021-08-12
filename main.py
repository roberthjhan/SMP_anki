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





def cloze(data):
    '''
    "string STRING string c1 string c2"
    return a card
    '''
    cloze_count=1
    ret = ""
    # for n in data[0][1:-1]:
    #look for numbers if number is found check if it's immediately preceded by "c". Should not be double digit clozes lol wtf
    for n in range(1, len(data)-1):
        print(n)
        if int(data[0][n]):
            if ret == "":
                ret = data[0][n-1] + data[cloze_count+1] + data[0][n+1]
            else:
                ret = ret[0:n]+ data[cloze_count] + ret[n:]
            cloze_count+=1
    return ret


dat = ["1 string STRING c 23 string c1 string c2", "cloze", "CLOZE1", "aMERICA"]
print(cloze(dat))

























def read_from_csv(filename):
    xl = pd.ExcelFile(filename)



    pass





import genanki
import pandas as pd
modelID = 8
# modelID should be random number hardcoded into myModel
# deckID should be a random number hardcoded into myDeck




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

































def read_from_csv(filename):
    xl = pd.ExcelFile(filename)



    pass





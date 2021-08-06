
import genanki
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



class Card:
    """
    Card class inputs ______ returns array len 3 containing question, answer

    """

    def __init__(self):
        self.question = str
        self.answer = str
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








































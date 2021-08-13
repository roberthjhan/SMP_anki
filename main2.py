
'''
need way to skip existing cards

'''



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



def check_cloze(data):
        if "cloze" in data[1].lower():
                return True
        return False


if check_cloze(data = None):
        pass
# call cloze function


"""
main
- import data from sheets
- define the anki pieces
- start building cards
-- iterate sheet
- 


- upload decks to google drive




"""
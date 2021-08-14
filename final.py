from quickstart import *
from helpers import *
from anki_boi import *
import genanki


# Set up decks for Block 1
anatomy = genanki.Deck(int, "Anatomy")
biochem = genanki.Deck(int, "Biochemistry")
embryology = genanki.Deck(int, "Embryology")
histology = genanki.Deck(int, "Histology")
physiology = genanki.Deck(int, "Physiology")


# Request sheet from google sheets API
sheet = get_sheet()
print(sheet)

for row in sheet[1]:
    tags = row[4]
    # I need to make this part cooler... This is really dumb
    if "anat" in tags.lower():
        deck = anatomy
        pass
    elif "bioc" in tags.lower():
        deck = biochem
        pass
    elif "embry" in tags.lower():
        deck = embryology
        pass
    elif "hist" in tags.lower():
        deck = histology
        pass
    elif "physio" in tags.lower():
        deck = physiology
        pass
    else: # Make a sick error class for this
        print("Wtf is this shit bro", tags)
        exit()







# Export decks as .apkg files
def export():
    genanki.Package(histology).write_to_file('Histology.apkg')
    genanki.Package(biochem).write_to_file('Biochemistry.apkg')
    genanki.Package(physiology).write_to_file('Physiology.apkg')
    genanki.Package(anatomy).write_to_file('Anatomy.apkg')
# Upload to google drive







for row in sheet[1:]:
    if check_cloze(row):





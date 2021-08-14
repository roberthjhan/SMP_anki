from quickstart import *
from helpers import *
from anki_boi import basic_model, cloze_model
import genanki
import os


# Set up decks for Block 1
anatomy = genanki.Deck(3894355937, "Anatomy")
biochem = genanki.Deck(4373484538, "Biochemistry")
embryology = genanki.Deck(769030955, "Embryology")
histology = genanki.Deck(3792015712, "Histology")
physiology = genanki.Deck(6735817679, "Physiology")


# Request sheet from google sheets API
sheet = get_sheet()


# Export decks as .apkg files
def export():
    genanki.Package(histology).write_to_file('Histology.apkg')
    genanki.Package(biochem).write_to_file('Biochemistry.apkg')
    genanki.Package(physiology).write_to_file('Physiology.apkg')
    genanki.Package(anatomy).write_to_file('Anatomy.apkg')

# Upload to google drive
def upload(filelist):
    for file in filelist:
        pass


for row in sheet[1:]:
    while len(row)< len(sheet[0]):
        row.append("")
    tags = row[4]
    # I need to make this part cooler... This is really dumb
    print(row)
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

    if check_cloze(row):
        row = cloze(row)
        my_note = genanki.Note(
            model= cloze_model,
            fields=[row[0], row[3]],# Front, Extra, (, card[6]))Images
            tags= row[5].replace(" ", "").split(","))
    else:
        my_note = genanki.Note(
            model=basic_model,
            fields=[row[0], row[1], row[6]], # Front, back, Images
            tags= row[5].replace(" ", "").split(","))
    deck.add_note(my_note)

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'Block 1 Anki')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

export()











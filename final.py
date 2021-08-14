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
basic_model = genanki.Model(
      model_id = 5168282460,
      name = 'Basic',
      fields = [
            {'name': 'Front'},
            {'name': 'Back'},
            {'name': "Image"}],
      templates = [
            {
              'name': 'Basic Card',
              'qfmt': '{{Front}}',
              'afmt': '{{FrontSide}}<hr id="back">{{Back}}<br>{{Image}}<br>',
            },
      ],
    css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n')

cloze_model = genanki.Model(
      8922529321,
      'Cloze (genanki)',
      model_type=genanki.Model.CLOZE,
      fields=[
              {'name': 'Text'},
              {'name': "Extra"}
            ],
      templates=[
                {
                  'name': 'Cloze',
                  'qfmt': '{{cloze:Text}}',
                  'afmt': '{{cloze:Text}}<br>{{Extra}}<br id="extra">',
                }
                ],
      css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n\n'
          '.cloze {\n font-weight: bold;\n color: blue;\n}\n.nightMode .cloze {\n color: lightblue;\n}'
        )
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

    if check_cloze(row):
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


# Export decks as .apkg files
def export():
    genanki.Package(histology).write_to_file('Histology.apkg')
    genanki.Package(biochem).write_to_file('Biochemistry.apkg')
    genanki.Package(physiology).write_to_file('Physiology.apkg')
    genanki.Package(anatomy).write_to_file('Anatomy.apkg')
# Upload to google drive










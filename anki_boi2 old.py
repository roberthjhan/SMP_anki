import genanki

"""
Contains card models made with genanki


# Generate random 10-digit ID
import random
random.randint(0, 10000000000)
"""



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
css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n'
)

# cloze_model = genanki.CLOZE_MODEL(
#   # Cloze only needs front
#   model_id = 5475291651,
#   name = 'Cloze',
#   model_type = genanki.Model.CLOZE,
#   fields=[
#     {'name': 'Text'},
#     {'name': "Extra"}],
#   templates=[
#     {'name': 'Cloze Card',
#      'qfmt': '{{cloze:Text}}',
#      'afmt': '{{cloze:Text}}<hr>{{cloze:Extra}}<hr id="extra">',
#      },
#   ]
# )
cloze_model = genanki.Model(
  8922529321,
  'Cloze (genanki)',
  model_type=genanki.Model.CLOZE,
  fields=[
      {'name': 'Text'},
      {'name': "Extra"}],
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

# my_deck = genanki.Deck(
#   2059400190,
#   'test')

# def test_cloze_old(data):
#   for card in data:
#     print(card[0])
#     if "cloze" in card[1].lower():
#       my_note = genanki.Note(
#         model= cloze_model,
#         fields=[card[0], card[3]],# Front, Extra, (, card[6]))Images
#         tags= card[5].replace(" ", "").split(","))
#     else:
#       my_note = genanki.Note(
#         model=basic_model,
#         fields=[card[0], card[1], card[6]], # Front, back, Images
#         tags= card[5].replace(" ", "").split(","))
#     my_deck.add_note(my_note)
#
# cloze_data = [
# ["nothisispatrick.png", "peepeepoopoo", "", "", "DECK", "bio, poopoo, peepee", "IMAGES"],
# ["welcometothe krustycrab.png", "peepeepoopoo", "", "", "DECK", "bio, poopoo, peepee", "IMAGES"],
# ['Meedial: {{c1::to midline::...}}\nLateral: {{c1::to midline::...}}', 'cloze', '', '', 'DECK', 'anatomy, poopoo, peepee', 'IMAGES'],
# ['weefwefwe: {{c1::to qweqweqw::...}}\nLatefwefral: {{c1::to qweqweqw::...}}', 'cloze', '', '', 'DECK', 'anatomy, poopoo, peepee', 'IMAGES']
# ]
#
#
# test_cloze(cloze_data)
#
# # Export for anki
# genanki.Package(my_deck).write_to_file('test.apkg')
basic_model_old = genanki.Model(
  model_id = 9954356041,
  name = 'Basic',
  fields = [
    {'name': 'Front'},
    {'name': 'Back'},
    {'name': "Image"},
    {'name': "Tags"}],
  templates = [
    {
      'name': 'Basic Card',
      'qfmt': '{{Front}}',
      'afmt': '{{FrontSide}}<hr id="back">{{Back}}{{Image}}{{Tags}}',
    },
  ])
my_deck = genanki.Deck(
  2059400110,
  'test')

# my_note = genanki.Note(
#   model=my_model,
#   fields=['Capital of Argentina', 'Buenos Aires'],
#   tags=["tag1", "another_tag"]
# )

def test_cloze(data):
  for card in data:
    print(card[0])
    if "cloze" in card[1].lower():
      my_note = genanki.Note(
        model= cloze_model,
        fields=[card[0], card[3], card[6], card[5].replace(" ", "")])# Front, Extra, Images, Tags
        #tags= card[5].replace(" ", "").split(","))
    else:
      my_note = genanki.Note(
        model=basic_model,
        fields=[card[0], card[1], card[6], card[5].replace(" ", "")]) # Front, back, Images, Tags,
        # tags= card[5].replace(" ", "").split(","))
    my_deck.add_note(my_note)

cloze_data = [
["Medial: c1\nLateral: c1", "cloze", ["to midline", "away from midline"], "", "DECK", "anatomy, poopoo, peepee", "IMAGES"],
["wefwefwe: c1\nLatefwefral: c1", "cloze", ["to qweqweqw", "qw qweqweqw midlfffine"], "", "DECK", "anatomy, poopoo, peepee", "IMAGES"],
["nothisispatrick.png", "peepeepoopoo", "", "", "DECK", "bio, poopoo, peepee", "IMAGES"]
]
for i in cloze_data:
  print(len(i))

test_cloze(cloze_data)

# Export for anki
genanki.Package(my_deck).write_to_file('test.apkg')
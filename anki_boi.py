import genanki

"""
Contains card models made with genanki


# Generate random 10-digit ID
import random
random.randint(0, 10000000000)
"""



basic_model = genanki.Model(
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

cloze_model = genanki.Model(
  # Cloze only needs front
  model_id = 7312002106,
  name = 'Cloze',
  model_type = genanki.Model.CLOZE,
  fields=[
    {'name': 'Front'},
    {'name': "Extra"},
    {'name': "Image"},
    {'name': "Tags"}],
  templates=[
    {'name': 'Cloze Card',
     'qfmt': '{{cloze:Front}}<hr>{{cloze:Front}}',
     'afmt': '{{cloze:Extra}}<hr>{{cloze:Extra}}<hr id="extra">{{Image}}{{Tags}}',
     },
  ],
)


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
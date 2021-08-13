import genanki
'''
creds: kerrickstaley (genanki author)
https://github.com/kerrickstaley/genanki

TODO:
- anki select deck
- cloze cards are currently input as normal cards


NOTES:
- Adding cards doesnt delete old ones
- Updating a card in a master file will not update it in anki. The updated card will be added as a new card.
- Importing existing cards does not seem to overwrite the original in terms of learning data.
'''



#make anki decks

histology = genanki.Deck(int, "Histology")
biochem = genanki.Deck(int, "Biochemistry")
physiology = genanki.Deck(int, "Physiology")
anatomy = genanki.Deck(int, "Anatomy")

my_deck = genanki.Deck(
  2059400110,
  'test')

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

arr =[
  ["Front", "UPDATE"],
  ["1", "2"],
  ["3", "4"],
  ["empty test", "none"],
  ["cloze test", "hello my {{c1::friend::...}}"],
  ]

arr2 =[
  ["Fuck", "Bitches"],
  ["Get", "Money"],
  ["Peepee", "Poopoo"],
  ["empty test", "none"],
  ["cloze test", "hello my {{c1::friend::...}}"],
  ]

cloze_data= [["cloze test", "hello my {{c1::friend::...}}"],
             ["cloze test improper cloze1", "hello my {{1::friend::...}}"],
             ["cloze test improper cloze2", "hello my {{c1:friend::...}}"],
             ["cloze test improper cloze3", "hello my {{c::friend::...}}"],
              ["cloze test improper cloze4", "hello my {{c1::friend:...}}"],
             ]


my_model = genanki.Model(
  model_id = 1607392319,
  name = 'Simple Model',
  fields = [
    {'name': 'Front'},
    {'name': 'Back'}],
  templates = [
    {
      'name': 'Card 1',
      'qfmt': '{{Front}}',
      'afmt': '{{FrontSide}}<hr id="back">{{Back}}',
    },
  ])

cloze_model = genanki.Model(
  # cloze only needs front
  model_id = 2607392319,
  name = 'Cloze',
  model_type = genanki.Model.CLOZE,
  fields=[
    {'name': 'TextA'},
    {'name': "TextB"},
    {'name': "Extra"}],
  templates=[
    {'name': 'Cloze',
     'qfmt': '{{cloze:TextA}}<hr>{{cloze:TextB}}',
     'afmt': '{{cloze:TextA}}<hr>{{cloze:TextB}}<hr id="extra">{{Extra}}',
     },
  ],
)



# for card in arr2:
#   print(card)
#   my_note = genanki.Note(
#     model= my_model,
#     fields=[card[0], card[1]])
#   my_deck.add_note(my_note)


def test_cloze(data):
  for card in data:
    # print(card)
    my_note = genanki.Note(
      model= cloze_model,
      fields=[card[1], "None", "None"])
    my_deck.add_note(my_note)

test_cloze(cloze_data)

print(my_deck.notes)

# Export for anki
genanki.Package(my_deck).write_to_file('test.apkg')


def export(filelist):
    genanki.Package(histology).write_to_file('Histology.apkg')
    genanki.Package(biochem).write_to_file('Biochemistry.apkg')
    genanki.Package(physiology).write_to_file('Physiology.apkg')
    genanki.Package(anatomy).write_to_file('Anatomy.apkg')




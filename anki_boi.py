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
# cloze_model = genanki.Model(
#   # Cloze only needs front
#   model_id = 7312002106,
#   name = 'Cloze',
#   model_type = genanki.Model.CLOZE,
#   fields=[
#     {'name': 'Front'},
#     {'name': "Extra"},
#     {'name': "Image"},
#     {'name': "Tags"}],
#   templates=[
#     {'name': 'Cloze Card',
#      'qfmt': '{{cloze:Front}}<hr>{{cloze:Front}}',
#      'afmt': '{{cloze:Extra}}<hr>{{cloze:Extra}}<hr id="extra">{{Image}}{{Tags}}',
#      },
#   ],)



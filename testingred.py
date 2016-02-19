import requests
from lxml import html
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

auth_token = "farts"

client = EvernoteClient(token=auth_token, sandbox=True)

page = requests.get("http://www.jamieoliver.com/recipes/eggs-recipes/protein-pancakes/")
#page = requests.get("http://www.jamieoliver.com/recipes/vegetables-recipes/veggie-chilli/#vii0ZEWtgBcAe4vd.97")

tree = html.fromstring(page.content)

note_store = client.get_note_store()


#ingredients = tree.xpath('//ul[@class="ingred-list"]/li')
ingredients = [li.xpath('normalize-space(.)') for li in tree.xpath('//ul[@class="ingred-list"]/li')]
#ingredients = tree.xpath('//ul[@class="ingred-list"]/li/text()')

for item in ingredients:
    print item

note = Types.Note()

note.title = "Shopping List - TESTING"
note.content = '<?xml version="1.0" encoding="UTF-8"?>'
note.content += '<!DOCTYPE en-note SYSTEM ' \
'"http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Ingredients:'
for item in ingredients:
    note.content += item + "<br/>"
note.content += '</en-note>'

created_note = note_store.createNote(note)

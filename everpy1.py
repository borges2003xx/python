from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStore
import portachiavi

from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder


dev_token=portachiavi.dev_token

dev_token = "S=s1:U=91985:E=157f6e161c6:C=1509f3034a0:P=1cd:A=en-devtoken:V=2:H=936c3aed4d5f4738e7d2b70ba0d31981"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
    print n.name


#note = Types.Note()
#note.title = "I'm a test note!"
#note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
#note.content += '<en-note>Hello, world!</en-note>'
#note = noteStore.createNote(note)

#noteStore = client.get_note_store()
#notebook = Types.Notebook()
#notebook.name = "My Notebook"
#notebook = noteStore.createNotebook(notebook)
#print notebook.guid



client = EvernoteClient(token=dev_token)
note_store = client.get_note_store()

note_filter = NoteStore.NoteFilter()
note_filter.words = 'intitle:"test"'
notes_metadata_result_spec = NoteStore.NotesMetadataResultSpec()

notes_metadata_list = note_store.findNotesMetadata(note_filter, 0, 1, notes_metadata_result_spec)
note_guid = notes_metadata_list.notes[0].guid
note = note_store.getNote(note_guid, True, False, False, False)

print note



auth_token = 'your-token'
client = EvernoteClient(token=dev_token)
note_store = client.get_note_store()

updated_filter = NoteFilter(order=NoteSortOrder.UPDATED)
offset = 0
max_notes = 10
result_spec = NotesMetadataResultSpec(includeTitle=True)
result_list = note_store.findNotesMetadata(dev_token, updated_filter, offset, max_notes, result_spec)

# note is an instance of NoteMetadata
# result_list is an instance of NotesMetadataList
for note in result_list.notes:
    print note.title


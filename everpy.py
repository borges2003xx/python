from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStore
import portachiavi
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder


developer_token = portachiavi.dev_token

# Set up the NoteStore client 
client = EvernoteClient(token=developer_token)
note_store = client.get_note_store()
 
# Make API calls
notebooks = note_store.listNotebooks()
for notebook in notebooks:
    print "Notebook: ", notebook.name

userStore = client.get_user_store()
user = userStore.getUser()
print user.username

noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
    print n.name



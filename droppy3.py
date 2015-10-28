# Include the Dropbox SDK
import dropbox
import portachiavi

# Get your app key and secret from the Dropbox developer website
app_key = portachiavi.drop_app_key
app_secret = portachiavi.drop_app_secret

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()


client = dropbox.client.DropboxClient(portachiavi.drop_code)
print 'linked account: ', client.account_info()

f = open('working-draft.txt', 'rb')
response = client.put_file('/magnum-opus.txt', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.txt', 'wb')
out.write(f.read())
out.close()
print metadata

import pocket
import portachiavi
api = pocket.Api(consumer_key=portachiavi.pocket_consumer_key,access_token=portachiavi.pocket_access_token)
items_list = api.get()
for item in items_list:
         print "%s (%s)" % (item.title, item.resolved_url)

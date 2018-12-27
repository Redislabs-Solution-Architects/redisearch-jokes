import json
from redisearch import Client, TextField, TagField

with open('wocka.json', 'r') as f:
    jokes = json.load(f)

hostname = 'redis-17235.laurent.cs.redislabs.com'
port = 17235


client = Client('jokes', hostname, port)
client.create_index((TextField('title'), TextField('body'), TextField('category'), TagField('label')))

for joke in jokes:
    client.add_document(joke['id'], title=joke['title'], body=joke['body'], category=joke['category'],
                        label=joke['category'])


print("number of jokes in the json file: " + str(len(jokes)))


info = client.info()
print(info)

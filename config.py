import pymongo
import certifi

connection_string = "mongodb+srv://FortuneCookie14:FSDI107Ch54@fsdi-107.z4ooh.mongodb.net/?retryWrites=true&w=majority&appName=FSDI-107"

client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())

db = client.get_database("organika")
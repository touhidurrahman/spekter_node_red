from pymongo import MongoClient

# Replace the uri string with your MongoDB deployment's connection string.
client = MongoClient("mongodb+srv://spekterbangla:bPbpqQtXGUh8sQc1@cluster0.ujhky.mongodb.net/atlashub-prod-clone?retryWrites=true&w=majority")

# Replace 'your_database' and 'your_collection' with your database and collection names
db = client.kommdigital
collection = db.temp_sensor

# Find the document with the maximum value of temp_DS18B20
max_temp_document = collection.find_one(
    {},
    sort=[("data.uv", -1)]
)

# Extract the maximum temp_DS18B20 value
if max_temp_document:
    max_temp_value = max_temp_document["data"]["uv"]
    print(f"The maximum value is: {max_temp_value}")
else:
    print("No documents found.")



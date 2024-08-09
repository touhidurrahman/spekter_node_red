from pymongo import MongoClient

# Replace the uri string with your MongoDB deployment's connection string.
client = MongoClient("mongodb+srv://spekterbangla:bPbpqQtXGUh8sQc1@cluster0.ujhky.mongodb.net/atlashub-prod-clone?retryWrites=true&w=majority")

# Replace 'your_database' and 'your_collection' with your database and collection names
db = client.kommdigital
collection = db.soil_sensor

# Use the distinct method to get unique values of temp_DS18B20
distinct_temp_values = collection.distinct("data.temp_DS18B20")

print(distinct_temp_values)

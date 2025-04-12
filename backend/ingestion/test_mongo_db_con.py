from mongo_client import client, db, collection

def test_connection():
    # List of databases
    try:
        db_names = client.list_database_names()
        print("Databases:", db_names)

        #List of collections in the database 
        collection_names = db.list_collection_names()
        print("Collections:", collection_names)


        # Insert a test document into the collection
        test_doc = {"test": "mongo_db_con", "value": 1}
        result = collection.insert_one(test_doc)
        print("Inserted document:", result.inserted_id)

        #Fetch the inserted document
        fetched_doc = collection.find_one({"_id": result.inserted_id})
        print("Fetched document:", fetched_doc)

    except Exception as e:
        print("Error listing databases:", e)
        return
   
if __name__ == "__main__":
    test_connection()
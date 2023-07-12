import pandas as pd
from datetime import datetime
import pymongo


def export_csv(data):
    print("Creating CSV ...")
    df = pd.DataFrame(data)
    csv_file = "products_{}.csv".format(datetime.now().date())
    df.to_csv(csv_file, index=False)
    print("Done !!!")
    return True




def save_to_mongo(data):
    try:
        with pymongo.MongoClient("mongodb://localhost:27017/") as client:
            db = client["DB"]
            products = db["products"]
            products.insert_many(data)
        print("Data inserted successfully.")
    except pymongo.errors.ConnectionError:
        print("Failed to connect to MongoDB.")
    except pymongo.errors.PyMongoError as e:
        print("An error occurred:", e)

    
    
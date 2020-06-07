import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborly-from-raj:HrqKdTYrgVEMjl2JDxGEjYWsqv5rOTR8BSViWI483g83WHFseKRIOU46CuDQFVU9QknHaEHtfudObFRUXB9xeA==@neighborly-from-raj.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-from-raj@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['neighborlydb']
            collection = database['advertisements']
            
            # query = {'_id': ObjectId(id)} # THIS LINE OF CODE IS NOT WORKING SO COMMENTING IT OUT
            query = {'_id': id}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)

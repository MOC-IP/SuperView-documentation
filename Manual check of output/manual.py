from pymongo import MongoClient
from datetime import datetime

def getReviews(business_id, star_rating, type):
    client = MongoClient('mongodb://%s:%s@18.220.145.34' % ("project-admin", "ip-moc-password"))
    db = client['ip_db']
    collection = db['reviews']
    steptime = datetime.strptime("16/06/01", "%y/%m/%d")
    recent_reviews = list()
    documents = collection.find({"business_id": business_id})
    if type == "less":
        for document in documents:
            if document['stars'] <= star_rating and document['date'] > steptime:
                recent_reviews.append(document['text'])
    if type == "more":
        for document in documents:
            if document['stars'] >= star_rating and document['date'] > steptime:
                recent_reviews.append(document['text'])
    filename = business_id + '_' + str(star_rating) + ".txt"
    file = open(filename , 'w')
    for review in recent_reviews:
        file.write(review)
    
if __name__ == '__main__':
    # food bussinesses
    # getReviews("RESDUcs7fIiihp38-d6_6g", 2, type = "less")
    # getReviews("RESDUcs7fIiihp38-d6_6g", 4, type = "more")
    # getReviews("DkYS3arLOhA8si5uUEmHOw", 2, type = "less")
    # getReviews("DkYS3arLOhA8si5uUEmHOw", 4, type = "more")
    getReviews("SMPbvZLSMMb7KU76YNYMGg", 2, type = "less")
    getReviews("SMPbvZLSMMb7KU76YNYMGg", 4, type = "more")
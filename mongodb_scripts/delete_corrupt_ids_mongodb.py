import unittest
import sys
from pymongo import MongoClient
import hashlib
sys.path.append("..")
from scraper.scraper_selenium_fotocasa import ScraperSeleniumFotocasa


class ChangeIdsMongodb(unittest.TestCase):  

    def testFotocasa(self):
        self.client = MongoClient('mongodb://freshkore:1234@ds231460.mlab.com:31460/real-state-db')
        self.db = self.client['real-state-db']

        scraped_collection=self.db.scrapped
        for scraped_data in scraped_collection.find({ "_id":{"$regex": "^--"}}):
            print(" deleting " + scraped_data["_id"])
            scraped_collection.delete_one(scraped_data)
        self.assertTrue(True)
if __name__ == '__main__':
	    unittest.main()

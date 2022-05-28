import unittest
from etf import *

dfScrape = WebScraper.scrapeWebsite()
dfHeaderNames = WebScraper.addHeaderNames(dfScrape)
dfRemoveExcess = WebScraper.removeExcess(dfHeaderNames)

class Tests(unittest.TestCase):
    def testScrapeWebsite(self):
        self.assertFalse(WebScraper.scrapeWebsite().empty)

    def testAddHeaderNames(self):
        self.assertFalse(WebScraper.addHeaderNames(dfScrape).empty)

    def testRemoveExcess(self):
        self.assertFalse(WebScraper.removeExcess(dfHeaderNames).empty)

    def testForceColumnsAsType(self):
        self.assertFalse(WebScraper.forceColsAsTypeFloat(dfRemoveExcess).empty)

    def testCreateDF(self):
        self.assertFalse(WebScraper.createDF().empty)

if __name__=='__main__':
    unittest.main()


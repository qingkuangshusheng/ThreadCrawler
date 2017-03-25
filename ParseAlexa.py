#coding:utf-8
import csv
from zipfile import ZipFile
import zipfile
from StringIO import StringIO
from html_downLoader import HtmlDownLoader
class AlexaCallback:
    def __init__(self,maxurls=5):
        self.max_urls=maxurls
        self.seed_url="http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
        self.downloader=HtmlDownLoader()

    def __call__(self, url,):
        if url==self.seed_url:
            #zipped_data=self.downloader.downLoad("http://s3.amazonaws.com/alexa-static/top-1m.csv.zip")
            #zipped_data=open("top-1m.csv.zip","r").read()
            urls=[]
            #print zipfile.is_zipfile(StringIO(zipped_data))
            with ZipFile("top-1m.csv.zip") as zf:
                csv_filename=zf.namelist()[0]
                for _,website in csv.reader(zf.open(csv_filename)):
                    urls.append("http://"+website)
                    if len(urls)==self.max_urls:
                        break
            print urls
            return urls
# if __name__ == '__main__':
#     alexaCallback=AlexaCallback()
#     alexaCallback("http://s3.amazonaws.com/alexa-static/top-1m.csv.zip")

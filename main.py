#coding:utf-8
import time
import threading
from html_downLoader import HtmlDownLoader
import ParseAlexa
SLEEP_TIME=1
def threaded_crawler(alexaCallback,max_threads=10):
    threads=[]
    result={}
    crawl_queue=alexaCallback("http://s3.amazonaws.com/alexa-static/top-1m.csv.zip")
    dlownloader=HtmlDownLoader()
    def process_queue():
        while True:
            try:
                url=crawl_queue.pop()
            except IndexError,e:
                print e.message
                break
            else:
                html=dlownloader.downLoad(url)
                result[url]=html
                print "正在爬取%s"%url

    while threads or crawl_queue:
        while len(threads)<max_threads and crawl_queue:
            thread=threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
            time.sleep(SLEEP_TIME)
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        # print result
if __name__ == '__main__':
    alexaCallback=ParseAlexa.AlexaCallback()
    threaded_crawler(alexaCallback)




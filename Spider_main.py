import url_manager
import url_downloader
import url_parser
import url_outputer
import sqlite3

class SpiderMain():
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloads=url_downloader.UrlDownLoader()
        self.parses=url_parser.UrlParser()
        self.outputs=url_outputer.UrlOutputer()
    
    def craw(self,url):
        self.urls.add_new_url(url)
        count=0
        while self.urls.has_url():
            try:
                new_url=self.urls.get_new_url()
                url_download=self.downloads.downloads(new_url)
                new_urls,url_data=self.parses.parsers(new_url,url_download)
                self.urls.add_new_urls(new_urls)
                self.outputs.collector(url_data)
                
                count+=1
                print("第%s次 "%count)
                print("%s"%new_url)
                if count == 10:
                    break
            except:
                print("Url Error")
        self.outputs.output_data()

if __name__ == "__main__":
    start_url="http://baike.baidu.com/subview/13520/5136230.htm#viewPageContent"
    html_spider=SpiderMain()
    html_spider.craw(start_url)
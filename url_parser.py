from bs4 import BeautifulSoup
import re
import urllib.parse

class UrlParser():  
    def _get_new_urls(self,new_url,soup):
        new_urls=set()
        links=soup.find_all("a",href=re.compile(r'/view/\d+\.htm'))
        for cc in links:
            link=cc["href"]
            new_full_url=urllib.parse.urljoin(new_url,link)
#            print(new_full_url)
            new_urls.add(new_full_url)
        return new_urls
        
    def _get_new_data(self,new_url,soup):
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>男同性恋</h1>
        res_data={}
        res_data["url"]=new_url
        title_node=soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"]=title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find("div",class_="lemma-summary")
        res_data["summary"]=summary_node.get_text()
        
        return res_data
        
    def parsers(self,new_url,url_download):
        if new_url is None or url_download is None:
            return None
        soup=BeautifulSoup(url_download,"html.parser",from_encoding="utf-8")
        new_urls=self._get_new_urls(new_url,soup)
        new_data=self._get_new_data(new_url,soup)
        return new_urls,new_data
class UrlManager():
    def __init__(self):
        self.url_set=set()
        self.done_urls=set()
    
    def add_new_url(self,url):
        if url != None:
            self.url_set.add(url)
        else:
            return None
    
    def add_new_urls(self,new_urls):
        for link in new_urls:
            if link != None:
                self.url_set.add(link)
        
    def has_url(self):
        if len(self.url_set) != 0:
            return 1
    
    def get_new_url(self):
        done=self.url_set.pop()
        self.done_urls.add(done)
        return done
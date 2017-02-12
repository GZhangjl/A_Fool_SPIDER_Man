import urllib.request

class UrlDownLoader():
    def downloads(self,url):
        if url != None:
            response=urllib.request.urlopen(url)
            if response.getcode() != 200:
                return  None
            return response.read()
        else:
            return None
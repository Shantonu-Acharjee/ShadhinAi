import pyshorteners

class PythonLinkShortenerOnline:

    def __init__(self, link):
        self.big_link_url = link
        self.short_link_url = ''
        self.make_short_link()

    
    def make_short_link(self):
        
        self.short_link_url = pyshorteners.Shortener().tinyurl.short(self.big_link_url)
       
        




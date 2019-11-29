#xml simple parsing
import xml.sax
class UserHandler(xml.sax.ContentHandler):
    #Call when an element starts
    def startElement(self,tag,attributes):
        print("startElement called for ",tag)
    #Call when a character is read
    def characters(self,content):
        print("characters called for ",content)
    #Call when an element ends
    def endElement(self,tag):
        print('endElement called for ',tag)

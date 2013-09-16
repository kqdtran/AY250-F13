import argparse
import urllib
import urllib2
from bs4 import BeautifulSoup as Soup

def buildParser():
    """Build a simple parser that allows CalCalc to take in a string
    argument after calling the -s flag"""
    
    parser = argparse.ArgumentParser(description='Awesome Calculator')
    parser.add_argument('-s', action='store', dest='stringExp',
                        help='String expression to evaluate')
    results = parser.parse_args()
    return results

def evaluate(stringExp):
    """Use the evil 'eval' in a clean namespace to prevent injection.
    Suggested on http://stackoverflow.com/a/2372145/2465041

    stringExp - the string expression to be evaluated
                if exception, send to Wolfram Alpha"""
    
    ns = {'__builtins__': None}
    try:
        result = eval(stringExp, ns)
    except SyntaxError: # Wolfram Alpha helps meeee
        print "Querying Wolfram Alpha... Please wait..."
        url = "http://api.wolframalpha.com/v2/query"
        values = {'input': stringExp, 'format': 'plaintext', 'appid': 'UAGAWR-3X6Y8W777Q'}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        xmlDoc = response.read()
        soup = Soup(xmlDoc)
        resultList = soup.find_all('plaintext')
        result = resultList[1].string
    return result
    
if __name__ == "__main__":
    parseOptions = buildParser()
    stringExp = parseOptions.stringExp
    print evaluate(stringExp)
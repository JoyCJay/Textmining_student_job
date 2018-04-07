import json
from urllib.request import urlopen


def Sentiment(context):
    URL="http://api.datumbox.com/1.0/SentimentAnalysis.json"
    API="?api_key=0524ce14843851b0ffcf479659fb2a34"
    context_url="%22"+context.replace(' ','%20')+"%22"
    TEXT="&text="+context_url

    URL=URL+API+TEXT

    html = urlopen(URL)
    result = json.loads(html.read().decode())
    return result.get("output").get("result")

def Keyword(context):
    URL="http://api.datumbox.com/1.0/KeywordExtraction.json"
    API="?api_key=0524ce14843851b0ffcf479659fb2a34"
    context_url="%22"+context.replace(' ','%20')+"%22"
    TEXT="&text="+context_url

    URL=URL+API+"&n=3"+TEXT

    html = urlopen(URL)
    result = json.loads(html.read().decode())
    #result = json.dumps(result, indent=3);
    return result.get("output").get("result")

def Topic(context):
    URL="http://api.datumbox.com/1.0/TopicClassification.json"
    API="?api_key=0524ce14843851b0ffcf479659fb2a34"
    context_url="%22"+context.replace(' ','%20')+"%22"
    TEXT="&text="+context_url

    URL=URL+API+TEXT

    html = urlopen(URL)
    result = json.loads(html.read().decode())
    return result.get("output").get("result")

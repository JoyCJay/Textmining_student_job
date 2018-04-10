import json
from urllib.request import urlopen
import os,shutil


#copy/movefile-----------------------------------------------------------------
def movefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print("move successful \n%s -> %s"%( srcfile,dstfile))

def copyfile(srcfile,Topic):
    dstfile='./classification/'+Topic+'/'+srcfile
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy successful \n%s -> %s"%( srcfile,dstfile))


#------------------------------------------------------------------------------
def filter(i):
    for a in ["the","a","an","to","of"]:
        if a in i:
            return False
    return True

def Sentiment(context):
    URL="http://api.datumbox.com/1.0/SentimentAnalysis.json"
    API="?api_key=0524ce14843851b0ffcf479659fb2a34"
    context=context.replace("\n"," ")
    context=context.replace("-"," ")
    context=context.encode('ascii', 'ignore').decode('ascii')
    context_url="%22"+context.replace(' ','%20')+"%22"
    TEXT="&text="+context_url

    URL=URL+API+TEXT

    html = urlopen(URL)
    result = json.loads(html.read().decode())
    return result.get("output").get("result")

def Keyword(context):
    URL="http://api.datumbox.com/1.0/KeywordExtraction.json"
    API="?api_key=0524ce14843851b0ffcf479659fb2a34"
    context=context.replace("\n"," ")
    context=context.replace("-"," ")
    context=context.encode('ascii', 'ignore').decode('ascii')
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
    context=context.replace("\n"," ")
    context=context.replace("-"," ")
    context=context.encode('ascii', 'ignore').decode('ascii')
    context_url="%22"+context.replace(' ','%20')+"%22"
    TEXT="&text="+context_url

    URL=URL+API+TEXT

    html = urlopen(URL)
    result = json.loads(html.read().decode())
    return result.get("output").get("result")

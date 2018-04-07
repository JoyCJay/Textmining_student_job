import sys
import func
import json

f = open('./test')
context=f.read()
context=context[0:-1]#去除文件EOF

#print("context is :","\n",context,'\n')
#-------------------------------------------------------------------------------
print("1.Keyword :".center(80,'-'))
Keyword=func.Keyword(context)
print("Bi-gram:")
bi_gram={}
for i in Keyword.get("2"):
    if Keyword.get("2").get(i)>1:
        #print(i,Keyword.get("2").get(i))
        bi_gram[i]=Keyword.get("2").get(i)
#print(json.dumps(bi_gram, indent=3))
for elem in sorted(bi_gram.items(),key=lambda item:item[1],reverse=True):
    print("\t"+str(elem))

print("\nTri-gram:")
tri_gram={}
for i in Keyword.get("3"):
    if Keyword.get("3").get(i)>1:
        #print(i,Keyword.get("3").get(i))
        tri_gram[i]=Keyword.get("3").get(i)
#print(json.dumps(tri_gram, indent=3))
for elem in sorted(tri_gram.items(),key=lambda item:item[1],reverse=True):
    print("\t"+str(elem))
#-------------------------------------------------------------------------------
print("2.Topic Classification :".center(80,'-'))
Topic=func.Topic(context)
print(Topic,'\n')
#-------------------------------------------------------------------------------
print("3.Sentiment :".center(80,'-'))
Sentiment=func.Sentiment(context)
print(Sentiment,'\n')

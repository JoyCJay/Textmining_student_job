import os,json
import importlib,sys
import func
'''
for root, dirs,files in os.walk("./Sample"):
    for i in files:
        print(i) #当前路径下所有非目录子文件
'''
srcfile=sys.argv[1]
f = open(srcfile)
context=f.read()
#print("context is :","\n",context,'\n')
#-------------------------------------------------------------------------------

print("1.Keyword :".center(80,'-'))
Keyword=func.Keyword(context)
print("\nUni-gram:")
uni_gram={}
for i in Keyword.get("1"):
    if Keyword.get("1").get(i)>3 and func.filter(i):
        #print(i,Keyword.get("2").get(i))
        uni_gram[i]=Keyword.get("1").get(i)
#print(json.dumps(bi_gram, indent=3))
for elem in sorted(uni_gram.items(),key=lambda item:item[1],reverse=True):
    print("\t"+str(elem))

print("\nBi-gram:")
bi_gram={}
for i in Keyword.get("2"):
    if Keyword.get("2").get(i)>1 and "the" not in i and "of" not in i:
        #print(i,Keyword.get("2").get(i))
        bi_gram[i]=Keyword.get("2").get(i)
#print(json.dumps(bi_gram, indent=3))
for elem in sorted(bi_gram.items(),key=lambda item:item[1],reverse=True):
    print("\t"+str(elem))

print("\nTri-gram:")
tri_gram={}
for i in Keyword.get("3"):
    if Keyword.get("3").get(i)>1 and "the" not in i:
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
#-------------------------------------------------------------------------------

func.copyfile(srcfile,Topic)

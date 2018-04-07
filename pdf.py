from pdfminer.pdfparser import PDFParser

from pdfminer.pdfdocument import PDFDocument

from pdfminer.pdfpage import PDFPage

from pdfminer.pdfpage import PDFTextExtractionNotAllowed

from pdfminer.pdfinterp import PDFResourceManager

from pdfminer.pdfinterp import PDFPageInterpreter

from pdfminer.pdfdevice import PDFDevice

fp = open('./test.pdf', 'rb')

#创建一个PDF文档解析器对象

parser = PDFParser(fp)

#创建一个PDF文档对象存储文档结构

#提供密码初始化，没有就不用传该参数

document = PDFDocument(parser, password)

#检查文件是否允许文本提取

if not document.is_extractable:

    raise PDFTextExtractionNotAllowed

#创建一个PDF资源管理器对象来存储共享资源

rsrcmgr = PDFResourceManager()

#创建一个pdf设备对象

device = PDFDevice(rsrcmgr)

#创建一个PDF解析器对象

interpreter = PDFPageInterpreter(rsrcmgr, device)

#处理文档当中的每个页面

for page in PDFPage.create_pages(document):

    interpreter.process_page(page)

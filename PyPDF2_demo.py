# encoding:utf-8
from PyPDF2 import PdfFileReader, PdfFileWriter


# 读操作
def read_pdf(readFile):
    #readFile = 'C:/Users/Administrator/Desktop/RxJava 完全解析.pdf'
    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(readFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    # 获取 PDF 文件的文档信息
    documentInfo = pdfFileReader.getDocumentInfo()
    print('documentInfo = %s' % documentInfo)
    # 获取页面布局
    pageLayout = pdfFileReader.getPageLayout()
    print('pageLayout = %s ' % pageLayout)
    # 获取页模式
    pageMode = pdfFileReader.getPageMode()
    print('pageMode = %s' % pageMode)
    xmpMetadata = pdfFileReader.getXmpMetadata()
    print('xmpMetadata  = %s ' % xmpMetadata)
    # 获取 pdf 文件页数
    pageCount = pdfFileReader.getNumPages()
    print('pageCount = %s' % pageCount)
    for index in range(0, pageCount):
        # 返回指定页编号的 pageObject
        pageObj = pdfFileReader.getPage(index)
        print('index = %d , pageObj = %s' % (index, type(pageObj)))  # <class 'PyPDF2.pdf.PageObject'>
        # 获取 pageObject 在 PDF 文档中处于的页码
        pageNumber = pdfFileReader.getPageNumber(pageObj)
        print('pageNumber = %s ' % pageNumber)


# 写操作

def addBlankpage(readFile, outFile):
    #readFile = 'C:/Users/Administrator/Desktop/RxJava 完全解析.pdf'
    #outFile = 'C:/Users/Administrator/Desktop/copy.pdf'
    pdfFileWriter = PdfFileWriter()
    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(readFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    numPages = pdfFileReader.getNumPages()
    for index in range(numPages):
        pageObj = pdfFileReader.getPage(index)
        pdfFileWriter.addPage(pageObj)  # 根据每页返回的 PageObject,写入到文件
        pdfFileWriter.write(open(outFile, 'wb'))
    pdfFileWriter.addBlankPage()   # 在文件的最后一页写入一个空白页,保存至文件中
    pdfFileWriter.write(open(outFile,'wb'))

# 分割文档

def splitPdf(readFile, outFile):
    #readFile = 'C:/Users/Administrator/Desktop/RxJava 完全解析.pdf'
    #outFile = 'C:/Users/Administrator/Desktop/copy.pdf'
    pdfFileWriter = PdfFileWriter()
    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(readFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    # 文档总页数
    numPages = pdfFileReader.getNumPages()
    if numPages > 5:
        # 从第五页之后的页面，输出到一个新的文件中，即分割文档
        for index in range(5, numPages):
            pageObj = pdfFileReader.getPage(index)
            pdfFileWriter.addPage(pageObj)
        # 添加完每页，再一起保存至文件中
        pdfFileWriter.write(open(outFile, 'wb'))

# 合并文档

def mergePdf(inFileList, outFile):
    '''
    合并文档
    :param inFileList: 要合并的文档的 list
    :param outFile:    合并后的输出文件
    :return:
    '''
    pdfFileWriter = PdfFileWriter()
    for inFile in inFileList:
        # 依次循环打开要合并文件
        pdfReader = PdfFileReader(open(inFile, 'rb'))
        numPages = pdfReader.getNumPages()
        for index in range(0, numPages):
            pageObj = pdfReader.getPage(index)
            pdfFileWriter.addPage(pageObj)
        # 最后,统一写入到输出文件中
        pdfFileWriter.write(open(outFile, 'wb'))


# 粗略读取 PDF 文本内容
def getPdfContent(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""
    for i in range(0, pdf.getNumPages()):
        pageObj = pdf.getPage(i)
        extractedText = pageObj.extractText()
        content += extractedText + "\n"
        # return content.encode("ascii", "ignore")
    return content
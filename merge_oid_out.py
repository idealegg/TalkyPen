# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


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
        pdfReader = PdfFileReader(inFile)
        numPages = pdfReader.getNumPages()
        for index in range(0, numPages):
            pageObj = pdfReader.getPage(index)
            pdfFileWriter.addPage(pageObj)
        # 最后,统一写入到输出文件中
        pdfFileWriter.write(open(outFile, 'wb'))


if __name__ == "__main__":
    CMY_K_PDF_DIR = r'C:\Users\newer\Downloads\OidProducer\Design\_Output\Code_Sonix2\600dpi\CMY_K_PDF'
    input_list = (
        ('result_2021_11_03_12_04_24_474', r'火火兔故事'),
        ('result_2021_11_03_12_04_37_3888', r'火火兔儿歌'),
        ('result_2021_11_03_17_53_55_27976', r'贝乐虎儿歌'),
        ('result3', r'宝宝巴士古诗词'),
        ('学唱古诗词', r'学唱古诗词'),
    )
    for (pdf_prefix, out_name) in input_list:
        mergePdf(map(lambda x: os.path.join(CMY_K_PDF_DIR, x),
            filter(lambda x: x.startswith(pdf_prefix), os.listdir(CMY_K_PDF_DIR))),
                 "%s.pdf"%out_name)

from reportbuilder.PdfReportBuilder import PdfReportBuilder
if __name__ == '__main__':
    pdfBuilder = PdfReportBuilder('sample-filename', 'default-rendered')
    print('Hi, I am reportbuilder at your service!')
    pdfBuilder.buildReport('sample-data')
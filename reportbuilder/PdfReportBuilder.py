from reportbuilder.ReportBuilder import ReportBuilder

class PdfReportBuilder(ReportBuilder):
    def __init__(self, filename, pdf_renderer):
        super().__init__(filename)
        self.pdf_renderer = pdf_renderer

    def buildReport(self, data):
        print('Calling buildReport from PdfReportBuilder.')
        print('Filename is: {}'.format(self.filename))
        print('Renderer is {}'.format(self.pdf_renderer))
        return 'success'

from reportbuilder.ReportBuilder import ReportBuilder

class TextReportBuilder(ReportBuilder):
    def __init__(self, filename, text_ending):
        super().__init__(filename)
        self.text_ending = text_ending

    def buildReport(self, data):
        print('Calling buildReport from TextReportBuilder.')
        print('Filename is: {}'.format(self.filename))
        print('Text ending is {}'.format(self.text_ending))
        return 'success'

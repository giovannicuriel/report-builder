
class ReportBuilder:
    def __init__(self, filename):
        self.filename = filename

    def buildReport(self, data):
        print('Calling buildReport from ReportBuilder.')
        print('Filename is: {}'.format(self.filename))
        raise NotImplementedError()

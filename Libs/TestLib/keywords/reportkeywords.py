from robot.api.deco import keyword


class ReportKeywords(object):
    def __init__(self):
        pass

    @keyword
    def get_report(self, value):
        return value

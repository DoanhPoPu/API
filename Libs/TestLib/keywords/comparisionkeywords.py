from robot.api.deco import keyword


class ComparisionKeywords(object):
    def __init__(self):
        pass

    @keyword('Provide information', 'Customized kws')
    def get_value(self, value):
        return value

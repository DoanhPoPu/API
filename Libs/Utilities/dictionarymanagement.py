from robot.api import logger
import datetime

class DictionaryManagement(object):

    def compareResponseAndExpectedResult(self, response, expected_result):
        try:
            compare = True
            if type(response) is not dict: response = dict(response)
            if type(expected_result) is not dict: expected_result = dict(expected_result)
            for key, value in response.items():
                for rs_key, rs_value in expected_result.items():
                    if key == rs_key:
                        compare = True
                        if value is not None and (isinstance(value,str) == False and isinstance(value, datetime.datetime) == False):
                            compare = self.DictionaryCompare(value, rs_value)
                        break
                    else:
                        compare = False
                if compare == False:
                    return False
            return True
        except:
            print("An exception occurred")

    def DictionaryCompare(self, sub1, sub2):
        try:
            result = True
            if type(sub1) is not dict: sub1 = dict(sub1)
            if type(sub2) is not dict: sub2 = dict(sub2)
            for sub1_key, sub1_value in sub1.items():
                for sub2_key, sub2_value in sub2.items():
                    result = bool(sub1_key == sub2_key)
                    if result == True:
                        result = self.compareResponseAndExpectedResult(sub1_value, sub2_value)
                        if result == False:
                            return result
            return result
        except Exception as e:
            print(e)

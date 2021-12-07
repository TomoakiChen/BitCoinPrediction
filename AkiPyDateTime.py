# -*- coding: utf-8 -*-

# 這段以後可以拉出去，做時間相關lib
class AkiDateTimeUtil:
    @staticmethod
    def checkIsAfterEqSinceDate(desig_datetime, since_date = None):
        since_datetime = datetime.combine(since_date, datetime.min.time())
        return since_datetime == None or desig_datetime.timestamp() >= since_datetime.timestamp() # 如果沒有 since_date，則當作符合條件

    @staticmethod
    def checkIsBeforeEqUntilDate(desig_datetime, until_date = None):
        until_datetime = datetime.combine(until_date, datetime.max.time())
        return until_date == None or desig_datetime.timestamp() <= until_datetime.timestamp()

    @staticmethod
    def checkIsInInterval(desig_datetime, since_date = None, until_date = None):
        is_after_since = AkiDateTimeUtil.checkIsAfterEqSinceDate(desig_datetime, since_date)
        is_before_until = AkiDateTimeUtil.checkIsBeforeEqUntilDate(desig_datetime, until_date)
        return is_after_since and is_before_until

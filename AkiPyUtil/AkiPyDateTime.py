# -*- coding: utf-8 -*-
from datetime import datetime as DateTime, date as Date, timedelta as TimeDelta

class AkiDateTimeUtil:
    @staticmethod
    def checkIsAfterEqSinceDate(desig_datetime, since_date = None):
        since_datetime = None
        if since_date != None:
            since_datetime = DateTime.combine(since_date, DateTime.min.time())
        return since_datetime == None or desig_datetime.timestamp() >= since_datetime.timestamp() # 如果沒有 since_date，則當作符合條件

    @staticmethod
    def checkIsBeforeEqUntilDate(desig_datetime, until_date = None):
        until_datetime = None
        if until_date != None:
            until_datetime = DateTime.combine(until_date, DateTime.max.time())
        return until_datetime == None or desig_datetime.timestamp() <= until_datetime.timestamp()

    @staticmethod
    def checkIsInInterval(desig_datetime, since_date = None, until_date = None):
        is_after_since = AkiDateTimeUtil.checkIsAfterEqSinceDate(desig_datetime, since_date)
        is_before_until = AkiDateTimeUtil.checkIsBeforeEqUntilDate(desig_datetime, until_date)
        # print("desig_datetime = " +str(desig_datetime) + " since_date = " + str(since_date) + " until_date = " + str(until_date))
        # print("is_after_since = " + str(is_after_since) + " is_before_until = " + str(is_before_until))
        return is_after_since and is_before_until

    @staticmethod
    def obtainFirstTimeOfDate(desig_date):
        desig_datetime = None
        if desig_date != None:
            if isinstance(desig_date, str):
                desig_date = Date.fromisoformat(desig_date)
            desig_datetime = DateTime.combine(desig_date, DateTime.min.time())
        return desig_datetime

    @staticmethod
    def obtainLastTimeOfDate(desig_date):
        desig_datetime = None
        if desig_date != None:
            if isinstance(desig_date, str):
                desig_date = Date.fromisoformat(desig_date)            
            desig_datetime = DateTime.combine(desig_date, DateTime.max.time())
        return desig_datetime

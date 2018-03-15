# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mocker
   Description :
   Author :        Administrator
   date：          2018/3/15
-------------------------------------------------
   Change Activity:
                   2018/3/15:
-------------------------------------------------
"""
import mock as mock

from testcase.web.mock import Caculator

__author__ = 'Administrator'


class mocker():

    def t(self):
        Caculator.add = mock.Mock('add', 5, 6)
        mocker.return_value = 200


if __name__ == '__main__':
    mocker().t();

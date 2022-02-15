import pytest
from common.pl_helper import PolishLocaleHelper
import babel.dates
import locale
from datetime import datetime, timezone


def test_parse_pl_date_onet():
    locale.setlocale(locale.LC_ALL, "pl_PL.utf8")
    test1 = '16 stycznia 2022 15:34'
    # test1 = '16 styczeń 2022 17:04'
    result1 = PolishLocaleHelper.parse_pl_date_onet(test1)

    assert result1.day == 16
    assert result1.month == 1
    assert result1.year == 2022
    assert result1.hour == 15
    assert result1.minute == 34

    print(f'\nresult1.day: {result1.day}')
    print(f'result1.month: {result1.month}')
    print(f'result1.year: {result1.year}')
    print(f'result1.hour: {result1.hour}')
    print(f'result1.minute: {result1.minute}')

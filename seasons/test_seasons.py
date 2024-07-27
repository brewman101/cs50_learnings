import seasons
import pytest

from datetime import date
from datetime import datetime
from datetime import timedelta


def main():
    test1()
    test2()
    test3()

def test1():
    assert seasons.validate_date(str(date.today()-timedelta(days=365))) == "Five hundred twenty-five thousand, six hundred minutes"

def test2():
    with pytest.raises(SystemExit) as sample:
        seasons.validate_date("Blah")
    assert sample.type == SystemExit
    assert sample.value.code=="Invalid date"

def test3():
    assert seasons.validate_date(str(date.today()-timedelta(days=730))) == "One million, fifty-one thousand, two hundred minutes"


if __name__ =="__main__":
    main()

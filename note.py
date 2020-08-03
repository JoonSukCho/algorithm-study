from dateutil.parser import parse


date1 = parse('20200201')
date2 = parse('20200301')


if date1 < date2:
    print("true")
else:
    print("false")

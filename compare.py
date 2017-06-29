#!/usr/bin/python
import pandas as pd

df = pd.read_excel('/Users/aharon/Downloads/bank_compare.xlsx')

count_rows = df.shape[0]

start = 0
####
bank_date_line = 0
bank_date_index = 0
bank_value_line = 0
bank_value_index = 1
bank = {}

####
office_date_line = 0
office_date_index = 3
office_value_line = 0
office_value_index = 4
office = {}

while start < count_rows:

    bank[df.iloc[bank_date_line, bank_date_index]] = df.iloc[bank_value_line, bank_value_index]
    bank_date_line += 1
    bank_value_line += 1

    office[df.iloc[office_date_line, office_date_index]] = df.iloc[office_value_line, office_value_index]
    office_date_line += 1
    office_value_line += 1

    start += 1


bank_list = sorted(bank.iteritems())
office_list = sorted(office.iteritems())

counter = 0
results = {}

print "\n\n\nReport:\n~~~~~~~~~\n"
for key in bank_list:
    if bank.keys()[counter] == office.keys()[counter]:
        if bank.values()[counter] == office.values()[counter]:
            pass
        else:
            print "Value is not equal.\nPlease observe the details below:\n---------------------------------\nBank Value is %s on the %s\nAnd\nOffice Value is %s on the %s " % (bank.values()[counter],bank.keys()[counter],office.values()[counter], office.keys()[counter])
    else:
        print "\n\n\nDate is't equal.\nPlease observe the details below:\n---------------------------------\nBank Date is:  %s\nAnd\nOffice Date is %s" % (bank.keys()[counter],office.keys()[counter])

    counter += 1

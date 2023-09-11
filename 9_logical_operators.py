#conditions: if applicant has high income AND good credit
#            Eligible for loan

#has_high_income = True
has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print('Eligible for loan')

#conditions: if applicant has high income OR good credit
#            Eligible for loan
if has_high_income or has_good_credit:
    print('Still eligible for loan')

#conditions: if applicant has good credit AND doesn't have a criminal record
#            Eligible for loan
good_credit = True
has_criminal_record = False
if good_credit and not has_criminal_record:
    print('qualifies for loan')

# AND: Both
# OR: at least one
# NOT: inverts the boolean value
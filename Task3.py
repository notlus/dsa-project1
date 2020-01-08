"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


class TelephoneNumber(object):
    """
    All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a
    code indicating the location and/or type of the telephone number. There are three different
    kinds of telephone numbers, each with a different format:
        - Fixed lines start with an area code enclosed in brackets. The area codes vary in length
          but always begin with 0. Example: "(022)40840621".
        - Mobile numbers have no parentheses, but have a space in the middle of the number to help
          readability. The mobile code of a mobile number is its first four digits and they always
          start with 7, 8 or 9. Example: "93412 66159".
        - Telemarketers' numbers have no parentheses or space, but start with the code 140. Example:
          "1402316533".
    """

    def __init__(self, phone_number):
        super().__init__()
        self.phone_number = phone_number

    def prefix(self):
        if self.phone_number.startswith("140"):
            # telemarketer
            return "140"

        if self.phone_number.startswith("("):
            # land line
            prefix = ""
            for c in self.phone_number:
                if c != "(" and c != ")":
                    prefix += c

                if c == ")":
                    break

            # print("prefix: {}".format(prefix))
            return prefix

        if self.phone_number.startswith(("7", "8", "9")):
            # mobile
            return self.phone_number[:4]


class CallRecord(object):
    """
    A call record has the following columns:
        - sending telephone number (string)
        - receiving telephone number (string)
        - timestamp of call start time (string)
        - duration of the call
    """

    def __init__(self, call_record):
        super().__init__()
        self.sender = TelephoneNumber(call_record[0])
        self.receiver = TelephoneNumber(call_record[1])
        self.start_time = call_record[2]
        self.duration = int(call_record[3])

# Part A


def get_codes(calls):
    """
    Time complexity: O(nlogn)
    Space complexity: O(n) - The size of the set of unique prefixes
    """
    codes_set = set()
    for call in calls:
        call_record = CallRecord(call)
        if call_record.sender.prefix() == "080":
            # Bangalore area code
            codes_set.add(call_record.receiver.prefix())

    codes = list(codes_set)
    codes.sort()
    return codes


codes = get_codes(calls)
print("The numbers called by people in Bangalore have codes:")
for code in codes:
    print(code)

# Part B


def get_bangalore_pct():
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    sender_count = 0
    receiver_count = 0
    for call in calls:
        call_record = CallRecord(call)
        if call_record.sender.prefix() == "080":
            sender_count += 1
            if call_record.receiver.prefix() == "080":
                receiver_count += 1

    return 0 if sender_count == 0 else receiver_count / sender_count * 100


bangalore_pct = get_bangalore_pct()
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    bangalore_pct))

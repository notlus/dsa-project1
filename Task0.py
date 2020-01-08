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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
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
        self._sender = TelephoneNumber(call_record[0])
        self._receiver = TelephoneNumber(call_record[1])
        self.start_time = call_record[2]
        self.duration = call_record[3]

    @property
    def sender(self):
        return self._sender.phone_number

    @property
    def receiver(self):
        return self._receiver.phone_number


class TextRecord(object):
    """
    A text record has the following columns:
        - sending telephone number (string)
        - receiving telephone number (string)
        - timestamp of text message (string)
    """

    def __init__(self, text_record):
        super().__init__()
        self._sender = TelephoneNumber(text_record[0])
        self._receiver = TelephoneNumber(text_record[1])
        self.duration = text_record[2]

    @property
    def sender(self):
        return self._sender.phone_number

    @property
    def receiver(self):
        return self._receiver.phone_number


first_text_record = TextRecord(texts[0])
print("First record of texts, {} texts {} at time {}".format(
    first_text_record.sender, first_text_record.receiver, first_text_record.duration))

last_call_record = CallRecord(calls[-1])
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    last_call_record.sender, last_call_record.receiver, last_call_record.start_time, last_call_record.duration))

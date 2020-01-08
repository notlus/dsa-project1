"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
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
        self.duration = int(call_record[3])

    @property
    def sender(self):
        return self._sender.phone_number

    @property
    def receiver(self):
        return self._receiver.phone_number

def longest_call():
    """
    We need to track the total duration of all calls for a given number. The duration should include
    the number used as the sender and the receiver. Maintain a dictionary that maps phone numbers to
    the total duration.
        - look up sender in dictionary, if found then add duration, otherwise add to dictionary
        - look up receiver in dictionary, if found then add duration, otherwise add to dictionary

    Time complexity: O(n)
    Space complexity: O(k), where k = the number of unique phone numbers
    """

    # Map phone numbers to durations
    call_durations = {}
    for call in calls:
        call_record = CallRecord(call)
        # Handle sender number
        if call_record.sender in call_durations:
            call_durations[call_record.sender] += call_record.duration
        else:
            # Add to dictionary
            call_durations[call_record.sender] = call_record.duration

        # Handle receiver number
        if call_record.receiver in call_durations:
            # Already in the dictionary, so update
            call_durations[call_record.receiver] += call_record.duration
        else:
            # Add to dictionary
            call_durations[call_record.receiver] = call_record.duration

    # Get the key for the number with the highest value
    longest_number = max(call_durations, key=lambda key:call_durations[key])
    total_duration = call_durations[longest_number]
    return longest_number, total_duration


phone_number, duration = longest_call()
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number, duration))

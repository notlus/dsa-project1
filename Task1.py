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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def unique_phone_numbers(call_records, text_records):
    """
    Given a list of call or text records, return the count of unique phone numbers present.
    Time complexity: O(2n)
    Space complexity: O(k), where k = the number of unique phone numbers
    """
    phone_numbers = set()
    for record in call_records:
        phone_numbers.add(record[0])
        phone_numbers.add(record[1])

    for record in text_records:
        phone_numbers.add(record[0])
        phone_numbers.add(record[1])

    return len(phone_numbers)


total_numbers = unique_phone_numbers(calls, texts)

print("There are {} different telephone numbers in the records.".format(
    total_numbers))

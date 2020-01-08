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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def get_telemarketers():
    """
    Return a list of possible telemarketer phone numbers. The algorithm is the following:
        - Create a set of sender phone numbers
        - Create a set of receiver phone numbers
        - Enumerate the list of calls and and senders and receivers to their respective sets
        - Get the difference between the sets, to get the first set of candidates
        - Enumerate the list of texts, checking whether the sender or receiver is in the set
          created in the previous step. If found, remove from the difference set

    Time complexity: O(n + s), where s is the size of the difference set
    Space complexity: O(3s), where s is the size the sender, receiver and difference sets
    """

    # Build the sets of senders and receivers
    senders = set()
    receivers = set()
    for call in calls:
        senders.add(call[0])
        receivers.add(call[1])

    differences = senders.difference(receivers)

    for text in texts:
        if text[0] in differences:
            differences.remove(text[0])

        if text[1] in differences:
            differences.remove(text[1])

    return differences

telemarketers = get_telemarketers()

print("These numbers could be telemarketers: ")
for telemarketer in telemarketers:
    print(telemarketer)

# the AIM is to track the transactions and analyse them

# load data from the json file
import decimal
import json

with open('transaction.json') as f:
    data = json.load(f)

print("Data loaded successfully, contains {} transactions".format(len(data)))

# list unique transaction_descriptions
unique_descriptions = set()
for transaction in data:
    unique_descriptions.add(transaction['transaction_description'])

# print("Unique transaction descriptions({}): {}".format(
#     len(unique_descriptions), unique_descriptions))


# list transaction descriptions contains the word ["Interest Amount Amortization","INFINITY PAYMENT RECEIVED","IGST-CI@18"]

interest_amortization = []
for transaction in data:
    if transaction['transaction_description'].startswith("Interest Amount Amortization") or transaction['transaction_description'].startswith("Principal Amount Amortization") or transaction['transaction_description'].startswith("IGST-CI@18") or transaction['transaction_description'].startswith("GULF OWN MOBILES MALAPURAM") or transaction['transaction_description'].startswith("Processing Fee 199"):

        interest_amortization.append(transaction)

total = 0
for transaction in interest_amortization:

    print("{}\t{}\t{}\t{}".format(transaction['date'], transaction['transaction_amount'],
          transaction['transaction_type'], transaction['transaction_description']))

    total += decimal.Decimal(transaction['transaction_amount'])

print("Total: {}".format(total))
print("Transactions with Interest Amount Amortization: {}".format(
    len(interest_amortization)))

total = 0

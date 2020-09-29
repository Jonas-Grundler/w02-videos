'My Code'
# Initial balance of the bank account
initial_balance = 200

# Bank statement with all transactions for the past 6 months
statement = [[-119.02, -56.54, 1200, -80, -12.99, -550, -167.90, -5.58, -3.54, -9.99],
             [-138.32, -67.12, 1200, -80, -12.99, -268.10, -550, -92.90, -125.65],
             [-101.44, -48.83, -19.99, -92.12, 1200, -80, -67.33, -12.99, -550, -30.33],
             [-91.98, -45.65, -50, -9.99, 1200, -80, -414.22, -12.99, -550, -9.29, -67.12],
             [-159.53, -27.61, -168.45, 1200, -80, -12.99, -76.94, -550, -28.08, -27.89],
             [-141.97, 1200, -87.78, -80, -12.99, -67.92, -188.09, -550, -4.20, -13.68]]

# Your job: pay monthly 0.5% interest to this account.

# Update the account balance each month: OK!
# Calculate interest each month: OK!
# Pay the total interest (6 months) to the account:
# - pay the total (update the balance for the last month)
# - log that transaction into statement for 6th month.

'Function to get the account balance at the end of each month'
def update_balance(month, starting_balance):
    balance = starting_balance + sum(month)
    return balance

example_month = [100, 200, -300]
example_start = 100
result = update_balance(example_month, example_start)
print(result)

'Returns total interest paid for a given balance, at rate interest_rate (given in %).'
def calculate_interest(balance, interest_rate):
    interest = 0.01 * interest_rate * balance
    return interest

example_balance = 100
example_interest = 5
calculate_interest(example_balance, example_interest)


'Update the clients bank statement with interest payment.''
def update_statement(statement, initial_balance, interest_rate):
    balance = initial_balance
    total_interest = 0

    for month in statement:
        balance = update_balance(month, balance)
        total_interest = total_interest + calculate_interest(balance, interest_rate)

    statement[-1].append(total_interest)
    balance = balance + total_interest

    return total_interest, balance

print(update_statement(statement, initial_balance, 0.5))


'Second Test Example'
statement_2 = [[100, 100], [100, -100], [50, 250]]
balance_2 = 500
print(update_statement(statement_2, balance_2, 5))

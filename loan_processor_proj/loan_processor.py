# Program to approve/deny x number of loans for an applicant based on specific reqs

# import libraries
from time import sleep


# User input and validation functions
def ask_for(data_type, prompt, low, high):
    while True:
        try:
            x = data_type(input(prompt))
            if x < low or x > high:
                print(f"Must print a value between {low} and {high}")
            else:
                return x
        except ValueError:
            print("Invalid value, try again")


def ask_for_str(prompt, valid_values):
    if valid_values is not None:
        lower_valid_values = {value.lower() for value in valid_values}
    while True:
        x = input(prompt)
        if valid_values is None:
            break
        if x.lower() in lower_valid_values:
            break
        else:
            print("You must enter one of the following", valid_values)
    return x


# Loan approval function using validated inputs
def approve_loan(credit_score, dti_ratio, emp_type):
    if credit_score > 700 and dti_ratio <= 0.35 and emp_type != "Unemployed":
        return True
    else:
        return False


# Program Body

loans_to_process = ask_for(
    int, "How many loans would you like to process? Max of 10: ", 0, 10
)

loans_processed_count = 0
for i in range(loans_to_process):
    # Ask the user for their credit score
    credit_score = ask_for(int, "Enter your credit score, 300-850: ", 300, 850)
    print()
    print()

    # Ask the user for DTI Ration
    dti_ratio = ask_for(float, "Enter your Debt to Income Ratio, 0.0-1.0: ", 0.0, 1.0)
    print()
    print()

    # Ask the user for their emplyoment type
    valid_values = ("Full-time", "Part-time", "Self-employed", "Unemployed")
    print("Valid Employment types are", valid_values)

    emp_type = ask_for_str("Enter your employment type: ", valid_values)
    print()
    print()

    # Approve/deny loan
    result = approve_loan(credit_score, dti_ratio, emp_type)

    if result == True:
        print("Result: Your loan has been approved")
    else:
        print("Result: Your loan has been denied.")

    sleep(1.5)

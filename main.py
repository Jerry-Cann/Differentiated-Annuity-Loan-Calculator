import argparse
from math import ceil, log, pow, floor

parser = argparse.ArgumentParser(description="Stage 4")
parser.add_argument("--type")
parser.add_argument("--principal", default=0.0, type=float)
parser.add_argument("--periods", default=0, type=int)
parser.add_argument("--interest", default=0.0, type=float)
parser.add_argument("--payment", default=0.0, type=float)

args = parser.parse_args()


def annuity(interest_a=args.interest, principal_a=args.principal, payment_a=args.payment, periods_a=args.periods):
    # Checking for negatives
    if interest_a * principal_a * payment_a * periods_a < 0:
        return "Incorrect parameters"
    # Checking for correct number of values
    test_list = [interest_a, principal_a, payment_a, periods_a]
    count = 0
    for x in test_list:
        if x == 0.0:
            count += 1
        else:
            continue
    if count >= 2:
        return "Incorrect parameters"

    # Main body of annuity function
    rate_a = interest_a / (12 * 100)
    if not periods_a:
        periods_a = ceil(log(payment_a / (payment_a - rate_a * principal_a), 1 + rate_a))
        overpayment = principal_a - periods_a * payment_a
        print("It will take",
              f"{periods_a} months" if periods_a < 12
              else (f"{int(periods_a // 12)} year" if not periods_a % 12
                    else f"{int(periods_a // 12)} years and {ceil(periods_a % 12)} months"),
              "to repay this loan!")
        return f"Overpayment = {int(abs(overpayment))}"
    if not payment_a:
        payment_a = ceil(principal_a * rate_a * pow(1 + rate_a, periods_a) / (pow(1 + rate_a, periods_a) - 1))
        overpayment = principal_a - periods_a * payment_a
        print(f"Your annuity payment = {payment_a}!")
        return f"Overpayment = {int(abs(overpayment))}"
    if not principal_a:
        principal_a = floor(payment_a / (rate_a * pow(1 + rate_a, periods_a) / (pow(1 + rate_a, periods_a) - 1)))
        overpayment = principal_a - periods_a * payment_a
        print(f"Your loan principal = {principal_a}!")
        return f"Overpayment = {int(abs(overpayment))}"
    else:
        return "Incorrect parameters"


def differ(interest_d=args.interest, principal_d=args.principal, periods_d=args.periods):
    # Checking for correct number of values and negatives
    if interest_d * principal_d * periods_d < 0 or interest_d * principal_d * periods_d == 0:
        return "Incorrect parameters"

    # Main body of differentiated payment function
    rate_d = interest_d / (12 * 100)
    paid = 0
    for i in range(periods_d):
        this_month = ceil(
            principal_d / periods_d + rate_d * (principal_d - principal_d * ((i + 1.0) - 1.0) / periods_d))
        print(f"Month {i + 1}: payment is {this_month}")
        paid += this_month
    overpayment = int(paid - principal_d)
    return f"\nOverpayment = {overpayment}"


# Invoking the functions
if args.type == "diff":
    print(differ())
elif args.type == "annuity":
    print(annuity())
else:
    print("Incorrect parameters")

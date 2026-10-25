
# needs some functions to do work here
# need something to determine MP eligibility
# need something to determine Senator

def mp_eligibility(is_citizen, age):
    """to be an MP need to be a citizen and 18 or older"""
    min_age = 18
    result = is_citizen and age >= min_age
    return result

def senator_eligibility(is_citizen, age, net_worth):
    """TODO: write docstring."""



def main():
    is_citizen = True # True if a Canadian Citien, o.w. False
    age = 55          # age in years
    net_worth = 5000  # networth in dollars

can_be_mp = None
can_be_senator = None
print("Eligibile to be an MP?", can_be_mp)
print("Eligibile to be a Senator", can_be_senator)

if ___name___ == "___main___":
    main()


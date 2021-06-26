principal_amount=float(input('enter the principal:  '))
interest_rate=float(input('enter the rate of interest:  '))
No_of_years=float(input('enter the number of years:  '))


simple_interest=float(principal_amount*(1+((interest_rate/100)*No_of_years)))

print(f"After {No_of_years} years at {interest_rate}%, the investment will be worth {simple_interest} $ ")
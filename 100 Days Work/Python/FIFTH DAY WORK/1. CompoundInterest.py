principle=int(input("Enter the Principle Amount:"))
rate=int(input("Enter the rate of Interest:"))
time=int(input("For how many years:"))
def compound_interest(principle, rate, time):
    CI = principle * (pow((1 + rate / 100), time))
    print("Compound interest is", CI)
compound_interest(principle,rate,time)

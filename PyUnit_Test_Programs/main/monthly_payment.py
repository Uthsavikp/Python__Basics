'''
* @Author: Uthsavi KP
* @Date: 2020-12-29 17:32:32  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-29 17:32:32
* @Title : To Calculate Monthly Payment To Be Made
'''
import math

#To Calculate Monthly Payment
def get_monthly_payment(principal_loan_amount,no_of_years,rate_of_interest):
    
    year_in_months = 12 * no_of_years
    monthly_interest = rate_of_interest/ (12 * 100)

    payment_per_month = round(principal_loan_amount*monthly_interest/ (1 - math.pow((1 + monthly_interest),(-year_in_months))),2)
    print("Amount To Be Paid Every Month Is :", payment_per_month ,"Rupees")
    return payment_per_month
    
if __name__ == "__main__":
    principal_loan_amount = float(input("Enter Loan Mount: "))
    no_of_years = float(input("Enter Number Of Years: "))
    rate_of_interest = float(input("Enter Percentage Of Interest: "))

    get_monthly_payment(principal_loan_amount,no_of_years,rate_of_interest)
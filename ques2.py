"""Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate"""

gross_income=int(input("Enter gross income: "))
std_ded=10000
numb_dep=int(input("Number of dependent: "))
dep_ded=3000
Tax_inc=gross_income-std_ded-(dep_ded*numb_dep)
Tax=Tax_inc/5
print("Taxable Income: ",Tax_inc)
print("Tax: ",Tax)
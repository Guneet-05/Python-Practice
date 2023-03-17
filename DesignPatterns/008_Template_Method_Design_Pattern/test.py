from YoungMaleTaxCalculator import *
from SeniorCitizenTaxCalculator import *

youngMale = YoungMaleTaxCalculator()
print(youngMale.calculateTax(1000000))

oldMan = SeniorCitizenTaxCalculator()
print(oldMan.calculateTax(1000000))
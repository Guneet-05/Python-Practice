from TaxCalculator import *

class SeniorCitizenTaxCalculator(TaxCalculator):
    def applyStandardDeduction(self, income):
        return income - 100000
    
    def applyTaxRate(self, income):
        return income * 0.1
    
    def applySurcharge(self, tax):
        return tax
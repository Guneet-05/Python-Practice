from TaxCalculator import *

class YoungMaleTaxCalculator(TaxCalculator):
    def applyStandardDeduction(self, income):
        return income - 50000
    
    def applyTaxRate(self, income):
        return income * 0.2
    
    def applySurcharge(self, tax):
        return tax * 1.02
from abc import ABC, abstractmethod

class TaxCalculator(ABC):

    def calculateTax(self,income):
        incAfterSD = self.applyStandardDeduction(income)
        tax = self.applyTaxRate(incAfterSD)
        taxAfterSurcharge = self.applySurcharge(tax)
        return taxAfterSurcharge

    @abstractmethod
    def applyStandardDeduction(self,income):
        pass
    
    @abstractmethod
    def applyTaxRate(self,income):
        pass
    
    @abstractmethod
    def applySurcharge(self,tax):
        pass
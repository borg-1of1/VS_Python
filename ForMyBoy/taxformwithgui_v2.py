"""
File: taxformwithgui.py
Project 8.6
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and tax rates of
20% for Single
15% for Married
10% for Divorced
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")

        # Label and field for the income
        # (self.incomeField)
        self.addLabel(text="Gross Income",row=0,column=0)
        self.incomeField = self.addFloatField(value=0.00,row=0,column=1)

        # Label and field for the number of dependents
        # (self.depField)
        self.addLabel(text="Dependents",row=2,column=0)
        self.depField = self.addIntegerField(value=0,row=2,column=1)

        # Radio buttons for filing status
        # Button group (self.statusGroup)
        self.statusGroup = self.addRadiobuttonGroup(row=1,column=2,rowspan=3,columnspan=1)
        # Option for single (self.single)
        self.single = self.statusGroup.addRadiobutton("Single")        
        # Option for married (self.married)
        self.married = self.statusGroup.addRadiobutton("Married")
        # Option for divorced (self.divorced)
        self.divorced = self.statusGroup.addRadiobutton("Divorced")
        defaultRB = self.single
        self.statusGroup.setSelectedButton(self.single)
 
        # The compute button
        self.addButton(text="Compute",row=4,column=0,columnspan=2, command=self.computeTax)      

        # Label and field for the tax
        # (self.taxField)
        self.addLabel(text="Total Tax",row=6,column=0)
        self.taxField = self.addFloatField(value=0.00,row=6,column=1)

    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field (taxField)."""
        standardDeduction = 10000
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        exemptionAmount = 3000
        income = income - standardDeduction
        button = self.statusGroup.getSelectedButton()
        if(button == self.single):
            tr = 0.20
        elif(button == self.married):
            tr = 0.15
        elif(button == self.divorced):
            tr = 0.10
        else:
            tr = 0.2
        tax = (income - numDependents * exemptionAmount) * tr 
        self.taxField.setNumber(tax)
        
def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()


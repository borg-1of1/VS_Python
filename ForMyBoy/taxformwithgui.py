"""
File: taxformwithgui.py
Project 8.1
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and a flat tax rate
of 20%.
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator",width=300, height=150)

        # Label and field for the income        
        self.addLabel(text="Gross Income",row=0,column=0)
        self.incomeField = self.addFloatField(value=0.00,row=0,column=1)

        # Label and field for the number of dependents        
        self.addLabel(text="Dependents",row=2,column=0)
        self.depField = self.addIntegerField(value=0,row=2,column=1)

        # The command button
        self.addButton(text="Compute",row=4,column=0,columnspan=2, command=self.computeTax)

        # Label and field for the tax        
        self.addLabel(text="Total Tax",row=6,column=0)
        self.taxField = self.addFloatField(value=0.00,row=6,column=1)


    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        exemptionAmount = 1 + numDependents
        tax = (income - numDependents * exemptionAmount) * .15
        self.taxField.setNumber(tax)
        
        
def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()


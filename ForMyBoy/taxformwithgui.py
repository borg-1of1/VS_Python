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
        EasyFrame.__init__(self, title = "Tax Calculator")

        # Label and field for the income
        # (self.incomeField)

        # Label and field for the number of dependents
        # (self.depField)

        # The command button

        # Label and field for the tax
        # (self.taxField)

    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""
        pass
        
        
def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()


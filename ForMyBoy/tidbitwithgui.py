"""
File: tidbitwithgui.py
Project 8.7

GUI for tidbit program.

Inputs: purchase price and annual interest rate.
"""

from breezypythongui import EasyFrame

class TidbitGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self, title = "Tidbit Loan Scheduler")
        """Input fields"""
        # self.addLabel()
        # self.priceField()
        # self.addLabel()
        # self.rateField()
        """Command button"""
        # self.button()
        """Output text box"""
        # self.outputArea()

    def computeSchedule(self):
        """Event handler for the Compute button."""
        # Write your code here
        
def main():
    """Instantiate and pop up the window."""
    TidbitGUI().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")


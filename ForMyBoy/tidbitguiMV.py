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
        self.addLabel(text="Purchase Price",row=0,column=0)        
        # self.priceField()
        self.priceField = self.addFloatField(value=0.00,row=0,column=1)
        # self.addLabel()
        self.addLabel(text="Annual Interest Rate",row=1,column=0)
        # self.rateField()
        self.rateField = self.addFloatField(value=0.00,row=1,column=1)
        """Command button"""
        # self.button()
        self.addButton(text="Compute",row=3,column=0,columnspan=2, command=self.computeSchedule)
        """Output text box"""
        # self.outputArea()
        self.outputArea = self.addTextArea(text="",row=5,column=0,rowspan=1,columnspan=2,width=80,height=5)


def main():
    """Instantiate and pop up the window."""
    TidbitGUI().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")
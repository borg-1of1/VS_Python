"""
File: temperatureconverter.py
Project 8.3
Temperature conversion between Fahrenheit and Celsius.
Illustrates the use of numeric data fields.
"""

from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""        
        EasyFrame.__init__(self, title = "Temperature Converter")

        self.addLabel(text = "Celsius",row=0,column=0)
        self.celsiusField = self.addFloatField(value=0.0,row=1,column=0)        
        self.addLabel(text = "Fahrenheit", row=0,column=1)
        self.fahrField = self.addFloatField(value=32.0,row=1,column=1)
        
        self.calcFahr = self.addButton(text=">>>>",row=3,column=0,columnspan=1, command=self.computeFahr)
        self.calcCels = self.addButton(text="<<<<",row=3,column=1,columnspan=1, command=self.computeCelsius)                  
        #self.celsiusField.focus():
        self.celsiusField.bind("<Return>", lambda event: self.computeFahr())
        #self.fahrField.focus():
        self.fahrField.bind("<Return>", lambda event: self.computeCelsius())
    
    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        celcius = self.celsiusField.getNumber()
        fahr = (9 / 5) * celcius + 32
        self.fahrField.setNumber(fahr)
      

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        fahr = self.fahrField.getNumber()
        celcius = (fahr - 32) * (5/9)
        self.celsiusField.setNumber(celcius)
        
def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()


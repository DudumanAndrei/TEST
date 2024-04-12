'''
Module containing classes and functions to work with Romanian license plates.
'''

#Add validation

class RoLicensePlate:
    countyArray = ["AR", "BH", "SM", "TM", "CS", "HD", "AB", "CJ", "SJ", "MM", "MH", "GJ", "VL", "SB", "MS", "BN", "SV", "NT", "BC", "CV", "HR", "BV", "PH", "OT", "DJ", "TL", "DB", "AG", "BZ", "B", "IF", "IL", "CL", "CT", "TL", "GL", "BR", "VN", "VS", "IS", "BT", "GR"]
    print(len(countyArray))  
    flagValidCounty = True
    
    def __init__(self, license_str:str) -> None:
        '''
        Initialies a RoLicensePlate instance from a license number given as string.
        License string may or may not contain spaces.
        '''
        
        self.county = ""
        self.numbers = ""
        self.letters = ""
        
        
        #1) Normalize inputs by removing spaces.
        #2) Iterate character by character over the string
        #   2.1) First letters will be the county code
        #   2.2) After county code, you have the numbers
        #   2.3) After the numbers, we have the letters
        
        license_str = license_str.replace(" ", "")
        #print(license_str)
        found_county = False
        
        for i in license_str:
            if i.isalpha():
                if not found_county:
                    self.county +=i
                else:
                    self.letters +=i
            elif i.isdigit():
                found_county = True
                self.numbers +=i 
        
        self.numbers = int(self.numbers)
      
          
    def validCounty(self, countyArray):
        flagValidCounty = False
        for county in countyArray:
            if self.county == county:
                flagValidCounty = True
                break

        if not flagValidCounty:
            print("This license plate has a wrong County identifier")

        return flagValidCounty


    
    
        
    def __repr__(self):
        return f"<RoLicensePlate county={self.county}, numbers={self.numbers}, letters={self.letters}"
                
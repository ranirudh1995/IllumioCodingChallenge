# references:- https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/

class port:
    def __init__(self, portString):
        self.portString = portString
    
    # function to check if the given port string is single number or a range
    def isPortRange(self):
        if "-" in self.portString:
            return True
        return False
    
    # return the port values if range or else return just a single port number
    def portValues(self):
        if self.isPortRange():
            portNumbers = self.portString.split('-')
            for portNumber in range(int(portNumbers[0]),int(portNumbers[1])+1):
                yield int(portNumber)
        else:
            yield int(self.portString)
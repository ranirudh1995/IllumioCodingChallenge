class ipAddress:
    def __init__(self, ipAddressString):
        self.ipAddressString = ipAddressString
        
    # function to check if the given ipAddress string is single IP or a range
    def isIpAddressRange(self):
        if "-" in self.ipAddressString:
            return True
        return False
    
    # IP is represented by a tuple of 4 integer elements. return the 2 IPs, both same if the given ipString is not a range else return the given range 
    def ipAddressRange(self):
        if self.isIpAddressRange():
            ipRange = self.ipAddressString.split('-')
            return (tuple(map(lambda x:int(x),ipRange[0].split('.'))),tuple(map(lambda x:int(x),ipRange[1].split('.'))))
        else:
            address = self.ipAddressString.split('.')
            return (tuple(map(lambda x:int(x),address)),tuple(map(lambda x:int(x),address)))
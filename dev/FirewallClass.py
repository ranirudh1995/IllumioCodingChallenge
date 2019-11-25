from portClass import port
from ipAddressClass import ipAddress

class Firewall:
    def __init__(self, inputRulesFilePath):
        self.firewallRules = {} # dictionary maintaining a mapping of port and its corresponding address information for a (direction, protocol) tuple
        self.allowedProtocols = ["tcp","udp"]
        self.allowedDirections = ["inbound", "outbound"]
        with open(inputRulesFilePath,'r') as file:
            for rule in file:
                (direction, protocol, portString, ipAddressString) = rule.strip().split(',')
                self.addRule(direction, protocol, portString, ipAddressString)
    
    # function to add a rule present in the file
    def addRule(self, direction, protocol, portString, ipAddressString):
        self.firewallRules[(direction,protocol)] = {}
        portObject = port(portString) # port class object
        ipAddressObject = ipAddress(ipAddressString) # ipAddress class object
        ipAddressRange = ipAddressObject.ipAddressRange()
        for portNumber in portObject.portValues():
            if portNumber not in self.firewallRules:
                self.firewallRules[(direction,protocol)][portNumber] = [ipAddressRange]
            else:
                self.firewallRules[(direction,protocol)][portNumber].append(ipAddressRange)
                
        
    def accept_packet(self, direction, protocol, portString, ipAddressString):
        # if a given protocol or direction or port is not in rules given then return False
        if (portString not in self.firewallRules[(direction,protocol)]) or (direction not in self.allowedDirections) or (protocol not in self.allowedProtocols):
            return False
        elif portString in self.firewallRules[(direction,protocol)]:
            ipAddressRangeList = self.firewallRules[(direction,protocol)][portString]
            for ipAddressRange in ipAddressRangeList:
                lowerIP = ipAddressRange[0]
                upperIP = ipAddressRange[1]
                ipAddressTemp = ipAddressString.split('.')
                for i in range(len(ipAddressTemp)):
                    ipElement = int(ipAddressTemp[i])
                    if ipElement>=lowerIP[i] and ipElement<=upperIP[i]:
                        continue
                    else:
                        return False
                return True # return True only if the given ipAddress is equal to or in the range of ipAddress corresponding to that port
        return False
import unittest
from unittest import TestCase
import sys
# references:- https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
sys.path.append('../dev/')
from FirewallClass import Firewall

class TestFirewall(TestCase):
    def testBasicFunctionality(self):
        firewall = Firewall("testCases.csv")
        self.assertTrue(firewall.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
        self.assertTrue(firewall.accept_packet("inbound", "udp", 53, "192.168.2.1"))
        self.assertTrue(firewall.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
        self.assertTrue(firewall.accept_packet("outbound", "udp", 13, "192.192.192.1"))
        self.assertTrue(firewall.accept_packet("outbound", "udp", 12, "192.192.192.1"))
        self.assertTrue(not firewall.accept_packet("outbound", "udp", 13, "192.192.192.2"))
        self.assertTrue(not firewall.accept_packet("outbound", "tcp", 13, "192.192.192.1"))
        self.assertTrue(not firewall.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
        self.assertTrue(not firewall.accept_packet("inbound", "udp", 24, "52.12.48.92"))
        self.assertTrue(not firewall.accept_packet("inbound", "udp", 53, "52.12.48.92"))
if __name__ == '__main__':
    unittest.main()
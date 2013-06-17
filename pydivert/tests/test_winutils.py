import socket
import unittest
from pydivert.winutils import addr_to_string, string_to_addr

__author__ = 'fabio'


class WinInetTestCase(unittest.TestCase):

    def test_ipv4_loopback_conversion(self):
        """
        Tests IPv4 loopback address conversions
        """
        address = "127.0.0.1"
        addr_fam = socket.AF_INET
        self.assertEqual(address, addr_to_string(addr_fam, string_to_addr(addr_fam, address)))

    def test_ipv6_loopback_conversion(self):
        """
        Tests IPv6 loopback address conversions
        """
        address = "::1"
        addr_fam = socket.AF_INET6
        ipv6 = addr_to_string(addr_fam, string_to_addr(addr_fam, address))
        self.assertIn(ipv6, "::1")

    def test_ipv4_address_conversion(self):
        """
        Tests IPv4 address conversions
        """
        address = "192.168.1.1"
        addr_fam = socket.AF_INET
        self.assertEqual(address, addr_to_string(addr_fam, string_to_addr(addr_fam, address)))

    def test_ipv6_address_conversion(self):
        """
        Tests IPv6 address conversions
        """
        address = "2607:f0d0:1002:0051:0000:0000:0000:0004"
        addr_fam = socket.AF_INET6
        ipv6 = addr_to_string(addr_fam, string_to_addr(addr_fam, address))
        self.assertIn(ipv6, (address, "2607:f0d0:1002:51::4"))

    def test_ipv4_wrong_address_family(self):
        """
        Tests IPv4 address conversions
        """
        address = "192.168.1.1"
        addr_fam = -1
        self.assertRaises(ValueError, string_to_addr, addr_fam, address)
        addr = string_to_addr(socket.AF_INET, address)
        self.assertRaises(ValueError, addr_to_string, addr_fam, (addr,))

    def test_ipv6_wrong_address_family(self):
        """
        Tests IPv6 address conversions
        """
        address = "2607:f0d0:1002:0051:0000:0000:0000:0004"
        addr_fam = -1
        self.assertRaises(ValueError, string_to_addr, addr_fam, address)
        addr = string_to_addr(socket.AF_INET6, address)
        self.assertRaises(ValueError, addr_to_string, addr_fam, addr)
# Given a valid (IPv4) IP address,
# return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"


class Solution:
    def defangIPaddr(self, address: str) -> str:
        defangAddr = address
        return defangAddr.replace('.', '[.]')


ip = Solution('192.168.0.27')
print(ip.defangIPaddr())
# print(ip.defangIPaddr('192.168.0.27'))

# defanging-an-ip-address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_list = address.split('.')
        return '[.]'.join(address_list)

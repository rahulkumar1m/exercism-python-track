import re

class PhoneNumber:
    def __init__(self, number: str):
        self.pattern = re.compile(r'^\+?1?(?:[-. ]+)?\(?([2-9]\d{2})\)?(?:[-. ]+)?([2-9]\d{2})(?:[-. ]+)?(\d{4})$')
        try:
            self.area_code, self.exchange, self.subscriber = \
                self.pattern.search(number.strip()).groups()
        except:
            raise ValueError('Invalid `phone number`')
        self.number = self.area_code + self.exchange + self.subscriber
    
    def pretty(self)-> str:
        return f'({self.area_code})-{self.exchange}-{self.subscriber}'

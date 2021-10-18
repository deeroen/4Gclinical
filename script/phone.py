class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.digits = self.create_digits()

    def create_digits(self):
        """
        Remove duplicates digits and returns a set of digits if valid phone number
        :return: eg. {"3","4","5"}
        """
        if not self.number.isnumeric():
            raise(ValueError)
        return set(self.number)

    def get_digits(self):
        return self.digits

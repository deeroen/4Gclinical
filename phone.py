class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.digits = self.create_digits()

    def create_digits(self):
        """
        Remove duplicates digits and returns a set of digits if valid phone number
        :return: eg. "345"
        """
        if not self.number.isnumeric():
            print("Oops!  That was no valid phone number.  Try again...")
            exit(-1)
        return set(self.number)

    def get_digits(self):
        return self.digits

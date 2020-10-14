import math

# This class is for handling Binary inputs and ultimately converting them
class Binary:
    def __init__(self, number):
        self.number_int = int(number)
        self.number_str = str(number)

    def convert_to_list(self):
        string_list = []
        string_list[:0] = self.number_str
        return string_list

    def number_of_bits(self):
        bits = 0
        for i in self.convert_to_list():
            bits += 1
        bytes = bits / 8
        return bits, bytes

    def reverse_order(self):
        x = self.convert_to_list()
        y = []
        for i in range(len(x)):
            y.append(x.pop())
        return y

    def create_bin_dict(self):
        working_list = self.reverse_order()
        exponent_list = []
        counter = 0
        for i in range(len(working_list)):
            exponent_list.append(counter)
            counter += 1
        bin_dict = dict(zip(exponent_list, working_list))
        return bin_dict

    def calculate_dec(self):
        the_conversion = 0
        the_dict = self.create_bin_dict()
        dict_list = the_dict.items()
        for i in dict_list:
            if i[1] == '0':
                the_conversion += 0
            elif i[1] == '1':
                x = int(i[0])
                y = 2**x
                the_conversion += y
            else:
                continue
        return the_conversion

# This class is for handling Decimal inputs and ultimately converting them
class Decimal:
    def __init__(self, number):
        self.number_int = int(number)
        self.number_str = str(number)
        self.bits_reqd = int(math.log(self.number_int, 2))

    def bit_counter(self):
        bit_count = []
        bit_counter = 0
        while bit_counter <= self.bits_reqd:
            bit_count.append(bit_counter)
            bit_counter += 1
        return bit_count

    def reverse_order_bit_counter(self):
        x = self.bit_counter()
        y = []
        for i in range(len(x)):
            y.append(x.pop())
        return y

    def calculate_bin(self):
        base = 2
        bit_list = [base ** i for i in self.reverse_order_bit_counter()]
        checker = self.number_int
        for i in bit_list:
            idx = bit_list.index(i)
            if checker - bit_list[idx] >= 0:
                checker -= bit_list[idx]
                bit_list[idx] = str(1)
            else:
                bit_list[idx] = str(0)
        x = ''
        the_conversion = x.join(bit_list)
        return the_conversion

def classify_and_convert():
    conversion_setting = input('Will you be converting a binary number (b) or a decimal (d)?\n')
    if conversion_setting == 'b':
        user_input = input('Please enter the number you would like to convert below:\n')
        classify = Binary(user_input)
        for i in classify.convert_to_list():
            if i == '1':
                continue
            elif i == '0':
                continue
            else:
                classify = classify_and_convert()
                return classify.calculate_dec()
        return classify.calculate_dec()
    elif conversion_setting == 'd':
        user_input = input('Please enter the number you would like to convert below:\n')
        classify = Decimal(user_input)
        if isinstance(classify.number_int, int):
            return classify.calculate_bin()
        else:
            classify = classify_and_convert()
            return classify.calculate_bin()
    else:
        print('You somehow messed this up really bad...¯\\_(o.o)_/¯...You\'re going to have to relaunch this program. Sorry!')

x = classify_and_convert()

print('The number you entered converts to {0}'.format(x))
import logging

class Lists:
    logging.basicConfig(filename="list.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

    def __init__(self, l):
        self.l = l

    def reverse_list(self): # try to print the elements in reverse order
        try:
            logging.info('Given list will be printed in reverse order')
            return self.l[::-1]
        except Exception as e:
            logging.error('Error occurred, please check the given output')
            print(e)

    def check_value(self, value, data): # try to check the values in the list
        if isinstance(data, list) or isinstance(data, tuple):
            for i in data:
                if self.check_value(value, i):
                    return True
        elif isinstance(data, dict):
            for item in data.values():
                if self.check_value(value, item):
                    return True
        elif data == value:
            return True
        return False

    def access(self, value):
        try:
            logging.info(f'Trying to access the value {value} in the list')
            if self.check_value(value, self.l):
                return value
            else:
                raise ValueError('The given value does not exist in the list')
        except Exception as e:
            print('Error:', e)

    def extract_list(self):
        try:
            logging.info('Extracting list elements from the list')
            for i in self.l:
                if type(i)==list:
                    print(i)
        except Exception as e:
            print("There are no list elements in the list")
            print(e)
    def extract_dic(self):
        try:
            logging.info("Extracting teh dictionary elements from the list")
            for i in self.l:
                if type(i)==dict:
                    print(i)
        except Exception as e:
            print("There are no dictionary elements in the list")
            print(e)

    def extract_dict_key_list(self):
        try:
            l2=[]
            logging.info('Extracting the keys from the list')
            for i in self.l:
                if (type(i)==dict):
                    l2.append(i.keys())
            return l2
        except Exception as e:
            print(e)
            print('Error occured')
            logging.exception('The exception that we have got: '+'\n'+str(e))

    def extract_dict_value_list(self):
        try:
            logging.info('Extracting the key values from the list')
            for i in self.l:
                if type(i)==dict:
                    print(i.values())
        except Exception as e:
            print(e)
            print("Error occured")
            logging.exception("The exception that we have got:"+'\n'+str(e))



l1 = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6), {"key1": "sudh", 234: [23, 45, 656]}]

l_var = Lists(l1)

reversed_list = l_var.reverse_list()
print(reversed_list)

value_to_access = 234
accessed_value = l_var.access(value_to_access)

print(accessed_value)

l_var.extract_list()

dict_key=l_var.extract_dict_key_list()
print(dict_key)

dict_values=l_var.extract_dict_value_list()
print(dict_values)

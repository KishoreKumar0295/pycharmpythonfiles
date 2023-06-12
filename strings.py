import logging

logging.basicConfig(filename="string.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class strings_operations:
    """
    This class performs different tasks on strings.
    """

    def extract_data(self, s):
        """
        Task-1: Try to extract data from index one to index 300 with a jump of 3
        :param s: input string
        :return: slices the string s with a step of 3 starting from index 1 and ending at index 300
        """
        try:
            logging.info('Extracting the strings with a jump of 3 between index 1 to 300')
            s1 = s[1:300:3]
            return s1
        except Exception as e:
            print(e)
            print('Error occurred')

    def r_string(self, s):
        """
        TASK-1's task
        2 . Try to reverse a string without using reverse function
        :param s: input string
        :return: reverses the given string
        """
        try:
            s1=s[::-1]
            logging.info('The given string will be print in reverse order')
            return s1
        except Exception as e:
            print(e)
            logging.error('Please check the string value {s} once')

    def s_upper(self, s):
        """
        TASK-1's task
        3. Try to split a string after conversion of entire string in uppercase
        :param s: input string
        :return: it returns a list of string. which were converted to uppercase and then splitted using split().
        """
        try:
            s3=s.upper()
            logging.info('The given string will be print in upper case letters')
            return s3
        except Exception as e:
            print(e)
            logging.warning("Error occured")

    def lower_string(self, s):
        """
        TASK-1's task
        4. try to convert the whole string into lower case
        :param s: input string
        :return: return the given string with all characters in lowercase
        """
        try:
            s4=s.lower()
            logging.info('The given strings all will be print in lower cases only')
            return s4
        except Exception as e:
            print(e)
            logging.error("please check the string once")

    def cap_string(self, s):
        """
        TASK-1's task
        5 . Try to capitalize the whole string
        :param s: input string
        :return: return the given string in capitalize form
        """
        try:
            s5=s.capitalize()
            logging.info('The given strings first letter will be in capital letter only')
            return s5
        except Exception as e:
            print(e)
            logging.error('Error occured',s)
    def expandtabs(self,s):
        """TASK-1's task
            7. Try to give an example of expand tab
            :param s: input string
            :return: returns the given string with tab spaces
            """
        try:
            s6=s.expandtabs()
            logging.info("The given string for this operation is %s", s)
            return s6
        except Exception as e:
            print(e)
            logging.error('Error occured')
    def strips(self,s):
        """
               TASK-1's task
               8.(i) Give an example of strip
               :param s: input string
               :return: returns the given string with stripping the extra spaces present on its left and right side
               """
        try:
            s7=s.strip()
            logging.info("It will remove the unwanted spaces in the given strings left and right")
            return s7
        except Exception as e:
            print(e)
            logging.error()
    def lstrips(self,s):
        """
                TASK-1's task
                8.(i) Give an example of lstrip
                :param s: input string
                :return: returns the given string with stripping the extra spaces present on its left side
                """
        try:
            s8=s.lstrip()
            logging.info("It will remove the unwanted spaces in left side")
            return s8
        except Exception as e:
            print(e)
            logging.error('Error occured')
    def rstrips(self,s):
        """
                TASK-1's task
                8.(i) Give an example of lstrip
                :param s: input string
                :return: returns the given string with stripping the extra spaces present on its right side
                """
        try:
            s8=s.rstrip()
            logging.info("It will remove the unwanted spaces in left side")
            return s8
        except Exception as e:
            print(e)
            logging.error('Error occured')
    def replace_part_string(self,s):
        """
               TASK-1's task
               9.  Replace a string charecter by another charector by taking your own example
               :param s: input string
               :param pr: the part we want to replace
               :param tr: with what we want to replace
               :return:
               """
        try:
            s9=s.replace('tasks','Takes')
            logging.info('Replaceing the old text with new texts')
            return s9
        except Exception as e:
            print(e)
            logging.error('Error occured')
    def fill_space_with_special_charecters(self,s):
        """
                TASK-1's task
                10 . Try  to give a defination of string center function with and exmple
                :param s: input string
                :return: returns a strings with a fixed length and fills the characters if exists in header or trailer parts of string
                keeping the string at the center.
                """
        try:
            s10=s.center(50,'*')
            logging.info('It will print the special charecters in given space as per this function')
            return s10
        except Exception as e:
            print(e)
            logging.error("Errorc occered")

s1 = 'This is my own task which is related to the string tasks in PyCharm workspace using exceptions and logging in OOPs'
s2= '       The best teached i have meet in my life is MR.Sudhanshu sir Thank you for your dedication sir      '
s3='sudhnashu@ineuron.ai'
s_var = strings_operations()

data_extract_jump = s_var.extract_data(s1)
print(data_extract_jump)

reverse_string=s_var.r_string(s1)
print(reverse_string)

c_var=s_var.s_upper(s1)
print(c_var)

l_var=s_var.lower_string(s1)
print(l_var)

cap_var=s_var.cap_string(s1)
print(cap_var)

ex_tab=s_var.expandtabs(s1)
print(ex_tab)
stip_var=s_var.strips(s2)
print(stip_var)

l_strip_var=s_var.lstrips(s2)
print(l_strip_var)

r_strip_var=s_var.rstrips(s2)
print(r_strip_var)

replace_var=s_var.replace_part_string(s1)
print(replace_var)

sp_char=s_var.fill_space_with_special_charecters(s3)
print(sp_char)
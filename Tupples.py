import logging
logging.basicConfig(filename="tupples.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s  %(message)s')


class tuple_task:
    logging.info("class for tuple task")

#extract the tuples from list
    def ext_tuple(self,list_):
        logging.info("It will extract the Tupples from list ")
        self.list_ = list_
        try:
            if len(list_) ==0:
                raise Exception("This list is empty  ")
                logging.error("This list is empty")
            else:
                for i in list_:
                    if type(i) ==tuple:
                        logging.info("found Tupple in list ", i)
                        return i
                    else:
                        logging.error("There is no Tuple in list with in list")
        except Exception as e:
            logging.exception(e)

l1 = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6), {"key1": "sudh", 234: [23, 45, 656]}]

t_var = tuple_task()
e_t_var=t_var.ext_tuple(l1)
print(e_t_var)

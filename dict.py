import logging

logging.basicConfig(filename="dict.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s  %(message)s')


class dict_task:
    logging.info("class for dict task")

#extract the dictfrom list
    def ext_dict(self,list_):
        logging.info("this is the extact dict from list ")
        self.list_ = list_
        try:
            if len(list_) ==0:
                raise Exception("list is empty  ")
                logging.error("list is empty")
            else:
                for i in list_:
                    if type(i) ==dict:
                        logging.info("found dict in list ", i)
                        for j in i.items():
                            logging.info("found dict in list %s ", j)
                            return j
                else:
                    logging.error("no dictin list withi in ist")
        except Exception as e:
            logging.exception(e)



l1 = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6), {"key1": "sudh", 234: [23, 45, 656]}]

d_var = dict_task()
e_d_var=d_var.ext_dict(l1)
print(e_d_var)

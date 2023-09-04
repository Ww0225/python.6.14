import json
import random

var_1 : int = 10
var_2 : str = "ww"
var_3 : bool = True

class Student:
    pass
stu : Student = Student()

my_list : list = [1,2,3]
my_tuple : tuple = (1,2,3)
my_dict : dict = {"ww",666}

my_list : list[int] = [1,2,3]
my_tuple : tuple[int] = (1,2,3)
my_dict : dict[str,int] = {"ww",666}

var_1 = random.randint(1,10)  # type: int
var_2 = json.loads('{"name":"zhangsan"}') # type: dict[str,str]


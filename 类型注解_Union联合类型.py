from typing import Union
my_list: list[Union[int,str]] = [1,2,"ww"]

def func(data: Union[int,str]) -> Union[int,str]:
    pass

func()
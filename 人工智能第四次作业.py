# today = "sunny"
#
# if today == "sunny":
#     shopping = True
#     print("今天是晴天，我会去购物。")
#     if shopping:
#         print("我去购物了，所以我买了奶茶。")
# else:
#     print("今天不是晴天，我不会去购物。")
classical_logic = {
    "所有的金属都有光泽": True,
    "铁是一种金属": True
}

if classical_logic["所有的金属都有光泽"] and classical_logic["铁是一种金属"]:
    print("根据三段论推理，铁有光泽。")
else:
    print("无法推断铁是否有光泽。")
dict_graph = {
    "a":["b","d","f"],
    "b":["c","e"],
    "c":["d","e"],
    "d": ["e"],
    "f":["c","g","h"],
    "g":["f","h","i"],
    "h":["e","f","i"],
    "i": ["h"]
}
search_node = input("请输入你要查询的节点：")
if search_node in dict_graph:
    all_in_search_node = [node for node,bro in dict_graph.items() if search_node in bro]
    all_out_serarch_node = list(dict_graph.get(search_node,set()))
    for o in all_out_serarch_node:
        print(f"{search_node}-->{o}")
    for i in all_in_search_node:
        print(f"{i}-->{search_node}")
    in_degree = sum(1 for bro in dict_graph.values() if search_node in bro)
    out_degree = len(dict_graph.get(search_node,set()))
    print(f"入度：{in_degree}   出度：{out_degree}")
else:
    print("你要查询的节点不存在")

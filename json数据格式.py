import json
data = [{"name":"张大山","age":11},{"name":"ww","age":18}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

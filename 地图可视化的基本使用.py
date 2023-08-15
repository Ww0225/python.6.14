from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()

data = [
    ("北京",99),
    ("上海",199),
    ("湖南",299),
    ("台湾",399),
    ("广东",499)
]

map.add("测试地图",data,"china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True
    )
)
map.render()
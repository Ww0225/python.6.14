# “集体过马路”是网友对集体闯红灯现象的一种调侃，即“凑够一撮人就可以走了，与红绿灯无关。
# ”出现这种现象的原因之一是很多人认为法不责众，从而不顾交通法规和安全，但这种危险的过马路方式造成了很多不同程度的交通事故和人员伤亡。
# 现通过调查形式对过马路进行测试，在所有参考调查的市民中，“从不闯红灯”、“跟从别人闯红灯”、“带头闯红灯”的人数如下表所示，针对这组调查数据，
# 使用Python扩展库pandas、matplotlib编程实现绘制柱状图进行展示和对比。
# 性别	从不闯红灯  跟从别人闯红灯	带头闯红灯
# 男	450	          800	      200
# 女	150	          100	      300
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\SimSun.ttc')
plt.legend(prop=myfont)
df = pd.DataFrame({'男':(450,800,200),'女':(150,100,300)})
df.plot(kind='bar',color=['red','blue'])
plt.xticks([0,1,2],['从不闯红灯','跟从别人闯红灯','带头闯红灯'],color='black',fontproperties=myfont)
plt.yticks(list(df['男'].values)+list(df['女'].values))
plt.ylabel('人数',fontproperties=myfont,fontsize=14)
plt.title('集体过马路方式',fontproperties=myfont,fontsize=20)
plt.show()
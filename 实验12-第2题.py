# 使用jieba库提取《西游记》中的关键字（50个），并使用wordcloud库实现统计《西游记》人物出现次数，并生孙悟空蒙层词云图。
# 操作方法与步骤：
# （1）导入jieba结巴库，使用该库相关的函数实现《西游记》中关键字（可连同词性）的提取，并打印输出。
# （2）调用wordcloud库中的Wordcloud类以及generator方法实现词云类的生成，以及词云的显示，注意使用mask参数实现蒙层的设置。
# 过程代码截图如下：
import jieba.analyse
file = open('image/西游记.txt',encoding='gbk')
str = file.read()
file.close()
jieba.analyse.set_stop_words('image/stopwords.txt')
rs1 = jieba.analyse.textrank(str,50,False,('nr',))
print(rs1)
import wordcloud
import jieba.posseg
import imageio.v2 as imageio
word_list = jieba.posseg.lcut(str)
word_times = {}
name_list = []
stop_word = []
for i in word_list:
    if i.flag == 'nr':
        word_times[i.word] = word_times.get(i.word,0) + 1
        name_list.append(i.word)
    else:
        stop_word.append(i.word)
text=' '.join(name_list)
maskimage = imageio.imread(r'image\孙悟空.jpg')
cloud=wordcloud.WordCloud(font_path='simsun.ttc',background_color='white'
                           ,stopwords=stop_word,collocations=False,max_words=50
                           ,width=640,height=480,mask=maskimage).generate(text)  	#generate()内的对象必须是一个字符串，生成词云
file = cloud.to_file(r'C:\Users\28953\Desktop\python实验报告\wordcloud.png')

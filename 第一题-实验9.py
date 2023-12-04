# “record.txt”文件有3段对话,分别用“=========……”分隔，请对老师下发的“record.txt”文件，进行编程，实现以下功能：
# (1)、要根据不同的角色（小甲鱼、小客服），将每段对话内容分别存入对应的文件中；
# (2)、小甲鱼的说话内容存入boy_1，boy_2......文件中去；
# (3)、小客服的说话内容存入girl_1，girl_2......文件中去；
# (4)、请定义函数完成，完成后，将会生成6个文件，如下图所示：
# (5)、统计并输出record.txt文本文件中对话内容最长那一行的对话内容长度以及该行的内容。
def open_read_file(filename):
    with open(filename,mode='r',encoding='gbk') as of:
        jiayu_word = []
        kefu_word = []
        count = 1
        for line in of.readlines():
            if '===' not in line:
                if line[0:3] == '小甲鱼':
                    jiayu_word.append(line)
                elif line[0:3] == '小客服':
                    kefu_word.append(line)
            else:
                save_file(jiayu_word,kefu_word,count)
                count += 1
                jiayu_word = []
                kefu_word = []

def save_file(data1,data2,count):
    boy_file = '第一题/boy_' + str(count) + '.txt'
    girl_file = '第一题/girl_' + str(count) + '.txt'
    with open(boy_file,'w',encoding='gbk') as f1:
        f1.writelines(data1)
    with open(girl_file, 'w', encoding='gbk') as f2:
        f2.writelines(data2)

def max_length(filename):
    with open(filename,mode='r',encoding='gbk') as of:
        speak_ans = []
        for line in of.readlines():
            if '===' not in line:
                speak_ans.append(line)
        sort_speak = sorted(speak_ans,key=lambda x:len(x))
        print(f'最长的一句话为：{sort_speak[-1]}')
        print(f'长度为：{len(sort_speak[-1])}')

if __name__ == '__main__':
    open_read_file("record.txt")
    max_length("record.txt")
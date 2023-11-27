# 编写函数，实现将数据经MD5（需要导入hashlib模块）加密返回给调用端。
# 主函数实现读取输入的用户名称和密码，调用加密函数，实现对用户名、密码加密输出结果。
def encrypt(user,passwd):
    import hashlib
    user_md = hashlib.md5()
    user_md.update(user.encode('utf-8'))
    passwd_md = hashlib.md5()
    passwd_md.update(passwd.encode('utf-8'))
    print(f"未加密用户名:{user}")
    print(f"未加密密码:{passwd}")
    print(f"已加密用户名:{user_md.hexdigest()}")
    print(f"已加密密码:{passwd_md.hexdigest()}")

if __name__ == '__main__':
    user = input("请输入用户名:")
    passwd = input("请输入密码:")
    encrypt(user,passwd)
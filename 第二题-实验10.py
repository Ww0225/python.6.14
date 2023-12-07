# 使用Python面向对象编程实现产品以及仓库的库存管理的相关应用。
# （1）关于产品Product类:
# 实例属性：id、名称、价格库、存数量。
# 实例方法：实现产品信息数据的输出。
# （2）关于库存Stock类:
# 存储各种产品数据
# 管理各种产品，包括增加库存（现有产品的库存，新产品的库存），修改现有产品存储，查询库存），并能实现计算现所有库存产品的总价值。
class Product():
    def __init__(self,id,name,price,num):
        self.id = id
        self.name = name
        self.price = price
        self.num = num

    def print_product(self):
        print(f"产品id为：{self.id}，名字为：{self.name}，价格为：{self.price}，存数量为：{self.num}")

class Stock():
    goods = []

    def add(self,product):
        self.goods.append(product)

    @staticmethod
    def searchid(product_id):
        for product in Stock.goods:
            if product_id == product.id:
                return True
        return False

    @staticmethod
    def searchname(product_name):
        for product in Stock.goods:
            if product_name == product.name:
                return True
            return False

    def list_one(self,information):
        for product in self.goods:
            if information == product.id or information == product.name:
                product.print_product()
                break
        else:
            print(f"找不到关于 {information} 的产品...")

    def list_all(self):
        for product in self.goods:
            product.print_product()

if __name__ == '__main__':
    p1 = Product('1001','cafe',9.9,100)
    p2 = Product('1002','bread',6.6,200)
    stock = Stock()
    stock.add(p1)
    stock.add(p2)

    search_name = input("请输入你要查找产品的名字：")
    search_id = input("请输入你要查找产品的编号：")
    print(f"{search_name} 产品的存在情况：",stock.searchname(search_name))
    print(f"{search_id} 产品的存在情况：",stock.searchid(search_id))

    stock.list_one('bread')
    print("所有的产品：")
    stock.list_all()
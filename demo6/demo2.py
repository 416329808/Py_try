import sys
class product:
    name=""
    in_num=0
    storage=0
    in_price=0
    sold_num=0
    sold_price=0
    in_sum=0
    out_sum=0
    def show(self):
        if self.storage>0:
            print("商品名称：",self.name,"商品库存：",self.storage)
    def __init__(self,name,in_num,in_price):
        self.name=name
        self.in_num=in_num
        self.storage=in_num
        self.in_price=in_price
        self.in_sum=in_num*in_price
    def sold(self,sold_num,sold_price):
        if sold_num>self.storage:
            print("出售数目大于库存！")
        else:
            self.sold_num+=sold_num
            self.storage -= sold_num
            self.out_sum += sold_num * sold_price
    def show_soldproduct(self):
        if self.sold_num>0:
            print("商品名称：",self.name,"商品库存：",self.storage,"进货总价：",self.in_sum,"销售总价：",self.out_sum)
if __name__ == "__main__":
    def showmenu():
        print("1. 查询所有商品；2.增加新的商品；3.卖出商品；4.删除商品；5.汇总；-1.退出。")
        option = int(input("Please input a value listed above:"))
        if option == 1:
            for item in product_list:
                item.show()
        if option == 2:
            name=input("Please input the name of the product:")
            in_num=int(input("Please input the number of the product:"))
            in_price=int(input("Please input the buy in price of the product:"))
            new_product=product(name,in_num,in_price)
            product_list.append(new_product)
        if option == 3:
            name=input("Please input the name of the sold-out product:")
            sold_num=int(input("Please input the quantity:"))
            sold_price=int(input("Please input the sold out price:"))
            for item in product_list:
                if item.name == name:
                    item.sold(sold_num,sold_price)
        if option == 4:
            name=input("Please input the name of the product you want to delete:")
            for item in product_list:
                if item.name == name:
                    item.storage=0
        if option == 5:
            for item in product_list:
                item.show_soldproduct()
        if option == -1:
            sys.exit()
    product_list=[]
    a=product("test",0,0,)
    product_list.append(a)
    while True:
        showmenu()

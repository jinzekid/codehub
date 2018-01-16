# Author: Jason Lu

int_userStatus = 0
# 购物车list
list_cart = []
# 输入用户工资
salary_user = int(input("Your salary:"))
# 商品列表
list_products = [['Iphone', 5800],
                 ['Mac Pro', 12000],
                 ['Starback Latte', 31],
                 ['Alex Python', 81],
                 ['Bike', 800]]

while True:

    # 输出商品列表
    print("\n============Product List============\n")
    for idx, product in enumerate(list_products):
        print(idx+1, product[0], product[1])

    print(len(list_products) + 1, "Input Q to Quit!")
    print("\n============End of Product List============\n")


    # 提示用户输入需要选购的商品序号
    input_productId = int(input(">>>:"))
    if input_productId == len(list_products)+1:
        print("quit shopping...")
        break

    if input_productId - 1 < 0:
        print("没有商品序列号，请重新输入!!!")
        continue

    # 获取输入商品信息和价格
    product_detail = list_products[input_productId-1]
    product_info = '''
        choose product name:{_pname} and price:{_price}
    '''.format(_pname=product_detail[0], _price=product_detail[1])
    print(product_info)

    # 判断工资是否大于商品价格
    if salary_user >= int(product_detail[1]):
        cart_info = '''
                add [{_pname}] to your shoppint cart
            '''.format(_pname=product_detail[0])
        print(cart_info)
        list_cart.append(product_detail)
    else:
        print("Not enough salary to buy the product!!")

    # 提示用户是否继续购买
    while True:
        print("\n========================\n")
        print("1. Continue Shopping")
        print("2. Quit")
        int_userinput = int(input("Your choice is:"))

        print("\n========================\n")


        if int_userinput == 2:
            int_userStatus = 2
            break
        else:
            int_userStatus = 1
            break

    # 判断用户是否推出购买程序
    if int_userStatus == 2:
        break
    else:
        continue

    int_userStatus = 0


# 输出购物车列表
print("\n============Cart List============\n")
if len(list_cart) > 0:
    for idx, product in enumerate(list_cart):
        print(idx + 1, product[0], product[1])
else:
    print("Your cart is empty!!")

print("\n============End of Cart List============\n")
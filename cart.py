"""以下是提取的图片文字内容：
采用面向对象编程思想完成如下需求

--采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5.退出购物车。"""


class Cart(object):


    def __init__(self):
        self.items = {}
        self.decode()

    def decode(self):
        with open('cart.txt', 'r') as f:
            for i in f.readlines():
                a = i.strip().split(':')
                self.items[a[0].strip()] = (float((a[1]).strip()), int((a[2]).strip()))
        return self.items

    def encode(self):
        with open('cart.txt', 'w') as f:
            val = self.items.items()
            for key, value in val:
                f.write(f'{key} : {value[0]} : {value[1]}\n')


    def add_to_cart(self):
        name = input('请输入商品名称：').strip()
        if name not in self.items:
            price = float(input('请输入商品单价：').strip())
            amount = int(input('请输入商品数量：').strip())
            self.items[name] = (price, amount)  # 最新字典
            self.encode()  # 重新写入字典
        else:
            print('该商品已存在，不能添加，只能修改！！')

    def alter_cart(self):  # 只能全部覆盖
        name = input('请输入要修改的商品名称：').strip()
        if name in self.items:
            price = float(input('请输入商品单价：').strip())
            amount = int(input('请输入商品数量：').strip())
            self.items[name] = (price, amount)
            self.encode()  # 重新写入字典
        else:
            print('没有这个商品！！')

    def remove_from_cart(self):  # 只能全覆盖
        name = input('请输入要修改的商品名称：').strip()
        if name in self.items:
            self.items.pop(name)
            self.encode()  # 重新写入字典
        else:
            print('不存在此商品！！！')

    def print_all_cart(self):
        if self.items:
            for name in self.items:
                print(f'商品名称：{name}，商品价格：{self.items[name][0]}，商品数量：{self.items[name][1]}')
        else:
            print('哎呀 没东西呢！！🤭')

    def run(self):
        print('==============================😀购物车😀=======================================')
        while True:
            print('\n\t\t1.添加购物车\n\t\t2.修改购物车\n\t\t3.删除购物车\n\t\t4.查询购物车\n\t\t5.退出购物车\n')
            user_input = input('输入操作\n：')
            try:
                if user_input == '1':
                    self.add_to_cart()
                elif user_input == '2':
                    self.alter_cart()
                elif user_input == '3':
                    self.remove_from_cart()
                elif user_input == '4':
                    self.print_all_cart()
                elif user_input == '5':
                    return
                else:
                    print('输入1-5数字！！！！！！！！！！！\n')
            except:
                print('输入不合法！！！！！\n')

if __name__ =="__main__":
    Cart().run()

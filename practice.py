# class shoppinglist:
#     def __init__(self,buget):
#         self.buget=buget
#         self.items={}
#     def add_item(self,item_name,price):
#         self.items[item_name]=price
#
#     def remove_item(self,item_name):
#         del self.items[item_name]
#     def tatol(self):
#         return sum(self.items.values())
#     def print_list(self):
#         print('購物清單:')
#         for item,price in self.items.items():
#          print(f'總價:{item},{price}')
#
#
#
# while True:
#    buget = float(input('請輸入預算:'))
#    shopping_list = shoppinglist(buget)
#
#    item_name=input('請輸入商品名稱(或按Q結束購物):')
#    if item_name =='Q':
#     break
#
#    price=float(input('請輸入商品價格:'))
#    shopping_list.add_item(item_name,price)
#    tatol=shopping_list.tatol()
#    print(f'總價:{tatol}')
#
#    if tatol>buget:
#        print('超出預算,請刪除一些商品')
#        shopping_list.print_list()
#
#        remove_item=input('請選擇要刪除的商品:')
#        shopping_list.remove_item(remove_item)
#
#
# shopping_list.print_list()
# print('總價:{}'.format(shopping_list.tatol()))
# print('謝謝使用')

# numbers=1
# odd_sum=0
# while numbers<=50:
#     if numbers %2 != 0:
#         odd_sum+=numbers
#     numbers+=1
#
#
# print('總和:',odd_sum)

class shoppinglist:
    def __init__(self,buget):
        self.buget=buget
        self.items={}
    def add_item(self,item_name,price):
        self.items[item_name]=price
    def remove_item(self,item_name):
        del self.items[item_name]
    def tatol(self):
        return sum(self.items.values())
    def print_list(self):
        print('購物清單:')
        for item,price in self.items.items():
            print(f'{item}:{price}')
buget=float(input('請輸入預算金額:'))
shopping_list=shoppinglist(buget)

while True:
   item_name=input('請輸入商品名稱(或案Q結束購物):')
   if item_name == 'Q':
       break
   price=float(input('請輸入商品價格:'))
   shopping_list.add_item(item_name,price)

   tatol=shopping_list.tatol()
   print(f'總價:{tatol}')

   if tatol>buget:
       print('超出預算金額,請刪除一些商品')
       shopping_list.print_list()
       print(f'目前總價:{tatol}')
       remove_item=input('請選擇要刪除的商品:')
       shopping_list.remove_item(remove_item)
       shopping_list.print_list()
       print(f'目前總價:{tatol}')



shopping_list.print_list()
print(f'總價:{tatol}')
print('謝謝購物')
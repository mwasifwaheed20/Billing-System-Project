# # def add_product():
# #     products={}
# #     n=int(input("enter the number of products you want to store="))
# #     for i in range(n):
# #         brand=input("enter the brand name of product=")
# #         name=input(f"enter the name of {i+1} product=")
# #         price=int(input(f"enter the price of{i+1} product="))
# #         products[name]=price
# #         products["brand"]=brand
# #         # products[brand]=brand
# #         # products[name]=price
# #     print(products)
# # add_product()


# store={
#     101:{"brand_name":"nike","product_item":"shoes","price":15000,"units_in_stocks":50},
#     102:{"brand_name":"addidas","product_item":"shoes","price":20000,"units_in_stocks":70},
#     103:{"brand_name":"jordan","product_item":"shoes","price":12000,"units_in_stocks":30}
#     }

# # def for_calling():
# #     while True:
# #         id=int(input("enter the product id="))
# #         if id==0:
# #             break
# #         product=store.get(id)
# #         if product:
# #             print(product)
# #         else:
# #             print("product not found pls enter correct id")
# # for_calling()   

# def biling():
#     while True:
#         selection=input("Select the product =")
#         if selection not in store:
#             print("product not found,pls enter valid product")
#         else:
#             print(store[selection])
# biling()

drinks={
    "coke":{"price":100,"stock":250},
    "pepsi":{"price":90,"stock":225},
    "7up":{"price":85,"stock":210},
    "sprite":{"price":95,"stock":150},
    "dew":{"price":105,"stock":180},
    "string":{"price":120,"stock":130}
}
snacks={
    "salted lays":{"price":50,"stock":130},
    "chili lays":{"price":50,"stock":170},
    "french lays":{"price":50,"stock":80},
    "salva":{"price":20,"stock":165},
    "chaty chin":{"price":70,"stock":100}
}
chocolate={
    "dairymilk":{"price":100,"stock":50},
    "now":{"price":30,"stock":60},
    "sonet":{"price":30,"stock":60},
    "bubbly":{"price":180,"stock":30}
}
dairy_products={
    "milk":{"price":290,"stock":20},
    "yougurt":{"price":250,"stock":15}
}
biscuits={
    "chocolate":{"price":40,"stock":25},
    "sandwish":{"price":50,"stock":30},
    "super":{"price":40,"stock":40},
    "candy":{"price":55,"stock":25}
}
store={
    "drinks":drinks,
    "snaks":snacks,
    "chocolates":chocolate,
    "dairy products":dairy_products,
    "biscuits":biscuits
}
catagory={
    1:drinks,
    2:snacks,
    3:chocolate,
    4:dairy_products,
    5:biscuits
}
print(store.keys())
print("Choose Catagory")
print("1: Drinks")
print("2: Snacks")
print("3: Chocolate")
print("4: Dairy Products")
print("5: Biscuits ")
from colorama import Fore,Style
def biling():
    total_bill=0
    item_cost=0
    while True:
        item=input("choose item=")
        if item=="exit":
            return total_bill
            return
        if item not in selected_catagory:
            print(f"{Fore.RED}item is not avaiable,pls choose form above one{Style.RESET_ALL}")
            continue
        product=selected_catagory[item]
        quantity=int(input("enter the quantity="))
        if quantity==0:
            continue
        if quantity>product["stock"]:
            print(f"{Fore.RED}Not Enough stock avaiable right now{Style.RESET_ALL}")
            continue
        item_cost=product["price"]*quantity
        product["stock"]-=quantity
        total_bill+=item_cost
        print("Remaining Units",product["stock"])
        print(f"Cost of {Fore.GREEN}{item.upper()}{Style.RESET_ALL} is",item_cost)
        return total_bill

def user():
    total_bill=0
    while True:
        choose=int(input("Choose the catagory=").strip())
        if choose==" ":
            print("pls enter a number ")
            continue
        if choose==0:
            print(f"{Fore.CYAN}Your Total Bill is:{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}{total_bill}{Style.RESET_ALL}")
            break
        if choose not in catagory:
            print(f"{Fore.RED}Invalid Catagory,pls choose correct one{Style.RESET_ALL} ")
        else:
            selected_catagory=catagory[choose]
            print(selected_catagory.keys())
            bill=biling()
            total_bill+=bill
print("uesr/admin mode")
mode=input("enter the mode=")
if mode=="user":
    user()
    

#Define the menu of restrant
Menu={
    'Pizza':150,
    'White Sauce Pasta':110,
    'Burger':80,
    'Veg Momo': 60,
    'Cold Coffe':90,
    'Milkshake': 90,
}

#greet
print("welcome to our Cafe")
print("Here is our Menu:")
print("Pizza: Rs150\nWhite Sauce Pasta: Rs110\nBurger: Rs80\nVeg Momo: Rs60\nCold Coffe: Rs90\nMilkshake: Rs90")

order_total=0
item_1=input("Enter the name of item you want to order =")
if item_1 in Menu:
      order_total +=Menu[item_1]
      print(f"your item {item_1} has been added to your order")

else:
      print(f"order item {item_1} is not avaialable yet!")

another_order =input("Do you want to add another item?(Yes/NO) ") 
if another_order =="Yes":
   item_2= input("Enter the name of second item =")
   if item_2 in Menu:
         order_total += Menu[item_2]
         print(f"Item {item_2} has been added to order")

   else:
       print(f"ordered Item {item_2} is not avaialable!")
print(f"The total amount of items to pay is {order_total} ")
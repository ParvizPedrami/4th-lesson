products = []
def read_file():
    f = open("store.txt","r")
    for line in f:
        result=line.split(",")
        my_dic={"id":result[0],"name":result[1],"price":result[2],"count":result[3]}
        products.append(my_dic)
        print(result)
read_file()


def add():
    new1_id=input("id: ")
    new1_name=input("name: ")
    new1_price=input("price: ")
    new1_count=input("count: ")
    new_dice={"id":new1_id,"name":new1_name,"price":new1_price,"count":new1_count}
    products.append(new_dice)
    print(new_dice)
def remove():
    idkey1=input("enter your key:")
    for product in products:
       if product["id"] == idkey1 or product["name"]== idkey1 :    
          products.remove(product)
          print("item has been deleted")
          break
def search():
    idkey=input("enter your key:")
    for product in products:
        if product["id"] == idkey or product["name"]== idkey :
            print(product)
            break
    else:
        print("not found")
def edite():
    print("1-name_edit")
    print("2-price_edit")
    print("3-count-edit")
def name():
    idkey3=input("enter your key:")
    new_name=input("please enter new name for product")
    for product in products:
        if product["id"] == idkey3 or product["name"]== idkey3 : 
            product["name"]=new_name
            print(product)
            print("name has been changed")
            break 
              
               
def price(): 
    idkey4=input("enter your key:")
    new_price=int(input("please enter new price"))
    for product in products:
        if product["id"] == idkey4 or product["name"]== idkey4 : 
            product["price"]=new_price
            print(product)
            print("price is changed")
            break 

def count(): 
    idkey5=input("enter your key:")
    new_count=int(input("please enter new count"))
    for product in products:
        if product["id"] == idkey5 or product["name"]== idkey5 : 
            product["count"]=new_count
            print(product)
            print("count has been changed")
            break 

def show_list():
     print("id,\nname","\t","price","\t","count")
     for product in products:
         print(product["id"],"\t",product["name"],"\t",product["price"],product["count"])
      
                
       
def buy():
    sabad_kharid=[]
    while True:
        moshtari=input("do you want to buy???""y or n")
        if moshtari=="y":
            print("please enter ID or name of the product") 

        if moshtari=="n":
            exit()

        idkey2=input("enter your key:")
        
        for product in products:
            if product["id"] == idkey2 or product["name"] == idkey2:
                print(product)
                mo=int(input("how many items do you want to buy?"))
                x=int(product['count'])
                y=int(product['price'])
    
                if x==0:
                    print("sold out")
                elif mo >= x:
                    print("your request is more than stock")
                elif x <= mo:
                    z=mo*y
                    print(z)
                    sabad_kharid.append(z)
                    print(sabad_kharid)
                
        else:
            print("there is no any item with identical ID or name")

def show_menu():
    print("1-Add")
    print("2-Remove")
    print("3-Search")
    print("4-Edit")
    print("5-show list")
    print("6-Buy")
    print("7-Exit")

read_file()
while True:
    show_menu()
    
    user_choice=int(input("enter your choice: "))
    if user_choice==1:
        add()
    elif user_choice==2: 
        remove()
    elif user_choice==3: 
        search()
    elif user_choice==4:
        edite() 
        user_choice_edite=int(input("enter your choice for edit: "))
        if user_choice_edite==1:
            name()
        elif user_choice_edite==2:
            price()
        elif user_choice_edite==3:
            count()
        else:
            print("please select another")  
    elif user_choice==5: 
        show_list()
    elif user_choice==6: 
        buy()
    elif user_choice==7:
        save=input("do you want to save the changes?y or n")
        if save=="y":
            f = open("store.txt","w")
            for product in products:
                f.write(product["id"]+product["name"]+product["price"]+product["count"])
                f.write("")
                f.close() 


        exit()  
    
        
    
    else:
        print("please select another")  

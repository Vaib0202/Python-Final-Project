import main
import json
from json import JSONDecodeError

print("Welcome to Food Ordering App")
c=1
while c!=0:
    print("Press:")
    print("0: Exit")
    print("1: Register as Admin")
    print("2: Register as User")
    print("3: Login as Admin")
    print("4: Login as User")
    c=int(input())
    if c==1:
        print("Enter Full Name:")
        F=input()
        print("Enter Phone Number:")
        N=input()       
        print("Enter Email:")
        E=input()
        print("Enter Address:")
        A=input()
        print("Enter Password:")
        P=input()
        if '@' in E and '.com' in E and len(P)!=0 and len(E)!=0 and len(A)!=0 and len(F)!=0 and len(N) == 10:
            main.registration('admin','admin.json','user.json',F,N,E,A,P)
            print("Registered Successfully as Admin !!")
        else:
            print("Please Enter Valid Data")
    elif c==2:
        print("Enter Full Name:")
        F=input()
        print("Enter Phone Number:")
        N=input()       
        print("Enter Email:")
        E=input()
        print("Enter Address:")
        A=input()
        print("Enter Password:")
        P=input()

        if '@' in E and '.com' in E and len(P)!=0 and len(E)!=0 and len(A)!=0 and len(F)!=0 and len(N) == 10:
            main.registration('user','admin.json','users.json',F,N,E,A,P)
            print("Registered Successfully as User !!")
        else:
            print("Please Enter Valid Data")
    elif c==3:
        print("Enter Email")
        E=input()
        print("Enter Password")
        P=input()
        success=main.login('admin','admin.json','users.json',E,P)
        if success==True:
            temp=open('admin.json','r')
            adms=json.load(temp)
            admin_details=[]
            for i in range(len(adms)):
                if adms[i]["Email"]==E and adms[i]["Password"]==P:
                    admin_details.append(adms[i])
                    break
            while True:
                print("Press: ")
                print("1: Add Item")
                print("2: View Item")
                print("3: Edit Item")
                print("4: Remove Item")
                print("0: Logout")
                in1=int(input())
                if in1==1:
                    p_id=main.autogenerate_foodId()
                    print("Food ID generated is "+str(p_id))
                    print("Enter Dish Name: ")
                    dish=input()
                    print("Enter Quantity: ")
                    quantity=input()
                    print("Enter Price: ")
                    price=input()
                    print("Enter Discount: ")
                    discount=input()
                    if '%' not in discount:
                        discount+="%"
                    print("Enter Available Stock: ")
                    stock=input()
                    try:
                        int(price)
                    except ValueError:
                        price=""
                    try:
                        int(stock)
                    except ValueError:
                        stock=""
                    if len(p_id)!=0 and len(dish)!=0 and len(price)!=0 and len(discount)!=0 and len(stock)!=0:
                        main.addItem(admin_details[0]["Full Name"],'add_items.json',p_id,dish,quantity,int(price),discount,int(stock))
                        print("Item successfully added !!")
                    else:
                        print("Adding unsuccessful, Please Enter Valid Data")
                elif in1==2:
                    print("Press :")
                    print("1: View All Items")
                    print("2: View Item by Food ID")
                    in2=int(input())
                    if in2==1:
                        l=main.viewItem(admin_details[0]["Full Name"],'add_items.json')
                        if len(l)==0:
                            print("No products created till now!!")
                        else:
                            for i in range(len(l)):
                                print("Food ID: "+str(l[i]["Food ID"]))
                                print("Dish: "+str(l[i]["Dish"]))
                                print("Admin: "+str(l[i]["Admin"]))
                                print("Price: "+str(l[i]["Price"]))
                                print("Discount: "+str(l[i]["Discount"]))
                                print("Stock Available: "+str(l[i]["Total Stock Available"]))
                    elif in2==2:
                        print("Enter Food ID :")
                        pr_id=input()
                        dtls=[]
                        main.viewByFoodID('add_items.json',pr_id,dtls)
                        if len(dtls)==0:
                            print("Invalid ID")
                        else:
                            print("Dish: "+str(dtls[i]["Dish"]))
                            print("Admin: "+str(dtls[i]["Admin"]))
                            print("Price: "+str(dtls[i]["Price"]))
                            print("Discount: "+str(dtls[i]["Discount"]))
                            print("Stock Available: "+str(dtls[i]["Total Stock Available"]))
                    else:
                        print("Invalid Choice")
                elif in1==3:
                    print("Enter Food ID: ")
                    prd_id=input()
                    print("Enter Detail to be udpdated: ")
                    detail_tbu=input()
                    print("Enter Updated detail: ")
                    u_detail=input()
                    dn=main.updateItem('add_items.json',prd_id,detail_tbu,u_detail)
                    if dn==True:
                        print("Item Update Successfully")
                    else:
                        print("Invalid Item Detail")
                elif in1==4:
                    print("Enter Food ID: ")
                    pr_id=input()
                    dn=main.deleteItem('add_items.json',pr_id)
                    if dn==True:
                        print("Item Deleted Successfully")
                    else:
                        print("Invalid Food ID")
                elif in1==0:
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid Credentials")
    elif c==4:
        print("Enter Email")
        E=input()
        print("Enter Password")
        P=input()
        success=main.login('user','admin.json','users.json',E,P)
        if success==True:
            temp=open('users.json','r')
            mems=json.load(temp)
            member_details=[]
            for i in range(len(mems)):
                if mems[i]["Email"]==E and mems[i]["Password"]==P:
                    member_details.append(mems[i])
                    break
            while True:
                print("Press: ")
                print("1: Create New Order")
                print("2: View Order History")
                print("3: Update Profile")
                print("4: Logout")
                in3=int(input())
                if in3==1:
                    temp=open('add_items.json','r')
                    try:
                        content=json.load(temp)
                        temp.close()
                        print("Select from below:")
                        for i in range(len(content)):
                            print(i+1,content[i]["Dish"],"(",content[i]["Quantity"],")","INR",content[i]["Price"])
                        id_pr=input()
                        o_id=main.autogenerate_OrderId()
                        ch=main.placeOrder('order.json',member_details[0]["Full Name"],member_details[0]["Address"],'products.json',id_pr,o_id)
                        if ch==True:
                            print("Order Successfully Placed with order id: "+str(o_id))
                        else:
                            print("Order Unsuccessful")
                    except JSONDecodeError:
                        print("No Item Available")
                elif in3==2:
                    l=[]
                    main.orderHistory('order.json',member_details[0]["Full Name"],l)
                    if len(l)==0:
                        print("No orders Placed Yet !!")
                    else:
                        for i in range(len(l)):
                            print("Order ID: "+str(l[i]["Order ID"]))
                            print("Dish: "+str(l[i]["Product Name"]))
                            print("MRP: "+str(l[i]["Price"]))
                            print("Discount: "+str(l[i]["Discount"]))
                            print("Price after Discount: "+str(l[i]["Price after Discount"]))
                            print("Quantity: "+str(l[i]["Quantity"]))
                            print("Grand Total: "+str(l[i]["Total Cost"]))
                            print("Delivering to: "+str(l[i]["Delivering to"]))
                elif in3==3:
                    print("Enter Detail to be updated: ")
                    dtl_tbu=input()
                    print("Enter Update Detail: ")
                    up_dtl=input()
                    ch=main.updateProfile('users.json',member_details[0]["Full Name"],dtl_tbu,up_dtl)
                    if ch==True:
                        print("Detail Updated Successfully !!")
                    else:
                        print("Invalid Detail")
                elif in3==4:
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid Credentials")
    elif c==0:
        break
    else:
        print("Invalid Choice")
# print("Hello")
#biryani_kitchen
    #input(rice,paneer)
    #output
#cake_kitchen
# name=input("Enter your name:")
# print(name)
# n1=int(input("Enter first number:")) 
# n2=int(input("Enter second number:"))   
# result=n1+n2
# print(result)
# company_name="ammu"
#Function definition
# def add_two_numbers(x,y):
#     print(company_name)
    # first_number=int(x)
    # second_number=int(y)
    # sum=first_number+second_number
    # return sum,x,y
# print(sum)
# #function call
# call,x1,x2=add_two_numbers(5432,98759)
# print(call)

# numbers=[54,38,72,90]
# result=sum(numbers)
# print(result)

# def greet(name,message="Hello"):
#     print(f"{message} {name}")

# greet("Appu")    
# greet("Appu","Good Morning")

#lambda function
# multiply=lambda a,b:a*b
# def mult(a,b):
#     return a*b
# print(multiply(a=20,b=40))


# s = my_list[1:]
# print(s)

#filter
# def is_even_number_func(n):
#     rem = n % 2
#     if rem == 0:
#         return True
#     else:
#         return False
# print(is_even_number_func(10))    
# even_numbers = list(filter(is_even_number_func,my_list))
# print(even_numbers)

#shorthand syntax
# def is_even_number_func(n):
#     return (n % 2)== 0
# odd_numbers = list(filter(lambda n: (n % 2) != 0, my_list))
# print(odd_numbers)

# my_list = [75,48,59,3,4,555,89]
# my_list.sort()
# print(my_list)

products = [
    {
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
        "rating": {
            "rate": 3.9,
            "count": 120
        }
    },
    {
        "id": 2,
        "title": "Mens Casual Premium Slim Fit T-Shirts ",
        "price": 22.3,
        "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
        "rating": {
            "rate": 4.1,
            "count": 259
        }
    },
    {
        "id": 3,
        "title": "Mens Cotton Jacket",
        "price": 55.99,
        "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg",
        "rating": {
            "rate": 4.7,
            "count": 500
        }
    },
    {
        "id": 4,
        "title": "Mens Casual Slim Fit",
        "price": 15.99,
        "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg",
        "rating": {
            "rate": 2.1,
            "count": 430
        }
    },
    {
        "id": 5,
        "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
        "price": 695,
        "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
        "category": "jewelery",
        "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg",
        "rating": {
            "rate": 4.6,
            "count": 400
        }
    }
]
def sort_by_price(p):
    return p["price"]
products.sort(key=sort_by_price,reverse=True)
print(products)
    
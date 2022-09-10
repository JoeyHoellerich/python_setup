def hello():
    print("Hello User!")


def pack(item1, item2, item3):
    return ([item1, item2, item3])


def eat_lunch(input_list):
    for item in range(0, len(input_list) + 1, 1):
        if (item == 0):
            print(f"First I eat {input_list[item]}")
        elif (item == len(input_list)):
            print("My lunchbox is empty!")
        else:
            print(f"Next I eat {input_list[item]}")


lunch = ["bread", "cheese", "eggs"]


hello()
print(pack(1, 2, 3))
eat_lunch(lunch)

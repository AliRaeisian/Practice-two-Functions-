def max(**kwargs):
    max = 0
    for fruit in kwargs.keys():
        if kwargs[fruit] > max:
            max = kwargs[fruit]
    for fruit in kwargs.keys():
        if kwargs[fruit] == max:
            return fruit


def min(**kwargs):
    min = next(iter(kwargs.values()))
    for fruit in kwargs.keys():
            if kwargs[fruit] < min:
                min = kwargs[fruit]
    for fruit in kwargs.keys():
        if kwargs[fruit] == min:
            return fruit


def fruit(**kwargs):
    count = len(kwargs)
    total_cost = sum(kwargs.values())
    most_exspensive = max(**kwargs)
    chipest = min(**kwargs)

    print(f"You have {count} fruits in your shopping list")
    print(f"The total cost of the shopping list is {total_cost}")
    print(f"The most expensive fruit is {most_exspensive} with the price of {kwargs[most_exspensive]}")
    print(f"The cheapest fruit is {chipest} with the price of {kwargs[chipest]}")


def main():
    fruits1 = {}
    while True:
        fruits_info = input()
        if fruits_info == "finish":
            break

        fruit_name , price = fruits_info.split()
        fruits1[fruit_name] = int(price)

    fruit(**fruits1)

    



main()



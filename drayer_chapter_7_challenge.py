import csv

# Pull in the CSV file
filename = 'Chapter_7Challenge.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    name = []
    candy_type_1 = []
    candy_type_2 = []
    candy_price_1 = []
    candy_price_2 = []

    candies = {}

    for row in reader:
        name = row[1].lower()
        candy_1 = row[2].lower()
        candy_2 = row[4].lower()
        price_1 = float(row[3])
        price_2 = float(row[5])
        step = {
            name : {
                candy_1: price_1,
                candy_2: price_2,
            }
        }
        candies.update(step)

    # Print each list
print(candies)

while True:
    candy_requester = input("What is your name? ")
    candy_requester = candy_requester.lower()
    if candy_requester in candies:
        break
    else:
        continue

while True:
    print(candies[candy_requester])

    reason = input("(add, remove, quit) Would you like to add or "
                "remove anything from your list? ")
    if reason == 'add':
        while True:
            add_candy = input("('quit' to stop)What candy would "
                              "you like to add? ")
            add_candy = add_candy.lower()
            if add_candy == 'quit':
                break
            else:
                while True:
                    add_price = input("(in numbers)What is the price"
                                      " of the candy? ")
                    try:
                        # I had to use the internet tell me exactly
                        # how to do this, I have never used this before
                        # but needed to make sure it is a float.
                        add_price = float(add_price)
                        break
                    except ValueError:
                        add_price = input("(in numbers)What is the "
                                          "price of the candy? ")
                        continue

                candies[candy_requester][add_candy] = add_price
        continue

    elif reason == 'remove':
        while True:
            remove_candy = input("('quit' to stop)What candy "
                                 "would you like to remove? ")
            remove_candy = remove_candy.lower()
            if remove_candy in candies[candy_requester]:
                del candies[candy_requester][remove_candy]
                continue
            elif remove_candy == 'quit':
                break
            else:
                print(candies[candy_requester])
                print("Please write a candy from your list")
                continue

    elif reason == 'quit':
        break

    else:
        print("please input either 'add', 'remove', or 'quit'")
        continue

print("Your candies are as follows:")
candies_chosen = candies[candy_requester]
for candy in candies_chosen:
    print(candy)

price = candies[candy_requester]
total_price = sum(price.values())
print(f"Your total price is ${total_price}")
print("Your changes have been added to the survey data!")

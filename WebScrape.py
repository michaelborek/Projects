import requests
import bs4

# Accessing to internet library
basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# Place where we hold our searched books
our_bookshelf = []

choice = "player's choice"

# Input place, where player choose what he want search
while True:
    a = input('How rated books do you want to search? Choose among(One star, Two star, Three star, Four star, Five star: ')
    if a.lower() == ('one star' or 'two star' or 'three star' or 'four star' or 'five star'):
        choice = a.split()[0].capitalize()
        break
    else:
        print('Wrong choice!')


# Searching books at different pages
for i in range(1,51):
    res = requests.get(basic_url.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # Searching the product_pod class which information about books
    products = soup.select('.product_pod')
    # Checking every book on a page
    for product in products:
        # Checking if book is one star rated
        if len(product.select(f'.star-rating.{choice}')) != 0:
            # Selecting our one star book
            book = product.select('a')[1]['title']
            our_bookshelf.append(book)

# Printing the list of our one star books
print(our_bookshelf)

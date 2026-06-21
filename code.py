import csv

def get_books(filename):
    books = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        header = next(reader)
        for row in reader:
            books.append(row)
    return books

def get_total_prices(books):
    result = []
    for book in books:
        isbn = book[0]
        quantity = int(book[3])
        price = float(book[4])
        total = quantity * price
        result.append((isbn, total))
    return result

if __name__ == "__main__":
    books = get_books("books.csv")
    print("Список книг:")
    for book in books:
        print(book)

    print("\nСтоимость по isbn:")
    totals = get_total_prices(books)
    for item in totals:
        print(item)

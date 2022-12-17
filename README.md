# Django Models

## how it works from shell

```shell
python manage.py shell

>>> from book_outlet.models import Book
>>> harry_potter = Book(title="Harry Potter 1 - The Philosopher's Stone", rating=5)
>>> harry_potter.save()
>>> lord_of_the_rings = Book(title="Lord of the Rings", rating=4)
>>> lord_of_the_rings.save()
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
# after adding str in models
<QuerySet [<Book: Harry Potter 1 - The Philosopher's Stone(5)>, <Book: Lord of the Rings(4)>]>
```

``ctrl + D`` to exit the shell

### After modifying the model

```shell
>>> from book_outlet.models import Book
>>> Book.objects.all()[1].author
>>> Book.objects.all()[1]
<Book: Lord of the Rings(4)>
>>> Book.objects.all()[1].is_bestselling
False
>>> Book.objects.all()[1].rating
4
>>>
```

### Update the data in the database

```shell
>>> harry_potter = Book.objects.all()[0]
>>> harry_potter.title
>>> harry_potter.author = "J.K. Rowling"
>>> harry_potter.is_bestselling = True
>>> harry_potter.save()
>>> Book.objects.all()[0].author
'J.K. Rowling'
```

### Deleting Data from the database

```shell
>>> lotr = Book.objects.all()[1]
>>> lotr.delete()
(1, {'book_outlet.Book': 1})
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter 1 - The Philosopher's Stone(5)>]>
>>>
```

## Using Create instead of Save

```shell
>>> Book.objects.create(title="Lord of the Rings", rating=4, author="J.R.R. Tolkien", is_bestselling=False)
>>> Book.objects.create(title="Random Book", rating=1, author="Random", is_bestselling=False)
```

### Get Data from database

> get method just return one value

```shell

>>> Book.objects.get(id=3)
<Book: Lord of the Rings(4)>
>>> Book.objects.get(id=1)
<Book: Harry Potter 1 - The Philosopher's Stone(5)>

```

> filter method return multiple values

```shell

>>> Book.objects.filter(is_bestselling=True)
<QuerySet [<Book: Harry Potter 1 - The Philosopher's Stone(5)>]>

>>> Book.objects.filter(is_bestselling=False)
<QuerySet [<Book: Lord of the Rings(4)>, <Book: My Story(2)>, <Book: Random Book(1)>]>

>>> Book.objects.filter(is_bestselling=False, rating=2)
<QuerySet [<Book: My Story(2)>]>

>>> Book.objects.filter(rating__lte=3)
<QuerySet [<Book: My Story(2)>, <Book: Random Book(1)>]>

>>> Book.objects.filter(rating__lt=2)
<QuerySet [<Book: Random Book(1)>]>

>>> Book.objects.filter(rating__lt=3, title__contains="Story")
<QuerySet [<Book: My Story(2)>]>

```

## OR Condition (|)

> and condition using comma(,)

```shell
>>> from django.db.models import Q
>>> Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True))
<QuerySet [<Book: Harry Potter 1 - The Philosopher's Stone(5)>, <Book: My Story(2)>, <Book: Random Book(1)>]>

>>> Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), Q(author="J.K. Rowling"))
<QuerySet [<Book: Harry Potter 1 - The Philosopher's Stone(5)>]>

# and , should be at the end if you are using Q or OR condition
>>> Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), author="J.K. Rowling")
<QuerySet [<Book: Harry Potter 1 - The Philosopher's Stone(5)>]>

```

## Author and Book model (one to many relationship)

```shell
>>> from book_outlet.models import Book, Author
>>> jkrowling = Author(first_name="J.K.", last_name="Rowling")
>>> jkrowling.save()
>>> Author.objects.all()
<QuerySet [<Author: Author object (1)>]>
>>> Author.objects.all()[0].first_name
'J.K.'

>>> hp1 = Book(title="Harry Potter 1", rating=5, is_bestselling=True, slug="harry-potter-1", author=jkrowling)
>>> hp1.save()
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter 1(5)>]>

>>> harrypotter = Book.objects.get(title="Harry Potter 1")
>>> harrypotter
<Book: Harry Potter 1(5)>
>>> harrypotter.author.last_name
'Rowling'

>>> books_by_rowling = Book.objects.filter(author__last_name="Rowling")
>>> books_by_rowling
<QuerySet [<Book: Harry Potter 1(5)>]>

>>> books_by_rowling = Book.objects.filter(author__last_name__contains="wling")
>>> books_by_rowling
<QuerySet [<Book: Harry Potter 1(5)>]>

>>> jkr = Author.objects.get(first_name="J.K.")
>>> jkr
<Author: Author object (1)>
>>> jkr.book_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7f25a0eab1c0>
>>> jkr.book_set.all()
<QuerySet [<Book: Harry Potter 1(5)>]>

## After add related name = books in Book model author
>>> from book_outlet.models import Book, Author
>>> jkr = Author.objects.get(first_name="J.K.")
>>> jkr.books.all()
<QuerySet [<Book: Harry Potter 1(5)>]>
```

## Author and Address models (one to one relationship)

```shell

>>> from book_outlet.models import Book, Author, Address
>>> Author.objects.all()[0].address
>>> addr1 = Address(street="Some Street", postal_code="12345", city="London")
>>> addr2 = Address(street="Another Street", postal_code="67890", city="New York")
>>> addr1.save()
>>> addr2.save()
>>> jkr = Author.objects.get(first_name="J.K.")
>>> jkr.address
>>> jkr.address = addr1
>>> jkr.save()
>>> jkr.address
<Address: Address object (1)>
>>> jkr.address.street
'Some Street'

```

## Many to Many Relationship

```shell
>> spain = Country(name="Spain", code="ES")
>>> spain.save()
>>> mys.published_countries.add(spain)
>>> mys.published_countries.filter(code="ES")
<QuerySet [<Country: Country object (1)>]>
>>> Country.objects.all()
<QuerySet [<Country: Country object (1)>]>
>>>

```

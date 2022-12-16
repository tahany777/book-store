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

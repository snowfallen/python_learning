# Cheatsheet for Learning Python
***
## What is Python
Python is a popular programming language. It was created in 1991 by Guido van Rossum.
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
It is used for:
- web development (server-side),
- software development,
- mathematics,
- system scripting.

### What can Python do?
- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex mathematics.
- Python can be used for rapid prototyping, or for production-ready software development.

### Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-orientated way or a functional way.

### References
- [w3schools.com](https://www.w3schools.com/python/python_intro.asp)
- https://github.com/trekhleb/learn-python
***
## Variables
Unlike other programming languages, Python has no command for
declaring a variable. A variable is created the moment you first assign
a value to it.
### Rules for Python variables:
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
- Variable names are case-sensitive (age, Age and AGE are three different variables).
***
## Operators
### Arithmetic operators
``(+, -, *, /, //, %, **)``

`+` Addition.

`-` Subtraction.

`*` Multiplication.

`/` Division. Result of division is float number.

`//` Floor division.

`%` Modulus

`**` Exponentiation
### Bitwise operators
``(&, |, ^, >>, <<, ~)``

`&` AND
```
    # Sets each bit to 1 if both bits are 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 & 3 == 1  # 0b0001
```

`|` OR
```
    # Sets each bit to 1 if one of two bits is 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
```

`^` XOR
```
    # Sets each bit to 1 if only one of two bits is 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert 5 ^ 3 == 6  # 0b0110
```

`>>` Signed right shift
```
    # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost
    # bits fall off.
    #
    # Example:
    # 5 = 0b0101
    assert 5 >> 1 == 2  # 0b0010
    assert 5 >> 2 == 1  # 0b0001
```


`<<` Zero fill left shift
```
    # Shift left by pushing zeros in from the right and let the leftmost bits fall off.
    #
    # Example:
    # 5 = 0b0101
    assert 5 << 1 == 10  # 0b1010
    assert 5 << 2 == 20  # 0b10100
```

`~` NOT
```
    # Inverts all the bits.
    assert ~5 == -6    
```
### Assignment operators
``[=, +=, -=, /=, //= etc.]``

`+=`
```
    number = 5
    number += 3
    assert number == 8
```
`-=`
```
    number = 5
    number -= 3
    assert number == 2
```
`/=`
```
    number = 8
    number /= 4
    assert number == 2
```

`//=`
```
    number = 5
    number //= 3
    assert number == 1
```

`*=`
```
    number = 5
    number *= 3
    assert number == 15
```

`**=`
```
    number = 5
    number **= 3
    assert number == 125
```

`%=`
```
    number = 8
    number %= 3
    assert number == 2
```

`&=`
```
    number = 5  # 0b0101
    number &= 3  # 0b0011
    assert number == 1  # 0b0001
```

`|=`
```
    number = 5  # 0b0101
    number |= 3  # 0b0011
    assert number == 7  # 0b0111
```

`^=`
```
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert number == 6  # 0b0110
```

`>>=`
``` 
    number = 5
    number >>= 3
    assert number == 0  # (((5 // 2) // 2) // 2)
```

`<<=`
```
    number = 5
    number <<= 3
    assert number == 40  # 5 * 2 * 2 * 2
```
### Comparison operators
```(==, !=, >, <, >=, <=)```

`==` Equal.
```
    number = 5
    assert number == 5
```
`!=` Not equal.
```
    number = 5
    assert number != 3
```
`>` Greater than.
```
    number = 5
    assert number > 3
```
`<` Less than.
```
    number = 5
    assert number < 8
```
`>=` Greater than or equal to
```
    number = 5
    assert number >= 5
    assert number >= 4
```
`<=` Less than or equal to
```   
    number = 5
    assert number <= 5
    assert number <= 6
```
### Logical operators
```(and, or, not)```

`and` And.

`or` Or.

`not` Not.
```
    first_number = 5
    second_number = 10

    # Returns True if both statements are true.
    assert first_number > 0 and second_number < 20
    
    # Returns True if one of the statements is true
    assert first_number > 5 or second_number < 20
    
    # Reverse the result, returns False if the result is true.
    assert not first_number == second_number
    assert first_number != second_number
```
### Identity operators
`(is, is not)`

```
    # Let's illustrate identity operators based on the following lists.
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    # is
    # Returns true if both variables are the same object.

    # Example:
    # first_fruits_list and third_fruits_list are the same objects.
    assert first_fruits_list is third_fruits_list

    # is not
    # Returns true if both variables are not the same object.

    # Example:
    # first_fruits_list and second_fruits_list are not the same objects, even if they have
    # the same content
    assert first_fruits_list is not second_fruits_list

    # To demonstrate the difference between "is" and "==": this comparison returns True because
    # first_fruits_list is equal to second_fruits_list.
    assert first_fruits_list == second_fruits_list
```
### Membership operators
`(in, not in)`

```
    # Let's use the following fruit list to illustrate membership concept.
    fruit_list = ["apple", "banana"]

    # in
    # Returns True if a sequence with the specified value is present in the object.

    # Returns True because a sequence with the value "banana" is in the list
    assert "banana" in fruit_list

    # not in
    # Returns True if a sequence with the specified value is not present in the object

    # Returns True because a sequence with the value "pineapple" is not in the list.
    assert "pineapple" not in fruit_list
```
***
## Data Types
### Numbers
There are three numeric types in Python:
- int (e.g. 2, 4, 20)
    - bool (e.g. False and True, acting like 0 and 1)
- float (e.g. 5.0, 1.6)
- complex (e.g. 5+6j, 4-3j)
#### Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
```
    positive_integer = 3255522
    negative_integer = -3255522
    big_integer = 35656222554887711
```
#### Boolean
 Booleans represent the truth values False and True. The two objects representing the values
 False and True are the only Boolean objects. The Boolean type is a subtype of the integer type,
 and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the
 exception being that when converted to a string, the strings "False" or "True" are returned,
 respectively.
```
    true_boolean = True
    false_boolean = False
```
#### Float type
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
```
    float_number = 7.0
    # Another way of declaring float is using float() function.
    float_number_via_function = float(7)
    float_negative = -35.59
    
    # Float can also be scientific numbers with an "e" to indicate
    # the power of 10.
    float_with_small_e = 35e3
    float_with_big_e = 12E4
```
#### Complex Type
```
    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j
    assert complex_number_1 * complex_number_2 == 27 + 8j
```
### String
```
    name_1 = 'Sano'
    name_2 = "Sano"
    # Strings created with different kind of quotes are treated the same.
    
    # \ can be used to escape quotes.
    # use \' to escape the single quote or use double quotes instead.
    single_quote_string = 'doesn\'t'
    double_quote_string = "doesn't" 
    
    # \n means newline.
    multiline_string = 'First line.\nSecond line.'
    
    # Strings can be indexed, with the first character having index 0.
    # There is no separate character type; a character is simply a string
    # of size one. Note that since -0 is the same as 0, negative indices
    # start from -1.
    word = 'Python'
    assert word[0] == 'P'  # First character.
    assert word[5] == 'n'  # Fifth character.
    assert word[-1] == 'n'  # Last character.
    assert word[-2] == 'o'  # Second-last character.
    assert word[-6] == 'P'  # Sixth from the end or zeroth from the beginning.
    
    # In addition to indexing, slicing is also supported. While indexing is
    # used to obtain individual characters, slicing allows you to obtain
    # substring:
    assert word[0:2] == 'Py'  # Characters from position 0 (included) to 2 (excluded).
    assert word[2:5] == 'tho'  # Characters from position 2 (included) to 5 (excluded).

    # Note how the start is always included, and the end always excluded.
    # This makes sure that s[:i] + s[i:] is always equal to s:
    assert word[:2] + word[2:] == 'Python'
    assert word[:4] + word[4:] == 'Python'
    
    # Slice indices have useful defaults; an omitted first index defaults to
    # zero, an omitted second index defaults to the size of the string being
    # sliced.
    assert word[:2] == 'Py'  # Character from the beginning to position 2 (excluded).
    assert word[4:] == 'on'  # Characters from position 4 (included) to the end.
    assert word[-2:] == 'on'  # Characters from the second-last (included) to the end.
    
    # Attempting to use an index that is too large will result in an error.
    with pytest.raises(Exception):
        not_existing_character = word[42]
        
    # However, out of range slice indexes are handled gracefully when used
    # for slicing:
    assert word[4:42] == 'on'
    assert word[42:] == ''
    
    # Python strings cannot be changed — they are immutable. Therefore,
    # assigning to an indexed position in the string
    # results in an error:
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        word[0] = 'J'
        
    
    # If you need a different string, you should create a new one:
    assert 'J' + word[1:] == 'Jython'
    assert word[:2] + 'py' == 'Pypy'

    # The built-in function len() returns the length of a string:
    characters = 'supercalifragilisticexpialidocious'
    assert len(characters) == 34
    
    # String literals can span multiple lines. One way is using triple-quotes: """..."""
    # or '''...'''. End of lines are automatically included in the string, but it’s possible
    # to prevent this by adding a \ at the end of the line. The following example:
    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''
```
#### Basic operation and methods
```
    Strings can be concatenated (glued together) with the + operator,
    and repeated with *: 3 times 'un', followed by 'ium'

    assert 3 * 'un' + 'ium' == 'unununium'
    
    # This feature is particularly useful when you want to break long strings:
    text = (
        'Put several strings within parentheses '
        'to have them joined together.'
    )
    assert text == 'Put several strings within parentheses to have them joined together.'
    
    # If you want to concatenate variables or a variable and a literal, use +:
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'
    
    
    hello_world_string = "Hello, World!"

    # The strip() method removes any whitespace from the beginning or the end.
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # The len() method returns the length of a string.
    assert len(hello_world_string) == 13

    # The lower() method returns the string in lower case.
    assert hello_world_string.lower() == 'hello, world!'

    # The upper() method returns the string in upper case.
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # The replace() method replaces a string with another string.
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # The split() method splits the string into substrings if it finds instances of the separator.
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # Converts the first character to upper case
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # Returns the number of times a specified value occurs in a string.
    assert 'low letter at the beginning'.count('t') == 4

    # Searches the string for a specified value and returns the position of where it was found.
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # Converts the first character of each word to upper case
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # Returns a string where a specified value is replaced with a specified value.
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # Joins the elements of an iterable to the end of the string.
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # Returns True if all characters in the string are upper case.
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # Check if all the characters in the text are letters.
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # Returns True if all characters in the string are decimals.
    assert '1234'.isdecimal()
    assert not 'a21453'.isdecimal()
```
#### String formatting.
```
    # To use formatted string literals, begin a string with f or F before the opening quotation
    # mark or triple quotation mark. Inside this string, you can write a Python expression
    # between { and } characters that can refer to variables or literal values.
    year = 2018
    event = 'conference'

    assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

    # The str.format() method of strings requires more manual effort. You’ll still use { and } to
    # mark where a variable will be substituted and can provide detailed formatting directives,
    # but you’ll also need to provide the information to be formatted.
    yes_votes = 42_572_654  # equivalent of 42572654
    no_votes = 43_132_495   # equivalent of 43132495
    percentage = yes_votes / (yes_votes + no_votes)

    assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'

    # When you don’t need fancy output but just want a quick display of some variables for debugging
    # purposes, you can convert any value to a string with the repr() or str() functions. The str()
    # function is meant to return representations of values which are fairly human-readable, while
    # repr() is meant to generate representations which can be read by the interpreter (or will
    # force a SyntaxError if there is no equivalent syntax). For objects which don’t have a
    # particular representation for human consumption, str() will return the same value as repr().
    # Many values, such as numbers or structures like lists and dictionaries, have the same
    # representation using either function. Strings, in particular, have two distinct
    # representations.

    greeting = 'Hello, world.'
    first_num = 10 * 3.25
    second_num = 200 * 200

    assert str(greeting) == 'Hello, world.'
    assert repr(greeting) == "'Hello, world.'"
    assert str(1/7) == '0.14285714285714285'

    # The argument to repr() may be any Python object:
    assert repr((first_num, second_num, ('spam', 'eggs'))) == "(32.5, 40000, ('spam', 'eggs'))"

    # Formatted String Literals

    # Formatted string literals (also called f-strings for short) let you include the value of
    # Python expressions inside a string by prefixing the string with f or F and writing
    # expressions as {expression}.

    # An optional format specifier can follow the expression. This allows greater control over how
    # the value is formatted. The following example rounds pi to three places after the decimal.
    pi_value = 3.14159
    assert f'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

    # Passing an integer after the ':' will cause that field to be a minimum number of characters
    # wide. This is useful for making columns line up:
    table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    table_string = ''
    for name, phone in table_data.items():
        table_string += f'{name:7}==>{phone:7d}'

    assert table_string == ('Sjoerd ==>   4127'
                            'Jack   ==>   4098'
                            'Dcab   ==>   7678')

    # The String format() Method

    # Basic usage of the str.format() method looks like this:
    assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

    # The brackets and characters within them (called format fields) are replaced with the objects
    # passed into the str.format() method. A number in the brackets can be used to refer to the
    # position of the object passed into the str.format() method
    assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'
    assert '{1} and {0}'.format('spam', 'eggs') == 'eggs and spam'

    # If keyword arguments are used in the str.format() method, their values are referred to by
    # using the name of the argument.
    formatted_string = 'This {food} is {adjective}.'.format(
        food='spam',
        adjective='absolutely horrible'
    )

    assert formatted_string == 'This spam is absolutely horrible.'

    # Positional and keyword arguments can be arbitrarily combined
    formatted_string = 'The story of {0}, {1}, and {other}.'.format(
        'Bill',
        'Manfred',
        other='Georg'
    )

    assert formatted_string == 'The story of Bill, Manfred, and Georg.'

    # If you have a really long format string that you don’t want to split up, it would be nice if
    # you could reference the variables to be formatted by name instead of by position. This can be
    # done by simply passing the dict and using square brackets '[]' to access the keys

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

    # This could also be done by passing the table as keyword arguments with the ‘**’ notation.
    formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'
```
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
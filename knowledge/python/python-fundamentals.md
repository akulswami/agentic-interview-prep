# Python Fundamentals — A Complete Beginner's Guide

A structured, hands-on path through core Python, distilled from **Part I (Basics)** of
*Python Crash Course* by Eric Matthes (1st edition, No Starch Press). It covers everything
a complete beginner needs to read, write, and reason about everyday Python — the foundation
for the DSA, scripting, and tooling work elsewhere in this repository.

> **Scope.** This guide intentionally covers only **Part I** of the book (Chapters 1–11).
> Part II is three large projects (a Pygame arcade game, data visualization, and Django web
> apps) — useful later, but not part of the fundamentals. Master the chapters here first.
>
> These are *original study notes* (concepts paraphrased, examples reworked) — not a copy of
> the book. To go deeper or do the full exercises, read the source PDF at
> [docs/books/Python-Crash-Course.pdf](../../docs/books/Python-Crash-Course.pdf).

## How to use this guide

1. **Go in order.** Each chapter builds on the previous one. Don't skip ahead.
2. **Type every example yourself.** Reading code is not the same as writing it. Run each
   snippet, then change something and predict the result before re-running.
3. **Do the Practice prompts** at the end of each chapter before moving on. Coding the ideas
   is what makes them stick.
4. **Keep a scratch file open** (e.g. `practice.py`) and experiment freely.
5. **Read the tracebacks.** When something breaks, the error message tells you what and where.
   Learning to read errors is a core skill, not a distraction.

A reasonable pace for a beginner is **one chapter per study session**, with Chapters 8
(Functions) and 9 (Classes) often worth two sessions each.

## Setup quickstart

You need Python 3 and a text editor or IDE. Chapter 1 walks through full installation; the
short version:

```bash
# Check whether Python 3 is already installed (Linux/macOS)
python3 --version

# Start an interactive Python session to experiment
python3

# Run a script you've written
python3 hello_world.py
```

Recommended editors for beginners: **VS Code** (used in this workspace), Sublime Text, or
the bundled **IDLE**. Once you're comfortable, use a project virtual environment to keep
dependencies isolated:

```bash
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install --upgrade pip
```

## What's covered

| # | Chapter | You'll be able to… |
|---|---------|--------------------|
| 1 | [Getting Started](#chapter-1--getting-started) | Install Python, run code in a terminal and an editor |
| 2 | [Variables and Simple Data Types](#chapter-2--variables-and-simple-data-types) | Use variables, strings, and numbers |
| 3 | [Introducing Lists](#chapter-3--introducing-lists) | Store and access ordered collections of items |
| 4 | [Working with Lists](#chapter-4--working-with-lists) | Loop, slice, build numeric lists, use tuples |
| 5 | [if Statements](#chapter-5--if-statements) | Make decisions with conditional logic |
| 6 | [Dictionaries](#chapter-6--dictionaries) | Store and look up data by key |
| 7 | [User Input and while Loops](#chapter-7--user-input-and-while-loops) | Take input and repeat until a condition changes |
| 8 | [Functions](#chapter-8--functions) | Package reusable behavior with parameters and returns |
| 9 | [Classes](#chapter-9--classes) | Model things with attributes, methods, and inheritance |
| 10 | [Files and Exceptions](#chapter-10--files-and-exceptions) | Read/write files and handle errors gracefully |
| 11 | [Testing Your Code](#chapter-11--testing-your-code) | Write automated tests so changes don't break things |

## After Part I

Once these feel solid, good next steps for this repo's goals:

- **Practice on DSA problems** — see [knowledge/dsa/](../dsa/). Implementing algorithms is the
  fastest way to cement loops, lists, dicts, and functions.
- **Write small scripts** that read files, parse logs, or automate a chore — fundamentals
  applied to real problems.
- **Skim the standard library docs** for `os`, `pathlib`, `json`, `argparse`, and `subprocess`
  as you need them.

---

## Chapter 1 — Getting Started

> This chapter helps you get Python installed and a text editor set up so you can write and run your very first program, `hello_world.py`.

**What you'll learn:**
- The difference between Python 2 and Python 3, and which to use
- How to check whether Python is already installed on your computer
- How to install a beginner-friendly text editor (Geany or Sublime Text)
- How to run code two ways: in an interactive terminal session and from a saved file
- How to troubleshoot common setup problems

### What Python Is (and Python 2 vs. Python 3)
Python is a cross-platform programming language, meaning a program you write should run on any modern computer that has Python installed, regardless of the operating system. Two versions are still in use: the older Python 2 and the newer Python 3. The language keeps improving over time, and a few changes mean some Python 2 code won't run correctly under Python 3.

The recommendation is simple: **use Python 3** if you can. Only fall back to Python 2 if it's the only version already on your system and you'd rather start coding immediately. Even then, plan to switch to Python 3 soon.

### Two Ways to Run Python Code
There are two ways to run Python, and you'll use both:

1. **The interactive interpreter (terminal session)** — Python comes with an interpreter that runs inside a terminal window. You type a line, press Enter, and see the result immediately. This is great for trying out small ideas without saving a file. You'll recognize interpreter output by the `>>>` prompt:

```python
>>> print("Hello Python interpreter!")
Hello Python interpreter!
```

2. **Saved program files** — Most real programs are written in a text editor, saved as a `.py` file, and then run. This is how you'll write most of your code throughout the book.

### The Hello World Program
By tradition, the first program you write in a new language prints a "Hello world!" message. In Python this takes just one line:

```python
print("Hello world!")
```

It looks trivial, but it's meaningful: if this runs correctly on your machine, your Python setup is working and other programs should run too.

### Checking for Python and Installing It
The setup steps vary slightly by operating system, but the general flow is the same: check whether Python is already installed, install it if needed, then install a text editor.

- **Linux:** Python is almost always preinstalled. Open a terminal (in Ubuntu, `Ctrl-Alt-T`) and type `python` to see the default version. Type `python3` to check for Python 3 specifically. Press `Ctrl-D` or type `exit()` to leave the prompt.
- **macOS (OS X):** Python is usually preinstalled too. Open Terminal (Applications → Utilities → Terminal) and run `python`, then `python3`, to see what's available.
- **Windows:** Python usually is *not* preinstalled. Open a command window and type `python`. If you see an error saying it's not recognized, download an installer from python.org/downloads, run it, and **be sure to check "Add Python to PATH"** during installation — this saves a lot of configuration trouble later.

A handy detail: if `python` gives you Python 2 but `python3` works, then anywhere the book says `python`, type `python3` instead.

### Setting Up a Text Editor
A good editor highlights your code and can run programs for you. The book recommends:
- **Geany** on Linux and Windows (`sudo apt-get install geany` on most Linux systems, or download from geany.org on Windows).
- **Sublime Text** on macOS (download from sublimetext.com).

After installing, create a project folder called `python_work` (use lowercase letters and underscores — a common Python naming convention), then save an empty file named `hello_world.py` inside it. The `.py` extension tells the editor the file is Python and to highlight it accordingly.

Type your one line of code and save:

```python
print("Hello Python world!")
```

If your system uses `python3` rather than `python`, you may need to point the editor at the right interpreter (in Geany via **Build → Set Build Commands**; in Sublime Text by creating a new build system). Then run the program — in Geany press `F5` or click Execute; in Sublime Text press `Ctrl-B` (or `Cmd-B`). You should see:

```
Hello Python world!
```

### Running a Program from a Terminal
Sometimes you'll want to run an existing program without opening it in an editor. You can do this on any system once you can navigate to the file's folder:
- `cd` (change directory) moves you into a folder.
- `ls` (Linux/macOS) or `dir` (Windows) lists the files in the current folder.

```text
~$ cd Desktop/python_work/
~/Desktop/python_work$ ls
hello_world.py
~/Desktop/python_work$ python hello_world.py
Hello Python world!
```

Once you're in the right folder, just run `python hello_world.py` (or `python3 ...`).

### Troubleshooting Setup Problems
If `hello_world.py` won't run, don't panic. When something is seriously wrong, Python prints a **traceback** that hints at the problem. Reread the relevant steps and check your code character by character. A few practical remedies: take a short break and look again with fresh eyes, delete the file and recreate it from scratch, have someone watch you repeat the steps, or ask for help — including online forums. The Python community is friendly to beginners, and every programmer has been stuck before.

### Common pitfalls
- Capitalizing `print` (Python is case-sensitive, so `Print` causes an error).
- Forgetting one or both quotation marks, or one or both parentheses.
- On Windows, forgetting to check "Add Python to PATH," which leads to the "`python` is not recognized" error.
- Using `python` when your system actually needs `python3`.
- Using spaces or uppercase in file and folder names instead of the lowercase-with-underscores convention.

### Practice
- Visit python.org and browse the site to find topics that interest you.
- Open `hello_world.py` and deliberately introduce a typo, then run it. Try to find a typo that produces an error and read the message — and one that surprisingly does *not* cause an error.
- Imagine you had unlimited programming skill: jot down three programs you'd love to build, and keep this as a running "ideas" list.

### Key takeaways
- Python runs on every major operating system; the setup steps differ slightly per OS but the goal is the same.
- Prefer Python 3 over Python 2 for new learning.
- You can run code interactively at the `>>>` prompt or by saving and running `.py` files; you'll use both.
- A text editor like Geany or Sublime Text makes writing and running programs much easier.
- Syntax matters: even a missing quote or wrong capitalization stops a program, and tracebacks help you find the cause.

---

## Chapter 2 — Variables and Simple Data Types

> This chapter introduces the basic building blocks of Python: variables that store data, and the simple data types (strings and numbers) you'll use in almost every program.

**What you'll learn:**
- How to create and name variables, and how to read and fix name errors.
- How to work with strings: changing case, inserting variable values, and managing whitespace.
- How to work with numbers (integers and floats) and avoid type errors.
- How to write comments that explain your code.
- The guiding philosophy behind well-written Python ("The Zen of Python").

### Variables
A *variable* is a label that points to a value. You create one by assigning a value with `=`, then you can use the variable wherever you'd use that value. A variable can be reassigned at any time, and Python always tracks its current value.

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

**Naming rules and guidelines:**
- Names may contain only letters, numbers, and underscores, and must start with a letter or underscore (not a number). `message_1` is valid; `1_message` is not.
- No spaces are allowed; use underscores to separate words (`greeting_message`, not `greeting message`).
- Avoid Python keywords and built-in function names (don't name a variable `print`).
- Keep names short but descriptive: `student_name` beats both `s_n` and `length_of_persons_name`.
- Stick to lowercase for now, and be careful with `l`/`O`, which look like `1`/`0`.

### Avoiding name errors
If you reference a variable that Python doesn't recognize (usually a typo), you get a `NameError`. Python prints a *traceback* showing the file, the line number, and the kind of error. Read it from the bottom up to see what went wrong.

```python
message = "Hello reader!"
print(mesage)   # typo: 'mesage' was never defined
# NameError: name 'mesage' is not defined
```

Python only checks that names are spelled *consistently* — it doesn't spellcheck English. If you misspell the name the same way everywhere, the program still runs.

### Strings
A *string* is a series of characters wrapped in quotes. You can use single or double quotes, which lets you include the other kind inside the string.

```python
"This is a string."
'This is also a string.'
'I told my friend, "Python is my favorite language!"'
```

**Changing case with methods.** A *method* is an action Python performs on a piece of data, written with a dot after the value. `title()` capitalizes each word; `upper()` and `lower()` convert the whole string. Using `lower()` is handy for normalizing user input before storing it.

```python
name = "ada lovelace"
print(name.title())   # Ada Lovelace
print(name.upper())   # ADA LOVELACE
print(name.lower())   # ada lovelace
```

**Using variables in strings.** You can combine strings with the `+` operator (called *concatenation*) to build messages from stored values.

```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")   # Hello, Ada Lovelace!
```

> Note: Modern Python also offers *f-strings*, which are usually cleaner: `print(f"Hello, {full_name.title()}!")`. The 1st-edition book teaches concatenation here, but f-strings are worth knowing as you progress.

**Whitespace with tabs and newlines.** *Whitespace* means nonprinting characters like spaces, tabs, and line breaks. Use `\t` for a tab and `\n` for a newline to organize output.

```python
print("\tPython")                               # indented with a tab
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Languages:
#     Python
#     C
#     JavaScript
```

**Stripping whitespace.** Extra spaces can make two strings that look identical compare as different (important when checking usernames, for example). Use `rstrip()`, `lstrip()`, and `strip()` to remove whitespace from the right, left, or both sides. These methods return a new value, so reassign it to make the change stick.

```python
favorite_language = ' python '
favorite_language = favorite_language.strip()   # 'python'
```

### Numbers
**Integers** are whole numbers. You can add (`+`), subtract (`-`), multiply (`*`), divide (`/`), and raise to a power (`**`). Python respects order of operations, and parentheses let you control it.

```python
print(3 / 2)        # 1.5
print(3 ** 2)       # 9 (3 to the power of 2)
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

**Floats** are any numbers with a decimal point. They usually behave as expected, but occasionally you'll see extra trailing decimal places (e.g. `0.1 + 0.2` gives `0.30000000000000004`). This happens in every language and is normally nothing to worry about.

**Avoiding type errors with `str()`.** You can't directly join a number to a string with `+` — Python raises a `TypeError`. Wrap the number in `str()` to convert it to text first.

```python
age = 23
# message = "Happy " + age + "rd Birthday!"   # TypeError
message = "Happy " + str(age) + "rd Birthday!"
print(message)   # Happy 23rd Birthday!
```

### Comments
A comment is a note written in plain English for human readers; Python ignores it. Start a comment with a hash mark (`#`). Good comments explain *why* and *how* your code works, which saves time when you (or others) return to it later.

```python
# Say hello to everyone.
print("Hello Python people!")
```

### The Zen of Python
Type `import this` in a Python session to read "The Zen of Python" by Tim Peters — a short set of guiding principles such as "Beautiful is better than ugly," "Simple is better than complex," and "Readability counts." The takeaway: favor clear, simple solutions, and write code that works now rather than chasing perfection.

### Common pitfalls
- **Name errors:** misspelling a variable name or using it before assigning it raises `NameError`.
- **Mixing strings and numbers:** `"Age: " + 23` raises a `TypeError`; convert the number with `str()` first.
- **Mismatched or missing quotes:** an apostrophe inside single quotes (`'Python's'`) ends the string early and causes a `SyntaxError`; use double quotes around it instead.
- **Forgetting to reassign:** `strip()` and friends return a new string — `text.strip()` alone doesn't change `text`.

### Practice
- Store a message in a variable and print it. Then change the variable's value and print the new message.
- Store a person's name in a variable and print it three ways: lowercase, uppercase, and titlecase.
- Store a quote and its author, then print a formatted sentence like `Albert Einstein once said, "..."`.
- Store a name padded with `\t` and `\n` whitespace, print it as-is, then print it cleaned up with `lstrip()`, `rstrip()`, and `strip()`.

### Key takeaways
- Variables hold values; use clear, lowercase, underscore-separated names.
- Read tracebacks bottom-up — they tell you the error type and location.
- Strings have handy methods (`title()`, `upper()`, `lower()`, `strip()`) and can be combined with `+`.
- Numbers come as integers and floats; use `str()` when putting a number inside a string.
- Write comments for the reader, and aim for simple, readable code.

---

## Chapter 3 — Introducing Lists

> A list lets you store an ordered collection of items in a single variable, and Python gives you simple tools to read, change, grow, shrink, and organize that collection.

**What you'll learn:**
- How to create a list and access its items by index
- Why indexing starts at 0, and how `-1` reaches the last item
- How to modify, add, and remove elements (`append()`, `insert()`, `del`, `pop()`, `remove()`)
- How to organize a list (`sort()`, `sorted()`, `reverse()`, `len()`)
- How to recognize and avoid index errors

### What a list is
A list is a collection of items kept in a particular order. You can store anything you like in it, and the items don't have to be related. In Python you write a list with square brackets and separate items with commas. Because a list usually holds many things, it's conventional to name it with a plural noun.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# ['trek', 'cannondale', 'redline', 'specialized']
```

### Accessing elements by index
To pull out a single item, write the list name followed by the item's index (its position) in square brackets. Python returns just that value, without brackets or quotes. You can also call string methods on a retrieved element.

```python
print(bicycles[0])          # trek
print(bicycles[0].title())  # Trek
```

### Index positions start at 0
The first item is at index `0`, the second at `1`, and so on — so the *fourth* item is `bicycles[3]`. This zero-based counting is the most common source of beginner mistakes. Negative indexes count from the end: `-1` is the last item, `-2` the second-to-last, and so on. Using `-1` is handy when you don't know the list's length.

```python
print(bicycles[1])   # cannondale
print(bicycles[-1])  # specialized (last item)
```

### Using individual values from a list
A value pulled from a list behaves like any other variable, so you can use it to build strings or messages.

```python
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)  # My first bicycle was a Trek.
```

### Modifying elements
To change an item, assign a new value to it by its index.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']
```

### Adding elements
- **`append()`** adds an item to the *end* of the list. It's great for building a list one item at a time, even starting from an empty list `[]`.
- **`insert()`** adds an item at a specific index, shifting everything after it to the right.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')     # ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.insert(0, 'ducati')  # puts 'ducati' at the front
```

### Removing elements
- **`del`** removes an item by index when you don't need its value afterward.
- **`pop()`** removes the *last* item (or the item at a given index with `pop(i)`) and *returns* it, so you can keep using it.
- **`remove()`** removes the first matching item by *value* when you don't know its index.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]                  # removes 'honda', value discarded
last = motorcycles.pop()            # removes & returns 'suzuki'
first = motorcycles.pop(0)          # removes & returns by index

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')        # removes by value
```

Rule of thumb: use `del` when you're done with the item, and `pop()` when you still want to use it. Note that `remove()` deletes only the *first* occurrence of a value.

### Organizing a list
- **`sort()`** sorts the list alphabetically *in place* (permanently); pass `reverse=True` to sort in reverse.
- **`sorted()`** returns a sorted copy for display while leaving the original order untouched; it also accepts `reverse=True`.
- **`reverse()`** flips the current order in place (not an alphabetical sort); call it twice to restore the original order.
- **`len()`** returns the number of items in the list.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()                 # permanent: ['audi', 'bmw', 'subaru', 'toyota']
print(sorted(cars))         # temporary sorted copy
cars.reverse()              # flips current order
print(len(cars))            # 4
```

### Avoiding index errors
Asking for an index that doesn't exist raises `IndexError: list index out of range`. The classic cause is the off-by-one mistake: a three-item list has valid indexes `0`, `1`, `2` — there is no index `3`. If you hit an index error, try adjusting your index by one. `[-1]` always works for the last item *except* on an empty list, which has no items to return. When confused, print the list or its `len()` to see what it actually contains.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])  # IndexError: list index out of range
```

### Common pitfalls
- **Off-by-one errors:** the first item is index `0`, so the *n*th item is at index `n - 1`.
- **`pop()` vs `remove()` vs `del`:** `pop()` returns the removed value (and defaults to the last item), `del` discards it by index, `remove()` deletes by value (first match only).
- **`sort()` vs `sorted()`:** `sort()` changes the list permanently; `sorted()` leaves it alone and gives you a sorted copy.
- **`reverse()` isn't a sort:** it just flips the existing order.
- **`[-1]` on an empty list** still raises an index error.

### Practice
- **Friends:** Store a few friends' names in a list called `names` and print each name by accessing it one element at a time.
- **Guest list:** Make a list of at least three people you'd invite to dinner, then print a personalized invitation message to each.
- **Changing guests:** Starting from your guest list, announce that one guest can't come, replace their name with someone new, and reprint the invitations.
- **Travel sort:** Store five places you'd like to visit (not in order), then practice every organizing tool — print the original, `sorted()` both ways, `reverse()` twice, and `sort()` both ways — confirming after each step.

### Key takeaways
- A list is an ordered, square-bracketed collection accessed by zero-based index, with `-1` for the last item.
- Modify items by index assignment; grow lists with `append()` and `insert()`.
- Remove items with `del` (by index, discarded), `pop()` (by index, returned), or `remove()` (by value).
- Organize with `sort()` (permanent), `sorted()` (temporary copy), `reverse()` (flip order), and measure with `len()`.
- Most beginner list bugs are off-by-one index errors — print the list or its length to debug.

---

## Chapter 4 — Working with Lists

> Learn to loop through lists efficiently, build and slice numerical lists, copy lists safely, use immutable tuples, and style your code with PEP 8.

**What you'll learn:**
- How to process every item in a list with a `for` loop and why indentation defines the loop body
- How to spot and fix the most common indentation and syntax errors
- How to generate numerical lists with `range()`, `list()`, and list comprehensions
- How to grab part of a list with slices and copy a list correctly
- What tuples are, why immutability matters, and the basics of writing clean, readable code

### Looping through an entire list
When you want to do the same thing to every item in a list, a `for` loop saves you from repeating yourself. Python pulls each value out one at a time, stores it in a temporary variable, and runs the loop body for it.

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
```

Read it as "for every magician in the list of magicians, do this." Pick a meaningful singular name for the loop variable (`magician`, `cat`, `item`) to make the code easy to follow.

### Indentation and the loop body
Python uses indentation, not braces, to decide which lines belong to the loop. Every indented line after the `for` statement runs once per item. Lines that come after the loop and are *not* indented run only once, after the loop finishes.

```python
for magician in magicians:
    print(magician.title() + ", that was a great trick!")   # runs each pass
    print("Looking forward to your next trick.\n")          # also each pass
print("Thank you, everyone!")                               # runs once, after the loop
```

### Avoiding indentation errors
A few mistakes show up over and over:
- **Forgetting to indent** the line after `for` raises `IndentationError: expected an indented block`.
- **Forgetting to indent an extra line** is a logical error: the line runs only once (after the loop) instead of every pass, so your output is wrong without any crash.
- **Indenting unnecessarily** raises `IndentationError: unexpected indent`. Only indent when you have a reason to.
- **Forgetting the colon** at the end of the `for` line causes a `SyntaxError`.

### Making numerical lists with range()
`range()` generates a series of numbers. It starts at the first value and stops *before* the second (the classic off-by-one behavior), so `range(1, 5)` gives 1–4. Wrap it in `list()` to build an actual list, and add a third argument as a step size.

```python
numbers = list(range(1, 6))        # [1, 2, 3, 4, 5]
even_numbers = list(range(2, 11, 2))   # [2, 4, 6, 8, 10]
```

You can also build lists in a loop, for example the first ten squares:

```python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)     # ** is the exponent operator
```

Python provides quick statistics for number lists:

```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))   # 0
print(max(digits))   # 9
print(sum(digits))   # 45
```

### List comprehensions
A list comprehension builds a list in a single line by combining the expression and the `for` loop. Note there is no colon at the end.

```python
squares = [value ** 2 for value in range(1, 11)]
```

Reach for these once writing ordinary lists feels comfortable and repetitive.

### Working with part of a list (slicing)
A slice grabs a range of items. Like `range()`, it stops one item before the end index. Omit the start index to begin at the front, omit the end index to run to the back, and use negative indices to count from the end.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])   # ['charles', 'martina', 'michael']
print(players[:4])    # first four
print(players[2:])    # third through last
print(players[-3:])   # last three
```

You can also loop over just a slice:

```python
for player in players[:3]:
    print(player.title())
```

### Copying a list with [:]
To make a genuine, independent copy of a list, slice the whole thing with `[:]`. Changes to one copy then leave the other untouched.

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]      # a real copy
my_foods.append('cannoli')
friend_foods.append('ice cream')
# the two lists now differ
```

Writing `friend_foods = my_foods` does *not* copy — both names point at the same list, so a change to one shows up in the other.

### Tuples
A tuple is an immutable list: once defined, its values cannot change. Use parentheses instead of square brackets, and access items by index just like a list.

```python
dimensions = (200, 50)
print(dimensions[0])     # 200
# dimensions[0] = 250    # TypeError: 'tuple' object does not support item assignment
```

You can loop over a tuple with `for`, and although you cannot change individual items, you *can* reassign the whole variable to a new tuple.

```python
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)   # overwriting the whole tuple is fine
```

Use tuples for sets of values that should stay fixed for the life of the program.

### Styling your code (PEP 8 basics)
Code is read far more often than it is written, so make it readable. PEP 8 is Python's official style guide; a few essentials for now:
- **Indentation:** use four spaces per level (set your editor to insert spaces, never mix tabs and spaces).
- **Line length:** keep lines under about 79–80 characters so files fit side by side onscreen.
- **Blank lines:** use them to group related sections, but don't stack several in a row.

### Common pitfalls
- Forgetting to indent the loop body, or forgetting the colon after `for`.
- Indenting a line that belongs after the loop, so it wrongly repeats every pass.
- Expecting `range()` or a slice to include the end value — it stops one short.
- Aliasing a list with `b = a` instead of copying it with `b = a[:]`, so edits leak between the two.
- Trying to change a tuple item in place, which raises a `TypeError`.

### Practice
- Store three favorite pizzas in a list, loop over it to print a sentence like "I like pepperoni pizza," and print a closing line outside the loop.
- Make a list of the numbers 1 to one million, then use `min()`, `max()`, and `sum()` to confirm its range and total.
- Use a list comprehension to build a list of the first ten cubes.
- Store five foods in a tuple, loop over them, confirm Python rejects an edit, then reassign the whole tuple to a new menu and loop again.

### Key takeaways
- A `for` loop applies the same action to every item in a list, no matter how long it is.
- Indentation defines the loop body; the wrong indentation causes either errors or silent logic bugs.
- `range()`, `list()`, `min()`/`max()`/`sum()`, and list comprehensions make working with number lists easy.
- Slices pull out subsets, and `[:]` is the safe way to copy a list — plain assignment just creates an alias.
- Tuples hold values that shouldn't change, and following PEP 8 (4-space indents, short lines, sensible blank lines) keeps your code readable.

---

## Chapter 5 — if Statements

> Learn to write conditional tests that evaluate to True or False, and use `if` statements to make your programs respond differently depending on the current situation.

**What you'll learn:**
- How to write conditional tests using equality, inequality, and numerical comparisons.
- How to combine conditions with `and`/`or`, and check membership with `in`/`not in`.
- How to build `if`, `if-else`, and `if-elif-else` structures to handle two or more cases.
- How to combine `if` statements with lists (special items, empty lists, multiple lists).
- How to style conditional tests cleanly following PEP 8.

### Conditional tests
Every `if` statement is built on a *conditional test*: an expression that evaluates to `True` or `False`. If the test is `True`, Python runs the indented code; if `False`, it skips it.

**Equality (`==`) and inequality (`!=`).** A single `=` *assigns* a value; a double `==` *asks a question* ("are these equal?"). Use `!=` to check that two values differ.

```python
car = 'bmw'
print(car == 'bmw')   # True
print(car != 'audi')  # True

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

**Case sensitivity.** String comparisons are case sensitive, so `'Audi' == 'audi'` is `False`. If case shouldn't matter, compare against a lowercased copy with `.lower()` (which doesn't change the original):

```python
car = 'Audi'
print(car.lower() == 'audi')  # True
```

**Numerical comparisons.** You can use `==`, `!=`, `<`, `<=`, `>`, and `>=` with numbers.

```python
age = 19
print(age < 21)   # True
print(age >= 21)  # False
```

**Multiple conditions with `and` / `or`.** Use `and` when *both* tests must pass; use `or` when *at least one* must pass.

```python
age_0, age_1 = 22, 18
print(age_0 >= 21 and age_1 >= 21)  # False (age_1 fails)
print(age_0 >= 21 or age_1 >= 21)   # True (age_0 passes)
```

**Checking membership with `in` / `not in`.** Test whether a value is (or isn't) in a list.

```python
requested = ['mushrooms', 'onions']
print('mushrooms' in requested)  # True

banned_users = ['andrew', 'carolina']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response.")
```

**Boolean expressions.** A conditional test is also called a *Boolean expression*. A Boolean value is simply `True` or `False`, often used to track program state: `game_active = True`, `can_edit = False`.

### if statements
**Simple `if`.** One test, one action. Everything indented under the `if` runs only when the test passes.

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
```

**`if-else`.** Run one block when the test passes and a different block in every other case. Exactly one of the two blocks always runs.

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
```

**`if-elif-else` chain.** Test more than two situations. Python checks each test in order and runs only the *first* block that passes, then skips the rest.

```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")
```

**Multiple `elif` blocks.** Add as many `elif` blocks as you need for additional cases (for example, a senior discount).

**Omitting `else`.** The `else` block is optional. Since `else` catches *anything* not matched above (including bad data), a final, specific `elif` is sometimes clearer and safer than a catchall `else`.

**Testing multiple conditions independently.** When you need to act on *every* condition that's true (not just the first), use a series of separate `if` statements rather than an `if-elif-else` chain.

```python
requested = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested:
    print("Adding mushrooms.")
if 'extra cheese' in requested:
    print("Adding extra cheese.")
```

### Using if statements with lists
**Checking for special items.** Put an `if` inside a `for` loop to handle one value differently from the rest (e.g., a topping that's sold out).

```python
requested = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers.")
    else:
        print("Adding " + topping + ".")
```

**Checking a list isn't empty.** A list name used in an `if` is `True` when the list has items and `False` when empty—handy before looping.

```python
requested = []
if requested:
    for topping in requested:
        print("Adding " + topping + ".")
else:
    print("Are you sure you want a plain pizza?")
```

**Using multiple lists.** Check each requested value against a list of allowed values before acting on it.

```python
available = ['mushrooms', 'olives', 'extra cheese']
requested = ['mushrooms', 'french fries', 'extra cheese']
for topping in requested:
    if topping in available:
        print("Adding " + topping + ".")
    else:
        print("Sorry, we don't have " + topping + ".")
```

### Styling your if statements
PEP 8 recommends a single space around comparison operators. Write `if age < 4:` rather than `if age<4:`. The spacing doesn't change behavior—it just makes code easier to read.

### Common pitfalls
- Using `=` (assignment) where you meant `==` (equality test).
- Forgetting that string comparisons are case sensitive (`'Audi' != 'audi'`); use `.lower()` when case shouldn't matter.
- Using an `if-elif-else` chain when more than one condition should fire—it stops after the first match. Use separate `if` statements instead.
- Misusing `and`/`or`: `and` needs both sides true; `or` needs only one.
- Forgetting the colon `:` at the end of an `if`/`elif`/`else` line, or inconsistent indentation of the block.

### Practice
- Write at least 10 conditional tests, printing your prediction (True/False) before each one, and confirm you understand each result. Cover equality, inequality, `.lower()`, numeric comparisons, `and`/`or`, and `in`/`not in`.
- Assign `alien_color` a value of `'green'`, `'yellow'`, or `'red'`, then write an `if-elif-else` chain that awards 5, 10, or 15 points depending on the color.
- Write an `if-elif-else` chain that prints a person's stage of life (baby, toddler, kid, teenager, adult, elder) based on an `age` variable.
- Build a list of usernames including `'admin'`; loop through it, greeting `'admin'` specially and everyone else generically. Then add a check that prints a message if the list is empty.

### Key takeaways
- A conditional test always evaluates to `True` or `False` and decides whether an indented block runs.
- Use `==`/`!=` for equality, numeric operators for comparisons, `and`/`or` to combine tests, and `in`/`not in` for membership.
- Choose the structure to fit the cases: simple `if`, `if-else` for two outcomes, `if-elif-else` for many (only the first match runs).
- For acting on multiple independent conditions, use separate `if` statements, not a single chain.
- An empty list is `False` in an `if`, so you can check a list has items before looping over it.

---

## Chapter 6 — Dictionaries

> Dictionaries let you connect related pieces of information as key-value pairs, so you can store and look up data by a meaningful label instead of a position.

**What you'll learn:**
- What a dictionary is and how key-value pairs work
- How to access, add, modify, and remove items in a dictionary
- How to loop through a dictionary's pairs, keys, or values (including in sorted order)
- How to pull out unique values with `set()`
- How to nest dictionaries and lists inside one another to model richer data

### What a dictionary is
A dictionary is a collection of *key-value pairs*. Each key is linked to a value, and you use the key to look up its value. Dictionaries are wrapped in braces `{}`, a colon separates each key from its value, and commas separate the pairs. A value can be a number, string, list, or even another dictionary.

```python
alien_0 = {'color': 'green', 'points': 5}
# 'color' and 'points' are keys; 'green' and 5 are their values
```

### Accessing values
To get a value, put its key in square brackets after the dictionary name.

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])          # green
new_points = alien_0['points']   # 5
```

### Adding and starting empty
Dictionaries are dynamic—you can add pairs at any time by assigning to a new key. You can also start with an empty `{}` and fill it in, which is common when storing user input or generating many pairs programmatically.

```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0   # add another pair later
```

### Modifying and removing values
Assign a new value to an existing key to change it. Use `del` to permanently remove a key and its value.

```python
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'   # modify
del alien_0['color']          # remove the pair entirely
```

### Looping through a dictionary
Use `.items()` to loop over key-value pairs together. You choose the loop variable names.

```python
user = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user.items():
    print(key + ": " + value)
```

Use `.keys()` to loop over just the keys (this is also the default if you loop over the dictionary directly), and `.values()` for just the values. `keys()` is also handy for membership checks like `if 'erin' not in favorite_languages.keys():`.

```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'phil': 'python'}

for name in favorite_languages.keys():        # keys
    print(name.title())

for name in sorted(favorite_languages.keys()): # keys in sorted order
    print(name.title())

for language in set(favorite_languages.values()):  # unique values only
    print(language.title())
```

Wrapping `set()` around the values removes duplicates (here `python` appears once instead of twice).

### Nesting
You can nest to model more complex data: a list of dictionaries, a list inside a dictionary, or a dictionary inside a dictionary.

```python
# A list of dictionaries
aliens = [{'color': 'green'}, {'color': 'yellow'}, {'color': 'red'}]
for alien in aliens:
    print(alien)

# A list inside a dictionary
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
for topping in pizza['toppings']:
    print(topping)

# A dictionary inside a dictionary
users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein'},
    'mcurie':    {'first': 'marie',  'last': 'curie'},
}
for username, info in users.items():
    print(username + ": " + info['first'].title() + " " + info['last'].title())
```

Keep nested dictionaries that hold the same kind of object consistent in structure so you can loop over them uniformly—and avoid nesting too deeply, which usually signals a simpler design exists.

### Common pitfalls
- Asking for a key that doesn't exist (e.g. `alien_0['speed']`) raises a `KeyError`—check with `in` first when unsure.
- Don't rely on dictionary order (in this 1st-edition material, pairs are returned in an unpredictable order); sort the keys with `sorted()` if you need a specific order.
- `del` removes a pair permanently—there's no undo.
- Quoting matters: assigning `alien_0['speed'] = fast` (no quotes) refers to a variable, not the string `'fast'`.
- Looping with `.values()` includes duplicates unless you wrap it in `set()`.

### Practice
- Build a dictionary describing a person with keys like `first_name`, `last_name`, `age`, and `city`, then print each piece of information.
- Create a glossary where five programming terms are keys and their definitions are values, then loop through it printing each term and its meaning neatly.
- Make a `rivers` dictionary mapping rivers to countries, then use loops to print a sentence per river, all river names, and all country names.
- Build a `cities` dictionary where each city key maps to its own dictionary of `country`, `population`, and a `fact`, then print everything stored for each city.

### Key takeaways
- A dictionary maps keys to values; you access a value via its key in square brackets.
- Dictionaries are dynamic—add, modify, and `del` pairs freely, or start from an empty `{}`.
- Loop with `.items()`, `.keys()`, or `.values()`; combine with `sorted()` for order and `set()` for unique values.
- Use `in` / `not in` to safely test for keys and avoid `KeyError`.
- Nesting (lists of dicts, lists in dicts, dicts in dicts) lets you model real-world data, but keep structures consistent and shallow.

---

## Chapter 7 — User Input and while Loops

> Learn to collect information from users with `input()` and keep programs running on your terms with `while` loops.

**What you'll learn:**
- How to prompt for and capture user input with `input()`
- How to convert text input into numbers with `int()` and use the modulo operator `%`
- How to run code repeatedly with `while` loops and stop them cleanly
- How to steer loops with flags, `break`, and `continue` (and how to avoid infinite loops)
- How to use `while` loops to process lists and dictionaries of user data

### Getting input with input()
The `input()` function pauses your program, waits for the user to type something and press Enter, then hands that text back so you can store it in a variable. You pass it a *prompt* string that tells the user what to enter. End your prompts with a space so the typed answer doesn't crowd the prompt text.

```python
name = input("Please enter your name: ")
print("Hello, " + name + "!")
```

For longer prompts, build the string first (using `+=` to add to it across lines), then pass that variable to `input()`:

```python
prompt = "If you tell us who you are, we can personalize your messages."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
```

### Turning input into numbers with int()
`input()` always returns a **string**, even if the user types digits. If you try to compare that string to a number, Python raises a `TypeError`. Wrap the input in `int()` to convert it to an integer before doing math or comparisons:

```python
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")
```

### The modulo operator (%)
`%` divides one number by another and returns the **remainder** (not how many times it fits). When the remainder is `0`, the first number divides evenly by the second — a handy way to test for even/odd:

```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")
```

### while loops: running while a condition is true
A `for` loop runs once per item in a collection; a `while` loop runs as long as a condition stays true. This one counts from 1 to 5:

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

### Letting the user choose when to quit
Put the work inside a `while` loop and keep going until the user types a quit value. Give the test variable a starting value so Python has something to compare on the first pass:

```python
message = ""
while message != 'quit':
    message = input("Tell me something (or 'quit'): ")
    if message != 'quit':
        print(message)
```

### Using a flag
When many different events could end a program, track a single boolean *flag* and loop on that. Any event can flip the flag to `False`, keeping the `while` condition simple:

```python
active = True
while active:
    message = input("Say something (or 'quit'): ")
    if message == 'quit':
        active = False
    else:
        print(message)
```

### Using break to exit a loop
`break` exits a loop immediately, skipping any remaining code. A `while True:` loop runs forever until it hits a `break`:

```python
while True:
    city = input("A city you've visited (or 'quit'): ")
    if city == 'quit':
        break
    print("I'd love to go to " + city.title() + "!")
```

### Using continue to skip an iteration
`continue` jumps back to the top of the loop without finishing the current pass. This prints only odd numbers from 1 to 10:

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

### Avoiding infinite loops
Every `while` loop needs something that can eventually make its condition `False` (or reach a `break`). Forgetting to update the test variable — like leaving out `x += 1` — makes the loop run forever. If you get stuck, press `ctrl-C` or close the window, then check that some part of the loop can end it.

### while loops with lists and dictionaries
You shouldn't modify a list inside a `for` loop, but a `while` loop is built for it.

**Move items between lists** with `pop()` (which removes and returns an item) and `append()`:

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
```

**Remove every instance of a value** by looping until it's gone:

```python
pets = ['dog', 'cat', 'dog', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)  # ['dog', 'dog', 'rabbit']
```

**Fill a dictionary from user input**, collecting multiple values each pass:

```python
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb? ")
    responses[name] = response
    repeat = input("Let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
```

### Common pitfalls
- **Comparing input to a number without `int()`** — `input()` returns a string, so `age >= 18` fails with a `TypeError` until you convert with `int()`.
- **Infinite loops** — forgetting to change the variable in the loop's condition (e.g., omitting `x += 1`) keeps it `True` forever.
- **No initial value** — referencing a variable in the `while` condition before it's defined breaks the first comparison; set it (e.g., `message = ""`) first.
- **Modifying a list inside a `for` loop** — use a `while` loop when adding or removing items as you go.
- **Printing the quit value** — without an `if` guard, the loop may print or process the sentinel word itself.

### Practice
- **Multiples of Ten:** Ask the user for a number and report whether it's a multiple of 10.
- **Movie Tickets:** Loop asking each user's age, then print their ticket price (free under 3, $10 for ages 3–12, $15 over 12).
- **Deli:** Fill a `sandwich_orders` list, then use a loop to "make" each one (printing a message) and move it into a `finished_sandwiches` list; finally list all finished sandwiches.
- **Dream Vacation:** Poll users about where they'd travel, storing answers, then print all the results.

### Key takeaways
- `input()` always returns a string — convert with `int()` before numeric work.
- `while` loops run as long as a condition is true; always ensure they can end.
- Flags, `break`, and `continue` give you fine control over how a loop flows.
- `while` loops are the right tool for collecting and reshaping lists and dictionaries of user data.
- `%` returns a division remainder — great for divisibility and even/odd checks.

---

## Chapter 8 — Functions

> Functions are named, reusable blocks of code that do one specific job, so you write logic once and call it whenever you need it.

**What you'll learn:**
- How to define and document functions with `def` and docstrings
- The different ways to pass information in: positional, keyword, default, and arbitrary arguments
- How to return values (including dictionaries) and use functions inside loops
- How passing a list lets a function modify (or, with a copy, not modify) your data
- How to organize functions into modules you import into other programs

### Defining a function
Use the `def` keyword, a descriptive name, parentheses (which may hold parameters), and a colon. The indented lines below are the function body. The first line should be a *docstring* in triple quotes that briefly says what the function does. To run a function, *call* it by writing its name followed by parentheses.

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

### Passing arguments
A *parameter* is the variable listed in the definition; an *argument* is the actual value you pass in when calling. Python must match each argument to a parameter, and you have several ways to do that.

**Positional arguments** are matched by order, so the order you pass them must mirror the order of the parameters. Get the order wrong and you get nonsense (a "harry" named "Hamster"), not an error.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("I have a " + animal_type + " named " + pet_name.title() + ".")

describe_pet('hamster', 'harry')   # order matters
```

**Keyword arguments** are `name=value` pairs, so order no longer matters and each value's role is clear. Use the exact parameter names.

```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')   # equivalent
```

**Default values** let you give a parameter a fallback used when no argument is supplied. Any parameter with a default must come *after* all parameters without defaults, so positional matching still works.

```python
def describe_pet(pet_name, animal_type='dog'):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')                       # uses default 'dog'
describe_pet('harry', 'hamster')             # overrides the default
```

**Avoiding argument errors:** if you pass too few or too many arguments, Python raises a `TypeError` and the traceback names the missing parameters. Descriptive names make these messages easy to act on.

### Return values
A function can process data and send a result back with `return` instead of just printing. Store the returned value in a variable when you call it.

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')          # Jimi Hendrix
musician = get_formatted_name('john', 'hooker', 'lee')    # John Lee Hooker
```

Here `middle_name=''` makes the argument *optional* — an empty string is treated as `False`, so the `if` test skips it. A function can return any structure, including a **dictionary**, which turns loose values into a labeled, meaningful object.

```python
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
```

Functions also pair naturally with a **`while` loop** — for example, repeatedly prompting for input and calling `get_formatted_name()` until the user enters a quit value like `'q'`.

### Passing a list to a function
Passing a list gives the function direct access to its contents, which is handy for looping over names, numbers, or dictionaries.

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        print("Hello, " + name.title() + "!")
```

**Modifying a list in a function:** because the function works on the real list, any changes it makes are permanent. This is great for jobs like moving items from one list to another.

```python
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current = unprinted_designs.pop()
        completed_models.append(current)
```

**Preventing modification (passing a copy):** if you need to keep the original intact, send a slice copy with `[:]`. Changes then affect only the copy. Still, prefer passing the original unless you have a reason to copy, since copying costs time and memory on large lists.

```python
print_models(unprinted_designs[:], completed_models)   # original stays full
```

### Passing an arbitrary number of arguments
When you don't know how many arguments will come in, prefix a parameter with `*` to collect them into a **tuple**.

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

**Mixing positional and arbitrary arguments:** the `*` parameter must come *last* so Python can fill the named parameters first and sweep the rest into the tuple.

```python
def make_pizza(size, *toppings):
    ...
make_pizza(16, 'pepperoni')
```

**Arbitrary keyword arguments (`**kwargs`):** use `**` to collect arbitrary `name=value` pairs into a **dictionary** — useful when you don't know which extra attributes will be supplied.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary of everything we know about a user."""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

build_profile('albert', 'einstein', location='princeton', field='physics')
```

### Storing functions in modules
Move functions into a separate `.py` file (a *module*) and import it to keep your main program short and reuse code across projects. There are several import styles:

```python
import pizza                       # call as pizza.make_pizza(...)
from pizza import make_pizza        # call as make_pizza(...)
from pizza import make_pizza as mp  # alias a function: mp(...)
import pizza as p                   # alias a module: p.make_pizza(...)
from pizza import *                 # import everything (avoid for code you didn't write)
```

Importing the whole module (with dot notation) or naming specific functions is clearest. `from module import *` risks name clashes that silently overwrite functions, so avoid it for unfamiliar modules.

### Styling functions
- Use descriptive, lowercase names with underscores for both functions and modules.
- Give every function a docstring right after the `def` line so others can use it from the description alone.
- No spaces around `=` for default values and keyword arguments: `parameter_1='default'`.
- Keep lines under 79 characters; break long parameter lists onto multiple indented lines.
- Separate functions with two blank lines, and put all `import` statements at the top of the file.

### Common pitfalls
- **Wrong argument order:** with positional arguments, mismatched order produces wrong (but error-free) results — verify the order matches the definition.
- **Default-parameter placement:** parameters with defaults must follow those without, or Python can't resolve positional matches.
- **Forgetting `return`:** a function that only prints returns `None`; use `return` when the caller needs the value.
- **Unintended list modification:** passing a list lets the function change it permanently — pass `list_name[:]` if you must preserve the original.
- **`*args` / `**kwargs` placement:** the `*` (and `**`) parameter must come last in the definition.
- **`from module import *`:** can overwrite names that collide with your own; prefer explicit imports.

### Practice
- Write `make_shirt(size, message)` that prints the shirt's size and message. Call it once with positional arguments and once with keyword arguments. (8-3)
- Write `make_album(artist, title)` that returns a dictionary describing an album, then add an optional `tracks` parameter that's only stored when provided. (8-7)
- Make a list of magician names and pass it to `make_great()`, which prepends "the Great" to each name; then redo it passing a copy so the original list stays unchanged. (8-10, 8-11)
- Write `make_car(manufacturer, model, **info)` that returns a dictionary and works for a call like `make_car('subaru', 'outback', color='blue', tow_package=True)`. (8-14)

### Key takeaways
- Functions package one specific job under a descriptive name so you write code once and reuse it with a single call.
- Choose the argument style that's clearest: positional, keyword, defaults, or `*args`/`**kwargs` for unknown counts.
- Use `return` to send values (numbers, strings, lists, dictionaries) back to the caller; optional arguments via defaults keep calls simple.
- Passing a list shares it by reference — the function can modify it unless you pass a slice copy `[:]`.
- Store functions in modules and import them to keep main programs readable; favor explicit imports over `import *`.

---

## Chapter 9 — Classes

> Classes let you model real-world things and situations in code by bundling related data (attributes) and behavior (methods), then creating individual objects (instances) from that blueprint.

**What you'll learn:**
- How to define a class with `__init__()`, `self`, attributes, and methods
- How to create instances and access their attributes and methods
- How to read and modify attribute values directly or through methods
- How to reuse code with inheritance, `super()`, and method overriding
- How to organize classes into modules and import them, plus a peek at the standard library

### Creating and using a class

A class is a blueprint for a category of things. Capitalize class names by convention. Writing a `Dog` class describes any dog, not one specific dog.

```python
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")
```

**The `__init__()` method, `self`, and attributes.** A function inside a class is a *method*. `__init__()` is a special method Python runs automatically every time you create a new instance. Its first parameter, `self`, is always required and always first; Python passes it automatically. `self` is a reference to the instance itself, giving each instance access to the class's attributes and methods. Any variable prefixed with `self.` becomes an *attribute*, available to every method and reachable through any instance. Here `sit()` and `roll_over()` need no extra data, so they take only `self`.

### Making instances and creating multiple ones

Think of a class as instructions for building an instance. To make one, call the class with the arguments `__init__()` expects (skip `self`). Use dot notation to read attributes and call methods.

```python
my_dog = Dog('willie', 6)
print(my_dog.name.title())   # Willie
print(my_dog.age)            # 6
my_dog.sit()                 # Willie is now sitting.
```

You can create as many instances as you want; each is independent with its own attribute values:

```python
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
your_dog.sit()               # Lucy is now sitting.
```

Even two instances built with identical values are still separate objects.

### Working with classes and instances

Most of your time is spent working with instances. A `Car` class shows storing data and returning a formatted summary:

```python
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      # default value

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
```

**Setting a default value.** Every attribute needs an initial value. You can set one inside `__init__()` (like `odometer_reading = 0`) without adding a parameter for it.

**Modifying attribute values** can be done three ways:

```python
my_car = Car('audi', 'a4', 2016)

# 1. Directly through the instance
my_car.odometer_reading = 23

# 2. Through a method (which can also add logic)
def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")

# 3. Incrementing through a method
def increment_odometer(self, miles):
    self.odometer_reading += miles
```

Methods let you guard updates (e.g., reject rolling the odometer back), but anyone can still set an attribute directly, so this isn't true security.

### Inheritance

If a new class is a specialized version of an existing one, it can *inherit* all the parent's attributes and methods. The original is the *parent* class; the new one is the *child*.

**The child `__init__()` and `super()`.** The parent must be defined first in the file, and its name goes in the child's parentheses. `super()` calls the parent's `__init__()` so the child instance gets all the parent's attributes.

```python
class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)   # set up the parent's attributes
        self.battery_size = 70                 # new attribute for the child

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
```

**Overriding parent methods.** Define a method in the child with the same name as one in the parent; Python ignores the parent's version. For example, an electric car could override `fill_gas_tank()` to say it doesn't need one.

**Instances as attributes.** When a class grows too large, move part of it into a separate class and store an instance of that class as an attribute.

```python
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()   # an instance held as an attribute

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()   # reach the battery through the car
```

Deciding which class a method belongs to (e.g., is range a property of the battery or the car?) is part of modeling the real world—often there's no single right answer.

### Importing classes

To keep files uncluttered, store classes in modules and import what you need.

```python
# Import a single class
from car import Car

# Import multiple classes from one module
from car import Car, ElectricCar

# Import the whole module, then use dot notation
import car
my_beetle = car.Car('volkswagen', 'beetle', 2016)
```

You can also import every class with `from module_name import *`, but this is **not recommended**—it hides which classes you use and risks name conflicts. When a class in one module depends on one in another, import it at the top of that module (importing a module into a module):

```python
# inside electric_car.py
from car import Car

class ElectricCar(Car):
    --snip--
```

Start simple: put everything in one file, then split classes into modules once it works.

### The Python standard library

The standard library is a set of modules bundled with every Python install—just `import` what you want. For example, `OrderedDict` from the `collections` module behaves like a dictionary but remembers the order keys were added:

```python
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
```

### Styling classes

- Class names use **CamelCaps** (capitalize each word, no underscores); instances and modules use lowercase_with_underscores.
- Give every class a docstring right after its definition, and every module a docstring too.
- Use one blank line between methods, two between classes.
- List standard-library imports first, then a blank line, then your own modules.

### Common pitfalls
- Forgetting `self` as the first parameter of a method, or forgetting to prefix attributes with `self.`.
- Confusing the class (the blueprint, capitalized) with an instance (a specific object, lowercase).
- Forgetting to call `super().__init__()` in a child class, so parent attributes never get set.
- Defining the child class before the parent, or omitting the parent name in the child's parentheses.
- Using `from module import *`, which obscures dependencies and causes naming conflicts.

### Practice
- **Restaurant:** Make a `Restaurant` class whose `__init__()` stores `restaurant_name` and `cuisine_type`. Add `describe_restaurant()` and `open_restaurant()` methods, create an instance, and call both.
- **Users:** Make a `User` class with `first_name`, `last_name`, and a few profile attributes. Add `describe_user()` and `greet_user()` methods, create several users, and call both for each.
- **Ice Cream Stand:** Write an `IceCreamStand` class that inherits from `Restaurant`, add a `flavors` list attribute, and write a method that displays the flavors.
- **OrderedDict Rewrite:** Rewrite an earlier glossary program using `OrderedDict` so the output preserves the insertion order of key-value pairs.

### Key takeaways
- A class bundles attributes (data) and methods (behavior); `__init__()` sets up each new instance, and `self` ties everything to that instance.
- You create independent instances from one class and use dot notation to access their attributes and call their methods.
- Attributes can be given defaults and changed directly or, more safely, through methods.
- Inheritance plus `super()` lets a child class reuse a parent's code, add its own features, and override what doesn't fit; large classes can be split using instances as attributes.
- Store classes in modules and import them to keep files clean, and lean on the standard library for ready-made tools like `OrderedDict`.

---

## Chapter 10 — Files and Exceptions

> Learn to read and write files, handle errors gracefully with exceptions, and save user data so it survives between program runs.

**What you'll learn:**
- How to read a file's contents, all at once or one line at a time
- How to write new content to a file or append to an existing one
- How to catch and respond to errors using `try-except` blocks
- How to fail gracefully (or silently) instead of crashing with a traceback
- How to save and reload Python data with the `json` module

### Reading from a file
To work with a file, first open it. The cleanest way is the `with` statement, which automatically closes the file when you're done—even if something goes wrong. Inside the block, call `.read()` to pull the whole file into one string.

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())  # rstrip() trims the trailing blank line
```

`open()` looks for the file in the same directory as your running program unless you give it a path. A *relative path* points to a location relative to your program (e.g. `'text_files/pi.txt'`); an *absolute path* spells out the full location from the root of your system. Windows uses backslashes (`\`) in paths instead of forward slashes (`/`).

To process a file line by line, loop over the file object. Each line keeps its trailing newline, so `rstrip()` again helps:

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```

The file object only exists inside the `with` block. To keep the lines around afterward, store them in a list using `.readlines()`:

```python
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:        # works outside the with block now
    print(line.rstrip())
```

Once the contents are in memory, you can do anything with them—build one big string, search it, count things. Remember that file text is always read as *strings*; convert with `int()` or `float()` to do math. Python has no built-in limit on file size other than your computer's memory.

### Writing to a file
Pass a mode as the second argument to `open()`: `'w'` (write), `'a'` (append), `'r'` (read, the default), or `'r+'` (read and write). Use `.write()` to send a string to the file. Be careful: `'w'` mode erases an existing file before writing. If the file doesn't exist, Python creates it.

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```

`.write()` does not add newlines for you, so include `\n` yourself or the lines run together. To add to a file without wiping it, open in append mode:

```python
with open(filename, 'a') as file_object:
    file_object.write("I also love working with data.\n")
```

Python can only write strings, so convert numbers with `str()` first.

### Handling exceptions
When something goes wrong, Python creates an *exception* object. If you don't handle it, the program halts and prints a confusing traceback. A `try-except` block lets you respond instead and keep running.

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

If the `try` code succeeds, the `except` block is skipped. If it raises the matching error, the `except` block runs and the program continues. This is especially valuable in loops that prompt for input—a bad entry can be handled without crashing.

Add an `else` block for code that should run *only* when the `try` succeeds:

```python
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)
```

A common file error is `FileNotFoundError`. Wrap the `open()` call to handle a missing file:

```python
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file " + filename + " does not exist.")
else:
    words = contents.split()   # split() breaks text into a list of words
    print("The file has about " + str(len(words)) + " words.")
```

`split()` divides a string at its spaces, giving a quick way to count words. Moving this logic into a function lets you loop over many files; a missing one is reported but the rest still get analyzed.

Sometimes you'd rather an error pass quietly. Use `pass` in the `except` block to **fail silently**:

```python
except FileNotFoundError:
    pass
```

Whether to report or stay silent is a judgment call: tell users what they need to know, but don't bury them in messages about things they weren't expecting. Errors are most likely wherever your program depends on something external—user input, a file, a network connection.

### Storing data with json
The `json` module saves Python data structures to a file and loads them back later. JSON is a portable format shared across many languages, so it's a great way to persist user data between runs. Use the `.json` extension by convention.

`json.dump()` takes the data and a file object; `json.load()` reads it back:

```python
import json

numbers = [2, 3, 5, 7, 11, 13]
with open('numbers.json', 'w') as f_obj:
    json.dump(numbers, f_obj)

with open('numbers.json') as f_obj:
    numbers = json.load(f_obj)
print(numbers)   # [2, 3, 5, 7, 11, 13]
```

Combining this with exception handling lets a program remember a user: try to load the stored value, and if the file isn't there yet, prompt for it and save it.

```python
import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you next time, " + username + "!")
else:
    print("Welcome back, " + username + "!")
```

Once code works, you can **refactor** it—break it into small functions that each do one clear job (e.g. one to fetch a stored username returning `None` if missing, one to prompt for a new one, one to greet). This makes code easier to read, maintain, and extend.

### Common pitfalls
- Forgetting to close files. Use `with`, which closes automatically even on errors; avoid manual `open()`/`close()` pairs that can leave files open if a bug skips the `close()`.
- A leftover blank line or doubled blank lines in output—`read()` and looping leave newlines; use `rstrip()`.
- Opening with `'w'` when you meant `'a'`—`'w'` erases the existing file first.
- Forgetting `\n` in `.write()` calls, so lines run together.
- Treating file data as numbers without converting with `int()`/`float()`, or writing numbers without `str()`.
- File path confusion: Python looks only in the program's directory unless you give a relative or absolute path; mind `/` vs `\` on Windows.
- Catching too broadly or using `pass` everywhere—silent failures can hide real bugs. Report errors the user needs to know about.

### Practice
- **Learning Python:** Write a few lines starting with "In Python you can..." to a text file. Then read and print the file three ways: the whole file at once, by looping over the file object, and by storing lines in a list and printing outside the `with` block.
- **Guest Book:** Use a `while` loop to repeatedly ask visitors for their name. Greet each one on screen and append a line recording their visit to `guest_book.txt`, one entry per line.
- **Addition:** Prompt for two numbers and print their sum. Catch the error that occurs if the user types text instead of a number, printing a friendly message. Then wrap it in a `while` loop so they can keep trying.
- **Favorite Number Remembered:** Use `json.dump()` to save the user's favorite number. In one combined program, report the stored number if it exists, otherwise prompt for it and save it. Run it twice to confirm.

### Key takeaways
- Use `with open(...)` for both reading and writing—it handles closing the file safely.
- Choose the right mode: `'r'` to read, `'w'` to overwrite, `'a'` to append.
- `try-except` keeps programs running through errors; add `else` for code that depends on the `try` succeeding, and `pass` to fail silently when appropriate.
- Common exceptions to know: `ZeroDivisionError`, `FileNotFoundError`.
- `json.dump()` and `json.load()` persist user data so it isn't lost between runs; refactor working code into small, single-purpose functions.

---

## Chapter 11 — Testing Your Code

> Automated tests let you prove your functions and classes behave correctly, so you can change and grow your code with confidence that you haven't broken what already worked.

**What you'll learn:**
- Why testing matters and what unit tests and test cases are
- How to write tests with Python's `unittest` module by subclassing `unittest.TestCase`
- How to read passing vs. failing test output and respond to a failure the right way
- The common assert methods (`assertEqual`, `assertTrue`, `assertIn`, and friends)
- How to test a class and use `setUp()` to avoid repetitive setup

### Why test, and what a test is
A **unit test** checks that one specific aspect of your code behaves correctly. A **test case** is a collection of unit tests that together cover the range of situations your code should handle. You don't need 100% coverage on small beginner projects—focus on the critical behaviors, and aim for fuller coverage once a project sees real use.

The big payoff: when you later modify a function, you re-run the tests instead of manually retyping inputs. If everything passes, you know your change didn't break existing behavior.

> Aside: the book uses the standard-library `unittest`. Modern Python projects very often use **pytest** instead, which lets you write plain `assert` statements with less boilerplate—worth learning once you're comfortable with the basics here.

### Testing a function
Suppose you have a function to test, in `name_function.py`:

```python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()
```

To test it, import `unittest` and the function, then create a class that inherits from `unittest.TestCase`. Each test is a method whose name **starts with `test_`** (those run automatically). Inside, call the function and use an **assert method** to compare what you got against what you expected:

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

`unittest.main()` runs the tests. A **passing test** prints a dot and ends with `OK`:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

**A failing test.** If you change the function to require a `middle` argument, the original call breaks and you get an error report (`E`) showing exactly which test failed and a traceback explaining why.

**Responding to a failure:** don't change the test to make it pass—fix the *code*. A failing test is telling you your recent change broke desired behavior. Here the fix is to make `middle` optional with a default value:

```python
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
```

**Adding new tests:** once the original test passes again, add another method (e.g. `test_first_last_middle_name`) to cover the new behavior. Use long, descriptive method names so failure output tells you exactly what broke.

### Testing a class
Testing a class is similar—you mostly test the behavior of its methods. First you need a variety of assert methods.

**A variety of assert methods** (all called as `self.<method>(...)` inside a `TestCase`):

| Method | Verifies |
| --- | --- |
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `x` is `True` |
| `assertFalse(x)` | `x` is `False` |
| `assertIn(item, list)` | `item` is in `list` |
| `assertNotIn(item, list)` | `item` is not in `list` |

**A class to test** (`survey.py`)—it collects anonymous survey answers:

```python
class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def store_response(self, new_response):
        self.responses.append(new_response)
    # ...plus show_question() and show_results()
```

**Testing the class.** Make an instance, exercise a method, then assert on the result. Here we store a response and check it landed in the list with `assertIn`:

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def test_store_single_response(self):
        my_survey = AnonymousSurvey("What language did you first learn to speak?")
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

unittest.main()
```

**The `setUp()` method.** If several test methods each rebuild the same objects, that's repetitive. `unittest.TestCase` runs a `setUp()` method (if present) *before* every `test_` method. Create your shared objects there as `self.` attributes and reuse them everywhere:

```python
class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        """Create a survey and responses for use in all test methods."""
        self.my_survey = AnonymousSurvey("What language did you first learn to speak?")
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
```

Each test method now starts from a clean, identical setup—much easier to write and maintain.

### Common pitfalls
- **Changing the test instead of the code** when a test fails. A failure usually means your latest code change broke something—fix the code.
- **Test methods that don't start with `test_`.** They won't run automatically and you'll think everything passed.
- **Tests that depend on each other or on shared mutable state.** Each test should stand alone; use `setUp()` to get a fresh starting point per test.
- **Only testing the "happy path."** Add tests for edge cases (empty input, optional arguments present/absent, multiple items) since those are where bugs hide.
- **Forgetting `self`** when calling assert methods or referencing `setUp()` attributes (`self.assertEqual`, `self.my_survey`).

### Practice
- **City, Country:** Write `get_city_country(city, country)` in `city_functions.py` that returns `"City, Country"` (e.g. `"Santiago, Chile"`). In `test_cities.py`, write `test_city_country()` using `assertEqual` and confirm it passes.
- **Population:** Add a required `population` parameter so the function returns `"City, Country – population xxx"`. Run the test, watch it fail, then make `population` optional so the original test passes again. Add a second test `test_city_country_population()` for the version with population.
- **Employee:** Write an `Employee` class whose `__init__()` stores first name, last name, and salary, plus a `give_raise()` method that adds $5000 by default but accepts a custom amount. Write a test case with `test_give_default_raise()` and `test_give_custom_raise()`, using `setUp()` to create one shared employee instance.

### Key takeaways
- A unit test checks one behavior; a test case groups related unit tests to prove a function or class works across the inputs it should handle.
- Write tests by subclassing `unittest.TestCase`; methods named `test_*` run automatically, and assert methods compare actual results to expected ones.
- When a test fails, fix the code, not the test—the failure is pointing you straight at the break.
- Use `setUp()` to build shared objects once instead of repeating setup in every test method.
- Don't chase full coverage early; do test the critical behaviors so you can refactor and extend with confidence. (And know that pytest is the popular modern alternative once you've got the fundamentals.)

---

*Adapted as original study notes from* Python Crash Course *(1st ed.) by Eric Matthes, No Starch Press. Covers Part I (Chapters 1–11) only.*

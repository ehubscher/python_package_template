# Python Coding Standards

## Table of Contents

- [Python Coding Standards](#python-coding-standards)
  - [Table of Contents](#table-of-contents)
  - [Style Guide](#style-guide)
  - [Documentation](#documentation)
    - [Packages](#packages)
    - [Modules](#modules)
    - [Classes](#classes)
    - [Functions](#functions)
  - [Testing](#testing)
  - [Packaging](#packaging)
  - [Deploying](#deploying)

## Style Guide

In order to build extensible, maintainable, readable, scalable, and testable 
software, there must be a level of consistency and purposefulness when writing your code. 
All of your code. It does not matter if it's a fifty line bash script or an 
entire client-facing, hyper multi-threaded, distributed web application. 
Writing clean code is a habit that must be maintained at all times. Period. 

That being said, it is *imperative* that you familiarize yourself with the following PEPs;

1. [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
2. [PEP 20 - The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
3. [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)

These are some absolutely fantastic talks by Raymond Hettinger, an extremely 
talented *Python core developer*. If he mentions you something about Python, 
it may be worth heeding.

1. [Beyond PEP 8 - Best practices for beautiful intelligible code](https://www.youtube.com/watch?v=wf-BqAjZb8M')
2. [Transforming Code into Beautiful, Idiomatic Python](https://www.youtube.com/watch?v=OSGv2VnC0go)
3. [The Mental Game of Python](https://www.youtube.com/watch?v=UANN2Eu6ZnM&t=1350s)

## Documentation

Document your code! Don't do it "after" or "when you have time". 
Do it *as you write*. Here are some questions that may guide you in documenting 
constructs at the very least on a basic level:

### Packages

What does it contain?
Why is it relevant?
What features does it hold?

Got that down? Good, write a package-level docstring 
(i.e. at the top of the `__init__.py` file).

### Modules

What is it supposed to do?
What functionality does it insulate?

Have that down? Good, write a module-level docstring 
(i.e. at the top of the module)

### Classes

What is the intent of this class?
What is it's purpose?
What state does it manage?

Have that down? Good, write a class-level docstring 
(i.e. at the top of the class definition).

### Functions

What is this function supposed to do?
What arguments does it have?
What are their types?
What does it return?

Have that down? Good, write a function-level docstring 
(i.e. at the top of the function definition).

1. [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
2. [Here's an example of how they write their docstrings at Google](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## Testing

Write tests for your code! Don't do it "after" or "when you have time". 
Do it *as you write*. Acquire these skills. Your code will be more robust, 
maintainable, and best of all, __*deliverable*__. You win, your manager wins, 
the client wins, and the company wins.

Here are some helpful resources to get you started writing tests for your code:

1. [Keynote - Preventing, Finding, and Fixing Bugs On a Time Budget](https://www.youtube.com/watch?v=ARKbfWk4Xyw)
2. [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
3. [Introduction to Test Driven Development (TDD)](https://www.youtube.com/watch?v=Tul3DHCAJPY&t=268s)
4. [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
5. [Intro to Python Mocks](https://www.youtube.com/watch?v=smPbDqGjFAI)
6. [Mocking Strategies in Python](https://www.youtube.com/watch?v=zW0f4ZRYF5M)

## Packaging

If you would like to develop modular libraries operating under the same namespaces, 
your *library* packages *must* be created under the `namespace_name` namespace.
Okay, great. How is this accomplished?

__HINT__: The first directory before your package name directory in your project folder, will always be named `namespace_name`;

For *library* packages, the following folder structure is being enforced;

    namespace_name_my_new_library_package
        |__ namespace_name
        |   |__ my_new_library_package
        |       |__ __init__.py
        |       |__ __main__.py
        |__ tests
        |   |__ __init__.py
        |__ setup.py
        |__ setup.cfg
        |__ README.md
        |__ .gitignore
        |__ .gitlab-ci.yml

For *application* packages, the following folder structure is being enforced;

    my_new_application_package
        |__ my_new_application_package
        |   |__ __init__.py
        |   |__ __main__.py
        |__tests
        |   |__ __init__.py
        |__ setup.py
        |__ setup.cfg
        |__ README.md
        |__ .gitignore
        |__ .gitlab-ci.yml

1. [Python Packaging from Init to Deploy](https://www.youtube.com/watch?v=4fzAMdLKC5k)
2. [Packaging Namespace Packages](https://packaging.python.org/guides/packaging-namespace-packages/)
3. [PEP 402 - Simplified Package Layout and Partitioning](https://www.python.org/dev/peps/pep-0402/)
4. [PEP 420 - Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)

## Deploying

// TODO;

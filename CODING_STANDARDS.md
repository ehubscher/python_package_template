# Python Coding Standards

## Table of Contents

1. [Style Guide](#style_guide)
2. [Documentation](#documentation)
3. [Testing](#testing)
4. [Packaging](#packaging)
5. [Deploying](#deploying)

## Style Guide <a name='style_guide'></a>

In order to build __*extensible*__, __*maintainable*__, __*readable*__, __*scalable*__, and __*testable*__ software, there must be a level of consistency and purposefulness when writing your code. __*ALL OF YOUR CODE*__. It does not matter if it's a fifty line bash script or an entire client-facing, hyper multi-threaded, distributed web application.

### Writing clean code is a habit that must be maintained at all times. __*Period*__.

That being said, it is __*imperative*__ that you familiarize yourself with the following PEPs;

1. <a href='https://www.python.org/dev/peps/pep-0008/'>PEP 8 - Style Guide for Python Code</a>
2. <a href='https://www.python.org/dev/peps/pep-0020/'>PEP 20 - The Zen of Python</a>
3. <a href='https://www.python.org/dev/peps/pep-0484/'> PEP 484 - Type Hints</a>

These are some absolutely fantastic talks by Raymond Hettinger, an extremely talented *Python core developer*. If he tells you something about Python, you listen.

Why?

__*BECAUSE HE KNOWS MORE THAN YOU WHEN IT COMES TO PYTHON !!!*__

\#kthxbye

1. <a href='https://www.youtube.com/watch?v=wf-BqAjZb8M'>Beyond PEP 8 - Best practices for beautiful intelligible code</a>
2. <a href='https://www.youtube.com/watch?v=OSGv2VnC0go'>Transforming Code into Beautiful, Idiomatic Python</a>
3. <a href='https://www.youtube.com/watch?v=UANN2Eu6ZnM&t=1350s'>The Mental Game of Python</a>

## Documentation <a name='documentation'></a>

Documentation, documentation, __*D O C U M E N T A T I O N*__.

### Document your code!

Don't do it "after" or "when you have time".

Do it __*as you write*__:

- Just created a new package? FANTASTIC! What does it contain? Why is it relevant?
  - Got that down? Good, write a package-level docstring (i.e. at the top of the `__init__.py` file). You're welcome.
- Just created a new module? GREAT! What is it supposed to do?
  - Have that down? Good, write a module-level docstring (i.e. at the top of the module). You're welcome.
- Just created a new class? WOW! Even better! What is the intent of this class? What is it's purpose?
  - Have that down? Good, write a class-level docstring (i.e. at the top of the class definition). You're welcome.
- Just wrote a new function? MY MIND IS BLOWN! What is this function supposed to do? What arguments does it have? What are their types? What does it return?
  - Have that down? Good, write a function-level docstring (i.e. at the top of the function definition). You're welcome.

1. <a href='https://www.python.org/dev/peps/pep-0257/'>PEP 257 - Docstring Conventions</a>
2. <a href='https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html'>Here's an example of how they write their docstrings at Google.</a>

## Testing <a name='testing'></a>

Tests, tests, __*T E S T S*__.

### Write tests for your code!

Don't do it "after" or "when you have time".

Do it __*as you write*__.

Acquire these skills.

Your code will be more robust, maintainable, and best of all, __*deliverable*__.

You win, your manager wins, the client wins, and the company wins.

Here are some helpful resources to get you started writing tests for your code:

1. <a href='https://www.youtube.com/watch?v=ARKbfWk4Xyw'>Keynote - Preventing, Finding, and Fixing Bugs On a Time Budget</a>
2. <a href='https://docs.python.org/3/library/unittest.html'>unittest — Unit testing framework</a>
3. <a href='https://www.youtube.com/watch?v=Tul3DHCAJPY&t=268s'>Introduction to Test Driven Development (TDD)</a>
4. <a href='https://docs.python.org/3/library/unittest.mock.html'>unittest.mock — mock object library</a>
5. <a href='https://www.youtube.com/watch?v=smPbDqGjFAI'>Intro to Python Mocks</a>
6. <a href='https://www.youtube.com/watch?v=zW0f4ZRYF5M'>Mocking Strategies in Python</a>

## Packaging <a name='packaging'></a>

If you would like to develop modular libraries operating under the same namespaces, your __*LIBRARY*__ packages __*MUST*__ be created under the `namespace_name` namespace.
Okay, great. How do I do this?

__HINT__: The first directory before your package name directory in your project folder, will always be named `namespace_name`;

Follow the [1. Packaging Namespace Packages](#packaging_namespace_packages)</a> guide below.

For __*LIBRARY*__ packages, the following folder structure is being enforced;

    namespace_name_my_new_library_package
        |__namespace_name
        |   |__my_new_library_package
        |       |____init__.py
        |       |__module_1.py
        |__tests
        |   |____init__.py
        |__setup.py
        |__setup.cfg
        |__README.md
        |__.gitignore
        |__.gitlab-ci.yml

For __*APPLICATION*__ packages, the following folder structure is being enforced;

    my_new_application_package
        |__my_new_application_package
        |   |__init__.py
        |   |__app.py
        |__tests
        |   |____init__.py
        |__setup.py
        |__setup.cfg
        |__README.md
        |__.gitignore
        |__.gitlab-ci.yml

1. <a href='https://www.youtube.com/watch?v=4fzAMdLKC5k'>Python Packaging from Init to Deploy</a>
2. <a name='packaging_namespace_packages' href='https://packaging.python.org/guides/packaging-namespace-packages/'>Packaging Namespace Packages</a>
3. <a href='https://www.python.org/dev/peps/pep-0402/'>PEP 402 - Simplified Package Layout and Partitioning</a>
4. <a href='https://www.python.org/dev/peps/pep-0420/'>PEP 420 - Implicit Namespace Packages</a>

## Deploying <a name='deploying'></a>

// TODO;

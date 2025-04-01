"""
Python Style Guide

This guide adheres to PEP 8 conventions with examples of both good and bad practices.
"""

# Naming Conventions
# Bad Example
VarName = 42  # incorrect: Variable names should be in snake_case

# Good Example
variable_name = 42  # correct: Use snake_case for variable names


# Indentation
# Bad Example
def incorrect_indentation():
    a = 1
        b = 2  # incorrect: Inconsistent indentation
    return a + b

# Good Example
def correct_indentation():
    a = 1
    b = 2  # correct: Proper indentation with 4 spaces per level
    return a + b


# Spacing
# Bad Example
x= 10+5  # incorrect: Missing spaces around operators

# Good Example
x = 10 + 5  # correct: Spaces around operators for better readability


# Line Length
# Bad Example
long_variable = "This is an example of a line that exceeds the recommended 79 characters limit."  # incorrect

# Good Example
long_variable = (
    "This is an example of a properly split long line, staying within the limits of readability."
)  # correct


# Function Definitions
# Bad Example
def improperFunction( x,y ):
    return(x+y)  # incorrect: No spaces after commas, poor parentheses spacing

# Good Example
def proper_function(x, y):
    return x + y  # correct: Proper spacing and naming


# Imports
# Bad Example
import sys, os  # incorrect: Multiple imports on a single line

# Good Example
import sys
import os  # correct: One import per line


# Docstrings
# Bad Example
def missing_docstring():
    pass  # incorrect: Function should include a docstring

# Good Example
def documented_function():
    """This function performs no operation but follows good styling practices."""
    pass  # correct
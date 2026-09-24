import pytest

def square(n):
      return n ** 2

def cube(n):
      return n**3

def fifth_power(n):
      return n**5

def test_square():
      assert square(2) == 4 , "Test failed : square of 2 should be 4"
      assert square(3) == 9 , "Test failed : square of 3 should be 9"

# How it checks: The assert statement evaluates a condition (True or False)
# square(3) runs and returns 9. 9 == 9 is True, so test_square() passes successfully.
# What happens on failure: If square(2) returned 5, 
# the condition 5 == 4 would be False. Python would immediately stop, 
# throw an AssertionError, and output "Test failed : square of 2 should be 4" in your CI logs.      


def test_cube():
      assert cube(2) == 8 , "test failed : cube of 2 should be 8 "
      assert cube(3) == 27 , "test failed : cube of 3 should be 27 "
      
def test_fifth_power():
      assert fifth_power(2) == 32 , "test failed : fifth power of 2 should be 32"
      assert fifth_power(3) == 243 , "test failed : fifth power of 3 should be 243"
      
def test_invalid_input():
      with pytest.raises(TypeError):
            square("string")
            
# What it is checking: This checks how the function handles invalid data (a string instead of a number).   
# How it checks:with pytest.raises(TypeError): tells Pytest: "The code inside this block is expected to throw a TypeError.
# If it throws a TypeError, consider this test a PASS."  
# square("string") executes "string" ** 2 in Python.   
# Python cannot square a string, so it raises a TypeError.  
# Pytest catches that TypeError, matches it with the expected error, and marks test_invalid_input as Passed.  
# (Note: If square("string") somehow succeeded without raising a TypeError, Pytest would mark this test as Failed).






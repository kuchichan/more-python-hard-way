from stacksnqueues import __version__
from stacksnqueues.stack import StackNode, Stack

def test_version():
    assert __version__ == '0.1.0'

def test_push():
    stack =  Stack()
    stack.push("Hello")
    stack.push("Hi")
    assert stack.count() == 2

def test_pop():
    stack =  Stack()
    stack.push("Hello")
    stack.push("Hi")

    result = stack.pop()
    assert result == "Hi"

    result = stack.pop()
    assert result == "Hello"

    assert stack.count() == 0 

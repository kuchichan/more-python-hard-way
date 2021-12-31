from ..stacks_queues.stack import Stack, Queue


def test_push():
    stack = Stack()
    stack.push("Hello")
    stack.push("Hi")
    assert stack.count() == 2


def test_pop():
    stack = Stack()
    stack.push("Hello")
    stack.push("Hi")

    result = stack.pop()
    assert result == "Hi"

    result = stack.pop()
    assert result == "Hello"

    assert stack.count() == 0


def test_shift():
    queue = Queue()
    queue.shift("hello")
    queue.shift("Hi")

    assert queue.count() == 2
    assert queue.pop() == "hello"
    assert queue.pop() == "Hi"
    assert queue.count() == 0
    assert queue.pop() is None

    queue.dump()

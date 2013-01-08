from messege_filter import MessageFilter

def check_foo(filter):
    assert filter.detect("hello from foo"), "should detect message with NG word."
    assert not filter.detect("hello, world!"), "should not detect message without NG word."

def test_single_argument():
    filter = MessageFilter('foo')
    check_foo(filter)

def test_multiple_argument():
    filter = MessageFilter('foo', 'bar')
    assert filter.detect('hello from bar')
    check_foo(filter)

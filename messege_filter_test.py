from messege_filter import MessageFilter

def test_message_filter():
    filter = MessageFilter('foo')
    assert filter.detect("hello from foo"), "should detect message with NG word."

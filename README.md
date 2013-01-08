#最初のテスト

```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 1 items

messege_filter_test.py F

=================================== FAILURES ===================================
_____________________________ test_message_filter ______________________________

    def test_message_filter():
>       filter = MessageFilter('foo')
E       TypeError: object.__new__() takes no parameters

messege_filter_test.py:4: TypeError
=========================== 1 failed in 0.01 seconds ===========================
```

#コンストラクタ作成
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 1 items

messege_filter_test.py F

=================================== FAILURES ===================================
_____________________________ test_message_filter ______________________________

    def test_message_filter():
        filter = MessageFilter('foo')
>       assert filter.detect("hello from foo"), "should detect message with NG word."
E       AttributeError: 'MessageFilter' object has no attribute 'detect'

messege_filter_test.py:5: AttributeError
=========================== 1 failed in 0.01 seconds ===========================
```

#detectメソッド作成
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 1 items

messege_filter_test.py F

=================================== FAILURES ===================================
_____________________________ test_message_filter ______________________________

    def test_message_filter():
        filter = MessageFilter('foo')
>       assert filter.detect("hello from foo"), "should detect message with NG word."
E       AssertionError: should detect message with NG word.

messege_filter_test.py:5: AssertionError
=========================== 1 failed in 0.01 seconds ===========================
```
#仮実装
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 1 items

messege_filter_test.py .

=========================== 1 passed in 0.01 seconds ===========================
```
#三角測量
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 1 items

messege_filter_test.py F

=================================== FAILURES ===================================
_____________________________ test_message_filter ______________________________

    def test_message_filter():
        filter = MessageFilter('foo')
        assert filter.detect("hello from foo"), "should detect message with NG word."
>       assert not filter.detect("hello, world!"), "should not detect message without NG word."
E       AssertionError: should not detect message without NG word.

messege_filter_test.py:6: AssertionError
=========================== 1 failed in 0.01 seconds ===========================
```
#明白な実装
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 1 items

messege_filter_test.py .

=========================== 1 passed in 0.01 seconds ===========================
#test関数追加
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 2 items

messege_filter_test.py .F

=================================== FAILURES ===================================
____________________________ test_multiple_argument ____________________________

    def test_multiple_argument():
>       filter = MessageFilter('foo', 'bar')
E       TypeError: __init__() takes 2 positional arguments but 3 were given

messege_filter_test.py:9: TypeError
====================== 1 failed, 1 passed in 0.01 seconds ======================

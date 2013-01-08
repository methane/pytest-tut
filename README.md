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
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 1 items

messege_filter_test.py .

=========================== 1 passed in 0.01 seconds ===========================
```
#test関数追加
```
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
```
#ベタな実装
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 2 items

messege_filter_test.py ..

=========================== 2 passed in 0.01 seconds ===========================
```
#テストを追加
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 2 items

messege_filter_test.py ..

=========================== 2 passed in 0.01 seconds ===========================
```
#第三イテレーション開始
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 2 items

messege_filter_test.py FF

=================================== FAILURES ===================================
_____________________________ test_single_argument _____________________________

    def test_single_argument():
        filter = MessageFilter('foo')
>       check_foo(filter)

messege_filter_test.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filter = <messege_filter.MessageFilter object at 0x107e09f90>

    def check_foo(filter):
        assert filter.detect("hello from foo"), "should detect message with NG word."
        assert not filter.detect("hello, world!"), "should not detect message without NG word."
>       assert filter.ng_words, "should not be empty."
E       AttributeError: 'MessageFilter' object has no attribute 'ng_words'

messege_filter_test.py:6: AttributeError
____________________________ test_multiple_argument ____________________________

    def test_multiple_argument():
        filter = MessageFilter('foo', 'bar')
        assert filter.detect('hello from bar')
>       check_foo(filter)

messege_filter_test.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filter = <messege_filter.MessageFilter object at 0x107e09e90>

    def check_foo(filter):
        assert filter.detect("hello from foo"), "should detect message with NG word."
        assert not filter.detect("hello, world!"), "should not detect message without NG word."
>       assert filter.ng_words, "should not be empty."
E       AttributeError: 'MessageFilter' object has no attribute 'ng_words'

messege_filter_test.py:6: AttributeError
=========================== 2 failed in 0.02 seconds ===========================
```
#明白な実装
```
============================= test session starts ==============================
platform darwin -- Python 3.3.0 -- pytest-2.3.4
collected 2 items

messege_filter_test.py ..

=========================== 2 passed in 0.01 seconds ===========================
```

.. |pypi| image:: https://pypip.in/v/mock_matchers/badge.png
    :target: https://crate.io/packages/mock_matchers/
.. |license| image:: https://pypip.in/license/mock_matchers/badge.png
    :target: https://pypi.python.org/pypi/mock_matchers/
.. _PyHamcrest: https://pyhamcrest.readthedocs.org/en/latest/
.. _PyHamcrest Matchers: https://pyhamcrest.readthedocs.org/en/latest/library/
.. _mock: https://docs.python.org/3/library/unittest.mock.html

*************
mock_matchers
*************
|pypi| |license|

mock.matchers simply makes `PyHamcrest`_ matchers usable with the `mock`_ assertion calls.


Examples::

    from mock import Mock 
    import mock_matchers

    m = Mock()
    m.foo(1,2,3)
    m.bar([1,2,3])

    m.foo.assert_called_with(
        mock_matchers.instance_of(int),
        mock_matchers.instance_of(int),
        3
    )
    m.foo.assert_called_with(
        [
			mock_matchers.instance_of(int),
			2,
			3
        ]
    )
    m.foo.assert_called_with(mock_matchers.instance(list))



etc... For a full list of available matchers refer to the `PyHamcrest Matchers`_
documentation and simply replace ``from hamcrest import <name_of_matcher>``
with ``from mock_matchers import <name_of_matcher>``


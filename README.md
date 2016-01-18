Phoenix Go to Spec
================

A Sublime Text 3 plug-in. From an .ex file this plug-in will open the relevant
test. If the test doesn't exist it asks if it should be created.

Only supports _test.exs files at the moment.

Installation
------------

Usage
-----
- Run from menu > Goto > Phoenix Go to Spec
- Default key binding is command + shift + y
- Or run from command palette 'Phoenix Go to Spec'

Dev
----

    git clone git@github.com:theoretick/phoenix_go_to_spec.git PhoenixGoToSpec

Testing
-------

  python resolver_test.py

Acknowledgements
-----------

Huge props to [Sporto](https://github.com/sporto) for his original work on
[Rails Go to Spec](http://github.com/sporto/rails_go_to_spec), which I
shamelessly forked and changed minor configuration

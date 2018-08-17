pyleftpad
=========

Python version of `left pad`_.

.. _left pad: https://www.npmjs.com/package/left-pad


Install
~~~~~~~

.. code-block:: bash

   $ pip install pyleftpad


Usage
~~~~~

There are two way to use pyleftpad. First of all, you can use ``leftpad()``
function from ``leftpad`` module in your Python script.

.. code-block:: python

   from leftpad import leftpad
   
   def main():
       print(leftpad('hello world', 40))
   
   
   main()

Second of all, you can use directly `leftpad` command in your shell.

.. code-block:: bash
    
   $ leftpad -l 40 "hello world"

.. toctree::
   :maxdepth: 3

   leftpad


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

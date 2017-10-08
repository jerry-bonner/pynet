#!/usr/bin/env python

from mytest import *

obj = MyClass("Jerry", "wipe", "shoes")

obj.hello()
obj.not_hello()

obj = MyChildClass("Jerry", "wipe", "shoes")

obj.hello()
obj.not_hello()

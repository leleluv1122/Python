# animal package
# dog, cat modules
# dog, cat modules can say "hi"

from animal import dog # animal 패키지에서 dog 라는 모듈을 갖고와줘
from animal import cat

from animal import *

d = dog.Dog()
d.hi()

c = cat.Cat()
c.hi()

d = Dog()
c = Cat()

d.hi()
c.hi()
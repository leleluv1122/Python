# Tuple
x = (1,2,3)
y = ('a','b','c')
z = (1,"hello","there")

print(x + y)
print('a' in y)
print(z.index(1))

# 튜플 값을 update를 하는 것이 안된다 (list와 차이점)
# mutabke (가변) vs immutable (불변) V
# x[0] = 10
def foo(*args):
  for a in args:
    print(a)

def bar(**kargs):
  for a in kargs:
    print(a, kargs[a])

foo(1,2,3)

bar(name="x", value=27)
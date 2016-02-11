from typed import typed

@typed
def foo(i: int) -> bool:
	print("inside foo:", i)
	return bool(i)

foo(True)

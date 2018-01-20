


# @aaa
# def func():
#     pass
#
# func=aaa(func)
#
# @ccc
# @bbb
# @aaa
# def func():
#     pass
#
# func=ccc(bbb(aaa(func)))

@ccc('c')
@bbb('b')
@aaa('a')
def func():
    pass

func=ccc('c')(bbb('b')(aaa('a')(func)))
#__debug__ = False

def foo(n: object) -> object:
    assert n!=0, 'n can not be zero'
    print(n)

#foo(0)

def KelvinToFahrenheit(Temperature):
    if __debug__:
        assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32

try:
    print(int(KelvinToFahrenheit(273)))
    print(int(KelvinToFahrenheit(505.78)))
    print(int(KelvinToFahrenheit(-5)))
except Exception:
    print("Has error")

def test(ex1, ex2):
    assert (ex1 and ex2), "test false"
    return True

if test(True, True):
    print("is true")
else:
    print("is false")

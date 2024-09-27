def test_function():
    def inner_function():
            print("Я в области видимости функции test function")
    return inner_function()

#@inner_function


test_function()

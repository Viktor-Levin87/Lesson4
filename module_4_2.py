def test_function(x):
    def inner_function(x):
        print('Я в области видимости test_function')
    inner_function(x)


test_function(1)
#inner_function(2) - не возможно вызвать эту функцию по причине ее создания только в момент выполнения функции test_function

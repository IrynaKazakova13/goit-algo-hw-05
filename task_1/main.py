def caching_fibonacci(): 
    #Функція, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі
    cache = {}
    #Створюємо словник 

    def fibonacci(n):
        #створюємо внутрішню функцію, яка яка безпосередньо реалізовує розрахунки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        #Спочатку перевіримо, чи вже збережено значення для n у cache. Якщо так, воно повертається негайно
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        #Якщо значення відсутнє у cache, воно обчислюється рекурсивно і зберігається у словник cache    
        
        return cache[n]
    return fibonacci
    #Функція caching_fibonacci повертає внутрішню функцію fibonacci

fib = caching_fibonacci()
#Отримуємо функцію fibonacci

# Використовуємо функцію для обчислення чисел Фібоначчі
print(fib(10)) 
print(fib(15))  
print(fib(11))
print(fib(-1))




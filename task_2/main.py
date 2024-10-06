import re
from typing import Generator, Callable



def generator_numbers(text: str) -> Generator[str, None, None]:
# The function parses the text, identifies all valid numbers (parts of income) and returns them as a generator. The function takes the string as an argument and returns the Generator.   
    pattern = r"\d+\.\d*"
    numbers = re.findall(pattern, text)
    # Using RegEx to identify all real numbers in the text

    for num in numbers:
        yield num
    # Creating the Generator

def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]):
# The function uses the generator_numbers function to sum the identified in the text numbers and calculates the total sum of the numbers (total income).    
    total_sum = 0
    # Creating a variable total_sum which calculates the total sum of the numbers (total income)
    
    for num in func(text):
        total_sum += float(num)
        # Iteration over the identified numbers, convertion them to floats, calculation of the total_sum
    return total_sum
    

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
# Application of the sum_profit function

print(f"Загальний дохід: {total_income}")
# Final output of the information
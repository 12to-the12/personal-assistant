from scripts.postprocessing import run_python

def test_run_python():
    example = """print("this is not evaluated")
```python
print(1+1,end="")
```
print("this is added at the end")"""

    example_out = """print("this is not evaluated")
```python
print(1+1,end="")
```
Result: 2
print("this is added at the end")
"""
    result = run_python(example)
    # print(f"{example_out = }")
    # print(f"{result = }")

    assert result == example_out

    example = """```python
# Define the food items and their calorie values
food_items = {
    'chai': 300,
    'cookie': 120,
    'muffin': 130,
    'eggs_benedict': 350
}

# Calculate the total calories
total_calories = sum(food_items.values())

# Print the total
print(f"Total calories for the listed food items: {total_calories}")
```"""

    example_out = """```python
# Define the food items and their calorie values
food_items = {
    'chai': 300,
    'cookie': 120,
    'muffin': 130,
    'eggs_benedict': 350
}

# Calculate the total calories
total_calories = sum(food_items.values())

# Print the total
print(f"Total calories for the listed food items: {total_calories}")
```
Result: Total calories for the listed food items: 900

"""
    result = run_python(example)
    # print(f"{example_out = }")
    # print(f"{result = }")

    assert result == example_out

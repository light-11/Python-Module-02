def garden_operations(num: int) -> None:
    if num == 0:
        int("abc")
    if num == 1:
        10 / 0
    if num == 2:
        open("/non/existent/file")
    if num == 3:
        "abc" + 10


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i < 5:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e0:
            print(f"Caught ValueError: {e0}")
        except ZeroDivisionError as e1:
            print(f"Caught ZeroDivisionError: {e1}")
        except FileNotFoundError as e2:
            print(f"Caught FileNotFoundError: {e2}")
        except TypeError as e3:
            print(f"Caught TypeError: {e3}")
        i += 1
    print()
    print("All error types tested successfully!")


test_error_types()

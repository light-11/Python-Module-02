def input_temperature(temp_str: str) -> int:
    int_str = int(temp_str)
    if int_str > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    elif int_str < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    else:
        return int_str


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    print("Input data is '25'")
    str_value = "25"
    try:
        value = input_temperature(str_value)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is 'abc'")
    str_value = "abc"
    try:
        value = input_temperature(str_value)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is '100'")
    str_value = "100"
    try:
        value = input_temperature(str_value)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is '-50'")
    str_value = "-50"
    try:
        value = input_temperature(str_value)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


test_temperature()

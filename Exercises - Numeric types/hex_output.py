import re


def hex_output():
    """
    Convert a valid hexadecimal input to its decimal equivalent.

    Continuously prompts the user for a hexadecimal number,
    validates the input, and converts it to a decimal value.
    Handles both prefixed ('0x') and non-prefixed inputs.
    """
    while True:
        hex_input = input(
            "Enter hex number that consists from 0-9 and letter (A-F or a-f: )"
            ).strip()

        try:
            if not hex_input:
                print("Input cannot be empty. "
                      "Please enter a valid hexadecimal number."
                      )
                continue

            if re.match(r"^0x[0-9a-fA-F]+$|^[0-9a-fA-F]+$", hex_input):
                hex_input = hex_input[2:] if hex_input.startswith('0x') else hex_input
                print(int(hex_input, 16))
                break

            else:
                print("Invalid Input!")

        except ValueError:
            print("Wrong Value!")


hex_output()

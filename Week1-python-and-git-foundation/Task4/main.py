from modules.factorial import factorial
from modules.string_reverse import reverse_string

def main():
    number = 5
    text = "hello world"

    fact = factorial(number)
    reversed_text = reverse_string(text)

    print(f"The factorial of {number} is {fact}")
    print(f"The reversed string of '{text}' is '{reversed_text}'")

if __name__ == "__main__":
    main()

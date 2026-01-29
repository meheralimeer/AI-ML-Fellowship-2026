def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    print("Reversed string is: " + reverse_string(string))
def reverse_string(input_string):
    return input_string[::-1]


if __name__ == "__main__":
    my_input = str(input("Provide your input: "))
    resulted_string = reverse_string(my_input)
    print("Your reverse string is: {}".format(resulted_string))
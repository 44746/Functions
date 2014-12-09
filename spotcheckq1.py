#09-12-2014
#spot check q1
def set_up():
    password = ""
    return password

def length(password):
    pw_length = len(password)
    return pw_length

def validation(pw_length):
    password = "a"
    while pw_length < 8 or pw_length >16:
        password = input("Please enter your password: ")
        pw_length = length(password)
        if pw_length<8:
            print("Too short")
        elif pw_length >16:
            print("Too long")
            
    print("Password Accepted")

def main():
    password = set_up()
    pw_length = length(password)
    validation(pw_length)

main()

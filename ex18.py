

# this one is like your scripts with argv

def print_two(*argv):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")



def print_two_again(arg1, arg2):
    pring(f"arg1: {arg1}, arg2: {arg2}")



def print_one(arg1):
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

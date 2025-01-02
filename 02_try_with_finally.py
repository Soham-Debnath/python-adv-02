

try:
    a=int(input("a= "))
    # b=int(input("b= "))
    print(a)
except Exception as e:
    print(e)
finally:
    print("thank you")  # works in both case

print("End of the program")  # this also works in both case
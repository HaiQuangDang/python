def main():
    print(f"Hello script1 __name__ is {__name__}")


def hello():
    print("Hello from script1")


# using main only on this function, not run automatically on other function
if __name__ == "__main__":
    print("from acutal script 1")
    main()

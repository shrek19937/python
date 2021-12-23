#do this
#use f-string formatting
def found_err():
    raise Exception("this is an exception")

if __name__ == "__main__":
    v = "do this not that!"
    print(f"{v}")

    with open("what_not_to_do.py") as f:
        print(f.name)
        f.close()

    #handle exception
    try:
        found_err()
    except Exception:
        print("error found")

    d = { "a": 1, "b": 2, "c": 3}
    for key, val in d.items():
        print(key, val)
    
    
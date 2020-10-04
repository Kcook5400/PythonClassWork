


def score_input(prompt, retries =2, reminder='please try again'):
    while True:
        ok = input(prompt)
        if ok in("test"):
            return True
        if retries <0:
            raise ValueError("sorry, bad input")
        print("reminder")
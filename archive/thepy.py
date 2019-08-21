def ask_ok(prompt, retries=4, reminder='Please try again!'):
    ok = input(prompt)
    if ok in ('y', 'ye', 'yes'):
        return True
    elif ok in ('n', 'no', 'nop', 'nope'):
        return False
    retries = retries - 1
    if retries < 0:
        raise ValueError('invalid user response')
    print(reminder)


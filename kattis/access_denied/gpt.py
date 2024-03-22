# 3.8 run-time error 0/92

import sys
import time

def check_password(pwd1, pwd2):
    if len(pwd1) != len(pwd2):
        return False
    for i in range(len(pwd1)):
        if pwd1[i] != pwd2[i]:
            return False
    return True

password_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

for length in range(1, 21):
    for password in itertools.product(password_chars, repeat=length):
        password = ''.join(password)
        sys.stdout.write(password + '\n')
        sys.stdout.flush()
        start_time = time.time()
        response = input().strip()
        elapsed_time = (time.time() - start_time) * 1000
        if response == 'ACCESS GRANTED':
            sys.exit(0)
        else:
            print(f'{response} ({int(elapsed_time)} ms)', file=sys.stderr)

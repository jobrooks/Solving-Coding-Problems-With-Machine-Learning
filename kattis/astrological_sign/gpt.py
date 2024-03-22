# 2.3 wrong answer 0/15

# mapping of the start and end dates for each astrological sign
signs = {
    'aquarius': [('0120', '0218'), ('0121', '0219')],
    'pisces': [('0219', '0320'), ('0220', '0321')],
    'aries': [('0321', '0420'), ('0322', '0421')],
    'taurus': [('0421', '0521'), ('0422', '0522')],
    'gemini': [('0522', '0621'), ('0523', '0622')],
    'cancer': [('0622', '0723'), ('0623', '0722')],
    'leo': [('0723', '0823'), ('0724', '0822')],
    'virgo': [('0823', '0923'), ('0824', '0922')],
    'libra': [('0923', '1023'), ('0924', '1022')],
    'scorpio': [('1023', '1122'), ('1024', '1121')],
    'sagittarius': [('1122', '1222'), ('1123', '1221')],
    'capricorn': [('1222', '1231'), ('0101', '0119')]
}

while True:
    try:
        month, day = input().split()
    except:
        break

    date = month.zfill(2) + day.zfill(2)

    # iterate over each astrological sign
    for sign in signs:
        for start, end in signs[sign]:
            if start <= date <= end:
                print(sign)
                break
        else:
            continue
        break

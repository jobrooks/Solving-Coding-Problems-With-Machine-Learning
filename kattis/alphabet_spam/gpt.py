# 1.4 accepted 18/18

def spam_detection(email):
    whitespace_count = 0
    lowercase_count = 0
    uppercase_count = 0
    symbol_count = 0
    
    for char in email:
        if char == '_':
            whitespace_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            symbol_count += 1
    
    total_count = len(email)
    
    whitespace_ratio = whitespace_count / total_count
    lowercase_ratio = lowercase_count / total_count
    uppercase_ratio = uppercase_count / total_count
    symbol_ratio = symbol_count / total_count
    
    return (whitespace_ratio, lowercase_ratio, uppercase_ratio, symbol_ratio)

email = input()
spam_ratios = spam_detection(email)
for ratio in spam_ratios:
    print("%.6f" % ratio)
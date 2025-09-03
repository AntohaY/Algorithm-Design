def backspace(s):
    temp_stack = []
    for i in range(len(s)):
        if s[i] != '<':
            temp_stack.append(s[i])
        else:
            temp_stack.pop()

    print(''.join(temp_stack))
    
word = input().strip()

backspace(word)
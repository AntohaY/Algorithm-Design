word = input().strip()

echo_chamber = []
if word:
    for i in range(3):
        echo_chamber.append(word)
        
print(' '.join(echo_chamber))

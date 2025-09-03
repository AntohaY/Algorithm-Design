n, t = map(int, input().split())

a = list(map(int, input().split()))

def median_of_three(x, y, z):
    return sorted([x, y, z])[1]

def funny(n, t, a):
    match t:
        case 1:
            print(7)
        case 2:
            if a[0] > a[1]:
                print('Bigger')
            elif a[0] == a[1]:
                print('Equal')
            else:
                print('Smaller')
        case 3:
            a.sort()
            if n < 3:
                print("Array too small")
            else:
                m = median_of_three(a[0], a[1], a[2])
                print(m)
        case 4:
            print(sum(a))
        case 5:
            print(sum(x for x in a if x % 2 == 0))
        case 6:
            mapped = ''.join(chr((x % 26) + ord('a')) for x in a)
            print(mapped)
        case 7:
            visited = set()
            idx = 0
            while True:
                match idx:
                    case x if x < 0 or x >= n:
                        print("Out")
                        break
                    case x if x == n - 1:
                        print("Done")
                        break
                    case _:
                        if idx in visited:
                            print("Cyclic")
                            break
                        visited.add(idx)
                        idx = a[idx]

funny(n, t, a)
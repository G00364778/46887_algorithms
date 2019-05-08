def mystery(n):
    print(n)
    if n < 4:
        mystery(n+1)
    print(n)

if __name__ == '__main__':
    mystery(1)
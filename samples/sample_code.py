def simple():
    print("Helloo")

def medium(x):
    if x > 10:
        print("Lớn")
    else:
        print("Nhỏ")

def complex(x):
    if x > 10:
        for i in range(5):
            if i % 2 == 0:
                print(i)
    else:
        while x < 10:
            x += 1





def look_and_say(num):
    prev = None
    r = ""
    count = 0
    for ch in num:
        if prev != None and ch != prev:
            r += str(count) + prev
            count = 0
        count += 1
        prev = ch
    r += str(count) + prev
    return r


def main():
    cur = "1"
    for i in range(30):
        cur = look_and_say(cur)
    print(len(cur))
  
if __name__ == "__main__":
    main()

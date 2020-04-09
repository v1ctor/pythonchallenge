
import pickle

f = open("banner.p", "rb")
payload = pickle.load(f)


for row in payload:
    for block in row:
        print(block[0] * block[1], end="")
    print()


f.close()



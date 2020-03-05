import zipfile
import re


def main():
    f = zipfile.ZipFile("channel.zip")
    ans = "90052"
    comments = []
    while ans is not None:
        content = f.read(ans + ".txt").decode("utf-8")
        comments.append(f.getinfo(ans + ".txt").comment.decode("utf-8"))
        print(content)
        r = re.match(".*[nN]ext nothing is ([0-9]+)", content)

        if r is None:
            break

        ans = r.group(1)
    print("".join(comments))

if __name__ == "__main__":
    main()

import os

ROOT = r"C:\1py\3-soft-videoplayer"

found = 0

for current, dirs, files in os.walk(ROOT):
    for filename in files:
        if "audioplayer" in filename.lower() and filename.lower().endswith(".py"):
            path = os.path.join(current, filename)
            print(path)
            found += 1

print(f"\nFound: {found}")
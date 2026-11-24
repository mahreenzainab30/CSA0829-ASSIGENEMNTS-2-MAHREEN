
import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200000)]

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return ";".join(parts) + ";"

start = time.perf_counter()
text1 = build_plus(items)
time1 = time.perf_counter() - start

start = time.perf_counter()
text2 = build_join(items)
time2 = time.perf_counter() - start

print("Same text:", text1 == text2)
print("Length:", len(text1))
print("Plus time:", time1)
print("Join time:", time2)

def all_variants(text):
    for y in range(1, len(text) + 1):
        for x in range(0, len(text)-y+1):
            yield text[x:x+y]

a = all_variants("abc")
for i in a:
    print(i)
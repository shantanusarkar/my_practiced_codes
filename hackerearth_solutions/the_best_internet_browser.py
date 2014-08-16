tc = int(raw_input())
for x in range(0, tc):
    name = raw_input()
    original_size = len(name)
    new = name.split(".")
    website_name = new[1]
    website_name = list(website_name)
    new_website = []
    for y in website_name:
        if y != "a" and y != "e" and y != "i" and y != "o" and y != "u":
            new_website.append(y)
    new_website = ''.join(new_website)
    website_name = new_website + "." + new[2]
    new_size = len(website_name)
    print '%d/%d' % (new_size, original_size)
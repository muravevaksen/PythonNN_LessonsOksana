def find_needle(haystack):
    for i in range(0, len(haystack)):
        if haystack[i] == 'needle':
            return f"found the needle at position {i}"


print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
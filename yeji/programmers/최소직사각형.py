def solution(sizes):
    biggest = 0
    smallest = 0
    for w, h in sizes:
        biggest = max(max(w, h), biggest)
        smallest = max(min(w, h), smallest)
    return biggest * smallest
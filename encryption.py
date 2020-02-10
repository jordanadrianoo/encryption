#encryption code
# Jordan Adriano
# jan 9 2020
# This code will simply take a long string and swap each letter with their associated encryption

original=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"," "]

rot_01 = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
rot_02 = ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
rot_03 = ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
rot_15 = ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]

for x in (range(11)):
    print(original[x])

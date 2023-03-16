words = input("\n-----------\nHey, welcome to Is Palindrome?\nEnter some words: [-1 to exit]: ")

while words != "-1":
    words_list = words.split()

    for word in words_list:
        reversed_word = word[::-1]
        if(word == reversed_word):
            print("\n", word, "is palindrome!")
        else:
            print("\n", word, "is not palindrome :(")
    
    words = input("\nEnter more words: [-1 to exit]: ")

print("\nThanks, come back later!")
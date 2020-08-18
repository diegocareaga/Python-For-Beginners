def run():
    sentences = input('Type a sentences: ').replace(' ','').lower()
    palindrome = lambda x : True if x == x[::-1] else False
    print('Is palindrome' if palindrome(sentences) else 'Is not palindrome')   


if __name__ == '__main__':
    run()
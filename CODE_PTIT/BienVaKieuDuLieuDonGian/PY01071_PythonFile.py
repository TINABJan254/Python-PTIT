if __name__ == '__main__':
    n = input()
    if n[-3::].lower() == '.py':
        print('yes')
    else:
        print('no')
def rememberer(thing):
    # open file
    # 'WITH' keyword - instead of file.close
    with open('E:\\code\\test\\database.txt', 'a') as file:
        # write thing to file
        file.write(thing + '\n')
        # close file
        file.close()


if __name__ == '__main__':
    rememberer(input("What should I remember? "))
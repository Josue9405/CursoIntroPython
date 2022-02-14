def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No puedo encontrar el archivo config.txt")


if __name__ == '__main__':
    main()
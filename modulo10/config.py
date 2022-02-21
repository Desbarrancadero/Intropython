def main():
    try:
        configuration = open('config.py')
    except FileNotFoundError:
        print( 'No se pudo encontrrar el archivo config.txt')

if __name__ == '__main__':
    main()

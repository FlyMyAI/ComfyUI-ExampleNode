import pathlib

if __name__ == '__main__':
    print(
        "IF YOU SEE ME - INSTALLATION COMPLETED SUCCESSFULLY "
        "TO ACCESS NODE FILES USE __file__ ATTRIBUTE OF install MODULE "
        f"FOR EXAMPLE: {(pathlib.Path(__file__).parent / 'assets' / 'example.jpg')=}"
    )

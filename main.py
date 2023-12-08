from Logic import *


def main() -> None:
    """
    starts up the gui.
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()



from controller.campus_controller import CampusController


def main():
    controlador = CampusController()
    controlador.ejecutar()
    controlador.menu_interactivo()


if __name__ == "__main__":
    main()
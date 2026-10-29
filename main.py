

from controller.campus_controller import CampusController


def main():
    controlador = CampusController()

    # Ejecutar casos de uso iniciales
    controlador.ejecutar()

    # Iniciar menu interactivo
    controlador.menu_interactivo()


if __name__ == "__main__":
    main()

from db.database import create_tables
from repository.sessao_repository import SessaoRepository
from service.cinema_service import CinemaService
from controller.cinema_controller import CinemaController
from view.terminal_view import TerminalView

def main():
    # Inicializa o banco
    create_tables()

    # Injeção de Dependências (Bootstrap)
    repo = SessaoRepository()
    service = CinemaService(repo)
    controller = CinemaController(service)
    view = TerminalView(controller)

    # Inicia a aplicação
    while True:
        view.exibir_menu()
        if input("\nDeseja continuar? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()
    
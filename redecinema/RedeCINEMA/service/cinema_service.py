class CinemaService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_publico(self, sessao_id, quantidade):
        sessao = self.repository.buscar_por_id(sessao_id)
        if not sessao:
            raise ValueError("Sessão não encontrada.")

        # RN04: Limite de Ocupação
        if sessao.publico_atual + quantidade > sessao.capacidade:
            raise ValueError(f"Capacidade excedida! Limite: {sessao.capacidade}")

        novo_total = sessao.publico_atual + quantidade
        self.repository.atualizar_publico(sessao_id, novo_total)
        return novo_total 
class CinemaController:
    def __init__(self, service):
        self.service = service

    def vender_ingresso(self, sessao_id, qtd):
        try:
            total = self.service.registrar_publico(sessao_id, qtd)
            return {"status": "sucesso", "total": total}
        except ValueError as e:
            return {"status": "erro", "mensagem": str(e)}
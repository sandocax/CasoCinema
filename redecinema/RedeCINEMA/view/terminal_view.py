class TerminalView:
    def __init__(self, controller):
        self.controller = controller

    def exibir_menu(self):
        print("\n--- REGISTRO DE PÚBLICO ---")
        sessao_id = int(input("ID da Sessão: "))
        qtd = int(input("Quantidade de Ingressos: "))
        
        resultado = self.controller.vender_ingresso(sessao_id, qtd)
        
        if resultado["status"] == "sucesso":
            print(f"✅ Sucesso! Novo público total: {resultado['total']}")
        else:
            print(f"❌ Erro: {resultado['mensagem']}")
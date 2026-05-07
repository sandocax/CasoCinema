from db.database import get_connection
from model.sessao import Sessao

class SessaoRepository:
    def buscar_por_id(self, sessao_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sessoes WHERE id = ?", (sessao_id,))
            row = cursor.fetchone()
            if row:
                return Sessao(row[0], row[1], row[2], row[3])
            return None

    def atualizar_publico(self, sessao_id, novo_total):
        with get_connection() as conn:
            conn.execute("UPDATE sessoes SET publico_atual = ? WHERE id = ?", (novo_total, sessao_id))
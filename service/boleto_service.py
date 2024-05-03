from repository.boleto_repository import BoletoRepository
from util.log_util import log


class BoletoService(object):

    def __int__(self):
        self.boleto_repository = BoletoRepository()

    def get_boleto(self, id_boleto: int = None) -> tuple:
        try:
            return self.boleto_repository.get_boleto(id_boleto), 200
        except Exception as e:
            log.error(str(e), e)
            return {"status": 500, "message": "Erro ao recuperar boleto"}, 500

from flask import Blueprint, request

from service.boleto_service import BoletoService

bp = Blueprint("boleto", __name__)


class BoletoController(object):

    @staticmethod
    @bp.route("", methods=["GET"])
    def get_boleto():
        return BoletoService().get_boleto(request.args.get("idBoleto", type=int))

import json
import time


def create_routes(blueprint, request, utils, models):
    api = blueprint('api', __name__)

    @api.route('/', methods=['GET'])
    def index():
        return 'rélou!', 200


    @api.route('/api/sorveterias', methods=['GET', 'POST'])
    def sorveterias_list_create():
        if request.method == 'GET':
            return utils.get_sorveterias(models.Sorveteria)
        if request.method == 'POST':
            return utils.create_sorveteria(models.Sorveteria, request.get_json())


    @api.route('/api/sorveterias/<string:id>', methods=['GET', 'PATCH', 'DELETE'])
    def sorveterias_details(id):
        if request.method == 'GET':
            return utils.get_sorveteria(models.Sorveteria, id)
        if request.method == 'DELETE':
            return utils.delete_sorveteria(models.Sorveteria, id)
        if request.method == 'PATCH':
            return utils.update_sorveteria(models.Sorveteria, id, request.get_json())


    @api.route('/api/sorveterias/<string:id>/sorvetes', methods=['GET', 'POST'])
    def sorvetes_list_create(id):
        if request.method == 'GET':
            return utils.get_sorvetes(models.Sorveteria, id)
        if request.method == 'POST':
            return utils.create_sorvete(models.Sorveteria, models.Sorvete,
                                        id, request.get_json(), int(time.time()))


    @api.route('/api/sorveterias/<string:id>/sorvetes/<string:s_id>',
               methods=['GET','PATCH', 'DELETE'])
    def sorvetes_details(id, s_id):
        if request.method == 'GET':
            return utils.get_sorvete(models.Sorveteria, id, s_id)
        if request.method == 'DELETE':
            return utils.delete_sorvete(models.Sorveteria, id, s_id)
        if request.method == 'PATCH':
            return utils.update_sorvete(models.Sorveteria, id, s_id, request.get_json())

    return api

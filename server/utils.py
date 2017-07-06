import json


def get_sorveterias(sorveteria_model):
    try:
        return transform_output(sorveteria_model.objects.to_json()), 200
    except:
        return 'Unable to retrieve data from sorveterias', 404


def get_sorveteria(sorveteria_model, id):
    try:
        sorveteria = sorveteria_model.objects.get(id=id)
        return transform_output(sorveteria.to_json()), 200
    except:
        return 'Unable to retrieve {}.'.format(id), 404


def create_sorveteria(sorveteria_model, data):
    try:
        new = {
            'name': '',
            'slogan': '',
            'sorvetes': []
        }

        for k in list(new.keys()):
            if k in data:
                new[k] = data[k]

        sorveteria = sorveteria_model(**new)
        sorveteria.save()
        return 'You created your new Sorveteria!! Yay!', 201
    except:
        return 'Error on creating new Sorveteria. =/', 400


def delete_sorveteria(sorveteria_model, id):
    try:
        sorveteria = sorveteria_model.objects.get(id=id)
        sorveteria.delete()
        return 'You deleted your Sorveteria! No more ice-cream for you.'
    except:
        return 'Error on deleting your Sorveteria.', 400


def update_sorveteria(sorveteria_model, id, data):
    try:
        sorveteria = sorveteria_model.objects.get(id=id)
        if 'name' in data:
            sorveteria.update(name=data['name'])
        if 'slogan' in data:
            sorveteria.update(slogan=data['slogan'])
        if 'sorvetes' in data:
            sorveteria.update(sorvetes=data['sorvetes'])
        sorveteria.save()
        return 'You updated your sorveteria info.', 200
    except:
        return 'Error on updating your Sorveteria.', 400


def get_sorvetes(sorveteria_model, id):
    try:
        sorveteria = sorveteria_model.objects.get(id=id)
        sorvetes = [dict(s.to_mongo()) for s in sorveteria.sorvetes]
        return json.dumps({'sorvetes': sorvetes})
    except:
        return 'Unable to retrieve sorvetes from {}'.format(id), 404


def get_sorvete(sorveteria_model, id, s_id):
    try:
        sorveteria = sorveteria_model.objects.get(id=id)
        return transform_output(sorveteria.sorvetes.get(s_id=s_id).to_json()), 200
    except:
        return 'Unable to retrieve sorvete {}'.format(s_id), 404


def create_sorvete(sorveteria_model, sorvete_model, id, data, time):
    try:
        new = {
            'name': '',
            'description': '',
            'price': 0.0
        }

        for k in list(new.keys()):
            if k in data:
                new[k] = data[k]
        sorvete = sorvete_model(**new, s_id=time)
        sorveteria = sorveteria_model.objects.get(id=id)
        sorveteria.sorvetes.append(sorvete)
        sorveteria.save()
        return 'Yum! A new sorvete was added!', 201
    except:
        return 'Unable to create a new sorvete. =/', 201


def delete_sorvete(sorveteria_model, id, s_id):
    try:
        sorveteria = sorveteria_model.objects.get(id=id)
        sorveteria.sorvetes.filter(s_id=s_id).delete()
        sorveteria.save()
        return 'You deleted a sorvete. Sad. Think about the little children.', 200
    except:
        return 'Error on deleting your Sorvete.', 400


def update_sorvete(sorveteria_model, id, s_id, data):
    try:
        sorveteria = sorveteria_model.objects.get(id=id)
        sorvete = sorveteria.sorvetes.get(s_id=s_id)

        if 'price' in data:
            sorvete.price = data['price']
        sorveteria.save()
        return 'You changed the price of your sorvete. I hope it is not too expensive...', 200
    except:
        return 'Error on updating your Sorvete.', 400


def transform_output(s):
    return json.dumps(json.loads(s))

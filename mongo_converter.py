import os
from translator import mongoid_mongoengine
import pickle


def clean_code(code):
    """
    strips lines from code and returns non commented ones
    """
    return [line.strip() for line in code if len(line.strip()) != 0 and line.strip().find('#') != 0]


def starts_at(model, model_name):
    """
    returns index of model creation line
    """
    try:
        return [idx for idx, line in enumerate(model) if f"class {model_name}" in line][0]
    except IndexError:
        return 0


def unsymbolize(string):
    return string.find(':')


def retrieve_fields(model, translator):
    fields = []
    raw_fields = [line for line in model if 'field' in line]
    for raw_field in raw_fields:
        definitions = raw_field.split(',')
        field = {}
        for define in definitions:
            type = define[:unsymbolize(define)].strip()
            value = define[unsymbolize(define)+1:].strip()
            if type in ['field', 'type', 'default']:
                field[type] = translator(value)
        if len(field) > 0 and 'type' in field.keys():  # Type required validation
            fields.append(field)
    return fields


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.capitalize() for x in components)


def get_fields_from(directory='models', to='fields.pkl', translator: mongoid_mongoengine):
    great_fields = {}
    for file in os.listdir(directory):
        model_name = to_camel_case(file.split('.')[0])
        try:
            with open(f'{directory}/{file}', 'r') as model:
                model = model.readlines()
        except IsADirectoryError:
            pass
        model = clean_code(model)
        model = model[starts_at(model, model_name):]
        fields = retrieve_fields(model, translator)
        if len(fields) > 0:
            great_fields[model_name] = fields
    pickle.dump(great_fields, open(to, 'wb'))



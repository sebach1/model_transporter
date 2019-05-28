import pickle


def import_fields(model_name, fields_dir='fields.pkl'):
    fields = pickle.load(open(fields_dir, 'rb'))[model_name]
    var_fields = {}
    for field in fields:
        if 'field' in field.keys() and 'type' in field.keys():
            if field.get('default'):
                field_type = field['type'] + f"(default={field['default']})"
            else:
                field_type = field['type']+'()'
            var_fields[field['field']] = field_type
        else:
            continue
    return var_fields


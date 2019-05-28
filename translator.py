def mongoid_mongoengine(ruby_type):
    if ruby_type == 'Array':
        return "ListField"
    elif ruby_type == 'Hash':
        return "DictField"
    elif ruby_type == 'String':
        return "StringField"
    elif ruby_type == 'Boolean':
        return "BooleanField"
    elif ruby_type == 'Integer':
        return "IntField"
    elif ruby_type == 'Float':
        return "FloatField"
    elif ruby_type == 'BSON::ObjectId':
        return "ObjectIdField"
    elif ruby_type == 'DateTime' or ruby_type == 'Time':
        return "DateTimeField"
    elif ruby_type == 'false':
        return False
    elif ruby_type == 'true':
        return True
    else:
        return ruby_type


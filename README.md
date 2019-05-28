# MODEL TRANSPORT
Easily transport all your mongo models from Ruby to Python and viceversa.

After installation, simply:

```
from mongo_converter import get_fields_from

get_fields_from(directory=INPUT_MODELS_FOLDER, to=OUTPUT_INTERMEDIATE_PICKLE)
```

then, on your model initialization (example with mongoengine):

```
from importer import import_fields
from mongoengine import Document
from mongoengine.fields import *
...

class Foo(Document):
    import_fields('Foo')
```

And now you've all your model info from ruby to python.

If wanna create another translation (for example: from Mongoid to pymongo), just add a function on translator.py named `{from}_{to}` and pass it through `get_fields_from(... translator=TRANSLATOR)`

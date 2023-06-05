import marshal
import json



def deserialize_data(serialized_data):
    data = json.loads(serialized_data)

    return data



# code = """
# def add(a, b):
#     return a + b
# """

# compiled_code = compile(code, '<string>', 'exec')
# code = marshal.dumps(compiled_code)
# print(code)

deserialized_data = deserialize_data('{"name": "John", "age": 20}')
print(deserialized_data)



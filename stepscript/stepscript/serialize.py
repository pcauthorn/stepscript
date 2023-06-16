import base64
import pickle
from stepscript.data import Test, TestDataClass


def serialize(obj):
    return base64.b64encode(pickle.dumps(obj))


def unserialize(str_data: bytes):
    return pickle.loads(base64.b64decode(str_data))


def main():
    r = serialize(Test('yo', 'sup', 1))
    print(unserialize(r))
    r = serialize(TestDataClass('String data', 42, {'a': 'b'}))
    print(unserialize(r))
    # You can base64



if __name__ == '__main__':
    main()

def decorator(cls):
    print("6666666")
    return cls


@decorator
class Model(object):
    def __init__(self):
        print("model created")


if __name__ == '__main__':
    model = Model()
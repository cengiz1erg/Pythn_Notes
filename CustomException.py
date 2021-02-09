class ValueIsTooSmallError(ValueError):
    pass


def inputfonk(name):
    if len(name) < 6:
        raise ValueIsTooSmallError(name)
    print("busdfasd bakjfdjg")


inputfonk("skdj")

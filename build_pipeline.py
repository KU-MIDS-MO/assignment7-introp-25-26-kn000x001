def build_pipeline(operation_names):
    ### Replace with your own code (begin) ###
    operations = {
        "add_one": lambda x: x + 1,
        "square": lambda x: x * x,
        "double": lambda x: x * 2,
        "negate": lambda x: -x,
        "triple": lambda x: x * 3,
    }

    pipeline = []

    for name in operation_names:
        try:
            pipeline.append(operations[name])
        except KeyError:
            raise KeyError(name)

    def apply_pipeline(value):
        result = value
        for operation in pipeline:
            result = operation(result)
        return result

    return apply_pipeline
    pass
    ### Replace with your own code (end)   ###

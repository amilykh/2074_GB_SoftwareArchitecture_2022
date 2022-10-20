from ModelFactory import ModelFactory


def model_client():
    model_factory = ModelFactory()
    model_name = input("Enter the name of the model: ")

    model = model_factory.create_model(model_name)

    print(f"The type of model created: {type(model)}")


if __name__ == '__main__':
    model_client()

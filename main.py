def get_data(path):
    pass

def preprocess_data(data):
    pass

def train(data):
    pass

def main():
    path = ''
    data = get_data(path)
    data = preprocess_data(data)
    model = train(data)
    test_data = get_data(path)
    output = model.predict(test_data)
    print(output)

if __name__=="__main__":
    main()
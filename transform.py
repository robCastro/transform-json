import json

def transform() -> None:
    with open('input.json') as input_file:
        data = json.load(input_file)
    print('===================== ANTES =====================')
    print(data)
    data['properties'] = {
        'messageId': data['messageId'],
        'originalTimestamp': data['originalTimestamp'],
    }
    # Remover los originales
    data.pop('messageId')
    data.pop('originalTimestamp')
    print('===================== DESPUES =====================')
    print(data)
    with open('output.json', 'w') as output_file:
        json.dump(data, output_file, indent=4)


if __name__ == "__main__":
    transform()

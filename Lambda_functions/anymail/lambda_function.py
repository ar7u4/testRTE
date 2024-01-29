import json

def lambda_handler(event, context):
    # Load the data from the provided example
    data = {
        "items": [
            {"id": 1, "name": "Item 1", "price": 10.99},
            {"id": 2, "name": "Item 2", "price": 15.99},
            {"id": 3, "name": "Item 3", "price": 20.99},
        ]
    }

    # Calculate total price of all items
    total_price = sum(item['price'] for item in data['items'])

    return {
        'statusCode': 200,
        'body': json.dumps({'items': data['items'], 'total_price': total_price})
    }
import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        item_id = body.get('id')
        name = body.get('name')
        price = body.get('price')

        # Validate and calculate additional fields
        if price is None or price <= 0:
            raise ValueError("Invalid price")
        tax = price * 0.07  # Calculate 7% tax
        total_price = price + tax

        # Simulate creating an item (replace with actual logic)
        print(f"Creating item with ID: {item_id}, Name: {name}, Price: {price}, Tax: {tax}, Total Price: {total_price}")

        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Item created successfully'})
        }
    except Exception as e:
        print(f"Error creating item: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Error creating item: Invalid input'})
        }

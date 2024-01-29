import json

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']

        # Simulate finding the item (replace with actual logic)
        for item in data['items']:
            if item['id'] == item_id:
                # Validate deletion criteria (replace with your logic)
                if item['quantity'] > 0:
                    raise ValueError("Cannot delete item with remaining quantity")
                data['items'].remove(item)
                print(f"Deleted item with ID: {item_id}")
                return {
                    'statusCode': 200,
                    'body': json.dumps({'message': 'Item deleted successfully'})
                }

        # Item not found
        raise ValueError(f"Item with ID: {item_id} not found")

    except Exception as e:
        print(f"Error deleting item: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f"Error deleting item: {e}"})
        }


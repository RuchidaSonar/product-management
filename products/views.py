from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import snowflake.connector
from config.snowflake_config import SNOWFLAKE_CONFIG

class ProductView(APIView):
    def get(self, request):
        try:
            conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
            cursor = conn.cursor()
            cursor.execute("SELECT product_id, product_name, price, quantity FROM products")
            products = [
                {
                    'product_id': row[0],
                    'product_name': row[1],
                    'price': float(row[2]),
                    'quantity': row[3]
                }
                for row in cursor.fetchall()
            ]
            cursor.close()
            conn.close()
            return Response(products, status=status.HTTP_200_OK)
        except snowflake.connector.errors.OperationalError as e:
            return Response({"error": f"Snowflake connection failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        data = request.data
        errors = {}
        
        if not data.get('product_name'):
            errors['product_name'] = "This field is required."
        if not isinstance(data.get('price'), (int, float)) or data.get('price', -1) < 0:
            errors['price'] = "Price must be a non-negative number."
        if not isinstance(data.get('quantity'), int) or data.get('quantity', -1) < 0:
            errors['quantity'] = "Quantity must be a non-negative integer."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO products (product_name, price, quantity) VALUES (%s, %s, %s)",
                (data['product_name'], float(data['price']), data['quantity'])
            )
            conn.commit()
            cursor.close()
            conn.close()
            return Response(data, status=status.HTTP_201_CREATED)
        except snowflake.connector.errors.OperationalError as e:
            return Response({"error": f"Snowflake connection failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
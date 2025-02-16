import cv2
import requests
from pyzbar.pyzbar import decode

def fetch_product_info(barcode):
    """Fetch product details from Open Food Facts API"""
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    data = response.json()

    if data.get("status") == 1:  # Product found
        product = data["product"]
        product_name = product.get("product_name", "Unknown Product")
        brand = product.get("brands", "Unknown Brand")
        ingredients = product.get("ingredients_text", "No ingredients available")
        calories = product.get("nutriments", {}).get("energy-kcal", "N/A")

        return {
            "name": product_name,
            "brand": brand,
            "ingredients": ingredients,
            "calories": calories
        }
    else:
        return {"error": "Product not found"}

def scan_barcode():
    """Scan barcode using a webcam"""
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        barcodes = decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")
            print(f"Scanned Barcode: {barcode_data}")

            # Fetch product details
            product_info = fetch_product_info(barcode_data)

            if "error" in product_info:
                print("Product not found.")
            else:
                print(f"Product Name: {product_info['name']}")
                print(f"Brand: {product_info['brand']}")
                print(f"Ingredients: {product_info['ingredients']}")
                print(f"Calories: {product_info['calories']} kcal")

            # Draw a rectangle around the barcode
            x, y, w, h = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_barcode()

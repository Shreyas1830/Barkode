# Barcode Scanner with Open Food Facts API

This Python script allows you to scan barcodes using a webcam and fetch product details from the Open Food Facts API.

## Features
- Scans barcodes using a webcam.
- Retrieves product details such as name, brand, ingredients, and calories.
- Uses Open Food Facts API for product information.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install opencv-python requests pyzbar
```

## Usage
Run the script to start scanning barcodes:

```bash
python script.py
```

Press `q` to exit the barcode scanner.

## How It Works
1. The script captures video from the webcam.
2. It detects and decodes barcodes in real-time.
3. The scanned barcode data is sent to the Open Food Facts API.
4. The product details (if available) are displayed on the terminal.

## Example Output
```
Scanned Barcode: 123456789
Product Name: Sample Product
Brand: Sample Brand
Ingredients: Water, Sugar, Flavor
Calories: 120 kcal
```





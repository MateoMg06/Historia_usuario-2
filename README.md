# Inventory Management System

A simple Python-based inventory and sales management application that allows users to register product sales and view a summary of transactions.

## Overview

This application provides a command-line interface for managing product sales. It enables users to register product information (name, price, quantity), performs input validation, and displays a summary of all registered sales with aggregated quantities per product.

## Features

- **Product Registration**: Register products with name, price, and quantity with built-in validation
- **Input Validation**: Ensures proper data types and prevents negative values
- **Sales Summary**: Displays aggregated sales data showing total quantities per product and total amount

## Project Structure

```
├── Inventory.py              # Main entry point of the application
├── Register_product.py       # Module for registering product sales
├── Show_summary.py           # Module for displaying sales summary
└── README.md                 # Project documentation
```

## Files Description

### `Inventory.py`
The main script that orchestrates the application flow:
- Imports and calls the `register_sale()` function
- Collects sales data
- Displays the summary of registered sales

### `Register_product.py`
Contains the `register_sale()` function that:
- Prompts the user to enter product name, price, and quantity
- Validates product name (must be text, non-empty)
- Validates price (must be a number, non-negative)
- Validates quantity (must be a whole number, non-negative)
- Returns a dictionary with sale information

### `Show_summary.py`
Contains the `show_summary()` function that:
- Displays a summary of all sales
- Aggregates quantities for products with the same name
- Shows total quantity per product
- Displays the overall total amount

## Usage

Run the application from the command line:

```bash
python Inventory.py
```

Follow the prompts to enter product information:
1. Enter the product name (text only)
2. Enter the product price (positive number)
3. Enter the quantity (positive whole number)

The application will then display a summary showing:
- Product names and total quantities
- Overall total amount

## Input Validation

The application includes robust input validation:
- **Product Name**: Must contain only letters, cannot be empty
- **Price**: Must be a valid number and cannot be negative
- **Quantity**: Must be a whole number and cannot be negative

Invalid inputs prompt the user to re-enter the correct information.
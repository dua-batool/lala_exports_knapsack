# Lala Exports Knapsack

A Python application for managing export orders using the Knapsack algorithm. It provides a graphical interface for users to input customer details, select furniture items, generate invoices, and export the final invoice in PDF format. This is the project for the course Data Structures and Algorithms taken in the second semester at Habib University in Spring 2022.

## Features

- Graphical user interface (GUI) using Tkinter
- Input customer details such as name and phone number
- Select items from a list of furniture
- Calculate total price, weight, and tax
- Generate a provisional list of selected items
- Generate a final invoice with customer details and items 
- Export the final invoice in PDF format

## Knapsack problem usage

The Knapsack problem is used to create a final invoice. In case the selected items go beyond the weight limit, the items to export would be chosen in such a way that the profit is maximized.

## Dependencies
- Python 
- Tkinter
- fpdf
- pdfkit

### Notice

This project was created in early stages of learning and there might be a few discrepancies in the implementation of the knapsack problem.

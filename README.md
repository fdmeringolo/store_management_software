# Store Management Software

## Description
This project is a Python-based store management software designed to help manage inventory, sales, and customer data efficiently. The software is text-based, so it will be used via the command line.

## Features
- Register new products, with name, quantity, selling price, and purchase price.
- List all available products.
- Record sales made.
- Display gross and net profits.
- Show a help menu with all available commands.

**Attention**: the interaction is in italian as shown in the specification files.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/fdmeringolo/store_management_software.git
    ```
2. Navigate to the project directory:
    ```bash
    cd store_management_software
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:
    ```bash
    python main.py
    ```
2. Follow the on-screen instructions to manage your store.

## Requirements
- Python 3.8 or higher
- Required libraries (listed in `requirements.txt`)

## Project Structure
```
store_management_software/
├── main.py
├── application/
│   ├── __init__.py
│   ├── commands.py
│   ├── store.py
│   └── vaidation.py
├── project_specification_eng.md
├── project_specification_ita.md
├── README.md
└── requirements.txt
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Contact
For any inquiries, please contact [fd.meringolo@outlook.it].

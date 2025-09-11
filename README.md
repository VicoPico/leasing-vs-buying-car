# Leasing vs Buying Car Cost Comparison

This Python project helps you compare the financial costs of leasing versus buying a car over a chosen time horizon. It calculates the present value of all costs for both options, allowing you to make an informed decision based on your own parameters.

## Features

- Calculates present value (NPV) of buying and leasing a car
- Considers maintenance, insurance, fees, and resale value
- Plots cost comparison and highlights breakeven year
- Easy to customize parameters

## Usage

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib rich
   ```
3. Run the script:
   ```bash
   python leasing_vs_buying_car.py
   ```
4. Adjust parameters in the script as needed for your scenario.

> **Note:**  
> Use `python3` and `pip3` if your system distinguishes between Python 2 and Python 3.  
> On some systems, you may use `python` and `pip` if they point to Python 3.

## Output

- Prints a table comparing costs for each year
- Shows the breakeven year (if any)
- Displays a plot of cost over time

## License

See [LICENSE](LICENSE) for details.

---

Created by VicoPico.

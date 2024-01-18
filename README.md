# DCA Simulator

## Project Description
The DCA Simulator is a web-based stock investment simulator designed to demonstrate and analyze the long-term performance of a dollar-cost averaging investment strategy. It allows users to input multiple stock symbols, along with a monthly investment amount, start date, and end date, and then displays the Return on Investment (ROI) for each stock.

## Features
- Analyze multiple stocks simultaneously.
- User-friendly interface for inputting stock symbols, investment amount, and date range.
- Visualization of investment growth over time.
- Calculation of ROI for each stock.

### Installation Using Docker
The easiest way to run the DCA Simulator is using Docker. Follow these steps:
1. Clone the repository:
``` bash
    git clone https://github.com/yourusername/dca-simulator.git
```
2. Navigate to the project directory:
``` bash
    cd dca-simulator
```
3. Build the Docker image:
``` bash
    docker build -t dca-simulator .
```

4. Run the Docker container:
``` bash
    docker run -p 5000:5000 dca-simulator
```
## Installation without Docker

To set up the DCA Simulator without Docker, follow these steps:

1. Clone the repository:
``` bash
    git clone https://github.com/yourusername/dca-simulator.git
```
2. Navigate to the project directory:
``` bash
    cd dca-simulator
```
3. Install the required dependencies (if applicable):
``` bash
    pip install -r requirements.txt
```


## Usage

To run the DCA Simulator:

1. Start the Flask server:
``` bash
    python app.py
```
2. Open your web browser and navigate to:

``` bash
    http://localhost:5000
```
3. Enter the stock symbols, monthly investment amount, start date, and end date.
4. Click 'Simulate' to view the investment results.

## Contributing
Contributions to the DCA Simulator are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
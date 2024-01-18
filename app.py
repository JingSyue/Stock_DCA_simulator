import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


def fetch_data(symbol, start='2000-01-01', end='2021-01-01'):
    try:
        data = yf.download(symbol, start=start, end=end)
        if data.empty:
            raise ValueError(f"No data found for {symbol}")
        return data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def simulate_investment(stock_data, start_date, end_date, monthly_investment, investment_day):
    if stock_data is None:
        return None, None, None

    invested_amount = 0
    shares_held = 0
    current_date = start_date

    while current_date <= end_date:
        # Adjust the date if it's not a trading day
        while current_date not in stock_data.index:
            current_date += timedelta(days=1)
            if current_date > end_date:
                break

        if current_date > end_date:
            break

        monthly_price = stock_data.loc[current_date, 'Close']
        shares_bought = monthly_investment / monthly_price
        shares_held += shares_bought
        invested_amount += monthly_investment

        # Set the date for the next investment
        if current_date.month == 12:
            current_date = datetime(current_date.year + 1, 1, investment_day)
        else:
            current_date = datetime(current_date.year, current_date.month + 1, investment_day)

    current_value = shares_held * stock_data['Close'].iloc[-1]
    roi = (current_value - invested_amount) / invested_amount * 100
    return roi, invested_amount, current_value


@app.route('/simulate', methods=['POST'])
def simulate():
    # 从表单获取数据
    symbols = request.form.getlist('symbol[]')  # 获取股票代码数组
    monthly_investment = float(request.form.get('monthly_investment'))
    investment_day = int(request.form.get('investment_day'))
    start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
    end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')

    result_data = []
    for symbol in symbols:
        symbol = symbol.strip()  # 清理空格
        stock_data = fetch_data(symbol, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

        if stock_data is not None:
            roi, invested_amount, current_value = simulate_investment(stock_data, start_date, end_date, monthly_investment, investment_day)
            result_data.append({
                'symbol': symbol,
                'ROI': roi,
                'Total_Invested': invested_amount,
                'Current_Value': current_value
            })
        else:
            result_data.append({
                'symbol': symbol,
                'error': 'Failed to retrieve data'
            })

    return render_template('result.html', data=result_data)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
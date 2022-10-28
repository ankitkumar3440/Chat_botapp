from flask import Flask ,request,jsonify
import requests

app=Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data=request.get_json()
    source_currency=data['queryresult']['parameters']['unit-currency']['currency']
    amount=data['queryresult']['parameters']['unit-currency']['currency']
    target_currency=data['queryresult']['parameters']['currency-name']
    print(data)
    print(source_currency)
    print(amount)
    print(target_currency)
    cf=fetch_conversion_factor(source_currency,target_currency)

    final_amount=amount*cf
    response={
        'fulfillmentText':"{}  {} is {}  {}".format(amount,source_currency,final_amount,target_currency)
    }
    return jsonify(response)
def fetch_conversion_factor(source,target):
    url="https://free.currconv.com/api/v7/convert?q=INR_PHP,PHP_USD&compact={}_{" \
        "}ultra&apiKey=9aa0c54f5ad4c460c36d".format(source,target)

    response=requests.get(url)
    response=response.json()
    return response['{}_{}'.format(source,target)]
if __name__  == "__main__":
    app.run(debug=True)
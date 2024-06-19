from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests  # Ensure requests is installed or install via pip install requests

def deribit_data(request):
    # Example: Fetching data from a public API (ensure this endpoint is just for demonstration)
    response = requests.get("https://www.deribit.com/api/v2/public/get_order_book?instrument_name=BTC-PERPETUAL")
    data = response.json()
    return JsonResponse(data, safe=False)  # safe=False is used when returning a list instead of a dictionary

from PIL import Image
import requests
import torch
from flask import Flask, request, redirect
import json
from util import imgPred

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
    request_data = json.loads(request.get_data(), encoding="UTF-8")
    print(request_data)
    return ""

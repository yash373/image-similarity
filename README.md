# Image Similarity Project

## Overview

This project aims to measure the similarity between images using various algorithms and techniques. The goal is to develop a system that can accurately determine the similarity between two or more images.

## Features

- Image upload functionality using Imgur API
- Image similarity measurement using Llama-Groq-70B-8192-Tool-Use-Preview

## Requirements

- Python 3.x
- Groq API Key
- Image files (JPEG, PNG, etc.)

## Installation

1. Clone the repository: `git clone https://github.com/yash373/image-similarity.git`
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment: `env\Scripts\activate` (Windows) or `source env/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a .env.local file and add your groq api key.
6. Run the application: `python main.py`
# Environmental Anomalies

This web app allows users to explore past natural disasters around the globe with a simple and intuitive interface. On the home screen, users can select a specific region of Earth and initiate a search for historical natural disasters that have occurred in that area.

Once the "Search" button is clicked, a detailed map of the Earth is displayed, featuring icons that represent various natural disasters. Each icon provides a brief description of the event, including its date and type, enabling users to easily learn about the impact of these disasters in the selected region.

## Installation

1. **Clone the repository:**
```
git clone https://github.com/jthomas981/environmental-anomalies/
cd environmental-anomalies
```

2. **Set up a virtual environment:**
If you don’t have virtualenv installed, you can install it via pip:
```
pip install virtualenv
```
Then create and activate a virtual environment:
* For macOS/Linux:
```
virtualenv venv
source venv/bin/activate
```
* For Windows:
```
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies using the provided script:**
* For macOS/Linux:
```
./build.sh
```
* For Windows:
```
build.bat
```

This script will:
* Install the necessary Python packages listed in requirements.txt.
* Collect static files for your app.
* Apply any outstanding database migrations.

## Usage 

After running the build script, you can start your application using:
```python manage.py runserver```
Access the app at http://127.0.0.1:8000.

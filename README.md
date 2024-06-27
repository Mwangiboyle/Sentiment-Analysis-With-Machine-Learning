# Sentiment Analysis Tool

This project is a web application built using Streamlit that performs sentiment analysis on user-inputted text. The app uses pre-trained machine learning models to predict whether the sentiment of the input text is positive or negative.

## Project Structure

- `app.py`: The main application file.
- `models/`: Directory containing the saved machine learning models.
- `requirements.txt`: Lists the Python packages required for the project.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- scikit-learn
- joblib

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Mwangiboyle/Sentiment-Analysis-With-Machine-Learning.git
    cd Sentiment-Analysis-With-Machine-Learning
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open your web browser** and go to `http://localhost:8501`.

3. **Use the app**:
    - Enter the text in the provided text area.
    - Select the machine learning model (SVM or Multinomial).
    - Click the "Submit" button to get the prediction.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

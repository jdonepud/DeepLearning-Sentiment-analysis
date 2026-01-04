# DeepLearning Sentiment Analysis

A Streamlit web application for performing real-time sentiment analysis using a Hugging Face Transformer model powered by PyTorch. The app classifies text as positive, negative, or neutral and displays confidence scores for each class.

## Features
- Real-time sentiment prediction from user input
- Transformer-based NLP pipeline via `transformers` and `torch`
- Simple Streamlit UI with probability visualization
- Lightweight deployment that runs locally or in the cloud

## Project Structure
- `app.py` – Streamlit application entry point that loads the model and renders the UI.
- `requirements.txt` – Python dependencies needed to run the app.

## Getting Started
### Prerequisites
- Python 3.10+ recommended
- Virtual environment tool such as `venv` or `conda`

### Installation
1. Clone the repository and enter the project directory.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
Launch the Streamlit server from the project root:
```bash
streamlit run app.py
```
The app will provide a local URL (typically `http://localhost:8501`) where you can enter text and view predicted sentiment labels with confidence scores.

## Deployment Notes
- Model weights are downloaded at runtime; ensure outbound network access on first launch.
- For containerized deployments, cache the model by running the app once during the image build or specify a model path via environment configuration if you extend the code.

## Contributing
Issues and pull requests are welcome. Please ensure changes include appropriate tests or manual verification steps when applicable.

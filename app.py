from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

@app.route('/')
def index():
    """Render the main page with the input form."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_code():
    """Generate code based on natural language description."""
    try:
        # Get the user's request from the form
        user_request = request.form.get('request', '').strip()
        
        if not user_request:
            return render_template('index.html', error='Please provide a code request.')
        
        # Create a prompt for the LLM
        prompt = f"""
You are a helpful coding assistant. Generate clean, well-commented code based on the user's request.
You can include HTML formatting like <pre>, <code>, <b>, <i> tags to make the output look better.
Feel free to use any HTML tags that would improve the presentation.

User request: {user_request}

Please provide the code with HTML formatting:
"""
        
        # Initialize Gemini model
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Call Gemini API
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=1000,
                temperature=0.7,
            )
        )
        
        generated_code = response.text.strip()
        
        # VULNERABILITY: Directly rendering LLM output without sanitization
        # This allows the LLM output to contain malicious HTML/JavaScript
        return render_template('index.html', 
                             generated_code=generated_code, 
                             user_request=user_request,
                             success=True)
        
    except Exception as e:
        return render_template('index.html', error=f'Error generating code: {str(e)}')

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # Check if Gemini API key is set
    if not os.getenv('GEMINI_API_KEY'):
        print("Warning: GEMINI_API_KEY environment variable not set!")
        print("Please set your Gemini API key in a .env file or environment variable.")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

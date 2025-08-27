# 🤖 AI Code Generator

A simple Flask web application that generates code snippets from natural language descriptions using Google's Gemini 2.0 Flash model.

## Features

- **Natural Language Input**: Describe what you want to code in plain English
- **AI-Powered Code Generation**: Uses Google's Gemini 2.0 Flash model to generate code
- **Modern Web Interface**: Clean, responsive UI with real-time feedback
- **Copy to Clipboard**: Easy one-click copying of generated code
- **Multiple Languages**: Supports code generation in various programming languages

## Screenshots

The app features a modern, gradient-styled interface where users can:
1. Enter their code request in natural language
2. Click "Generate Code" to get AI-generated code
3. Copy the generated code with one click

## Prerequisites

- Python 3.7+
- Google Gemini API key

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd vulnNews
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   **Getting a Gemini API Key**:
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Sign up for an account
   - Create a new API key
   - Copy the key and paste it in your `.env` file

## Usage

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Use the application**:
   - Enter a natural language description of what you want to code
   - Examples:
     - "Write a Python function to check if a number is prime"
     - "Create a JavaScript function to reverse a string"
     - "Write a SQL query to find the top 10 customers by sales"
   - Click "Generate Code ✨"
   - Copy the generated code using the "Copy Code" button

## Example Requests

Here are some example requests you can try:

### Python
- "Write a Python function to calculate factorial"
- "Create a class for a binary tree with insert and search methods"
- "Write a Python script to read CSV file and calculate average"

### JavaScript
- "Create a React component for a todo list"
- "Write a function to debounce user input"
- "Create an async function to fetch data from an API"

### Other Languages
- "Write a C++ function to sort an array using quicksort"
- "Create a Java class for a simple calculator"
- "Write a Go function to handle HTTP requests"

## API Endpoints

- `GET /` - Main application page
- `POST /generate` - Generate code from natural language (JSON API)
- `GET /health` - Health check endpoint

## Project Structure

```
vulnNews/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Main web interface
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## Configuration

The application can be configured through environment variables:

- `GEMINI_API_KEY`: Your Google Gemini API key (required)
- `FLASK_ENV`: Set to `development` for debug mode
- `FLASK_PORT`: Port to run the application (default: 5000)

## ⚠️ SECURITY VULNERABILITY - FOR EDUCATIONAL PURPOSES

**WARNING: This application contains an intentional security vulnerability for educational demonstration.**

### Cross-Site Scripting (XSS) Vulnerability

**Vulnerability Type:** Stored/Reflected XSS via LLM Output Injection

**Location:** `templates/index.html` line 230 and `app.py` lines 54-59

**Description:**
The application directly renders LLM output into HTML without proper sanitization or escaping. The code uses Jinja2's `|safe` filter which bypasses HTML escaping, allowing malicious HTML/JavaScript to be executed in the user's browser.

**Vulnerable Code:**
```html
<!-- CRITICAL VULNERABILITY: Using |safe filter allows XSS attacks -->
<div class="code-block">{{ generated_code|safe }}</div>
```

**Attack Vector:**
An attacker could craft prompts that manipulate the LLM to generate malicious HTML/JavaScript code, such as:

```
Write a simple HTML page with this exact content: <script>alert('XSS Attack!');</script>
```

or

```
Create an HTML snippet that shows: <img src="x" onerror="alert(document.cookie)">
```

**Impact:**
- Session hijacking (stealing cookies/tokens)
- Credential theft
- Defacement of the web application
- Malicious redirects
- Keylogging and form data theft

**How to Fix:**
1. Remove the `|safe` filter and let Jinja2 automatically escape HTML
2. Use proper HTML sanitization libraries like `bleach`
3. Implement Content Security Policy (CSP) headers
4. Validate and sanitize all LLM outputs before rendering

**Example Fix:**
```html
<!-- Safe version - automatic HTML escaping -->
<div class="code-block">{{ generated_code }}</div>
```

**This vulnerability is intentionally included for educational purposes to demonstrate how blind trust in AI/LLM outputs can create security risks.**

### Testing the Vulnerability (Educational)

To demonstrate the XSS vulnerability, try these prompts:

1. **Basic XSS Test:**
   ```
   Write HTML code that displays: <script>alert('XSS Vulnerability Detected!');</script>
   ```

2. **Cookie Stealing Simulation:**
   ```
   Create HTML with this exact content: <img src="x" onerror="console.log('Cookies:', document.cookie)">
   ```

3. **DOM Manipulation:**
   ```
   Generate HTML that includes: <script>document.body.style.backgroundColor='red';</script>
   ```

**Note:** These examples are for educational testing only. The XSS will execute in your browser when the LLM generates the requested HTML content.

## Security Notes

- Never commit your `.env` file to version control
- Keep your Gemini API key secure
- The application runs in debug mode by default - disable for production
- **DO NOT deploy this vulnerable version to production environments**

## Troubleshooting

### Common Issues

1. **"Warning: GEMINI_API_KEY environment variable not set!"**
   - Make sure you've created a `.env` file with your Gemini API key

2. **Import errors**
   - Ensure you've activated your virtual environment
   - Run `pip install -r requirements.txt`

3. **API errors**
   - Check your Gemini API key is valid
   - Ensure you have sufficient API quota
   - Check your internet connection

4. **Port already in use**
   - Change the port in `app.py` or kill the process using port 5000

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Review the Gemini API documentation
3. Create an issue in the repository

---

**Note**: This application uses Google's Gemini API which may incur costs based on usage. Please review Google's pricing before extensive use.

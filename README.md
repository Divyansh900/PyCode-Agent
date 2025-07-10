# PyCode-Agent 🐍🤖

A powerful Python coding assistant powered by Google's Gemini AI that can write, test, and execute Python code with integrated memory and tool support.

## 🌟 Features

- **AI-Powered Code Generation**: Leverages Google's Gemini 2.5 Flash model for intelligent code generation
- **Code Execution**: Built-in Python code runner with safety constraints
- **Memory Management**: Maintains conversation history for context-aware responses
- **Library Support**: Pre-loaded with popular data science libraries (pandas, numpy, matplotlib, seaborn)
- **File Operations**: Can read, write, and manipulate files in the current working directory
- **Safety First**: Restricted execution environment with controlled built-in functions
- **Streamlit Integration**: Easy-to-use web interface for seamless interaction

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Google AI API Key (Get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Divyansh900/PyCodeAgent.git
   cd PyCodeAgent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit>=1.28.0
langchain>=0.0.350
langchain-google-genai>=0.0.8
python-dotenv>=1.0.0
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

## 🏗️ Architecture

### Core Components

1. **PyCodeAgent Class**: Main agent class that orchestrates the AI model, memory, and tools
2. **CodeOutputParser**: Custom parser for handling AI responses in the required format
3. **Tool System**: Integrated tools for code execution, calculation, and library checking
4. **Memory System**: Conversation buffer for maintaining context across interactions

### Available Tools

- **Code Runner**: Executes Python code in a controlled environment
- **Calculator**: Evaluates mathematical expressions
- **Library Checker**: Verifies availability of pre-loaded libraries


## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google AI API key | Yes |

### Model Configuration

The agent uses Gemini 2.5 Flash with the following default settings:
- **Temperature**: 0.85 (adjustable for creativity vs consistency)
- **Model**: gemini-2.5-flash

## 📁 Project Structure

```
PyCodeAgent/
├── main.py                 # Streamlit web interface
├── pycode_agent.py         # Core agent implementation
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── .env.example           # Example environment file
├── README.md              # This file
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE               # License file
└── files/                # Directory for file operations
```

## 🎯 Key Features Explained

### Intelligent Code Generation
The agent follows a structured approach:
1. **Thought Process**: Analyzes the problem
2. **Action Selection**: Chooses appropriate tools
3. **Code Execution**: Tests the generated code
4. **Final Answer**: Provides the complete solution

### Safety Features
- Restricted execution environment
- Limited built-in functions
- Controlled library imports
- Error handling and reporting

### Memory Management
- Maintains conversation history
- Context-aware responses
- Memory size tracking
- Reset functionality

## 🔒 Security Considerations

- **Sandboxed Execution**: Code runs in a controlled environment
- **Limited Built-ins**: Only safe built-in functions are available
- **No External Imports**: Only pre-approved libraries can be used
- **Error Handling**: Comprehensive error catching and reporting

## 📊 Pre-loaded Libraries

The agent comes with the following libraries ready to use:

- **pandas (pd)**: Data manipulation and analysis
- **numpy (np)**: Numerical computing
- **matplotlib.pyplot (plt)**: Plotting and visualization
- **seaborn (sns)**: Statistical data visualization

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- File operations require files to be in the `files/` directory
- Library imports are restricted to pre-loaded ones
- Large code outputs may be truncated in the interface

## 🔮 Future Enhancements

- [ ] Support for additional libraries
- [ ] Enhanced file management
- [ ] Code optimization suggestions
- [ ] Multi-language support
- [ ] Advanced debugging tools
- [ ] Database support for SQL servives

## 💡 Tips for Best Results

1. **Be Specific**: Provide clear, detailed requirements
2. **Test Cases**: The agent automatically runs tests - mention expected outputs
3. **File Operations**: Specify exact file names and paths, create a folder named for file operations
4. **Library Usage**: Use the library checker tool to verify availability
5. **Iterative Development**: Build complex solutions step by step

## 🆘 Support

If you encounter any issues:

1. Check the [Issues](https://github.com/Divyansh900/PyCodeAgent/issues) page
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

## 👨‍💻 Author

**Divyansh Vishwkarma**
- GitHub: [@Divyansh900](https://github.com/Divyansh900)
- Repository: [PyCodeAgent](https://github.com/Divyansh900/PyCodeAgent)

## 🙏 Acknowledgments

- Google AI for the Gemini model
- LangChain for the agent framework
- Streamlit for the web interface
- The Python community for the amazing libraries

---

**Made with ❤️ by Divyansh Vishwkarma**

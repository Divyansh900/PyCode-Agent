# PyCodeAgent API Documentation

## Overview

PyCodeAgent provides a simple yet powerful API for AI-powered Python code generation and execution. This document covers all available classes, methods, and their usage.

## Core Classes

### PyCodeAgent

The main class that provides the AI-powered coding assistant functionality.

#### Constructor

```python
PyCodeAgent()
```

Creates a new instance of the PyCodeAgent with default configuration.

**Parameters:** None

**Returns:** `PyCodeAgent` instance

**Example:**
```python
from pycode_agent import PyCodeAgent

agent = PyCodeAgent()
```

#### Methods

##### `generate(prompt: str) -> str`

Generates Python code based on the provided prompt.

**Parameters:**
- `prompt` (str): The user's request for code generation

**Returns:** 
- `str`: Generated Python code with comments and explanations

**Raises:**
- `ValueError`: If prompt is empty or invalid
- `Exception`: If API call fails

**Example:**
```python
agent = PyCodeAgent()
code = agent.generate("Create a function to calculate factorial")
print(code)
```

##### `reset_agent() -> None`

Resets the agent's memory and reinitializes the conversation.

**Parameters:** None

**Returns:** None

**Example:**
```python
agent = PyCodeAgent()
# ... some interactions ...
agent.reset_agent()  # Fresh start
```

##### `get_memory_size() -> int`

Returns the current size of the conversation memory.

**Parameters:** None

**Returns:** 
- `int`: Number of messages in memory

**Example:**
```python
agent = PyCodeAgent()
agent.generate("Hello")
print(agent.get_memory_size())  # Output: 2 (user + assistant message)
```

### CodeOutputParser

Custom output parser for handling AI model responses.

#### Constructor

```python
CodeOutputParser()
```

Creates a new instance of the custom output parser.

#### Methods

##### `parse(llm_op: str) -> Union[AgentAction, AgentFinish]`

Parses the LLM output into structured agent actions or final answers.

**Parameters:**
- `llm_op` (str): Raw output from the language model

**Returns:**
- `Union[AgentAction, AgentFinish]`: Parsed action or final result

**Raises:**
- `OutputParserException`: If parsing fails

## Built-in Tools

### Code Runner Tool

Executes Python code in a sandboxed environment.

**Name:** `"Run Code"`

**Description:** Runs Python code and returns output or exceptions

**Available Libraries:**
- pandas (as `pd`)
- numpy (as `np`)
- matplotlib.pyplot (as `plt`)
- seaborn (as `sns`)

**Safety Features:**
- Restricted built-in functions
- No external imports
- Error handling and reporting

**Example Usage:**
```python
# This is handled automatically by the agent
code = """
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.head())
"""
# Agent will execute this code using the tool
```

### Calculator Tool

Evaluates mathematical expressions.

**Name:** `"Calculator"`

**Description:** Evaluates simple mathematical expressions

**Example Usage:**
```python
# Agent can use this for calculations
expression = "2 + 3 * 4"
result = "14"  # Calculated by the tool
```

### Library Checker Tool

Verifies availability of libraries in the execution environment.

**Name:** `"Libraries"`

**Description:** Checks if libraries are available for use

**Available Libraries:**
- numpy, np
- pandas, pd
- matplotlib, matplotlib.pyplot, plt
- seaborn, sns

**Example Usage:**
```python
# Agent checks library availability
library_check = agent.check_library("pandas")
# Returns: "Library is present. Hence no need to write import statement."
```

## Error Handling

### Common Exceptions

#### `OutputParserException`

Raised when the AI output cannot be parsed correctly.

**Common Causes:**
- Malformed AI response
- Missing required patterns
- Unexpected response format

**Example:**
```python
try:
    result = agent.generate("invalid prompt")
except OutputParserException as e:
    print(f"Parsing error: {e}")
```

#### `ValueError`

Raised for invalid input parameters.

**Common Causes:**
- Empty prompt
- Invalid parameter types
- Configuration errors

**Example:**
```python
try:
    result = agent.generate("")
except ValueError as e:
    print(f"Invalid input: {e}")
```

## Configuration

### Environment Variables

#### Required

- `GOOGLE_API_KEY`: Your Google AI API key

#### Optional

- `MODEL_NAME`: Gemini model name (default: "gemini-2.5-flash")
- `MODEL_TEMPERATURE`: Model temperature (default: 0.85)

### Model Configuration

```python
# The agent uses these default settings:
model_config = {
    "model": "gemini-2.5-flash",
    "temperature": 0.85,
    "google_api_key": os.getenv("GOOGLE_API_KEY")
}
```

## Response Format

The agent follows a structured response format:

```
Thought: [Agent's reasoning process]
Action: [Tool name to use]
Action Input: [Input for the tool]
Observation: [Tool's output]
Final Answer: [Complete solution with code]
```

## Usage Patterns

### Basic Code Generation

```python
agent = PyCodeAgent()
response = agent.generate("Create a function to sort a list")
```

### Data Analysis

```python
agent = PyCodeAgent()
response = agent.generate("""
Create a pandas DataFrame with sales data and generate
a bar chart showing monthly sales trends
""")
```

### File Operations

```python
agent = PyCodeAgent()
response = agent.generate("""
Read data from 'sales.csv', calculate summary statistics,
and save results to 'summary.txt'
""")
```

### Error Handling Pattern

```python
try:
    agent = PyCodeAgent()
    result = agent.generate(user_prompt)
    print(result)
except ValueError as e:
    print(f"Input error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Best Practices

### Prompt Engineering

1. **Be Specific**: Provide clear, detailed requirements
2. **Include Context**: Mention expected inputs and outputs
3. **Specify Libraries**: Mention which libraries to use
4. **Error Cases**: Describe how to handle errors

### Memory Management

```python
# Check memory usage
if agent.get_memory_size() > 20:
    agent.reset_agent()  # Reset to free memory
```

### Performance Optimization

```python
# Reuse agent instances
agent = PyCodeAgent()

# Multiple requests with same agent
for prompt in prompts:
    result = agent.generate(prompt)
    process_result(result)
```

## Rate Limits and Quotas

- **API Calls**: Limited by Google AI API quotas
- **Memory**: Conversation buffer has practical limits
- **Execution Time**: Code execution has timeout limits

## Security Considerations

### Code Execution Safety

- Sandboxed execution environment
- Limited built-in functions
- No network access
- Restricted file system access

### API Key Security

- Never commit API keys to version control
- Use environment variables
- Rotate keys regularly
- Monitor API usage

## Troubleshooting

### Common Issues

1. **API Key Errors**
   ```
   Solution: Verify GOOGLE_API_KEY in .env file
   ```

2. **Import Errors**
   ```
   Solution: Only use pre-loaded libraries (pandas, numpy, matplotlib, seaborn)
   ```

3. **Memory Issues**
   ```
   Solution: Use agent.reset_agent() to clear memory
   ```

4. **Parsing Errors**
   ```
   Solution: Check prompt format and try again
   ```

## Examples

### Complete Example

```python
from pycode_agent import PyCodeAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize agent
agent = PyCodeAgent()

# Generate code
prompt = """
Create a function that:
1. Takes a list of numbers as input
2. Calculates mean, median, and standard deviation
3. Returns a dictionary with these statistics
4. Include error handling for empty lists
"""

try:
    result = agent.generate(prompt)
    print("Generated Code:")
    print(result)
    
    # Check memory usage
    print(f"Memory size: {agent.get_memory_size()}")
    
except Exception as e:
    print(f"Error: {e}")
```

## Version History

- **v1.0.0**: Initial release with basic code generation
- **v1.1.0**: Added memory management and file operations
- **v1.2.0**: Enhanced error handling and library support

---

For more examples and advanced usage, see the [examples](examples/) directory in the repository.

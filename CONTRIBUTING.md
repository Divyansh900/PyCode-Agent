# Contributing to PyCodeAgent

Thank you for your interest in contributing to PyCodeAgent! We welcome contributions from the community and are grateful for your help in making this project better.

## 🎯 Ways to Contribute

- **Bug Reports**: Report bugs and issues
- **Feature Requests**: Suggest new features
- **Code Contributions**: Submit pull requests
- **Documentation**: Improve documentation and examples
- **Testing**: Help with testing and quality assurance

## 🚀 Getting Started

### Development Environment Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/PyCodeAgent.git
   cd PyCodeAgent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## 📋 Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Example Code Style

```python
def generate_code(self, prompt: str) -> str:
    """
    Generate Python code based on the given prompt.
    
    Args:
        prompt (str): The user's request for code generation
        
    Returns:
        str: Generated Python code
        
    Raises:
        ValueError: If prompt is empty or invalid
    """
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    # Implementation here
    return generated_code
```

### Commit Messages

Use clear, descriptive commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding or modifying tests

Examples:
```
feat: add support for matplotlib plotting
fix: resolve memory leak in conversation buffer
docs: update installation instructions
```

## 🐛 Reporting Issues

When reporting bugs, please include:

1. **Clear Description**: What happened and what you expected
2. **Steps to Reproduce**: Step-by-step instructions
3. **Environment**: Python version, OS, dependencies
4. **Error Messages**: Full error traceback
5. **Code Sample**: Minimal code that reproduces the issue

### Bug Report Template

```markdown
## Bug Description
A clear description of the bug.

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should have happened.

## Actual Behavior
What actually happened.

## Environment
- Python version:
- OS:
- PyCodeAgent version:
- Dependencies:

## Error Messages
```
Full error traceback here
```

## Additional Context
Any other relevant information.
```

## 💡 Feature Requests

When suggesting features:

1. **Use Case**: Explain why this feature would be useful
2. **Description**: Detailed description of the feature
3. **Examples**: Code examples or mockups if applicable
4. **Alternatives**: Any alternative solutions you've considered

## 🔧 Pull Request Process

### Before Submitting

1. **Check Issues**: Make sure your PR addresses an existing issue
2. **Test Your Changes**: Ensure your code works correctly
3. **Update Documentation**: Update relevant documentation
4. **Follow Style Guide**: Ensure code follows project conventions

### PR Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Code is commented, particularly in hard-to-understand areas
- [ ] Documentation updated if needed
- [ ] Changes generate no new warnings
- [ ] Tests added/updated for new functionality
- [ ] All tests pass

### PR Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Manual testing completed
- [ ] All tests pass

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings generated
```

## 🧪 Testing

### Running Tests

```bash
python -m pytest tests/
```

### Writing Tests

- Write tests for new functionality
- Use descriptive test names
- Test edge cases and error conditions
- Aim for good test coverage

### Test Example

```python
def test_code_generation():
    """Test basic code generation functionality."""
    agent = PyCodeAgent()
    result = agent.generate("Create a function to add two numbers")
    
    assert "def" in result
    assert "add" in result.lower()
    assert result is not None
```

## 📚 Documentation

### Documentation Standards

- Use clear, concise language
- Include code examples
- Update README.md for significant changes
- Add inline comments for complex logic
- Document all public APIs

### Documentation Locations

- **README.md**: Main project documentation
- **Code Comments**: Inline documentation
- **Docstrings**: Function and class documentation
- **Examples**: Usage examples and tutorials

## 🎯 Areas for Contribution

### High Priority

- [ ] Additional library support
- [ ] Enhanced error handling
- [ ] Performance optimizations
- [ ] Better test coverage
- [ ] Documentation improvements

### Medium Priority

- [ ] Code optimization suggestions
- [ ] Advanced debugging tools
- [ ] Multi-language support
- [ ] Plugin system
- [ ] Configuration management

### Low Priority

- [ ] UI/UX improvements
- [ ] Advanced analytics
- [ ] Integration with other tools
- [ ] Performance monitoring
- [ ] Advanced caching

## 🤝 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Focus on what's best for the community
- Show empathy towards other contributors
- Give constructive feedback
- Accept feedback gracefully

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or inflammatory comments
- Public or private harassment
- Publishing others' private information
- Unprofessional conduct

## 🚨 Security

If you discover a security vulnerability:

1. **Do NOT** create a public issue
2. Email the maintainer directly
3. Provide detailed information about the vulnerability
4. Allow time for the issue to be addressed

## 📞 Getting Help

- **Issues**: Use GitHub Issues for questions
- **Discussions**: Use GitHub Discussions for general questions
- **Email**: Contact maintainer for sensitive issues

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing to PyCodeAgent! Your help makes this project better for everyone. 🙏

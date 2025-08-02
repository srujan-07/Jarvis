# Tests Directory

This directory contains all test files for the Jarvis project.

## Test Structure

- `test_*.py` - Unit tests for specific modules
- `test_integration.py` - Integration tests that check module interactions
- `__init__.py` - Test configuration and path setup

## Running Tests

### Quick Test Run
```bash
python -m pytest tests/ -v
```

### Comprehensive Test Run (with all checks)
```bash
python run_tests.py
```

### Run specific test files
```bash
python -m pytest tests/test_calculatenumbers.py -v
python -m pytest tests/test_greetme.py -v
```

### Run with coverage
```bash
python -m pytest tests/ --cov=. --cov-report=html
```

## Test Categories

### Unit Tests
- `test_calculatenumbers.py` - Tests for calculator functionality
- `test_greetme.py` - Tests for greeting functionality

### Integration Tests
- `test_integration.py` - Tests module imports and basic integration

## Dependencies

Install test dependencies:
```bash
pip install -r requirements-dev.txt
```

## CI/CD Integration

Tests are automatically run in GitHub Actions:
- **Main CI Workflow** (`python-app.yml`) - Quick syntax checks
- **Python Tests Workflow** (`python-tests.yml`) - Comprehensive testing

## Adding New Tests

1. Create a new test file following the `test_*.py` naming convention
2. Import the module you want to test
3. Create test classes inheriting from `unittest.TestCase`
4. Use `@patch` decorators to mock external dependencies
5. Add appropriate assertions

Example:
```python
import unittest
from unittest.mock import patch, MagicMock

class TestMyModule(unittest.TestCase):
    @patch('mymodule.external_dependency')
    def test_my_function(self, mock_dep):
        mock_dep.return_value = "expected_result"
        result = mymodule.my_function()
        self.assertEqual(result, "expected_result")
```

## Code Quality

The test suite includes:
- **Linting** with flake8
- **Code formatting** with Black
- **Import sorting** with isort
- **Type checking** with mypy (optional)
- **Security scanning** with bandit
- **Coverage reporting** with pytest-cov

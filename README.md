# Text-to-Number

Convert textual numerical descriptions into their digit forms within strings, like turning "one apple" into "1 apple". Ideal for preprocessing text data for analysis or applications requiring numerical representations.

## Installation

Install via pip:

```bash
pip install text-to-number
```

## Usage

To convert text in your Python code:

```python
from text_to_number import text_to_number

result = text_to_number("I have two apples and three bananas.")
print(result)  # Outputs: "I have 2 apples and 3 bananas."
```

## Features

- Converts words to digits within a string.
- Supports numbers from zero to billions.
- Handles both singular and compound numbers (e.g., "twenty-one").

## Contributing

Contributions are welcome! See our contributing guidelines on GitHub.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Soham Padia - <sohampadia10@gmail.com>

Project Link: <https://github.com/soham-padia/textToInt>

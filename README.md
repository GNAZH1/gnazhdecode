<div align="center">
  <img src="https://telegra.ph/file/e87601e9b2fffde7c577f.jpg" alt="Gnazh Logo" width="300"/>

  # GNAZH
  
  🔒 Advanced Python Marshal Decoder & Analysis Framework

  [![PyPI version](https://badge.fury.io/py/gnazh.svg)](https://badge.fury.io/py/gnazh)
  [![Python](https://img.shields.io/pypi/pyversions/gnazh.svg)](https://pypi.org/project/gnazh/)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
  [![Downloads](https://pepy.tech/badge/gnazh)](https://pepy.tech/project/gnazh)
  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

  <p align="center">
    <a href="#features">Features</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#documentation">Docs</a> •
    <a href="#contributing">Contributing</a>
  </p>
</div>

---

## 🚀 Features

### Core Capabilities
- 🔓 Multi-layer marshal decoding
- 🔍 Advanced pattern detection
- 📊 Comprehensive bytecode analysis
- 🧬 Deep string analysis
- 🛡️ Multiple encryption support
- 🔄 Automatic layer detection
- 🎯 Code decompilation
- 📈 Statistical analysis

### Advanced Analysis
- 🔐 Encryption pattern detection
- 🧪 Entropy analysis
- 🎨 Control flow visualization
- 🔧 Code structure analysis
- 📱 Dynamic code analysis
- 🎭 Obfuscation detection
- 🎪 String extraction & analysis
- 🎲 Pattern matching

## ⚡ Quick Start

### Installation
```bash
pip install gnazh
```

### Basic Usage
```python
from gnazh import LayeredDecoder, PatternMatcher

# Initialize decoder
decoder = LayeredDecoder()

# Decode marshalled file
with open('encrypted.pyc', 'rb') as f:
    decoded = decoder.decode_all_layers(f.read())

# Analyze patterns
patterns = PatternMatcher().detect_patterns(decoded)
```

### Advanced Usage
```python
from gnazh import (
    LayeredDecoder,
    PatternMatcher,
    BytecodeAnalyzer,
    StringAnalyzer
)

# Initialize components
decoder = LayeredDecoder(debug=True)
analyzer = BytecodeAnalyzer()
string_analyzer = StringAnalyzer()

# Process file
with open('complex_encrypted.pyc', 'rb') as f:
    data = f.read()

# Full analysis
results = {
    'decoded': decoder.decode_all_layers(data),
    'patterns': PatternMatcher().detect_patterns(data),
    'bytecode': analyzer.analyze_bytecode(decoded),
    'strings': string_analyzer.analyze_strings(decoded)
}
```

## 📚 Documentation

### Decoders
- `LayeredDecoder`: Multi-layer decoding
- `PatternMatcher`: Pattern detection
- `BytecodeAnalyzer`: Bytecode analysis
- `StringAnalyzer`: String analysis

### Supported Formats
- ✅ Python Marshalled Files (.pyc)
- ✅ Base64 Encoded
- ✅ AES Encrypted
- ✅ XOR Encrypted
- ✅ Custom Encryption
- ✅ Zlib Compressed
- ✅ Multi-layer Encoding

### Analysis Features
```python
# Bytecode Analysis
bytecode_analysis = analyzer.analyze_bytecode(code_obj)
print(bytecode_analysis.control_flow)
print(bytecode_analysis.complexity_metrics)

# Pattern Detection
patterns = matcher.detect_patterns(data)
print(patterns.encryption_type)
print(patterns.encoding_layers)

# String Analysis
strings = string_analyzer.analyze_strings(decoded)
print(strings.entropy)
print(strings.patterns)
```

## 🛠️ Advanced Configuration

### Custom Pattern Detection
```python
matcher = PatternMatcher()
matcher.add_pattern('custom_pattern', r'your_regex_here')
matcher.add_encryption_signature('custom_enc', b'signature')
```

### Decoder Configuration
```python
decoder = LayeredDecoder(
    debug=True,
    max_depth=10,
    ignore_errors=False,
    analysis_mode='deep'
)
```

## 🔥 Performance Tips

### Optimization
```python
# Enable parallel processing
decoder = LayeredDecoder(parallel=True, workers=4)

# Use memory efficient mode
decoder.enable_memory_efficient()

# Enable caching
decoder.enable_cache(max_size=1000)
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/yourusername/gnazh.git
cd gnazh
pip install -e ".[dev]"
```

### Running Tests
```bash
pytest tests/
pytest tests/ --cov=gnazh
```

## 📈 Benchmarks

| Operation | Time (ms) | Memory (MB) |
|-----------|-----------|-------------|
| Simple Decode | 5 | 2.3 |
| Deep Analysis | 15 | 4.7 |
| Pattern Match | 3 | 1.2 |

## 🔐 Security

- ✅ Safe for production use
- ✅ Memory safe operations
- ✅ Input validation
- ✅ Error handling
- ✅ Resource cleanup

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

Special thanks to all contributors and the Python security community.

---

<div align="center">
  <sub>Built with ❤️ by Security Researchers for Security Researchers</sub>
</div>

from .core.advanced_decoder import AdvancedDecoder
from .core.pattern_matcher import PatternMatcher
from .core.bytecode_analyzer import BytecodeAnalyzer
from .core.string_analyzer import StringAnalyzer
from .core.encryption_handler import EncryptionHandler
from .utils.helpers import *
from .version import __version__

__all__ = [
    'AdvancedDecoder',
    'PatternMatcher',
    'BytecodeAnalyzer',
    'StringAnalyzer',
    'EncryptionHandler',
    'decode_file',
    'decode_string',
    'analyze_code',
    'detect_encryption',
    '__version__'
]

def decode_file(file_path: str, **kwargs):
    """Quick function to decode a file"""
    decoder = AdvancedDecoder(**kwargs)
    return decoder.decode_file(file_path)

def decode_string(data: str, **kwargs):
    """Quick function to decode a string"""
    decoder = AdvancedDecoder(**kwargs)
    return decoder.decode_data(data)

def analyze_code(code_obj, **kwargs):
    """Quick function to analyze code object"""
    analyzer = BytecodeAnalyzer(**kwargs)
    return analyzer.analyze(code_obj)

def detect_encryption(data: bytes, **kwargs):
    """Quick function to detect encryption type"""
    matcher = PatternMatcher(**kwargs)
    return matcher.detect_encryption(data)

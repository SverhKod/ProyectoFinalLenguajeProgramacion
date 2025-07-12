# braille/functional.py

from typing import List, Callable, Dict
from .core import ConversionResult, BrailleConverter

def create_batch_converter(converter: BrailleConverter) -> Callable[[List[str], str], List[ConversionResult]]:
    def batch_convert(texts: List[str], conversion_type: str) -> List[ConversionResult]:
        conversion_func = (converter.text_to_braille if conversion_type == 'text_to_braille'
                           else converter.braille_to_text)
        return list(map(conversion_func, texts))
    return batch_convert

def filter_successful_conversions(results: List[ConversionResult]) -> List[ConversionResult]:
    return list(filter(lambda result: result.success, results))

def analyze_conversion_patterns(results: List[ConversionResult]) -> Dict[str, float]:
    if not results:
        return {}
    from functools import reduce
    total_original = reduce(lambda acc, r: acc + r.stats['original_length'], results, 0)
    total_converted = reduce(lambda acc, r: acc + r.stats['converted_length'], results, 0)
    total_words = reduce(lambda acc, r: acc + r.stats['word_count'], results, 0)
    count = len(results)
    return {
        'average_original_length': total_original / count,
        'average_converted_length': total_converted / count,
        'average_word_count': total_words / count,
        'success_rate': len(filter_successful_conversions(results)) / count * 100
    }

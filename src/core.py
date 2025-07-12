# braille/core.py

from dataclasses import dataclass
from typing import List, Optional, Dict
import json
from .utils import BRAILLE_MAP, TEXT_MAP, normalize_text, validate_text_input, calculate_conversion_stats
from functools import reduce

@dataclass
class ConversionResult:
    original_text: str
    converted_text: str
    conversion_type: str
    stats: Dict[str, int]
    success: bool
    error_message: Optional[str] = None

class BrailleConverter:
    """Conversor principal que encapsula la lógica de conversión."""

    def __init__(self):
        self._braille_map = BRAILLE_MAP.copy()
        self._text_map = TEXT_MAP.copy()
        self._conversion_history: List[ConversionResult] = []
        self._error_count = 0

    def text_to_braille(self, text: str) -> ConversionResult:
        try:
            if not text:
                return ConversionResult(
                    original_text="", converted_text="",
                    conversion_type="text_to_braille",
                    stats=calculate_conversion_stats("", ""), success=True)
            normalized_text = normalize_text(text)
            if not validate_text_input(normalized_text):
                return ConversionResult(
                    original_text=text, converted_text="",
                    conversion_type="text_to_braille",
                    stats=calculate_conversion_stats(text, ""), success=False,
                    error_message="Texto contiene caracteres no soportados")
            braille_text = self._apply_conversion_mapping(normalized_text, self._braille_map)
            stats = calculate_conversion_stats(text, braille_text)
            result = ConversionResult(
                original_text=text, converted_text=braille_text,
                conversion_type="text_to_braille", stats=stats, success=True)
            self._conversion_history.append(result)
            return result
        except Exception as e:
            self._error_count += 1
            return ConversionResult(
                original_text=text, converted_text="",
                conversion_type="text_to_braille",
                stats=calculate_conversion_stats(text, ""), success=False,
                error_message=f"Error: {str(e)}")

    def braille_to_text(self, braille: str) -> ConversionResult:
        try:
            if not braille:
                return ConversionResult(
                    original_text="", converted_text="",
                    conversion_type="braille_to_text",
                    stats=calculate_conversion_stats("", ""), success=True)
            text = self._apply_conversion_mapping(braille, self._text_map)
            stats = calculate_conversion_stats(braille, text)
            result = ConversionResult(
                original_text=braille, converted_text=text,
                conversion_type="braille_to_text", stats=stats, success=True)
            self._conversion_history.append(result)
            return result
        except Exception as e:
            self._error_count += 1
            return ConversionResult(
                original_text=braille, converted_text="",
                conversion_type="braille_to_text",
                stats=calculate_conversion_stats(braille, ""), success=False,
                error_message=f"Error: {str(e)}")

    def _apply_conversion_mapping(self, text: str, mapping: dict) -> str:
        # Paradigma funcional
        return reduce(lambda acc, char: acc + mapping.get(char, char), text, "")

    def get_conversion_history(self) -> List[ConversionResult]:
        return self._conversion_history.copy()

    def get_statistics(self) -> Dict[str, int]:
        successful = sum(1 for result in self._conversion_history if result.success)
        return {
            'total_conversions': len(self._conversion_history),
            'successful_conversions': successful,
            'failed_conversions': self._error_count,
            'supported_characters': len(self._braille_map)
        }

    def export_history(self, filename: str) -> bool:
        try:
            data = [result.__dict__ for result in self._conversion_history]
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False

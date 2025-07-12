from src.core import ConversionResult, BrailleConverter
from src.functional import filter_successful_conversions, analyze_conversion_patterns, create_batch_converter
import sys

class BrailleConverterUI:
    def __init__(self):
        self.converter = BrailleConverter()
        self.batch_converter = create_batch_converter(self.converter)

    def display_menu(self):
        print("\n" + "="*50)
        print("     CONVERSOR BRAILLE-TEXTO MULTIPARADIGMA")
        print("="*50)
        print("1. Convertir Texto a Braille")
        print("2. Convertir Braille a Texto")
        print("3. Conversión en Lote")
        print("4. Ver Historial")
        print("5. Ver Estadísticas")
        print("6. Exportar Historial")
        print("7. Salir")
        print("="*50)

    def get_user_input(self, prompt):
        try:
            return input(prompt).strip()
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            sys.exit(0)
        except Exception:
            print("Error al leer entrada.")
            return ""

    def display_result(self, result):
        print("\n" + "-"*40)
        print(f"RESULTADO DE CONVERSIÓN")
        print("-"*40)
        print(f"Tipo: {result.conversion_type.replace('_', ' ').title()}")
        print(f"Original: {result.original_text}")
        print(f"Convertido: {result.converted_text}")
        if result.success:
            print(f"Estado: ✓ Exitosa")
            print(f"Estadísticas:")
            for key, value in result.stats.items():
                print(f"  - {key.replace('_', ' ').title()}: {value}")
        else:
            print(f"Estado: ✗ Fallida")
            print(f"Error: {result.error_message}")
        print("-"*40)

    def run_single_conversion(self, conversion_type):
        if conversion_type == "text_to_braille":
            text = self.get_user_input("Ingrese el texto a convertir: ")
            if text:
                result = self.converter.text_to_braille(text)
                self.display_result(result)
        else:
            braille = self.get_user_input("Ingrese el texto en Braille: ")
            if braille:
                result = self.converter.braille_to_text(braille)
                self.display_result(result)

    def run_batch_conversion(self):
        print("\nCONVERSIÓN EN LOTE")
        print("Ingrese los textos (uno por línea). Línea vacía para terminar:")
        texts = []
        while True:
            text = self.get_user_input("Texto: ")
            if not text:
                break
            texts.append(text)
        if not texts:
            print("No se ingresaron textos.")
            return
        conversion_type = self.get_user_input(
            "Tipo de conversión (1=texto a braille, 2=braille a texto): "
        )
        conv_type = ("text_to_braille" if conversion_type == "1" else "braille_to_text")
        results = self.batch_converter(texts, conv_type)
        print(f"\nRESULTADOS DE CONVERSIÓN EN LOTE ({len(results)} textos):")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result.original_text} → {result.converted_text}")
            if not result.success:
                print(f"   Error: {result.error_message}")

    def show_history(self):
        history = self.converter.get_conversion_history()
        if not history:
            print("\nNo hay conversiones en el historial.")
            return
        print(f"\nHISTORIAL DE CONVERSIONES ({len(history)} registros):")
        print("-"*60)
        for i, result in enumerate(history[-10:], 1):  # últimos 10
            status = "✓" if result.success else "✗"
            print(f"{i}. [{status}] {result.conversion_type}")
            print(f"   {result.original_text} → {result.converted_text}")

    def show_statistics(self):
        stats = self.converter.get_statistics()
        history = self.converter.get_conversion_history()
        print("\nESTADÍSTICAS DEL CONVERSOR:")
        print("-"*30)
        for key, value in stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        if history:
            patterns = analyze_conversion_patterns(history)
            print("\nPATRONES DE CONVERSIÓN:")
            for key, value in patterns.items():
                print(f"{key.replace('_', ' ').title()}: {value:.2f}")

    def export_history(self):
        filename = self.get_user_input("Nombre del archivo (sin extensión): ")
        if filename:
            filename += ".json"
            if self.converter.export_history(filename):
                print(f"Historial exportado a {filename}")
            else:
                print("Error al exportar el historial.")

    def run(self):
        print("¡Bienvenido al Conversor Braille-Texto Multiparadigma!")
        while True:
            self.display_menu()
            choice = self.get_user_input("Seleccione una opción (1-7): ")
            if choice == "1":
                self.run_single_conversion("text_to_braille")
            elif choice == "2":
                self.run_single_conversion("braille_to_text")
            elif choice == "3":
                self.run_batch_conversion()
            elif choice == "4":
                self.show_history()
            elif choice == "5":
                self.show_statistics()
            elif choice == "6":
                self.export_history()
            elif choice == "7":
                print("\n¡Gracias por usar el Conversor Braille-Texto!")
                break
            else:
                print("Opción no válida. Por favor, seleccione 1-7.")

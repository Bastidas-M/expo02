"""
Script principal para ejecutar la validación de requisitos de graduación.
"""
from src.generate_report import generate_graduation_csv_report

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Sistema de Validación de Requisitos de Graduación")
    print("================================================")
    
    # Generar el reporte CSV
    generate_graduation_csv_report()
    
    print("\nProceso completado.\n")

if __name__ == "__main__":
    main()
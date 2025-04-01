"""
Módulo para gestionar las conexiones a la base de datos.
En un entorno real, este módulo se conectaría a una base de datos.
Para pruebas unitarias, se utilizarán funciones simuladas.
"""

class DBConnector:
    """Clase para gestionar la conexión a la base de datos."""
    
    def __init__(self, connection_string=None):
        """
        Inicializa la conexión a la base de datos.
        
        Args:
            connection_string (str, optional): Cadena de conexión a la base de datos.
        """
        self.connection_string = connection_string
        # En un entorno real, aquí se inicializaría la conexión

    def check_student_enrollment(self, student_code):
        """
        Verifica si el estudiante está matriculado.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            bool: True si el estudiante está matriculado, False en caso contrario.
        """
        # En un entorno real, aquí habría una consulta a la base de datos
        # Para pruebas, se simula la respuesta
        from src.mock_data import get_student_data
        student_data = get_student_data(student_code)
        return student_data.get("enrollment", False)
    
    def get_student_average(self, student_code):
        """
        Obtiene el promedio académico del estudiante.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            float: Promedio académico del estudiante.
        """
        # En un entorno real, aquí habría una consulta a la base de datos
        # Para pruebas, se simula la respuesta
        from src.mock_data import get_student_data
        student_data = get_student_data(student_code)
        return student_data.get("average", 0.0)
    
    def check_university_welfare_status(self, student_code):
        """
        Verifica si el estudiante está a paz y salvo con Bienestar universitario.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            bool: True si el estudiante está a paz y salvo, False en caso contrario.
        """
        # En un entorno real, aquí habría una consulta a la base de datos
        # Para pruebas, se simula la respuesta
        from src.mock_data import get_student_data
        student_data = get_student_data(student_code)
        return student_data.get("welfare", False)
    
    def check_graduation_payment(self, student_code):
        """
        Verifica si el estudiante ha pagado los derechos de grado.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            bool: True si el estudiante ha pagado, False en caso contrario.
        """
        # En un entorno real, aquí habría una consulta a la base de datos
        # Para pruebas, se simula la respuesta
        from src.mock_data import get_student_data
        student_data = get_student_data(student_code)
        return student_data.get("payment", False)
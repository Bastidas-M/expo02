"""
Pruebas unitarias para el módulo de validación de requisitos de graduación.
"""
import pytest
from unittest.mock import Mock, patch
from src.validacion_grado import GraduationValidator

class TestGraduationValidator:
    """Clase para probar el validador de requisitos de graduación."""
    
    @pytest.fixture
    def mock_db_connector(self):
        """
        Fixture que proporciona un conector de base de datos simulado.
        
        Returns:
            Mock: Objeto mock para simular el conector de base de datos.
        """
        mock_db = Mock()
        return mock_db
    
    @pytest.fixture
    def validator(self, mock_db_connector):
        """
        Fixture que proporciona un validador con un conector de base de datos simulado.
        
        Args:
            mock_db_connector (Mock): Conector de base de datos simulado.
            
        Returns:
            GraduationValidator: Validador de requisitos de graduación.
        """
        return GraduationValidator(db_connector=mock_db_connector)
    
    def test_check_enrollment_true(self, validator, mock_db_connector):
        """
        Prueba que check_enrollment devuelve True cuando el estudiante está matriculado.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mock
        mock_db_connector.check_student_enrollment.return_value = True
        
        # Ejecutar
        result = validator.check_enrollment("12345")
        
        # Verificar
        assert result is True
        mock_db_connector.check_student_enrollment.assert_called_once_with("12345")
    
    def test_check_enrollment_false(self, validator, mock_db_connector):
        """
        Prueba que check_enrollment devuelve False cuando el estudiante no está matriculado.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mock
        mock_db_connector.check_student_enrollment.return_value = False
        
        # Ejecutar
        result = validator.check_enrollment("12345")
        
        # Verificar
        assert result is False
        mock_db_connector.check_student_enrollment.assert_called_once_with("12345")
    
    def test_check_academic_average_pass(self, validator, mock_db_connector):
        """
        Prueba que check_academic_average devuelve True cuando el promedio es suficiente.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mock
        mock_db_connector.get_student_average.return_value = 4.0
        
        # Ejecutar
        result = validator.check_academic_average("12345")
        
        # Verificar
        assert result is True
        mock_db_connector.get_student_average.assert_called_once_with("12345")
    
    def test_check_academic_average_fail(self, validator, mock_db_connector):
        """
        Prueba que check_academic_average devuelve False cuando el promedio es insuficiente.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mock
        mock_db_connector.get_student_average.return_value = 3.0
        
        # Ejecutar
        result = validator.check_academic_average("12345")
        
        # Verificar
        assert result is False
        mock_db_connector.get_student_average.assert_called_once_with("12345")
    
    def test_check_welfare_status_true(self, validator, mock_db_connector):
        """
        Prueba que check_welfare_status devuelve True cuando el estudiante está a paz y salvo.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mock
        mock_db_connector.check_university_welfare_status.return_value = True
        
        # Ejecutar
        result = validator.check_welfare_status("12345")
        
        # Verificar
        assert result is True
        mock_db_connector.check_university_welfare_status.assert_called_once_with("12345")
    
    def test_check_welfare_status_false(self, validator, mock_db_connector):
        """
        Prueba que check_welfare_status devuelve False cuando el estudiante no está a paz y salvo.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mock
        mock_db_connector.check_university_welfare_status.return_value = False
        
        # Ejecutar
        result = validator.check_welfare_status("12345")
        
        # Verificar
        assert result is False
        mock_db_connector.check_university_welfare_status.assert_called_once_with("12345")
    
    def test_check_payment_true(self, validator, mock_db_connector):
        """
        Prueba que check_payment devuelve True cuando el estudiante ha pagado.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mock
        mock_db_connector.check_graduation_payment.return_value = True
        
        # Ejecutar
        result = validator.check_payment("12345")
        
        # Verificar
        assert result is True
        mock_db_connector.check_graduation_payment.assert_called_once_with("12345")
    
    def test_check_payment_false(self, validator, mock_db_connector):
        """
        Prueba que check_payment devuelve False cuando el estudiante no ha pagado.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mock
        mock_db_connector.check_graduation_payment.return_value = False
        
        # Ejecutar
        result = validator.check_payment("12345")
        
        # Verificar
        assert result is False
        mock_db_connector.check_graduation_payment.assert_called_once_with("12345")
    
    def test_validate_graduation_requirements_all_pass(self, validator, mock_db_connector):
        """
        Prueba que validate_graduation_requirements devuelve True cuando se cumplen todos los requisitos.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mocks
        mock_db_connector.check_student_enrollment.return_value = True
        mock_db_connector.get_student_average.return_value = 4.0
        mock_db_connector.check_university_welfare_status.return_value = True
        mock_db_connector.check_graduation_payment.return_value = True
        
        # Ejecutar
        all_requirements_met, requirements = validator.validate_graduation_requirements("12345")
        
        # Verificar
        assert all_requirements_met is True
        assert requirements == {
            "matriculado": True,
            "promedio_minimo": True,
            "paz_y_salvo_bienestar": True,
            "derechos_de_grado_pagados": True
        }
    
    def test_validate_graduation_requirements_some_fail(self, validator, mock_db_connector):
        """
        Prueba que validate_graduation_requirements devuelve False cuando no se cumplen todos los requisitos.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mocks
        mock_db_connector.check_student_enrollment.return_value = True
        mock_db_connector.get_student_average.return_value = 3.0  # Por debajo del mínimo
        mock_db_connector.check_university_welfare_status.return_value = True
        mock_db_connector.check_graduation_payment.return_value = False  # No ha pagado
        
        # Ejecutar
        all_requirements_met, requirements = validator.validate_graduation_requirements("12345")
        
        # Verificar
        assert all_requirements_met is False
        assert requirements == {
            "matriculado": True,
            "promedio_minimo": False,
            "paz_y_salvo_bienestar": True,
            "derechos_de_grado_pagados": False
        }
    
    def test_generate_graduation_report_pass(self, validator, mock_db_connector):
        """
        Prueba que generate_graduation_report devuelve un mensaje de éxito cuando se cumplen todos los requisitos.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mocks
        mock_db_connector.check_student_enrollment.return_value = True
        mock_db_connector.get_student_average.return_value = 4.0
        mock_db_connector.check_university_welfare_status.return_value = True
        mock_db_connector.check_graduation_payment.return_value = True
        
        # Ejecutar
        report = validator.generate_graduation_report("12345")
        
        # Verificar
        assert "CUMPLE con todos los requisitos" in report
        assert "Matriculado: CUMPLE" in report
        assert "Promedio Minimo: CUMPLE" in report
        assert "Paz Y Salvo Bienestar: CUMPLE" in report
        assert "Derechos De Grado Pagados: CUMPLE" in report
    
    def test_generate_graduation_report_fail(self, validator, mock_db_connector):
        """
        Prueba que generate_graduation_report devuelve un mensaje de fallo cuando no se cumplen todos los requisitos.
        
        Args:
            validator (GraduationValidator): Validador de requisitos de graduación.
            mock_db_connector (Mock): Conector de base de datos simulado.
        """
        # Configurar mocks
        mock_db_connector.check_student_enrollment.return_value = False
        mock_db_connector.get_student_average.return_value = 3.0
        mock_db_connector.check_university_welfare_status.return_value = True
        mock_db_connector.check_graduation_payment.return_value = True
        
        # Ejecutar
        report = validator.generate_graduation_report("12345")
        
        # Verificar
        assert "NO CUMPLE con todos los requisitos" in report
        assert "Matriculado: NO CUMPLE" in report
        assert "Promedio Minimo: NO CUMPLE" in report
        assert "Paz Y Salvo Bienestar: CUMPLE" in report
        assert "Derechos De Grado Pagados: CUMPLE" in report
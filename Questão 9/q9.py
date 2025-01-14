import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# URL da página
URL = "https://www.vanilton.net/triangulo/#"

@pytest.fixture(scope="module")
def driver():
    options = Options()  
    service = Service('/usr/bin/chromedriver')  # Configurar o caminho do ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)  
    driver.implicitly_wait(3)  
    yield driver
    driver.quit() 

def preencher_campos(driver, vertice1, vertice2, vertice3):
    driver.get(URL)
    driver.find_element(By.NAME, "V1").clear()
    driver.find_element(By.NAME, "V2").clear()
    driver.find_element(By.NAME, "V3").clear()
    driver.find_element(By.NAME, "V1").send_keys(vertice1)
    driver.find_element(By.NAME, "V2").send_keys(vertice2)
    driver.find_element(By.NAME, "V3").send_keys(vertice3)
    driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

@pytest.mark.parametrize(
    "vertice1, vertice2, vertice3, expected_message", 
    [
   pytest.param ("5", "5", "5", "Equilátero", id="Triangulo Equilatero"),
   pytest.param ("5", "5", "3", "Isósceles", id="Triangulo Isosceles"),
   pytest.param ("5", "6", "7", "Escaleno", id="Triangulo Escaleno"),
   pytest.param ("1", "2", "10", "Os valores não formam um triângulo.", id="Valores invalido para um triangulo"),
   pytest.param ("", "5", "6", "Todos os campos devem ser preenchidos.", id="Vertice 1 vazio"),
   pytest.param ("5", "", "6", "Todos os campos devem ser preenchidos.", id="Vertice 2 vazio"),
   pytest.param ("5", "6", "", "Todos os campos devem ser preenchidos.", id="Vertice 3 vazio"),
   pytest.param ("A", "5", "6", "Todos os valores devem ser números.", id="Entrada nao numerica - letras"),
   pytest.param ("@", "5", "6", "Todos os valores devem ser números.", id="Entrada nao numerica - caracteres especiais"),
   pytest.param ("-3", "5", "6", "Os valores devem ser números positivos.", id="Entrada valor negativo"),
   pytest.param ("0", "5", "6", "Os valores devem ser maiores que zero.", id="Entrada zero"),
   pytest.param ("2", "2", "3", "Isósceles", id="Entrada limite minimo"),
   pytest.param ("1", "1", "1", "Os valores não formam um triângulo.", id="Todas as entradas igual a 1"),
   pytest.param (" 5 ", "6", " 7 ", "Escaleno", id="Entradas com espaços"),
    ])

def test_triangles(driver, vertice1, vertice2, vertice3, expected_message):
    preencher_campos(driver, vertice1, vertice2, vertice3)
    result = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(7)").text 
    assert result == expected_message
    

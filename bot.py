from selenium import webdriver
import time

# Configuración del navegador
driver = webdriver.Chrome()

# Número de veces que se abrira la pagina
for i in range(100):
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    driver.get("https://portal.senasofiaplus.edu.co/")
    
    print(f"Acceso número {i+1}")
    time.sleep(2)  # Esperar 2 segundos entre accesos

driver.quit()
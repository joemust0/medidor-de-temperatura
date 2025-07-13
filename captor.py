from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def buscar_dados():
    servico = Service(executable_path="chromedriver.exe")
    opcoes = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=servico, options=opcoes)

    try:
        driver.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp")
        wait = WebDriverWait(driver, 10)

        # Temperatura
        temperatura_elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "temperature__value")))
        temperatura = temperatura_elem.text.strip()

        # Umidade com XPath corrigido
        umidade_elem = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[7]/div[3]/div[1]/div[2]/div[2]/div[3]/div[1]/ul/li[4]/div/p")
        ))
        umidade = umidade_elem.text.strip()

        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        try:
            workbook = openpyxl.load_workbook("temperatura_sp.xlsx")
            sheet = workbook.active
        except FileNotFoundError:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["Data/Hora", "Temperatura", "Umidade"])

        sheet.append([agora, temperatura, umidade])
        workbook.save("temperatura_sp.xlsx")

        messagebox.showinfo("Sucesso", f"Dados salvos com sucesso!\nTemperatura: {temperatura}\nUmidade: {umidade}")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")
    
    finally:
        driver.quit()

# Interface
janela = tk.Tk()
janela.title("Captador de Temperatura - São Paulo")

botao = tk.Button(janela, text="Buscar previsão", command=buscar_dados, font=("Arial", 12), bg="lightblue", padx=20, pady=10)
botao.pack(pady=40)

janela.mainloop()
 
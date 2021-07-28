from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, database

class StatusInvest:
    def __init__(self):
        self.root = os.getcwd()
        self.chrome = webdriver.Chrome(executable_path= self.root + r'\chromedriver.exe')      
        self.infos_ativo = {}
        self.db = database.DatabaseSQL()

    def navigate(self,link):
        time.sleep(1)
        self.chrome.maximize_window()
        if "https://" not in link:
            link = "https://" + link
        self.chrome.get(link)

    def fecha_popup_instatus_invest(self):
        popup_fechado = False
        count_popup = 0

        while True:
            close_popup = self.chrome.execute_script('return document.querySelector("body > div.popup-fixed > div > div > div.text-right > button")')
            if close_popup != None:
                close_popup = self.chrome.execute_script('return document.querySelector("body > div.popup-fixed > div > div > div.text-right > button").click()')
                print(f'{count_popup.__round__(3)} seg para fechar o popup!')
                break
            count_popup += 0.001
            time.sleep(0.001)

    def get_data_from_status_invest(self):
        self.chrome.get("https://statusinvest.com.br/indices/ifix")
        aguarda_carregamento = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[1]/div[2]/div[1]/div/div/strong")))
        
        qtd_ativos_na_lista = self.chrome.execute_script('return document.getElementsByClassName("main-list")[0].getElementsByClassName("item  d-flex justify-between align-items-center ").length')
        qtd_ativos_na_lista -= 2 #desconta cabeçalho e rodapé da tabela
        
        for linha in range(1,qtd_ativos_na_lista + 1):
            ativo  = self.chrome.execute_script(f'return document.getElementsByClassName("main-list")[0].getElementsByClassName("item  d-flex justify-between align-items-center ")[{linha}].getElementsByClassName("ticker")[0].innerText')
            self.infos_ativo[ativo] = {}
            self.infos_ativo[ativo]["nome_ativo"] = self.chrome.execute_script(f'return document.getElementsByClassName("main-list")[0].getElementsByClassName("item  d-flex justify-between align-items-center ")[{linha}].getElementsByClassName("w-100")[0].innerText')
            self.infos_ativo[ativo]["setor_ativo"] = self.chrome.execute_script(f'return document.getElementsByClassName("main-list")[0].getElementsByClassName("item  d-flex justify-between align-items-center ")[{linha}].getElementsByClassName("d-block w-30 pb-1 pt-1 text-main waves-effect waves-on-white-bg  pl-1")[0].innerText')
            self.infos_ativo[ativo]["qtde_teorica"] = self.chrome.execute_script(f'return document.getElementsByClassName("main-list")[0].getElementsByClassName("item  d-flex justify-between align-items-center ")[{linha}].getElementsByClassName("quantity w-15 text-right pr-2")[0].innerText')
            self.infos_ativo[ativo]["participacao_ifix"] = self.chrome.execute_script(f'return document.getElementsByClassName("main-list")[0].getElementsByClassName("item  d-flex justify-between align-items-center ")[{linha}].getElementsByClassName("fw-700")[0].innerText')
        
        i = 1
        for ativo in self.infos_ativo.keys():
            database = "statusinvest"
            arr_tables = self.db.show_tables(database_name=database)
            
            if not any(ativo.lower() in table for table in arr_tables):
                print(f"Ativo : {ativo} adicionado ao database : {database}")
                self.db.create_table(table_name=ativo)
          
            self.chrome.get("https://statusinvest.com.br/fundos-imobiliarios/" + ativo)
            
            xpath={
                "valor_atual"       :"/html/body/main/div[2]/div[1]/div[1]/div/div[1]/strong",
                "ult_rend"          :"/html/body/main/div[2]/div[7]/div[2]/div/div[1]/strong",
                "min_52"            :"/html/body/main/div[2]/div[1]/div[2]/div/div[1]/strong",
                "max_52"            :"/html/body/main/div[2]/div[1]/div[3]/div/div[1]/strong",
                "dividend_yeld"     :"/html/body/main/div[2]/div[1]/div[4]/div/div[1]/strong",
                "valorizacao_12m"   :"/html/body/main/div[2]/div[1]/div[5]/div/div[1]/strong",
                "valor_patr_por_cota":"/html/body/main/div[2]/div[5]/div/div[1]/div/div[1]/strong",
                "valor_em_caixa"    :"/html/body/main/div[2]/div[5]/div/div[3]/div/div[1]/strong",
                "p_vp"              :"/html/body/main/div[2]/div[5]/div/div[2]/div/div[1]/strong",
                "num_cotistas"      :"/html/body/main/div[2]/div[5]/div/div[6]/div/div[1]/strong"
            }
            aguarda_carregamento = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.XPATH, xpath["ult_rend"])))
            
            self.infos_ativo[ativo]["ticker"] = ativo
            self.infos_ativo[ativo]["valor_atual"] = self.chrome.find_element_by_xpath(xpath["valor_atual"]).text
            self.infos_ativo[ativo]["ult_rend"] = self.chrome.find_element_by_xpath(xpath["ult_rend"]).text
            self.infos_ativo[ativo]["min_52"] = self.chrome.find_element_by_xpath(xpath["min_52"]).text
            self.infos_ativo[ativo]["max_52"] = self.chrome.find_element_by_xpath(xpath["max_52"]).text
            self.infos_ativo[ativo]["dividend_yeld"] = self.chrome.find_element_by_xpath(xpath["dividend_yeld"]).text
            self.infos_ativo[ativo]["valorizacao_12m"] = self.chrome.find_element_by_xpath(xpath["valorizacao_12m"]).text
            self.infos_ativo[ativo]["valor_patr_por_cota"] = self.chrome.find_element_by_xpath(xpath["valor_patr_por_cota"]).text    
            self.infos_ativo[ativo]["valor_em_caixa"] = self.chrome.find_element_by_xpath(xpath["valor_em_caixa"]).text
            self.infos_ativo[ativo]["p_vp"] = self.chrome.find_element_by_xpath(xpath["p_vp"]).text
            self.infos_ativo[ativo]["num_cotistas"] = self.chrome.find_element_by_xpath(xpath["num_cotistas"]).text
            self.infos_ativo[ativo]["atualizado_em"] = str(time.asctime())
            print(f'\nLinha {i} - {self.infos_ativo[ativo]}')
            i = i + 1
                                 
    def get_root(self):
        print(self.root)
     
    def get_infos_ativo(self):
        for ativo in self.infos_ativo.keys():
            floats = ["valor_atual", "participacao_ifix", "ult_rend", "min_52", "max_52", "dividend_yeld", "valorizacao_12m", "valor_patr_por_cota", "valor_em_caixa", "p_vp"]
            ints = ["num_cotistas", "qtde_teorica"]
            for key in self.infos_ativo[ativo].keys():
                # floats
                if key in floats:
                    self.infos_ativo[ativo][key] = float(self.infos_ativo[ativo][key].replace(".","").replace("-","0").replace(" ","").replace(",",".").replace("%",""))
                # ints
                if key in ints:
                    self.infos_ativo[ativo][key] = int(self.infos_ativo[ativo][key].replace("-","0").replace(" ","").replace(".","")) 
            
        return self.infos_ativo



        
        
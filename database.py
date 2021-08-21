import mysql.connector

class DatabaseSQL:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="testuser", passwd="SuaSenha")
        self.cursor = self.mydb.cursor()
    
    def create_database(self,database_name):
        self.cursor.execute(f"create database {database_name}")

    def show_databases(self):
        self.cursor.execute("show databases")
        for db in self.cursor:
            print(db)

    def show_tables(self,database_name="statusinvest"):
        """Devolve um array, contendo todas as tabelas existentes no database pesquisado"""
        
        self.mydb = mysql.connector.connect(host="localhost", user="testuser", passwd="SuaSenha", database=database_name)
        self.cursor = self.mydb.cursor()
        self.cursor.execute(f"show tables")
        arr_tables = []
        for table in self.cursor:
            arr_tables.append(table)
        return arr_tables

    def create_table(self, database_name="statusinvest", table_name="teste"):
        self.mydb = mysql.connector.connect(host="localhost", user="testuser", passwd="SuaSenha", database=database_name)
        self.cursor = self.mydb.cursor()
        self.cursor.execute(f"create table {table_name} (ticker varchar(10), \
                                                        valor_atual float(8), \
                                                        nome_ativo varchar(250), \
                                                        setor_ativo varchar(250), \
                                                        qtde_teorica int(15), \
                                                        participacao_ifix float(15), \
                                                        ult_rend float(15), \
                                                        min_52 float(15), \
                                                        max_52 float(15), \
                                                        dividend_yeld float(15), \
                                                        valorizacao_12m float(15), \
                                                        valor_patr_por_cota float(15), \
                                                        valor_em_caixa float(15), \
                                                        p_vp float(15), \
                                                        num_cotistas int(15), \
                                                        atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP)")
        
        print(f'Tabela "{table_name}" criada no db "{database_name}"')
    
    def insert_into(self, data, database_name="statusinvest"):
        self.mydb = mysql.connector.connect(host="localhost", user="testuser", passwd="SuaSenha", database=database_name)
        self.cursor = self.mydb.cursor()
        
        try:
            self.cursor.execute('DELETE * FROM geral')
        except:
            print('Não haviam dados salvos na table geral')
        
        arr_infos_ativo = []

        infos_ativo = data
        for ativo in infos_ativo.keys():
            ticker = infos_ativo[ativo]["ticker"]       
            valor_atual = infos_ativo[ativo]["valor_atual"]  
            nome_ativo = infos_ativo[ativo]["nome_ativo"]   
            setor_ativo = infos_ativo[ativo]["setor_ativo"]  
            qtde_teorica = infos_ativo[ativo]["qtde_teorica"] 
            participacao_ifix = infos_ativo[ativo]["participacao_ifix"] 
            ult_rend = infos_ativo[ativo]["ult_rend"]     
            min_52 = infos_ativo[ativo]["min_52"]       
            max_52 = infos_ativo[ativo]["max_52"]       
            dividend_yeld = infos_ativo[ativo]["dividend_yeld"] 
            valorizacao_12m = infos_ativo[ativo]["valorizacao_12m"] 
            valor_patr_por_cota = infos_ativo[ativo]["valor_patr_por_cota"] 
            valor_em_caixa = infos_ativo[ativo]["valor_em_caixa"] 
            p_vp = infos_ativo[ativo]["p_vp"]         
            num_cotistas = infos_ativo[ativo]["num_cotistas"] 

            tup = (ticker, valor_atual, nome_ativo, setor_ativo, qtde_teorica, participacao_ifix, ult_rend, min_52, max_52, dividend_yeld, valorizacao_12m, valor_patr_por_cota, valor_em_caixa, p_vp, num_cotistas)
            arr_infos_ativo.append(tup)
            
            print(f'len(arr_infos_ativo) : {len(arr_infos_ativo)}')
            sqlform1 = f'Insert into {ativo} (ticker, valor_atual, nome_ativo, setor_ativo, qtde_teorica, participacao_ifix, ult_rend, min_52, max_52, dividend_yeld, valorizacao_12m, valor_patr_por_cota, valor_em_caixa, p_vp, num_cotistas) values{tup}'
            sqlform2 = f'Insert into geral (ticker, valor_atual, nome_ativo, setor_ativo, qtde_teorica, participacao_ifix, ult_rend, min_52, max_52, dividend_yeld, valorizacao_12m, valor_patr_por_cota, valor_em_caixa, p_vp, num_cotistas) values{tup}'
            self.cursor.execute(sqlform1)
            self.cursor.execute(sqlform2)
            self.mydb.commit()

        print('Dados savos!')

    def insert_into__teste(self, database_name="statusinvest"):
        self.mydb = mysql.connector.connect(host="localhost", user="testuser", passwd="SuaSenha", database=database_name)
        self.cursor = self.mydb.cursor()
        
        ticker = "teste"       
        valor_atual = 1  
        nome_ativo = "teste"   
        setor_ativo = "teste"  
        qtde_teorica = 1
        participacao_ifix = 1 
        ult_rend = 1     
        min_52 = 1       
        max_52 = 1       
        dividend_yeld = 1
        valorizacao_12m = 1
        valor_patr_por_cota = 1
        valor_em_caixa = 1
        p_vp = 1         
        num_cotistas = 1 
        
        tup = (ticker, valor_atual, nome_ativo, setor_ativo, qtde_teorica, participacao_ifix, ult_rend, min_52, max_52, dividend_yeld, valorizacao_12m, valor_patr_por_cota, valor_em_caixa, p_vp, num_cotistas)
        sqlform = f'Insert into teste (ticker, valor_atual, nome_ativo, setor_ativo, qtde_teorica, participacao_ifix, ult_rend, min_52, max_52, dividend_yeld, valorizacao_12m, valor_patr_por_cota, valor_em_caixa, p_vp, num_cotistas) values{tup}'
        self.cursor.execute(sqlform)
        self.mydb.commit()

        print('Dados savos!')

    def get_top10_from_database(self, database_name="statusinvest"):
        """Param: database_name (str)
            
            Retorna um dicionario com as chaves:
            - mais_valorizadas 
            - mais_desvalorizadas
            - maiores_dy
            - menores_preco_ativo
            
            Cada chave contém:
            - ticker
            - valor_atual
            - nome_ativo
            - setor_ativo
            - qtde_teorica
            - participacao_ifix
            - ult_rend
            - min_52
            - max_52
            - dividend_yeld
            - valorizacao_12m
            - valor_patr_por_cota
            - valor_em_caixa
            - p_vp
            - num_cotistas
        """
        self.mydb = mysql.connector.connect(host="localhost", user="testuser", passwd="Chupetinha202", database=database_name)
        self.cursor = self.mydb.cursor()
        top10 = {}
        top10["mais_valorizadas"] = {}
        top10["mais_desvalorizadas"] = {}
        top10["maiores_dy"] = {}
        top10["menores_preco_ativo"] = {}

        for ranking in top10.keys():
            if ranking == "mais_valorizadas":
                self.cursor.execute(f"select * from geral order by valorizacao_12m desc limit 10")
                
            elif ranking == "mais_desvalorizadas":
                self.cursor.execute(f"select * from geral order by valorizacao_12m asc limit 10")
                
            elif ranking == "maiores_dy":
                self.cursor.execute(f"select * from geral order by dividend_yeld desc limit 10")
                
            elif ranking == "menores_preco_ativo":
                self.cursor.execute(f"select * from geral order by p_vp asc limit 10")

            retorno_db = self.cursor.fetchall()
            
            for item in retorno_db:
                ticker = item[0]     
                top10[ranking][ticker] = {}             
                top10[ranking][ticker]["ticker"] = ticker
                top10[ranking][ticker]["valor_atual"] = item[1]
                top10[ranking][ticker]["nome_ativo"] = item[2]
                top10[ranking][ticker]["setor_ativo"] = item[3]
                top10[ranking][ticker]["qtde_teorica"] = item[4]
                top10[ranking][ticker]["participacao_ifix"] = item[5]
                top10[ranking][ticker]["ult_rend"] = item[6]
                top10[ranking][ticker]["min_52"] = item[7]
                top10[ranking][ticker]["max_52"] = item[8]
                top10[ranking][ticker]["dividend_yeld"] = item[9]
                top10[ranking][ticker]["valorizacao_12m"] = item[10]
                top10[ranking][ticker]["valor_patr_por_cota"] = item[11]
                top10[ranking][ticker]["valor_em_caixa"] = item[12]
                top10[ranking][ticker]["p_vp"] = item[13]
                top10[ranking][ticker]["num_cotistas"] = item[14]
        
        return top10        

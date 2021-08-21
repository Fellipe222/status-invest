from functions import StatusInvest
from database import DatabaseSQL

status_invest = StatusInvest()

status_invest.navigate("https://statusinvest.com.br/fundos-imobiliarios")
status_invest.fecha_popup_instatus_invest()
status_invest.get_data_from_status_invest()

infos_ativo = status_invest.get_infos_ativo()

db = DatabaseSQL()
db.insert_into(infos_ativo,"statusinvest")

top10 = db.get_top10_from_database()

destinatarios = ["email1@email.com","email2@email.com"]
email = SendEmail("Um título bacana", destinatarios)
email.build_email(top10)
email.enviar_email()



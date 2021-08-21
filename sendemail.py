import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:
    def __init__(self, assunto:str,destinatarios:list):
        self.host = "smtp.gmail.com"
        self.port = 587
        self.username = "seu email"
        self.password = "sua senha"
        self.mail_to = destinatarios

        self.email_conect = smtplib.SMTP(self.host, self.port)
        self.email_conect.ehlo()
        self.email_conect.starttls()
        self.email_conect.login(self.username, self.password)

        self.html_text = ""

        self.msg = MIMEMultipart("alternative")
        self.msg["Subject"] = assunto
        self.msg["From"] = self.username

    def build_email(self, top10):

        mais_valorizadas = f"""
            <table>
            <tbody>
            <tr height="20" style="height:15pt">
              <td height="20" width="64" style="height:15pt;width:48pt;text-align:center;border-top:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;</td>
              <td width="61" style="border-left:none;width:46pt;color:white;font-weight:700;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">Ticker</td>
              <td width="162" style="border-left:none;width:122pt;color:white;font-weight:700;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap"><span zeum4c1="PR_13_0" data-ddnwab="PR_13_0" aria-invalid="spelling" class="LI ng">Valorizacao</span> <span zeum4c1="PR_14_0" data-ddnwab="PR_14_0" aria-invalid="grammar" class="Lm ng">ult</span>
              12m</td>
              <td width="98" style="border-left:none;width:74pt;color:white;font-weight:700;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">Nome ativo</td>
              <td width="100" style="border-left:none;width:75pt;color:white;font-weight:700;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">Valor atual</td>
              <td width="35" style="border-left:none;width:26pt;color:white;font-weight:700;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">DY</td>
              <td width="52" style="border-left:none;width:39pt;color:white;font-weight:700;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">P/VP</td>
              <td width="162" style="border-left:none;width:122pt;color:white;font-weight:700;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">Valor patr por cota</td>
             </tr>
            """
        mais_desvalorizadas = f"""
            <table>
            <tbody>
            <tr height="20" style="height:15pt">
              <td height="20" width="64" style="height: 15pt; width: 48pt; text-align: center; border-top: none; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-left: none; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-top: initial; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-color="">&nbsp;</td>
              <td width="61" style="border-left: none; width: 46pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Ticker</td>
              <td width="162" style="border-left: none; width: 122pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""><span zeum4c1="PR_19_0" data-ddnwab="PR_19_0" aria-invalid="spelling" class="LI ng">Valorizacao</span> <span zeum4c1="PR_20_0" data-ddnwab="PR_20_0" aria-invalid="grammar" class="Lm ng">ult</span>
              12m</td>
              <td width="98" style="border-left: none; width: 74pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Nome ativo</td>
              <td width="100" style="border-left: none; width: 75pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">&nbsp;Valor atua<br></td>
              <td width="35" style="border-left: none; width: 26pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">DY</td>
              <td width="52" style="border-left: none; width: 39pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">P/VP</td>
              <td width="162" style="border-left: none; width: 122pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Valor patr por
              cota</td>
            </tr>
            """
        maiores_dy = f"""
            <table>
            <tbody>
            <tr height="20" style="height:15pt">
              <td height="20" width="64" style="height: 15pt; width: 48pt; text-align: center; border-top: none; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-left: none; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-top: initial; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-color="">&nbsp;</td>
              <td width="61" style="border-left: none; width: 46pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Ticker</td>
              <td width="35" style="border-left: none; width: 26pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">DY</td>
              <td width="98" style="border-left: none; width: 74pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Valor atual</td>
              <td width="100" style="border-left: none; width: 75pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Nome ativo</td>
              <td width="168" style="border-left: none; width: 126pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""><span zeum4c1="PR_21_0" data-ddnwab="PR_21_0" aria-invalid="spelling" class="LI ng">Valorizacao</span> <span zeum4c1="PR_22_0" data-ddnwab="PR_22_0" aria-invalid="grammar" class="Lm ng">ult</span>
              12m</td>
              <td width="52" style="border-left: none; width: 39pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">P/VP</td>
              <td width="162" style="border-left: none; width: 122pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Valor patr por
              cota</td>
             </tr>
            """
        menores_preco_ativo = f"""
            <table>
            <tbody>
            <tr height="20" style="height:15pt">
              <td height="20" width="64" style="height: 15pt; width: 48pt; text-align: center; border-top: none; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-left: none; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-top: initial; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-color="">&nbsp;</td>
              <td width="61" style="border-left: none; width: 46pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Ticker</td>
              <td width="162" style="border-left: none; width: 122pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Valor patr por
              cota</td>
              <td width="100" style="border-left: none; width: 75pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Nome ativo</td>
              <td width="35" style="border-left: none; width: 26pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">DY</td>
              <td width="98" style="border-left: none; width: 74pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Valor atual</td>
              <td width="168" style="border-left: none; width: 126pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""><span zeum4c1="PR_23_0" data-ddnwab="PR_23_0" aria-invalid="spelling" class="LI ng">Valorizacao</span> <span zeum4c1="PR_24_0" data-ddnwab="PR_24_0" aria-invalid="grammar" class="Lm ng">ult</span>
              12m</td>
              <td width="52" style="border-left: none; width: 39pt; color: white; font-weight: 700; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; background: rgb(48, 84, 150); padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap; --darkreader-inline-border-left: initial; --darkreader-inline-color:#e8e6e3; --darkreader-inline-border-top:#8c8273; --darkreader-inline-border-right:#8c8273; --darkreader-inline-border-bottom:#8c8273; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#264378;" data-darkreader-inline-border-left="" data-darkreader-inline-color="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">P/VP</td>
             </tr>
            """

        for ranking in top10.keys():
            cont = 1
            if ranking == "mais_valorizadas":
                for ativo in top10["mais_valorizadas"].keys():
                    msg = f"""
                            <tr height="20" style="height:15pt">
                                <td height="20" style="height:15pt;border-top:none;color:white;font-weight:700;text-align:center;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">{cont}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;<a href="https://statusinvest.com.br/fundos-imobiliarios/{ativo}">{top10["mais_valorizadas"][ativo]["ticker"]}</a></td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["mais_valorizadas"][ativo]["valorizacao_12m"]} % </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["mais_valorizadas"][ativo]["nome_ativo"]} </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;R$ {top10["mais_valorizadas"][ativo]["valor_atual"]} </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["mais_valorizadas"][ativo]["dividend_yeld"]} % </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["mais_valorizadas"][ativo]["p_vp"]} </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;R$ {top10["mais_valorizadas"][ativo]["valor_patr_por_cota"]} </td>
                            </tr>"""
                    mais_valorizadas += msg
                    cont += 1
                mais_valorizadas += "</tbody></table>"

            elif ranking == "mais_desvalorizadas":
                for ativo in top10["mais_desvalorizadas"].keys():
                    msg = f"""
                            <tr height="20" style="height:15pt">
                                <td height="20" style="height:15pt;border-top:none;color:white;font-weight:700;text-align:center;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">{cont}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;<a href="https://statusinvest.com.br/fundos-imobiliarios/{ativo}">{top10["mais_desvalorizadas"][ativo]["ticker"]}</a></td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["mais_desvalorizadas"][ativo]["valorizacao_12m"]} % </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["mais_desvalorizadas"][ativo]["nome_ativo"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;R$ {top10["mais_desvalorizadas"][ativo]["valor_atual"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["mais_desvalorizadas"][ativo]["dividend_yeld"]} % </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["mais_desvalorizadas"][ativo]["p_vp"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;R$ {top10["mais_desvalorizadas"][ativo]["valor_patr_por_cota"]}</td>
                            </tr>"""
                    mais_desvalorizadas += msg
                    cont += 1
                mais_desvalorizadas += "</tbody></table>"

            elif ranking == "maiores_dy":
                for ativo in top10["maiores_dy"].keys():
                    msg = f"""
                            <tr height="20" style="height:15pt">
                                <td height="20" style="height:15pt;border-top:none;color:white;font-weight:700;text-align:center;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">{cont}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;<a href="https://statusinvest.com.br/fundos-imobiliarios/{ativo}">{top10["maiores_dy"][ativo]["ticker"]}</a></td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["maiores_dy"][ativo]["dividend_yeld"]} % </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;R$ {top10["maiores_dy"][ativo]["valor_atual"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["maiores_dy"][ativo]["nome_ativo"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["maiores_dy"][ativo]["valorizacao_12m"]} % </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["maiores_dy"][ativo]["p_vp"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;R$ {top10["maiores_dy"][ativo]["valor_patr_por_cota"]}</td>
                            </tr>"""
                    maiores_dy += msg
                    cont += 1
                maiores_dy += "</tbody></table>"

            elif ranking == "menores_preco_ativo":
                for ativo in top10["menores_preco_ativo"].keys():
                    msg = f"""
                            <tr height="20" style="height:15pt">
                                <td height="20" style="height:15pt;border-top:none;color:white;font-weight:700;text-align:center;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:0.5pt solid windowtext;background:rgb(48,84,150);padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">{cont}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;<a href="https://statusinvest.com.br/fundos-imobiliarios/{ativo}">{top10["menores_preco_ativo"][ativo]["ticker"]}</a></td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;R$ {top10["menores_preco_ativo"][ativo]["valor_patr_por_cota"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["menores_preco_ativo"][ativo]["nome_ativo"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["menores_preco_ativo"][ativo]["dividend_yeld"]} % </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;R$ {top10["menores_preco_ativo"][ativo]["valor_atual"]}</td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["menores_preco_ativo"][ativo]["valorizacao_12m"]} % </td>
                                <td style="border-top:none;border-left:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;padding-top:1px;padding-right:1px;padding-left:1px;color:black;font-size:11pt;font-family:Calibri,sans-serif;vertical-align:bottom;white-space:nowrap">&nbsp;{top10["menores_preco_ativo"][ativo]["p_vp"]}</td>
                            </tr>"""
                    menores_preco_ativo += msg
                    cont += 1
                menores_preco_ativo += "</tbody></table>"

        self.html_text = f"""
            <div>
                Veja o top 10 dos FIIs desta semana!
                <div>
                    <br>
                </div>
                <div>
                    <ul>
                        <li> 
                            As mais <span style="background-color: rgb(0, 255, 0);">valorizadas:</span>
                        </li>
                    </ul>
                    <div>
                        {mais_valorizadas}                    
                        <br>
                    </div>
                    <ul>
                        <li>
                            As mais <span style="background-color: rgb(234, 153, 153);">desvalorizadas:</span>
                        </li>
                    </ul>
                    <div>
                        {mais_desvalorizadas}
                        <br>
                    </div>
                    <ul>
                        <li>
                            Os maiores<b> dividend yields:</b>
                        </li>
                    </ul>
                    <div>
                        {maiores_dy}
                        <br>
                    </div>
                    <ul>
                        <li>
                            As com os menores&nbsp;<b>preco/ativo</b>:
                        </li>
                    </ul>
                    <div>
                        {menores_preco_ativo}
                        <br>
                    </div>
                </div>
            </div>
        """

    def enviar_email(self):
        self.msg.attach(MIMEText(self.html_text, "html"))
        self.email_conect.sendmail(self.username, self.mail_to, self.msg.as_string())
        self.email_conect.quit()
        print("Email enviado!")





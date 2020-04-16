import smtplib     
from email.MIMEText import MIMEText 

emisor = "mikeservices199@gmail.com" #Email para enviar 
receptor = "mikecardona076@gmail.com" #Email para recibir 

# Configuracion del mail 
mensaje = MIMEText("Este correo ha sido enviado desde Python") 
mensaje['From']=emisor 
mensaje['To']=receptor 
mensaje['Subject']="Mi primer correo desde Python" 

# Nos conectamos al servidor SMTP de Gmail 
serverSMTP = smtplib.SMTP('smtp.gmail.com',587) 
serverSMTP.ehlo() 
serverSMTP.starttls() 
serverSMTP.ehlo() 
serverSMTP.login(emisor,"Migueleldepredador5000") 

# Enviamos el mensaje 
serverSMTP.sendmail(emisor,receptor,mensaje.as_string()) 

# Cerramos la conexion 
serverSMTP.close()
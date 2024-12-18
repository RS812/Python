import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("anilmakwana03@gmail.com", "afzm wzqz bglx nyyj")
message = "hellooooooooooo"
s.sendmail("anilmakwana03@gmail.com"," anilmakwana03@gmail.com ", message)
s.quit()

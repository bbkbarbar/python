import smtplib
fromaddr = "barbaronpi@gmail.com"
toaddrs  = "bbk.barbar@gmail.com"
msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
username = "barbaronpi"
password = "helloka3"
server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
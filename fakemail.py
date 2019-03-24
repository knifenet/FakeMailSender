import smtplib
import os
import sys

os.system("clear")

print """
          ______ __  __  _____ 
         |  ____|  \/  |/ ____|
         | |__  | \  / | (___  
         |  __| | |\/| |\___ \ 
         | |    | |  | |____) |
         |_|    |_|  |_|_____/ 
                               
         - Fake Mail Sender -
"""

to_persona = raw_input("Recipient name: ")
print ""
to_email = raw_input("Recipient email: ")
print ""
da_persona = raw_input("Fake sender name: ")
da_email = da_persona.replace(" ", "")+"@tin.it"
s = raw_input("[*] The fake email sender will be: %s [Y/n]: " % (da_email))
if s == "y" or s == "Y" or s == "":
	pass
elif s == "n" or s == "N":
	nuovada_email = raw_input("Fake email sender (Must end in @tin.it): ")
	ncheck = nuovada_email.split("@")
	if not ncheck[1] == "tin.it":
		emailapp = ""
		emailapp = emailapp+ncheck[0]
		emailapp = emailapp+"@tin.it"
		da_email = emailapp
		print "[*] Email changed to", da_email
	else:
		da_email = nuovada_email
else:
	print "Answer not expected."
	sys.exit()
print ""
soggetto = raw_input("Subject: ")
print ""
messaggio = raw_input("Message: ")
message = """From: %s <%s>
To: %s <%s>
Subject: %s

%s
""" % (da_persona, da_email, to_persona, to_email, soggetto, messaggio)
print ""

try:
	email = smtplib.SMTP("mail.tin.it",25)
	email.ehlo()
	email.sendmail(da_email,to_email,message)
except:
	print "Error sending email."
else:
	print "Email correctly sent."

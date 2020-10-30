import win32com.client


subject = 'From rp outlook'
body = 'sample email 101'
recipient = '<some email>'


#Create and send email
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = subject
newMail.Body = body
newMail.To = recipient


#newMail.display()
newMail.Send()

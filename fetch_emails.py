import imaplib
from email.parser import Parser

url = "webmail.a10networks.com"
conn = imaplib.IMAP4_SSL(url,993)
user,password = ('pgupta',<pswd>)
conn.login(user,password)
conn.select('INBOX')

#status, response = conn.search('INBOX', 'UNSEEN')

status, response = conn.search(None,'UNSEEN')
status, response = conn.search(None, '(UNSEEN)', '(FROM "%s")' % (sender_of_interest))

msg_ids = response[0]
print msg_ids

msg_id_list = msg_ids.split()
# Print the count of all unread messages
print len(msg_id_list)


latest_email_id = msg_id_list[-1]
print latest_email_id
result,data = conn.fetch(latest_email_id,"(RFC822)")
raw_email = data[0][1]


p = Parser()
msg = p.parsestr(raw_email)

print msg.get('From')
print msg.get('Subject')


# Mark them as seen
for e_id in msg_id_list:
    conn.store(e_id, '+FLAGS', '\Seen')

conn.close()
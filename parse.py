
import mailbox
import email.utils
import logging
from time import mktime
from datetime import datetime
from email_reply_parser import EmailReplyParser
import model

box = 'shit.mbox'
#box = '/var/mail/gijs'

shitbox = mailbox.mbox(box)


def extract_body(shitmail):
    for part in shitmail.walk():
        if part.get_content_type() == 'text/plain':
            return part.get_payload(decode=True).decode('utf-8', errors='ignore')
    content = " ".join([p.get_content_type() for p in shitmail.walk()])
    print "mail doesn't have plain content only " + content
    return u""


def parse(shitmail):
    message_id = shitmail['Message-ID']
    date = datetime.fromtimestamp(mktime(email.utils.parsedate(shitmail['Date'])))
    from_ = shitmail['From']
    subject = shitmail['Subject']
    body = extract_body(shitmail)
    cleanup_body = EmailReplyParser.parse_reply(body)
    in_reply_to = shitmail['In-Reply-To']
    post = model.Post(message_id, date, from_, subject, cleanup_body, in_reply_to)
    model.session.add(post)
    model.session.commit()


def main():
    logging.basicConfig(level=logging.INFO)
    for key, shitmail in shitbox.iteritems():
        print "parsing:", key
        parse(shitmail)


if __name__ == '__main__':
    main()
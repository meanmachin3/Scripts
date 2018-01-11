#!/usr/bin/env ruby
# Crontab entry
# 0 */2 * * * ~/temp/scripts/tushar.sh >> ~/temp/scripts/tushar.log 2>&1

require 'gmail'
require 'csv'
require 'yaml'


GMAIL = Gmail.connect('some@company.com', 'password')
TUSHARS_EMAIL = 'receiver@company.com'
AKASHS_EMAIL = 'teamlead@company.com'

KEYWORDS_REGEX = /PNB|data|Metlife/i

def create_reply(subject, attachment)
  GMAIL.compose do
    to TUSHARS_EMAIL
    cc AKASHS_EMAIL
    subject "RE: #{subject}"
    body "Hi Tushar, \n\n There you go. \n\n Best regards,\n\n Manish Yadav."
    add_file attachment
  end
end
#puts "Before mail"
GMAIL.inbox.find(:unread, from: TUSHARS_EMAIL).each do |email|
  if email.body.raw_source[KEYWORDS_REGEX]
    system('cat pnb.rb | heroku run rails c -r live --no-tty | tee output.csv')
    data = IO.readlines("output.csv")[-2]
    attachment = "PNB" + (Date.today).strftime('%d%m%Y') +".csv"
    CSV.open(attachment, "w") do |csv|
        YAML.load(data).each do |hash|
          csv << hash
        end
    end
    email.read!
    email.label('PNB Metlife')
    reply = create_reply(email.subject, attachment)
    GMAIL.deliver(reply, attachment)
    puts "Mail Delivered"
  end
end

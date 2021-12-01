import win32com.client as win32

def send_report_notification(send_to, subject, body):
    '''
    This function sends email using local Outlook account.
    
    For multiple recipients, each address is separated by "; ".
    For example, 
        Joe.smith@imperialhealthholdings.com; James.johnson@imperialhealthholdings.com
    '''

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = 'henry.cheng@imperialhealthholdings.com'
    mail.Subject = 'Meail Tester from Python'
    mail.Body = 'Testing message'
    #mail.HTMLBody = '<h2>HTML Message body</h2>'


    print('Process complete.')

    # To attach a file to the email (optional):
    if False:
        attachment  = "Path to the attachment"
        mail.Attachments.Add(attachment)

    mail.Send()
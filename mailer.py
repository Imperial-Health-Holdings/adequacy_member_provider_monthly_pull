import win32com.client as win32

def send_report_notification(recipient:str, subject:str, text:str) -> None:
    '''
    This function sends email using local Outlook account.
    
    For multiple recipients, each address is separated by "; ".
    For example, 
        Joe.smith@imperialhealthholdings.com; James.johnson@imperialhealthholdings.com
    '''
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = recipient
    mail.Subject = subject
    mail.Body = text
    #mail.HTMLBody = '<h2>HTML Message body</h2>'

    # To attach a file to the email (optional):
    if False:
        attachment  = "Path to the attachment"
        mail.Attachments.Add(attachment)

    mail.Send()

if __name__ == '__main__':
    None
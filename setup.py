import re
yes = ('yes', 'y', 'aye', 'ha', 'haan', 'yeah', 'yup','k','ok')
no = ('no', 'n', 'nay', 'na', 'nhi','nahi', 'nah', 'nope')
end = ('end', 'break', 'drop', 'exit', 'bye', 'cancel', 'close')

def contains_link(message):
    urls = re.findall('^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$', message.lower())
    if urls:
        return True
    else:
        return False

async def addlog(ctx,client,text):
    assert client!=None
    
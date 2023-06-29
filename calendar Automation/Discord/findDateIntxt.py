import re



def getDate(l_event):
    pattern = "\d{2}[/.-]\d{2}[/.-]\d{4}"

    dates = re.findall(pattern, l_event)

    for date in dates:
        return date


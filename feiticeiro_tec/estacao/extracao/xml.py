def xml_get_text(text: str,column:str, afters=[]):
    try:
        for after in afters:
            if text.find(start) == -1:
                return False
            text = text[text.find(after)+len(after):]
        start = f'<{column}>'
        end = f'</{column}>'
        if text.find(start) == -1:
            return None
        text = text[text.find(start)+len(start):]
        text = text[:text.find(end)]
        return text
    except:
        ...
def get_text(data: str,column:str, afters=[]):
    try:
        data = data
        for after in afters:
            if data.find(start) == -1:
                return False
            data = data[data.find(after)+len(after):]
        start = f'<{column}>'
        end = f'</{column}>'
        if data.find(start) == -1:
            return None
        data = data[data.find(start)+len(start):]
        data = data[:data.find(end)]
        return data
    except:
        ...
def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    Dict = {}   
    answer=True
    for phone in phone_book:
        for i in range(len(phone)):
            try:
                Dict[phone[:i-1]].append(phone)
                answer=False
            except:
                Dict[phone] = [phone]
    return answer
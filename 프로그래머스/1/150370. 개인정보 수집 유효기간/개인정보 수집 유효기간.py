def to_days(date_str):
    y, m, d = map(int, date_str.split('.'))
    return (y * 12 * 28) + (m * 28) + d

def solution(today, terms, privacies):
    answer = []
    
    today_days = to_days(today)
    
    term_dict = {}
    for term in terms:
        t_type, t_month = term.split()
        term_dict[t_type] = int(t_month)
        
    for i, privacy in enumerate(privacies, 1):
        p_date, p_type = privacy.split()
        
        collected_days = to_days(p_date)
        expire_days = collected_days + (term_dict[p_type] * 28)
        
        if today_days >= expire_days:
            answer.append(i)
            
    return answer
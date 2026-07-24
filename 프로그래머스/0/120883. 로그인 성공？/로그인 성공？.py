def solution(id_pw, db): 
    input_id, input_pw = id_pw
    
    db_dict = dict(db)
    
    if input_id in db_dict:
        if db_dict[input_id] == input_pw:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"
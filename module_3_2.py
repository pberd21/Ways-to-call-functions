def semd_email(message, recipient,*,sender = "university.help@gmai.com"):
    valid_domains = (".com", ".ru", ".net")
    if "@" not in recipient or not recipient.endswith(valid_domains) or "@" not in sender or not sender.endswith(valid_domains):
        print(f"Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
        return
    if sender == reciept:
        print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
        return
    if sender == "university.help@gmai.com":
        print(f"Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")

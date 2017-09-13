def new_password(oldpassword, newpassword):
    if len(newpassword) >= 6 and newpassword != oldpassword:
        oldpassword = newpassword
        return "Het wachtwoord  is vernieuwd"
    elif len(newpassword) <= 6:
            return "Het opgegeven nieuwe wachtwoord is te klein"
    elif  newpassword == oldpassword:
        return "Het opgegeven nieuwe wachtwoord is hetzelfde als het oude wachtwoord"

oldpassword = "bananen"
newpassword = input("Geef een nieuw wachtwoord op:")
print(new_password(oldpassword, newpassword))

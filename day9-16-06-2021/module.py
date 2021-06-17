def camel_case():
    import camelcase
    import emoji
    import pyttsx3
    import time
    data = input("Enter the data: ")
    x = camelcase.CamelCase()
    if data == x.hump(data):
        print('Your data is in camelcase, ', emoji.emojize(':thumbs_up:'))
    else:
        string = x.hump(data)
        spk = pyttsx3.init()
        spk.say("Your data is not in camelcase. Coverting it!!")
        time.sleep(2)
        spk.say("Successfully converted your data into camelcase.")
        print("After converting into camel case: ",string)
        spk.runAndWait()
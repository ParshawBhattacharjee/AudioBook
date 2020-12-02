import PyPDF2
import pyttsx3
import PySimpleGUI as sg

layout = [[sg.Text('Choose PDF File to read'), sg.Input(), sg.FileBrowse()],
          [sg.Text('Enter start page no. or null to start page'), sg.InputText()],
          [sg.Text('Enter end page no. or null to last page'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Input', layout)
valid = False
# Event Loop to process "events" and get the "values" of the inputs
while True :
    event, values = window.read()
    # Here we read the path of the pdf file
    pdf = values[0]
    endPageNo = int(values[2])

    if event in (None, 'Cancel') :  # if user closes window or clicks cancel
        print("Exitting")
        window.close()
        exit()

    if event == "Ok" :

        if values[0] == "" :
            sg.Popup("Enter value", "Enter PDF file to be transcribed ")
        else :
            book = open(pdf, 'rb')
            reader = PyPDF2.PdfFileReader(book)

        if values[1] == "" :
            startPageNo = 0
        else :
            startPageNo = int(values[1])

        if values[2] == "" :
            endPageNo = reader.numPages

        if values[0] != "" and values[1] != "" :
            for char in values[1]:
                if char.isdigit() == False:
                    sg.Popup("Invalid value", "Enter valid number or numbers separated by -")
                    break
                else:
                    valid = True
                    break
        # Break while loop if valid first and last page numbers received
    if valid == True:
        print('AudioBook Started:\n', values[0])
        break

window.close()

speaker = pyttsx3.init()

if values[2] == "":
    endPageNo == reader.numPages

for page_num in range(startPageNo, endPageNo) :
    sg.popup_auto_close(page_num)
    text = reader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

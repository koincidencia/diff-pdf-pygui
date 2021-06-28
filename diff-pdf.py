import PySimpleGUI as sg
import os


def generate_pdf(a, b, out):
    cmd = 'diff-pdf.exe --output-diff=' + out + ' ' + a + ' ' + b
    print(cmd)
    result = os.system(cmd)
    if result == 0:
        sg.popup_ok('The two PDFs are identical')
    elif result == 1:
        sg.popup_ok('The two PDFs are different, diff written to ' + out)
    else:
        sg.popup_error('Something went wrong... diff-pdf.exe returned with ' +
                       str(result) + '. Maybe the paths are not ok?')


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Input(), sg.FileBrowse('Choose PDF A', key='FB-PDF-A',
                               file_types=(("PDF Files", "*.pdf"), ))],
    [sg.Input(), sg.FileBrowse('Choose PDF B', key='FB-PDF-B',
                               file_types=(("PDF Files", "*.pdf"), ))],
    [sg.Input(), sg.FileSaveAs('Choose Output PDF', key='FB-PDF-OUT',
                               file_types=(("PDF Files", "*.pdf"), ))],
    [sg.Button('START')]
]

# Create the Window
window = sg.Window('Window Title', layout, size=(800, 300))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break
    elif event == "START":
        generate_pdf(values["FB-PDF-A"],
                     values["FB-PDF-B"],
                     values["FB-PDF-OUT"])

window.close()

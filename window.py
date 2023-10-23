from lib.Window import Window
import json

window = Window()
string = "ersnlfd fignjdfg dfgjndfg "

data = {
    "data1": "ksdfjdkfg",
    "data2": "sdfjkndfj"
}

data = json.dumps(data, indent=4)

print(window.showInfoMessage(f'{data}'))
print(window.showErrorMessgae(f'{data}'))
print(window.showWarningMessgae(f'{string}'))


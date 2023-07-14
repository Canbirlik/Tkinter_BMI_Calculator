import tkinter

# window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=20,pady=20)

# weight_label
weight_label = tkinter.Label(text="Lütfen, kilonuzu giriniz: (Kg)", font=('Courier', 10, 'bold'))
weight_label.pack()

# weight_entry
weight_entry = tkinter.Entry(width=20)
weight_entry.pack()

# height_label
height_label = tkinter.Label(text="Lütfen, boyunuzu giriniz: (Cm)", font=('Courier', 10, 'bold'))
height_label.pack()

# height_entry
height_entry = tkinter.Entry(width=20)
height_entry.pack()

def calculate_fnc():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            BMI = weight / ( (height / 100) ** 2)
            if BMI < 16.0:
                BMI_Category = "Severely Underweight"
            elif BMI >= 16.0 and BMI <= 18.4:
                BMI_Category = "Underweight"
            elif BMI > 18.4 and BMI < 24.9:
                BMI_Category = "Normal"
            elif BMI > 24.9 and BMI < 29.9:
                BMI_Category = "Overweight"
            elif BMI > 29.9 and BMI < 34.9:
                BMI_Category = "Moderately Obese"
            elif BMI > 34.9 and BMI < 39.9:
                BMI_Category = "Severely Obese"
            elif BMI > 39.9:
                BMI_Category = "Morbidly Obese"
        except:
            BMI_label.config(text="Lütfen, geçerli bir değer giriniz", font=('Courier', 15, 'bold'))
        else:
            BMI_label.config(text=f"BMI Değeriniz: {BMI:.2f} ve BMI Kategoriniz: {BMI_Category}", font=('Courier', 15, 'bold'))

# calculate_button
calculate_button = tkinter.Button(text="Hesapla!", font=('Courier', 10, 'bold'), command=calculate_fnc)
calculate_button.pack()

BMI_label = tkinter.Label()
BMI_label.pack()

window.mainloop()
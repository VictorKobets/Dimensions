from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from decimal import Decimal
from material_database import material
from tolerance_database import tolerance_h, tolerance_H


class Dimension:
    '''Окно расчета размера.
    '''

    def __init__(self):
        self.result_x = 1637#
        self.result_y = 123#
        self.result_mx = 12#
        self.result_my = 10#
        self.result_tmax = 3#
        self.result_tmin = 4#

        # Глобальные настройки.
        self.window = Tk()
        self.window.geometry('350x530')
        self.window.title('Расчет размера')

        # Поле ввода номинала размера.
        lbl_nominal = Label(self.window, text='Номинал:')
        lbl_nominal.place(x=5, y=5)
        lbl_mm = Label(self.window, text='мм.')
        lbl_mm.place(x=315, y=5)
        self.txt_nominal = Entry(self.window, width=25)
        self.txt_nominal.place(x=75, y=3)
        self.txt_nominal_off = True

        # Кнопка ввода допуска.
        self.btn_tolerance = Button(
            self.window,
            text='Допуск',
            command=self.click_tolerance,
            width=37,
            height=7
        )
        self.btn_tolerance.place(x=5, y=35)
        self.btn_tolerance_off = True

        # Кнопка ввода температуры.
        self.btn_temp = Button(
            self.window,
            text='Температура',
            command=self.click_temp,
            width=37,
            height=9
        )
        self.btn_temp.place(x=5, y=155)
        self.btn_temp_off = True

        # Кнопка расчета.
        self.btn_solve = Button(
            self.window,
            text='Расчет',
            command=self.click_solve,
            width=37,
            height=13
        )
        self.btn_solve.place(x=5, y=310)
        self.btn_solve_off = True
        
        self.window.mainloop()
    
    def click_tolerance(self):
        '''Обработчки нажатия кнопки допуска.
        '''
        if self.btn_tolerance_off == True:
            self.btn_tolerance_off = False
            self.btn_tolerance.configure(height=2, fg='green')
            
            # Кнопка допуска +-.
            self.btn_plus_minus = Button(
                self.window,
                text='+-',
                command=self.click_plus_minus,
                width=9,
                height=4
            )
            self.btn_plus_minus.place(x=5, y=75)
            self.btn_plus_minus_off = True

            # Кнопка допуска +/-.
            self.btn_plus_or_minus = Button(
                self.window,
                text='+/-',
                command=self.click_plus_or_minus,
                width=9,
                height=4
            )
            self.btn_plus_or_minus.place(x=90, y=75)
            self.btn_plus_or_minus_off = True

            # Кнопка допуска h.
            self.btn_h = Button(
                self.window,
                text='h',
                command=self.click_h,
                width=9,
                height=4
            )
            self.btn_h.place(x=175, y=75)
            self.btn_h_off = True

            # Кнопка допуска H.
            self.btn_H = Button(
                self.window,
                text='H',
                command=self.click_H,
                width=9,
                height=4
            )
            self.btn_H.place(x=260, y=75)
            self.btn_H_off = True
    
    def click_plus_minus(self):
        '''Обработчик нажатия кнопки допуска +-.
        '''
        if self.btn_plus_minus_off == True:
            self.btn_plus_minus_off = False
            self.btn_plus_minus.configure(fg='green')

            self.btn_plus_or_minus.destroy()
            self.btn_h.destroy()
            self.btn_H.destroy()

            self.txt_max = Entry(self.window, width=22)
            self.txt_max.place(x=100, y=93)
            lbl_mm = Label(self.window, text='мм.')
            lbl_mm.place(x=315, y=93)

    def click_plus_or_minus(self):
        '''Обработчик нажатия кнопки допуска +/-.
        '''
        if self.btn_plus_or_minus_off == True:
            self.btn_plus_or_minus_off = False
            self.btn_plus_or_minus.configure(fg='green')
            self.btn_plus_or_minus.place(x=5, y=75)

            self.btn_plus_minus.destroy()
            self.btn_h.destroy()
            self.btn_H.destroy()

            lbl_max = Label(self.window, text='Max:')
            lbl_max.place(x=100, y=75)
            self.txt_max = Entry(self.window, width=18)
            self.txt_max.place(x=140, y=75)
            lbl_mm = Label(self.window, text='мм.')
            lbl_mm.place(x=315, y=75)

            lbl_min = Label(self.window, text='Min:')
            lbl_min.place(x=100, y=115)
            self.txt_min = Entry(self.window, width=18)
            self.txt_min.place(x=140, y=115)
            lbl_mm = Label(self.window, text='мм.')
            lbl_mm.place(x=315, y=115)

    def click_h(self):
        '''Обработчик нажатия кнопки допуска h.
        '''
        if self.btn_h_off == True:
            self.btn_h_off = False
            self.btn_h.configure(fg='green')
            self.btn_h.place(x=5, y=75)

            self.btn_plus_minus.destroy()
            self.btn_plus_or_minus.destroy()
            self.btn_H.destroy()

            self.combo_tolerance = Combobox(
                self.window,
                values=tuple(tolerance_h.keys()),
                width=24
            )
            self.combo_tolerance.place(x=100, y=93)

    def click_H(self):
        '''Обработчик нажатия кнопки допуска H.
        '''
        if self.btn_H_off == True:
            self.btn_H_off = False
            self.btn_H.configure(fg='green')
            self.btn_H.place(x=5, y=75)

            self.btn_plus_minus.destroy()
            self.btn_plus_or_minus.destroy()
            self.btn_h.destroy()

            self.combo_tolerance = Combobox(
                self.window,
                values=tuple(tolerance_H.keys()),
                width=24
            )
            self.combo_tolerance.place(x=100, y=93)
    
    def click_temp(self):
        '''Обработчки нажатия кнопки температуры.
        '''
        if self.btn_temp_off == True:
            self.btn_temp_off = False
            self.btn_temp.configure(height=2, fg='green')

            lbl_nominal = Label(self.window, text='Материал:')
            lbl_nominal.place(x=5, y=200)
            
            self.combo_material = Combobox(
                self.window,
                values=tuple(material.keys()),
                width=26
            )
            self.combo_material.place(x=85, y=200)

            lbl_max = Label(self.window, text='Max:')
            lbl_max.place(x=5, y=230)
            self.txt_max_temp = Entry(self.window, width=27)
            self.txt_max_temp.place(x=45, y=230)
            lbl_mm = Label(self.window, text='С')
            lbl_mm.place(x=315, y=230)

            lbl_min = Label(self.window, text='Min:')
            lbl_min.place(x=5, y=265)
            self.txt_min_temp = Entry(self.window, width=27)
            self.txt_min_temp.place(x=45, y=265)
            lbl_mm = Label(self.window, text='С')
            lbl_mm.place(x=315, y=265)
    
    def click_solve(self):
        '''Обработчки нажатия кнопки решение.
        '''
        self.logic()

        if self.btn_solve_off == True:
            self.btn_solve_off = False
            self.btn_solve.configure(height=2, fg='green')

        lbl_max = Label(self.window, text='Номинал max:')
        lbl_max.place(x=5, y=350)
        lbl_result_max = Label(self.window, text=self.result_x)
        lbl_result_max.place(x=160, y=350)
        lbl_mm = Label(self.window, text='мм.')
        lbl_mm.place(x=315, y=350)

        lbl_min = Label(self.window, text='Номинал min:')
        lbl_min.place(x=5, y=380)
        lbl_result_min = Label(self.window, text=self.result_y)
        lbl_result_min.place(x=160, y=380)
        lbl_mm = Label(self.window, text='мм.')
        lbl_mm.place(x=315, y=380)

        lbl_max = Label(self.window, text='Отклонение max:')
        lbl_max.place(x=5, y=410)
        lbl_result_max = Label(self.window, text=self.result_mx)
        lbl_result_max.place(x=160, y=410)
        lbl_mm = Label(self.window, text='мм.')
        lbl_mm.place(x=315, y=410)

        lbl_min = Label(self.window, text='Отклонение min:')
        lbl_min.place(x=5, y=440)
        lbl_result_min = Label(self.window, text=self.result_my)
        lbl_result_min.place(x=160, y=440)
        lbl_mm = Label(self.window, text='мм.')
        lbl_mm.place(x=315, y=440)

        lbl_max = Label(self.window, text='От температуры max:')
        lbl_max.place(x=5, y=470)
        lbl_result_max = Label(self.window, text=self.result_tmax)
        lbl_result_max.place(x=160, y=470)
        lbl_mm = Label(self.window, text='мм.')
        lbl_mm.place(x=315, y=470)

        lbl_min = Label(self.window, text='От температуры min:')
        lbl_min.place(x=5, y=500)
        lbl_result_min = Label(self.window, text=self.result_tmin)
        lbl_result_min.place(x=160, y=500)
        lbl_mm = Label(self.window, text='мм.')
        lbl_mm.place(x=315, y=500)
    
    def logic(self):
        '''Обрабатывает вероятные ошибки в входных данных.
        '''
        # Проверка корректности номинального размера.
        self.nominal = self.txt_nominal.get()
        if len(self.nominal) == 0:
            messagebox.showerror(
                'Ошибка', 'Вы не ввели номинал размера!'
            )
        self.check_num(
            self.nominal,
            'Не верный формат числовой записи номинала размера!'
        )
        self.nominal = Decimal(self.nominal)
        
        # Проверка корректности допуска на размер размера.
        if self.btn_tolerance_off == False:
            if (self.btn_plus_minus_off != False and
                self.btn_plus_or_minus_off != False and
                self.btn_h_off != False and
                self.btn_H_off != False):
                messagebox.showerror(
                    'Ошибка', 'Вы не ввели парамеры допуска на размер!'
                )
            # Проверка корректности допуска +-.
            elif self.btn_plus_minus_off == False:
                self.tolerance = self.txt_max.get()
                if len(self.tolerance) == 0:
                    messagebox.showerror(
                        'Ошибка', 'Вы не ввели парамеры допуска +- на размер!'
                    )
                self.check_num(
                    self.tolerance,
                    'Не верный формат числовой записи номинала размера!'
                )
                self.max_tolerance = Decimal(self.tolerance)
                self.min_tolerance = -Decimal(self.tolerance)
            
            # Проверка корректности допуска +/-.
            elif self.btn_plus_or_minus_off == False:
                self.max_tolerance = self.txt_max.get()
                self.min_tolerance = self.txt_min.get()
                if len(self.max_tolerance) == 0 or len(self.min_tolerance) == 0:
                    messagebox.showerror(
                        'Ошибка', 'Вы не ввели парамеры допуска +/- на размер!'
                    )
                self.check_num(
                    self.max_tolerance,
                    'Не верный формат числовой записи номинала размера!'
                )
                self.check_num(
                    self.min_tolerance,
                    'Не верный формат числовой записи номинала размера!'
                )
                self.max_tolerance = Decimal(self.max_tolerance)
                self.min_tolerance = Decimal(self.min_tolerance)
                if self.max_tolerance < self.min_tolerance:
                    messagebox.showerror(
                        'Ошибка', 'Вы перепустили max и min допуска +/- на размер!'
                    )
            
            # Проверка корректности допуска h.
            elif self.btn_h_off == False:
                self.tolerance = self.combo_tolerance.get()
                if len(self.tolerance) == 0:
                    messagebox.showerror(
                        'Ошибка', 'Вы не ввели парамеры допуска h на размер!'
                    )
                self.max_tolerance = Decimal(
                    tolerance_h[self.tolerance]['max']
                )
                self.min_tolerance = Decimal(
                    tolerance_h[self.tolerance]['min']
                )
            
            # Проверка корректности допуска H.
            elif self.btn_H_off == False:
                self.tolerance = self.combo_tolerance.get()
                if len(self.tolerance) == 0:
                    messagebox.showerror(
                        'Ошибка', 'Вы не ввели парамеры допуска H на размер!'
                    )
                self.max_tolerance = Decimal(
                    tolerance_H[self.tolerance]['max']
                )
                self.min_tolerance = Decimal(
                    tolerance_H[self.tolerance]['min']
                )
        else:
            self.max_tolerance = Decimal()
            self.min_tolerance = Decimal()
        
        # Проверка корректности температуры.
        if self.btn_temp_off == False:
            self.kltr = self.combo_material.get()
            self.max_temp = self.txt_max_temp.get()
            self.min_temp = self.txt_min_temp.get()
            if len(self.kltr) == 0:
                messagebox.showerror(
                    'Ошибка', 'Вы не выбрали материал детали!'
                )
            if len(self.max_temp) == 0 or len(self.min_temp) == 0:
                messagebox.showerror(
                    'Ошибка', 'Вы не ввели температурный диапазон!'
                )
            self.check_num(
                self.max_temp,
                'Не верный формат числовой записи температуры детали!'
            )
            self.check_num(
                self.min_temp,
                'Не верный формат числовой записи температуры детали!'
            )
    
    def check_num(self, num, message):
        '''Проверка формата числовых записей
        '''
        for char in num:
            if char not in '1234567890.-':
                messagebox.showerror('Ошибка', message)
        if num.count('.') > 1:
            messagebox.showerror('Ошибка', message)
 

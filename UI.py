from tkinter import *


class UX:
    def __init__(self):

        # Исходное окно пользовательского интерфейса
        self.window = Tk()
        self._window_size(350, 150)
        self.window.title('Калькулятор размеров ЕСКД')

        # Флажки активации кнопок
        self._btn_nominal_off = True ## Номинал
        self._btn_tolerance_off = True ## Допуск
        self._btn_tolerance_first_off = True ## +-
        self._btn_tolerance_second_off = True ## +/-
        self._btn_tolerance_third_off = True ## h
        self._btn_tolerance_fourth_off = True ## H
        self._btn_temp_off = True ## Температура
        self._btn_solve_off = True ## Расчитать
        self._btn_clean_off = True ## Сброс


        # Кнопка номинала
        self._btn_nominal = Button(
            self.window,
            text='Номинал',
            command=self._click_nominal,
            width=37
        )
        self._btn_nominal.place(x=5, y=5)

        # Кнопка допуска
        self._btn_tolerance = Button(
            self.window,
            text='Допуск',
            command=self._click_tolerance,
            width=37
        )
        self._btn_tolerance.place(x=5, y=30)

        # Кнопка температуры
        self._btn_temp = Button(
            self.window,
            text='Температура',
            command=self._click_temp,
            width=37
        )
        self._btn_temp.place(x=5, y=60)

        # Кнопка расчета
        self._btn_solve = Button(
            self.window,
            text='Расчитать',
            command=self._click_solve,
            width=37
        )
        self._btn_solve.place(x=5, y=90)

        # Кнопка сброса
        self._btn_clean = Button(
            self.window,
            text='Очистить',
            command=self._click_clean,
            width=37
        )
        self._btn_clean.place(x=5, y=120)
    
    # Функция размера окна
    def _window_size(self, x, y):
        self.window.geometry('{}x{}'.format(x, y))
        self.window.update()
    
    # Функция перемещения кнопок
    @staticmethod
    def _wiget_replace(x, y, *args):
        for arg in args:
            arg.place(x=arg.winfo_x() + x, y=arg.winfo_y() + y)
    
    # Функция перемещения кнопок от вышестоящей
    def _button_replace(self, x, y, before, after):
        after.place(
            x=before.winfo_x() + x,
            y=before.winfo_y() + y
        )
        self.window.update()
    
    # Функция активации кнопки номинала
    def _click_nominal(self):
        if self._btn_nominal_off is True:

            # Увеличение окна
            self._window_size(
                self.window.winfo_width(),
                self.window.winfo_height() + 30
            )
            self._txt_nominal = Entry(self.window, width=34)
            self._txt_nominal.place(x=17, y=30)

            # Перенос кнопок ниже
            if self._btn_tolerance_off is False:
                self._wiget_replace(
                    0,
                    30,
                    self._btn_tolerance,
                    self._btn_temp,
                    self._btn_solve,
                    self._btn_clean,
                    self._btn_tolerance_first,
                    self._btn_tolerance_second,
                    self._btn_tolerance_third,
                    self._btn_tolerance_fourth
                )
            else:
                self._wiget_replace(
                    0,
                    30,
                    self._btn_tolerance,
                    self._btn_temp,
                    self._btn_solve,
                    self._btn_clean
                )

            # Кнопка активирована
            self._btn_nominal_off = False
        else:

            self._txt_nominal.destroy()

            # Уменьшение окна
            self._window_size(
                self.window.winfo_width(),
                self.window.winfo_height() - 30
            )

            # Перенос кнопок выше
            if self._btn_tolerance_off is False:
                self._wiget_replace(
                    0,
                    -30,
                    self._btn_tolerance,
                    self._btn_temp,
                    self._btn_solve,
                    self._btn_clean,
                    self._btn_tolerance_first,
                    self._btn_tolerance_second,
                    self._btn_tolerance_third,
                    self._btn_tolerance_fourth
                )
            else:
                self._wiget_replace(
                    0,
                    -30,
                    self._btn_tolerance,
                    self._btn_temp,
                    self._btn_solve,
                    self._btn_clean
                )

            # Кнопка не активирована
            self._btn_nominal_off = True
    
    # Функция активации кнопки допуска
    def _click_tolerance(self):
        if self._btn_tolerance_off is True:

            # Увеличение окна
            self._window_size(
                self.window.winfo_width(),
                self.window.winfo_height() + 120
            )

            # Перенос кнопок ниже
            self._wiget_replace(
                0,
                120,
                self._btn_temp,
                self._btn_solve,
                self._btn_clean
            )

            ## Кнопка +-
            self._btn_tolerance_first = Button(
                self.window,
                text='+-',
                command=self._click_tolerance_first,
                width=10
            )
            self._button_replace(
                15,
                30,
                self._btn_tolerance,
                self._btn_tolerance_first
            )

            ## Кнопка +/-
            self._btn_tolerance_second = Button(
                self.window,
                text='+/-',
                command=self._click_tolerance_second,
                width=10
            )
            self._button_replace(
                0,
                30,
                self._btn_tolerance_first,
                self._btn_tolerance_second
            )

            ## Кнопка h
            self._btn_tolerance_third = Button(
                self.window,
                text='h',
                command=self._click_tolerance_third,
                width=10
            )
            self._button_replace(
                0,
                30,
                self._btn_tolerance_second,
                self._btn_tolerance_third
            )

            ## Кнопка H
            self._btn_tolerance_fourth = Button(
                self.window,
                text='H',
                command=self._click_tolerance_fourth,
                width=10
            )
            self._button_replace(
                0,
                30,
                self._btn_tolerance_third,
                self._btn_tolerance_fourth
            )

            # Кнопка активирована
            self._btn_tolerance_off = False
        else:

            self._btn_tolerance_first.destroy()
            self._btn_tolerance_second.destroy()
            self._btn_tolerance_third.destroy()
            self._btn_tolerance_fourth.destroy()
            
            # Уменьшение окна
            self._window_size(
                self.window.winfo_width(),
                self.window.winfo_height() - 120
            )

            # Перенос кнопок выше
            self._wiget_replace(
                0,
                -120,
                self._btn_temp,
                self._btn_solve,
                self._btn_clean
            )

            # Кнопка не активирована
            self._btn_tolerance_off = True
    
    # Функция активации подпункта раздела допуск
    def _click_tolerance_first(self):
        pass

    def _click_tolerance_second(self):
        pass
    
    def _click_tolerance_third(self):
        pass

    def _click_tolerance_fourth(self):
        pass

    # Функция активации кнопки температуры
    def _click_temp(self):
        if self._btn_temp_off is True:

            # Увеличение окна
            self._window_size(
                self.window.winfo_width(),
                self.window.winfo_height() + 30
            )

            # Перенос кнопок ниже
            self._wiget_replace(
                0,
                30,
                self._btn_solve,
                self._btn_clean
            )

            # Кнопка активирована
            self._btn_temp_off = False
        else:

            # Уменьшение окна
            self._window_size(
                self.window.winfo_width(),
                self.window.winfo_height() - 30
            )

            # Перенос кнопок выше
            self._wiget_replace(
                0,
                -30,
                self._btn_solve,
                self._btn_clean
            )

            # Кнопка не активирована
            self._btn_temp_off = True
    
    #
    def _click_solve(self):
        if self._btn_solve_off is True:

            # Увеличение окна
            self._window_size(
                self.window.winfo_width(),
                self.window.winfo_height() + 30
            )

            # Перенос кнопок ниже
            self._wiget_replace(
                0,
                30,
                self._btn_clean
            )

            # Кнопка активирована
            self._btn_solve_off = False
        else:

            # Уменьшение окна
            self._window_size(
                self.window.winfo_width(),
                self.window.winfo_height() - 30
            )

            # Перенос кнопок выше
            self._wiget_replace(
                0,
                -30,
                self._btn_clean
            )

            # Кнопка не активирована
            self._btn_solve_off = True

    #
    def _click_clean(self):
        pass

window = UX()
window.window.mainloop()

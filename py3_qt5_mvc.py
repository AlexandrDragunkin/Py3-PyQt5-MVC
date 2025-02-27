# -*- coding: utf-8 -*-
import sys
import os


class WidgetCodeGenerator(object):

    def __init__(self):

        self.ordered_funcs = [

            {'the_func': self.get_view_class_code,
             'func_single_only': True,
             'func_header': '#####################\n# views\MainView.py #\n#####################\n'},

            {'the_func': self.get_value_property_code,
             'func_single_only': False,
             'func_header': '\n\n    #### свойства для значения виджета ####'},

            {'the_func': self.get_enable_property_code,
             'func_single_only': False,
             'func_header': '\n\n    #### свойства для включенного виджета ####'},

            {'the_func': self.get_view_init_code,
             'func_single_only': True,
             'func_header': '\n'},

            {'the_func': self.get_model_set_code,
             'func_single_only': False,
             'func_header': '\n        #### установить модель Qt для совместимых типов виджетов ####'},

            {'the_func': self.get_signal_connect_code,
             'func_single_only': False,
             'func_header': '\n\n        #### подключить сигналы виджетов к функциям событий ####'},

            {'the_func': self.get_update_ui_code,
             'func_single_only': True,
             'func_header': '\n\n'},

            {'the_func': self.get_view_update_code,
             'func_single_only': False,
             'func_header': '        #### обновить значения виджета из модели ####'},

            {'the_func': self.get_view_def_code,
             'func_single_only': False,
             'func_header': '\n\n    #### функции события сигнала виджета ####'},

            {'the_func': self.get_ctrl_class_code,
             'func_single_only': True,
             'func_header': '\n\n\n###########################\n# ctrls\MainController.py #\n###########################\n'},

            {'the_func': self.get_ctrl_def_code,
             'func_single_only': False,
             'func_header': '    #### функции события виджета ####'},

            {'the_func': self.get_model_class_code,
             'func_single_only': True,
             'func_header': '\n\n\n##################\n# model\Model.py #\n##################\n'},

            {'the_func': self.get_model_qt_model_property_code,
             'func_single_only': False,
             'func_header': '    #### свойства для значения содержимого модели Qt ####'},

            {'the_func': self.get_model_init_code,
             'func_single_only': True,
             'func_header': '\n'},

            {'the_func': self.get_model_config_code,
             'func_single_only': False,
             'func_header': ''},

            {'the_func': self.get_model_close_config_code,
             'func_single_only': True,
             'func_header': ''},

            {'the_func': self.get_model_qt_model_var_code,
             'func_single_only': False,
             'func_header': '\n\n        #### создание моделей Qt для совместимых типов виджетов ####'},

            {'the_func': self.get_model_var_code,
             'func_single_only': False,
             'func_header': '\n\n        #### переменные модели ####'},

            {'the_func': self.get_model_update_code,
             'func_single_only': True,
             'func_header': '\n\n'},

            {'the_func': self.get_app_code,
             'func_single_only': True,
             'func_header': '\n\n##########\n# App.py #\n##########\n'},

        ]

        self.widget_types = {
            # buttons
            'pushButton': {'read_value': 'isChecked',      # способ считывания первичного значения
                           'write_value': 'setChecked',     # способ записи первичного значения
                           'value_signal': 'clicked',        # первичный сигнал для подключения
                           'value_signal_arg': 'checked',        # список аргументов, отправленных при первичном сигнале события
                           'config_read': 'getboolean'},    # метод ConfigParser-а для чтения значения
            'toolButton': {'read_value': 'isChecked',
                           'write_value': 'setChecked',
                           'value_signal': 'clicked',
                           'value_signal_arg': 'checked',
                           'config_read': 'getboolean'},
            'radioButton': {'read_value': 'isChecked',
                            'write_value': 'setChecked',
                            'value_signal': 'toggled',
                            'value_signal_arg': 'checked',
                            'config_read': 'getboolean'},
            'checkBox': {'read_value': 'isChecked',
                         'write_value': 'setChecked',
                         'value_signal': 'stateChanged',
                         'value_signal_arg': 'state',
                         'config_read': 'getboolean'},
            # containers
            'groupBox': {'read_value': None,             # exists only for isEnabled/setEnabled
                         'write_value': None,
                         'value_signal': None,
                         'value_signal_arg': None,
                         'config_read': None},
            'stackedWidget': {'read_value': 'currentIndex',
                              'write_value': 'setCurrentIndex',
                              'value_signal': 'currentChanged',
                              'value_signal_arg': 'index',
                              'config_read': 'getint'},
            # input widgets
            'comboBox': {'read_value': 'currentIndex',
                         'write_value': 'setCurrentIndex',
                         'value_signal': 'currentIndexChanged',
                         'value_signal_arg': 'index',
                         'config_read': 'getint'},
            'lineEdit': {'read_value': 'text',
                         'write_value': 'setText',
                         'value_signal': 'textEdited',
                         'value_signal_arg': 'text',
                         'config_read': 'get'},
            'textEdit': {'read_value': 'toPlainText',
                         'write_value': 'setPlainText',
                         'value_signal': 'textChanged',
                         'value_signal_arg': None,
                         'config_read': 'get'},
            'plainTextEdit': {'read_value': 'toPlainText',
                              'write_value': 'setPlainText',
                              'value_signal': 'textChanged',
                              'value_signal_arg': None,
                              'config_read': 'get'},
            'spinBox': {'read_value': 'value',
                        'write_value': 'setValue',
                        'value_signal': 'valueChanged',
                        'value_signal_arg': 'value',
                        'config_read': 'getint'},
            'doubleSpinBox': {'read_value': 'value',
                              'write_value': 'setValue',
                              'value_signal': 'valueChanged',
                              'value_signal_arg': 'value',
                              'config_read': 'getfloat'},
            'horizontalSlider': None,  # todo
            'verticalSlider': None,  # todo
            # отображать виджеты
            'label': {'read_value': 'text',
                      'write_value': 'setText',
                      'value_signal': None,
                      'value_signal_arg': None,
                      'config_read': 'get'},
            'progressBar': {'read_value': 'value',
                            'write_value': 'setValue',
                            'value_signal': 'valueChanged',
                            'value_signal_arg': 'value',
                            'config_read': 'getint'},
            # другое
            'action': {'read_value': 'isChecked',
                       'write_value': 'setChecked',
                       'value_signal': 'triggered',
                       'value_signal_arg': 'checked',
                       'config_read': 'getbool'},
            'toolBar': {'read_value': None,
                        'write_value': None,
                        'value_signal_arg': None,
                        'value_signal': None,
                        'config_read': None},
        }

    def get_view_class_code(self):
        return ''.join(['from PyQt5 import QtWidgets\nfrom gen.ui_MainView import Ui_MainView\n\nclass MainView(QtWidgets.QMainWindow):'])

    def get_value_property_code(self, widget_data):
        return ''.join(['\n    @property\n    def ',
                        widget_data['variable_name'],
                        '(self):\n        return self.ui.',
                        widget_data['widget_name'],
                        '.',
                        widget_data['func_names']['read_value'],
                        '()\n    @',
                        widget_data['variable_name'],
                        '.setter\n    def ',
                        widget_data['variable_name'],
                        '(self, value):\n        self.ui.',
                        widget_data['widget_name'],
                        '.',
                        widget_data['func_names']['write_value'],
                        '(value)'])

    def get_enable_property_code(self, widget_data):
        return ''.join(['\n    @property\n    def ',
                        widget_data['variable_name'],
                        '_enabled(self):\n        return self.ui.',
                        widget_data['widget_name'],
                        '.isEnabled()\n    @',
                        widget_data['variable_name'],
                        '_enabled.setter\n    def ',
                        widget_data['variable_name'],
                        '_enabled(self, value):\n        self.ui.',
                        widget_data['widget_name'],
                        '.setEnabled(value)'])

    def get_view_init_code(self):
        return ''.join(['\n    def __init__(self, model, main_ctrl):\n',
                        '        self.model = model\n',
                        '        self.main_ctrl = main_ctrl\n',
                        '        super(MainView, self).__init__()\n',
                        '        self.build_ui()\n',
                        '        # register func with model for model update announcements\n',
                        '        self.model.subscribe_update_func(self.update_ui_from_model)\n\n',
                        '    def build_ui(self):\n',
                        '        self.ui = Ui_MainView()\n',
                        '        self.ui.setupUi(self)\n'])

    def get_model_set_code(self, widget_data):
        if widget_data['widget_name'].startswith('comboBox'):
            return ''.join(['\n        self.ui.',
                            widget_data['widget_name'],
                            '.setModel(self.model.',
                            widget_data['variable_name'],
                            '_model)'])
        else:
            return ''

    def get_signal_connect_code(self, widget_data):
        if widget_data['func_names']['value_signal'] is not None:
            return ''.join(['\n        self.ui.',
                            widget_data['widget_name'],
                            '.',
                            widget_data['func_names']['value_signal'],
                            '.connect(self.on_',
                            widget_data['variable_name'],
                            ')'])
        else:
            return ''

    def get_update_ui_code(self):
        return ''.join(['    def update_ui_from_model(self):\n',
                        "        print('DEBUG: вызывается update_ui_from_model')\n", ])

    def get_view_update_code(self, widget_data):
        return ''.join(['\n        self.',
                        widget_data['variable_name'],
                        ' = ',
                        'self.model.',
                        widget_data['variable_name']])

    # todo - варьировать количество аргументов, включая их отсутствие, например, для кнопок.
    def get_view_def_code(self, widget_data):
        if widget_data['func_names']['value_signal_arg'] is not None:
            # todo very hacky =(
            if widget_data['widget_name'].startswith('pushButton'):
                return ''.join(['\n    def on_',
                                widget_data['variable_name'],
                                '(self): self.main_ctrl.change_',
                                widget_data['variable_name'],
                                '(self.',
                                widget_data['variable_name'],
                                ')'])
            else:
                return ''.join(['\n    def on_',
                                widget_data['variable_name'],
                                '(self, ',
                                widget_data['func_names']['value_signal_arg'],
                                '): self.main_ctrl.change_',
                                widget_data['variable_name'],
                                '(',
                                widget_data['func_names']['value_signal_arg'],
                                ')'])
        else:
            return ''

    def get_ctrl_class_code(self):
        return ''.join(['from PyQt5 import QtWidgets\n\nclass MainController(object):\n\n',
                        '    def __init__(self, model):\n',
                        '        self.model = model\n\n'
                        ])

    def get_ctrl_def_code(self, widget_data):
        if widget_data['func_names']['value_signal_arg'] is not None:
            return ''.join(['\n    def change_',
                            widget_data['variable_name'],
                            '(self, ',
                            widget_data['func_names']['value_signal_arg'],
                            '):\n        self.model.',
                            widget_data['variable_name'],
                            ' = ',
                            widget_data['func_names']['value_signal_arg'],
                            "\n        print('DEBUG: change_",
                            widget_data['variable_name'],
                            " вызывается со значением arg:', ",
                            widget_data['func_names']['value_signal_arg'],
                            ')'])
        else:
            return ''

    def get_model_class_code(self):
        return ''.join(['from PyQt5 import QtGui\n\nclass Model(object):\n\n'])

    def get_model_qt_model_property_code(self, widget_data):
        if widget_data['widget_name'].startswith('comboBox'):
            return ''.join(['\n    @property\n    def ',
                            widget_data['variable_name'],
                            '_items(self):\n        return self.',
                            widget_data['variable_name'],
                            '_model.stringList()\n    @',
                            widget_data['variable_name'],
                            '_items.setter\n    def ',
                            widget_data['variable_name'],
                            '_items(self, value):\n        self.',
                            widget_data['variable_name'],
                            '_model.setStringList(value)'])
        else:
            return ''

    def get_model_init_code(self):
        return ''.join(['\n    def __init__(self):\n',
                        '        self._update_funcs = []\n',
                        "        self.config_section = 'settings'\n",
                        '        self.config_options = ('])

    def get_model_config_code(self, widget_data):
        return ''.join(["\n            ('",
                        widget_data['variable_name'],
                        "', '",
                        widget_data['func_names']['config_read'],
                        "'),"])

    def get_model_close_config_code(self):
        return '\n        )'

    # todo default values valid types, eg bool or int, etc
    def get_model_var_code(self, widget_data):
        return ''.join(['\n        self.',
                        widget_data['variable_name'],
                        ' = None'])

    def get_model_qt_model_var_code(self, widget_data):
        if widget_data['widget_name'].startswith('comboBox'):
            return ''.join(['\n        self.',
                            widget_data['variable_name'],
                            '_model = Qt.QStringListModel()'])
        else:
            return ''

    def get_model_update_code(self):
        return ''.join(['    def subscribe_update_func(self, func):\n',
                        '        if func not in self._update_funcs:\n',
                        '            self._update_funcs.append(func)\n\n',
                        '    def unsubscribe_update_func(self, func):\n',
                        '        if func in self._update_funcs:\n',
                        '            self._update_funcs.remove(func)\n\n',
                        '    def announce_update(self):\n',
                        '        for func in self._update_funcs:\n',
                        '            func()\n', ])

    def get_app_code(self):
        return ''.join(['import sys\n',
                        'from PyQt5 import Qt\n',
                        'from model.Model import Model\n',
                        'from ctrls.MainController import MainController\n',
                        'from views.MainView import MainView\n\n',
                        'class App(Qt.QApplication):\n',
                        '    def __init__(self, sys_argv):\n',
                        '        super(App, self).__init__(sys_argv)\n',
                        '        self.model = Model()\n',
                        '        self.main_ctrl = MainController(self.model)\n',
                        '        self.main_view = MainView(self.model, self.main_ctrl)\n',
                        '        self.main_view.show()\n\n',
                        "if __name__ == '__main__':\n",
                        '    app = App(sys.argv)\n',
                        '    sys.exit(app.exec_())\n\n\n'])

    def process_file(self, argv):

        # проверить, открыть и прочесть файл
        if len(argv) > 1:
            if os.path.exists(argv[1]):
                widget_names = []
                with open(argv[1], 'r') as thefile:
                    for line in thefile:
                        widget_names.append(line.strip())
            else:
                raise Exception('ФАЙЛ НЕ НАЙДЕН.')
        else:
            raise Exception('АРГУМЕНТ НЕ УКАЗАН, НУЖЕН ФАЙЛ ДЛЯ ОБРАБОТКИ.')

        # собрать данные для каждого widget_name
        widget_data = []
        for widget_name in widget_names:
            if (len(widget_name) > 0 and
                not widget_name.startswith('#') and
                    '_' in widget_name):
                widget_type, variable_name = widget_name.split('_', 1)
                if widget_type in self.widget_types:
                    widget_data.append({'widget_name': widget_name,
                                        'variable_name': variable_name,
                                        'func_names': self.widget_types[widget_type]})
                else:
                    print('ПРЕДУПРЕЖДЕНИЕ: НЕИЗВЕСТНЫЙ ТИП ВИДЖЕТА:', widget_type)

        # получить сгенерированный код
        output = []
        for func in self.ordered_funcs:
            # добавить заголовок
            output.append(func['func_header'])
            # если func вызывается один раз в общей сложности
            if func['func_single_only']:
                output.append(func['the_func']())
            # или вызывается один раз для каждого виджета
            else:
                for data in widget_data:
                    # код
                    output.append(func['the_func'](data))

        # запись в новый файл
        with open(argv[1] + '.py', 'w') as thefile:
            thefile.write(''.join(output))


if __name__ == '__main__':

    WidgetCodeGenerator().process_file(sys.argv)



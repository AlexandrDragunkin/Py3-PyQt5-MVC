# -*- coding: utf-8 -*-
#####################
# views\MainView.py #
#####################
from PyQt5 import QtWidgets
from gen.ui_MainView import Ui_MainView


class MainView(QtWidgets.QMainWindow):

    #### свойства для значения виджета ####
    @property
    def contact_type(self):
        return self.ui.comboBox_contact_type.currentIndex()

    @contact_type.setter
    def contact_type(self, value):
        self.ui.comboBox_contact_type.setCurrentIndex(value)

    @property
    def forma_carcase(self):
        return self.ui.comboBox_forma_carcase.currentIndex()

    @forma_carcase.setter
    def forma_carcase(self, value):
        self.ui.comboBox_forma_carcase.setCurrentIndex(value)

    @property
    def name_object(self):
        return self.ui.lineEdit_name_object.text()

    @name_object.setter
    def name_object(self, value):
        self.ui.lineEdit_name_object.setText(value)

    @property
    def pict_karkase(self):
        return self.ui.label_pict_karkase.text()

    @pict_karkase.setter
    def pict_karkase(self, value):
        self.ui.label_pict_karkase.setText(value)

    @property
    def width(self):
        return self.ui.spinBox_width.value()

    @width.setter
    def width(self, value):
        self.ui.spinBox_width.setValue(value)

    @property
    def depth(self):
        return self.ui.spinBox_depth.value()

    @depth.setter
    def depth(self, value):
        self.ui.spinBox_depth.setValue(value)

    @property
    def height(self):
        return self.ui.spinBox_height.value()

    @height.setter
    def height(self, value):
        self.ui.spinBox_height.setValue(value)

    @property
    def dm(self):
        return self.ui.spinBox_dm.value()

    @dm.setter
    def dm(self, value):
        self.ui.spinBox_dm.setValue(value)

    @property
    def wm(self):
        return self.ui.spinBox_wm.value()

    @wm.setter
    def wm(self, value):
        self.ui.spinBox_wm.setValue(value)

    @property
    def bevel_position(self):
        return self.ui.checkBox_bevel_position.isChecked()

    @bevel_position.setter
    def bevel_position(self, value):
        self.ui.checkBox_bevel_position.setChecked(value)

    @property
    def hanging_skaf(self):
        return self.ui.checkBox_hanging_skaf.isChecked()

    @hanging_skaf.setter
    def hanging_skaf(self, value):
        self.ui.checkBox_hanging_skaf.setChecked(value)

    @property
    def full_type_object(self):
        return self.ui.comboBox_full_type_object.currentIndex()

    @full_type_object.setter
    def full_type_object(self, value):
        self.ui.comboBox_full_type_object.setCurrentIndex(value)

    @property
    def object_place(self):
        return self.ui.comboBox_object_place.currentIndex()

    @object_place.setter
    def object_place(self, value):
        self.ui.comboBox_object_place.setCurrentIndex(value)

    @property
    def type_object(self):
        return self.ui.comboBox_type_object.currentIndex()

    @type_object.setter
    def type_object(self, value):
        self.ui.comboBox_type_object.setCurrentIndex(value)

    @property
    def article(self):
        return self.ui.lineEdit_article.text()

    @article.setter
    def article(self, value):
        self.ui.lineEdit_article.setText(value)

    @property
    def user_type_object(self):
        return self.ui.lineEdit_user_type_object.text()

    @user_type_object.setter
    def user_type_object(self, value):
        self.ui.lineEdit_user_type_object.setText(value)

    @property
    def gap_right(self):
        return self.ui.spinBox_gap_right.value()

    @gap_right.setter
    def gap_right(self, value):
        self.ui.spinBox_gap_right.setValue(value)

    @property
    def gap_left(self):
        return self.ui.spinBox_gap_left.value()

    @gap_left.setter
    def gap_left(self, value):
        self.ui.spinBox_gap_left.setValue(value)

    @property
    def gap_back(self):
        return self.ui.spinBox_gap_back.value()

    @gap_back.setter
    def gap_back(self, value):
        self.ui.spinBox_gap_back.setValue(value)

    @property
    def gap_front(self):
        return self.ui.spinBox_gap_front.value()

    @gap_front.setter
    def gap_front(self, value):
        self.ui.spinBox_gap_front.setValue(value)

    @property
    def gap_down(self):
        return self.ui.spinBox_gap_down.value()

    @gap_down.setter
    def gap_down(self, value):
        self.ui.spinBox_gap_down.setValue(value)

    @property
    def cover_corner(self):
        return self.ui.checkBox_cover_corner.isChecked()

    @cover_corner.setter
    def cover_corner(self, value):
        self.ui.checkBox_cover_corner.setChecked(value)

    #### свойства для включенного виджета ####
    @property
    def contact_type_enabled(self):
        return self.ui.comboBox_contact_type.isEnabled()

    @contact_type_enabled.setter
    def contact_type_enabled(self, value):
        self.ui.comboBox_contact_type.setEnabled(value)

    @property
    def forma_carcase_enabled(self):
        return self.ui.comboBox_forma_carcase.isEnabled()

    @forma_carcase_enabled.setter
    def forma_carcase_enabled(self, value):
        self.ui.comboBox_forma_carcase.setEnabled(value)

    @property
    def name_object_enabled(self):
        return self.ui.lineEdit_name_object.isEnabled()

    @name_object_enabled.setter
    def name_object_enabled(self, value):
        self.ui.lineEdit_name_object.setEnabled(value)

    @property
    def pict_karkase_enabled(self):
        return self.ui.label_pict_karkase.isEnabled()

    @pict_karkase_enabled.setter
    def pict_karkase_enabled(self, value):
        self.ui.label_pict_karkase.setEnabled(value)

    @property
    def width_enabled(self):
        return self.ui.spinBox_width.isEnabled()

    @width_enabled.setter
    def width_enabled(self, value):
        self.ui.spinBox_width.setEnabled(value)

    @property
    def depth_enabled(self):
        return self.ui.spinBox_depth.isEnabled()

    @depth_enabled.setter
    def depth_enabled(self, value):
        self.ui.spinBox_depth.setEnabled(value)

    @property
    def height_enabled(self):
        return self.ui.spinBox_height.isEnabled()

    @height_enabled.setter
    def height_enabled(self, value):
        self.ui.spinBox_height.setEnabled(value)

    @property
    def dm_enabled(self):
        return self.ui.spinBox_dm.isEnabled()

    @dm_enabled.setter
    def dm_enabled(self, value):
        self.ui.spinBox_dm.setEnabled(value)

    @property
    def wm_enabled(self):
        return self.ui.spinBox_wm.isEnabled()

    @wm_enabled.setter
    def wm_enabled(self, value):
        self.ui.spinBox_wm.setEnabled(value)

    @property
    def bevel_position_enabled(self):
        return self.ui.checkBox_bevel_position.isEnabled()

    @bevel_position_enabled.setter
    def bevel_position_enabled(self, value):
        self.ui.checkBox_bevel_position.setEnabled(value)

    @property
    def hanging_skaf_enabled(self):
        return self.ui.checkBox_hanging_skaf.isEnabled()

    @hanging_skaf_enabled.setter
    def hanging_skaf_enabled(self, value):
        self.ui.checkBox_hanging_skaf.setEnabled(value)

    @property
    def full_type_object_enabled(self):
        return self.ui.comboBox_full_type_object.isEnabled()

    @full_type_object_enabled.setter
    def full_type_object_enabled(self, value):
        self.ui.comboBox_full_type_object.setEnabled(value)

    @property
    def object_place_enabled(self):
        return self.ui.comboBox_object_place.isEnabled()

    @object_place_enabled.setter
    def object_place_enabled(self, value):
        self.ui.comboBox_object_place.setEnabled(value)

    @property
    def type_object_enabled(self):
        return self.ui.comboBox_type_object.isEnabled()

    @type_object_enabled.setter
    def type_object_enabled(self, value):
        self.ui.comboBox_type_object.setEnabled(value)

    @property
    def article_enabled(self):
        return self.ui.lineEdit_article.isEnabled()

    @article_enabled.setter
    def article_enabled(self, value):
        self.ui.lineEdit_article.setEnabled(value)

    @property
    def user_type_object_enabled(self):
        return self.ui.lineEdit_user_type_object.isEnabled()

    @user_type_object_enabled.setter
    def user_type_object_enabled(self, value):
        self.ui.lineEdit_user_type_object.setEnabled(value)

    @property
    def gap_right_enabled(self):
        return self.ui.spinBox_gap_right.isEnabled()

    @gap_right_enabled.setter
    def gap_right_enabled(self, value):
        self.ui.spinBox_gap_right.setEnabled(value)

    @property
    def gap_left_enabled(self):
        return self.ui.spinBox_gap_left.isEnabled()

    @gap_left_enabled.setter
    def gap_left_enabled(self, value):
        self.ui.spinBox_gap_left.setEnabled(value)

    @property
    def gap_back_enabled(self):
        return self.ui.spinBox_gap_back.isEnabled()

    @gap_back_enabled.setter
    def gap_back_enabled(self, value):
        self.ui.spinBox_gap_back.setEnabled(value)

    @property
    def gap_front_enabled(self):
        return self.ui.spinBox_gap_front.isEnabled()

    @gap_front_enabled.setter
    def gap_front_enabled(self, value):
        self.ui.spinBox_gap_front.setEnabled(value)

    @property
    def gap_down_enabled(self):
        return self.ui.spinBox_gap_down.isEnabled()

    @gap_down_enabled.setter
    def gap_down_enabled(self, value):
        self.ui.spinBox_gap_down.setEnabled(value)

    @property
    def cover_corner_enabled(self):
        return self.ui.checkBox_cover_corner.isEnabled()

    @cover_corner_enabled.setter
    def cover_corner_enabled(self, value):
        self.ui.checkBox_cover_corner.setEnabled(value)

    def __init__(self, model, main_ctrl):
        self.model = model
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        self.build_ui()
        # register func with model for model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

    def build_ui(self):
        self.ui = Ui_MainView()
        self.ui.setupUi(self)

        #### установить модель Qt для совместимых типов виджетов ####
        self.ui.comboBox_contact_type.setModel(self.model.contact_type_model)
        self.ui.comboBox_forma_carcase.setModel(self.model.forma_carcase_model)
        self.ui.comboBox_full_type_object.setModel(self.model.full_type_object_model)
        self.ui.comboBox_object_place.setModel(self.model.object_place_model)
        self.ui.comboBox_type_object.setModel(self.model.type_object_model)

        #### подключить сигналы виджетов к функциям событий ####
        self.ui.comboBox_contact_type.currentIndexChanged.connect(self.on_contact_type)
        self.ui.comboBox_forma_carcase.currentIndexChanged.connect(self.on_forma_carcase)
        self.ui.lineEdit_name_object.textEdited.connect(self.on_name_object)
        self.ui.spinBox_width.valueChanged.connect(self.on_width)
        self.ui.spinBox_depth.valueChanged.connect(self.on_depth)
        self.ui.spinBox_height.valueChanged.connect(self.on_height)
        self.ui.spinBox_dm.valueChanged.connect(self.on_dm)
        self.ui.spinBox_wm.valueChanged.connect(self.on_wm)
        self.ui.checkBox_bevel_position.stateChanged.connect(self.on_bevel_position)
        self.ui.checkBox_hanging_skaf.stateChanged.connect(self.on_hanging_skaf)
        self.ui.comboBox_full_type_object.currentIndexChanged.connect(self.on_full_type_object)
        self.ui.comboBox_object_place.currentIndexChanged.connect(self.on_object_place)
        self.ui.comboBox_type_object.currentIndexChanged.connect(self.on_type_object)
        self.ui.lineEdit_article.textEdited.connect(self.on_article)
        self.ui.lineEdit_user_type_object.textEdited.connect(self.on_user_type_object)
        self.ui.spinBox_gap_right.valueChanged.connect(self.on_gap_right)
        self.ui.spinBox_gap_left.valueChanged.connect(self.on_gap_left)
        self.ui.spinBox_gap_back.valueChanged.connect(self.on_gap_back)
        self.ui.spinBox_gap_front.valueChanged.connect(self.on_gap_front)
        self.ui.spinBox_gap_down.valueChanged.connect(self.on_gap_down)
        self.ui.checkBox_cover_corner.stateChanged.connect(self.on_cover_corner)

    def update_ui_from_model(self):
        print('DEBUG: вызывается update_ui_from_model')
        #### обновить значения виджета из модели ####
        self.contact_type = self.model.contact_type
        self.forma_carcase = self.model.forma_carcase
        self.name_object = self.model.name_object
        self.pict_karkase = self.model.pict_karkase
        self.width = self.model.width
        self.depth = self.model.depth
        self.height = self.model.height
        self.dm = self.model.dm
        self.wm = self.model.wm
        self.bevel_position = self.model.bevel_position
        self.hanging_skaf = self.model.hanging_skaf
        self.full_type_object = self.model.full_type_object
        self.object_place = self.model.object_place
        self.type_object = self.model.type_object
        self.article = self.model.article
        self.user_type_object = self.model.user_type_object
        self.gap_right = self.model.gap_right
        self.gap_left = self.model.gap_left
        self.gap_back = self.model.gap_back
        self.gap_front = self.model.gap_front
        self.gap_down = self.model.gap_down
        self.cover_corner = self.model.cover_corner

    #### функции события сигнала виджета ####
    def on_contact_type(self, index): self.main_ctrl.change_contact_type(index)

    def on_forma_carcase(self, index): self.main_ctrl.change_forma_carcase(index)

    def on_name_object(self, text): self.main_ctrl.change_name_object(text)

    def on_width(self, value): self.main_ctrl.change_width(value)

    def on_depth(self, value): self.main_ctrl.change_depth(value)

    def on_height(self, value): self.main_ctrl.change_height(value)

    def on_dm(self, value): self.main_ctrl.change_dm(value)

    def on_wm(self, value): self.main_ctrl.change_wm(value)

    def on_bevel_position(self, state): self.main_ctrl.change_bevel_position(state)

    def on_hanging_skaf(self, state): self.main_ctrl.change_hanging_skaf(state)

    def on_full_type_object(self, index): self.main_ctrl.change_full_type_object(index)

    def on_object_place(self, index): self.main_ctrl.change_object_place(index)

    def on_type_object(self, index): self.main_ctrl.change_type_object(index)

    def on_article(self, text): self.main_ctrl.change_article(text)

    def on_user_type_object(self, text): self.main_ctrl.change_user_type_object(text)

    def on_gap_right(self, value): self.main_ctrl.change_gap_right(value)

    def on_gap_left(self, value): self.main_ctrl.change_gap_left(value)

    def on_gap_back(self, value): self.main_ctrl.change_gap_back(value)

    def on_gap_front(self, value): self.main_ctrl.change_gap_front(value)

    def on_gap_down(self, value): self.main_ctrl.change_gap_down(value)

    def on_cover_corner(self, state): self.main_ctrl.change_cover_corner(state)


###########################
# ctrls\MainController.py #
###########################
from PyQt5 import QtWidgets


class MainController(object):

    def __init__(self, model):
        self.model = model

    #### функции события виджета ####
    def change_contact_type(self, index):
        self.model.contact_type = index
        print('DEBUG: change_contact_type вызывается со значением arg:', index)

    def change_forma_carcase(self, index):
        self.model.forma_carcase = index
        print('DEBUG: change_forma_carcase вызывается со значением arg:', index)

    def change_name_object(self, text):
        self.model.name_object = text
        print('DEBUG: change_name_object вызывается со значением arg:', text)

    def change_width(self, value):
        self.model.width = value
        print('DEBUG: change_width вызывается со значением arg:', value)

    def change_depth(self, value):
        self.model.depth = value
        print('DEBUG: change_depth вызывается со значением arg:', value)

    def change_height(self, value):
        self.model.height = value
        print('DEBUG: change_height вызывается со значением arg:', value)

    def change_dm(self, value):
        self.model.dm = value
        print('DEBUG: change_dm вызывается со значением arg:', value)

    def change_wm(self, value):
        self.model.wm = value
        print('DEBUG: change_wm вызывается со значением arg:', value)

    def change_bevel_position(self, state):
        self.model.bevel_position = state
        print('DEBUG: change_bevel_position вызывается со значением arg:', state)

    def change_hanging_skaf(self, state):
        self.model.hanging_skaf = state
        print('DEBUG: change_hanging_skaf вызывается со значением arg:', state)

    def change_full_type_object(self, index):
        self.model.full_type_object = index
        print('DEBUG: change_full_type_object вызывается со значением arg:', index)

    def change_object_place(self, index):
        self.model.object_place = index
        print('DEBUG: change_object_place вызывается со значением arg:', index)

    def change_type_object(self, index):
        self.model.type_object = index
        print('DEBUG: change_type_object вызывается со значением arg:', index)

    def change_article(self, text):
        self.model.article = text
        print('DEBUG: change_article вызывается со значением arg:', text)

    def change_user_type_object(self, text):
        self.model.user_type_object = text
        print('DEBUG: change_user_type_object вызывается со значением arg:', text)

    def change_gap_right(self, value):
        self.model.gap_right = value
        print('DEBUG: change_gap_right вызывается со значением arg:', value)

    def change_gap_left(self, value):
        self.model.gap_left = value
        print('DEBUG: change_gap_left вызывается со значением arg:', value)

    def change_gap_back(self, value):
        self.model.gap_back = value
        print('DEBUG: change_gap_back вызывается со значением arg:', value)

    def change_gap_front(self, value):
        self.model.gap_front = value
        print('DEBUG: change_gap_front вызывается со значением arg:', value)

    def change_gap_down(self, value):
        self.model.gap_down = value
        print('DEBUG: change_gap_down вызывается со значением arg:', value)

    def change_cover_corner(self, state):
        self.model.cover_corner = state
        print('DEBUG: change_cover_corner вызывается со значением arg:', state)


##################
# model\Model.py #
##################
from PyQt5 import QtGui


class Model(object):

    #### свойства для значения содержимого модели Qt ####
    @property
    def contact_type_items(self):
        return self.contact_type_model.stringList()

    @contact_type_items.setter
    def contact_type_items(self, value):
        self.contact_type_model.setStringList(value)

    @property
    def forma_carcase_items(self):
        return self.forma_carcase_model.stringList()

    @forma_carcase_items.setter
    def forma_carcase_items(self, value):
        self.forma_carcase_model.setStringList(value)

    @property
    def full_type_object_items(self):
        return self.full_type_object_model.stringList()

    @full_type_object_items.setter
    def full_type_object_items(self, value):
        self.full_type_object_model.setStringList(value)

    @property
    def object_place_items(self):
        return self.object_place_model.stringList()

    @object_place_items.setter
    def object_place_items(self, value):
        self.object_place_model.setStringList(value)

    @property
    def type_object_items(self):
        return self.type_object_model.stringList()

    @type_object_items.setter
    def type_object_items(self, value):
        self.type_object_model.setStringList(value)

    def __init__(self):
        self._update_funcs = []
        self.config_section = 'settings'
        self.config_options = (
            ('contact_type', 'getint'),
            ('forma_carcase', 'getint'),
            ('name_object', 'get'),
            ('pict_karkase', 'get'),
            ('width', 'getint'),
            ('depth', 'getint'),
            ('height', 'getint'),
            ('dm', 'getint'),
            ('wm', 'getint'),
            ('bevel_position', 'getboolean'),
            ('hanging_skaf', 'getboolean'),
            ('full_type_object', 'getint'),
            ('object_place', 'getint'),
            ('type_object', 'getint'),
            ('article', 'get'),
            ('user_type_object', 'get'),
            ('gap_right', 'getint'),
            ('gap_left', 'getint'),
            ('gap_back', 'getint'),
            ('gap_front', 'getint'),
            ('gap_down', 'getint'),
            ('cover_corner', 'getboolean'),
        )

        #### создание моделей Qt для совместимых типов виджетов ####
        self.contact_type_model = Qt.QStringListModel()
        self.forma_carcase_model = Qt.QStringListModel()
        self.full_type_object_model = Qt.QStringListModel()
        self.object_place_model = Qt.QStringListModel()
        self.type_object_model = Qt.QStringListModel()

        #### переменные модели ####
        self.contact_type = None
        self.forma_carcase = None
        self.name_object = None
        self.pict_karkase = None
        self.width = None
        self.depth = None
        self.height = None
        self.dm = None
        self.wm = None
        self.bevel_position = None
        self.hanging_skaf = None
        self.full_type_object = None
        self.object_place = None
        self.type_object = None
        self.article = None
        self.user_type_object = None
        self.gap_right = None
        self.gap_left = None
        self.gap_back = None
        self.gap_front = None
        self.gap_down = None
        self.cover_corner = None

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def announce_update(self):
        for func in self._update_funcs:
            func()


##########
# App.py #
##########
import sys
from PyQt5 import Qt
from model.Model import Model
from ctrls.MainController import MainController
from views.MainView import MainView


class App(Qt.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())



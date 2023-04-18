from pywinauto import Desktop, timings
from pywinauto.application import Application
from os.path import isfile


def test_сreate_project():
    #Create with toolbar
    timings.always_wait_until(10, 10)
    #Select the main window
    main_dlg = Desktop(backend='uia').ZNZ
    #Click on the create project dutton
    main_dlg.button.click_input()
    #Select folder
    folder_selection_dlg = Application().connect(title='Выбор папки', timeout=10)
    folder_selection_dlg.window(title='Выбор папки').child_window(title='Выбор папки',
                                                                  class_name='Button').click_input()
    #Change name of project
    main_dlg.child_window(auto_id='2234', control_type='Edit').click_input()
    main_dlg.child_window(auto_id='2234', control_type='Edit').type_keys('^a {DELETE}')
                                                                    
    main_dlg.child_window(auto_id='2234', control_type='Edit').type_keys('ПС Ольгино',
                                                                         with_spaces=True,
                                                                         pause=0.05)
    #Accept changes                                                       
    main_dlg.button.click_input()
    #Close project
    main_dlg.child_window(title='Файл').click_input()
    main_dlg.MenuItem3.click_input()
    file_path = r'/ProjectZNZ/PS_Olgino/ПС Ольгино.xbpsc'
    assert isfile(file_path) == True
    



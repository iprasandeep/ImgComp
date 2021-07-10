
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFrame, QLineEdit, QPushButton, QComboBox, QFileDialog, QMainWindow, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import PyQt5.QtGui 
import PIL
from PIL import Image
import os, sys

from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys 


class App(QMainWindow):

    # QtWidgets.QMainWindow

    def __init__(self):
        super().__init__()
        width = 500
        height = 600
        self.setWindowIcon(QIcon("icons.png")) 
        self.setWindowTitle('Image-Compressor')
        self.setFixedSize(width, height)

        self.statusBar().showMessage('Status:')
        self.statusBar().setObjectName("status")
 
        self.setObjectName("main_window")

        with open("design.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
       

        self.initUI()
        self.image_width = 0
        

        
        
    def initUI(self):
        self.setWindowIcon(QIcon('icon.png')) 
        self.frame1 = QFrame(self)
        self.frame1.setObjectName("frame1")
        self.frame1.move(90, 90)
        self.frame1.mouseDoubleClickEvent = self.frame1_clicked

        self.frame1_heading = QLabel(self.frame1)
        self.frame1_heading.move(100, 8)
        self.frame1_heading.setText(" SINGLE IMAGE")
        self.frame1_heading.setObjectName("frame1_heading")

        self.frame1_para = QLabel(self.frame1)
        self.frame1_para.setText("If you have only one image then we'll recordmend you to click here.")
        self.frame1_para.setWordWrap(True)
        self.frame1_para.move(10,25)
        self.frame1_para.setObjectName("frame2_para")


        self.frame2 = QFrame(self)
        self.frame2.setObjectName("frame1")
        self.frame2.move(90, 250)
        self.frame2.mouseDoubleClickEvent = self.frame2_clicked


        self.frame2_heading = QLabel(self.frame2)
        self.frame2_heading.move(95, 8)
        self.frame2_heading.setText("MULTIPLE IMAGES")
        self.frame2_heading.setObjectName("frame2_heading")

        self.frame2_para = QLabel(self.frame2)
        self.frame2_para.setText("If you have multiple images then we'll recodmend you to click here.")
        self.frame2_para.setWordWrap(True)
        self.frame2_para.move(10,25)
        self.frame2_para.setObjectName("frame2_para")


        # ------------------New Window One----------------------
        
        self.nframe1 = QFrame(self)
        self.nframe1.setObjectName("frame3")
        self.nframe1.move(58, 100)
        self.nframe1.setVisible(False)
        
        # ------------------New Window Two----------------------

        self.frame3 = QFrame(self)
        self.frame3.setObjectName("frame3")
        self.frame3.move(58,100)
        self.frame3.setVisible(False)
        
        self.back_arrow = QLabel(self.nframe1)
        self.back_arrow.setObjectName("back_arrow")
        self.back_arrow.move(10,10)
        self.back_arrow.setTextFormat(Qt.RichText)
        self.back_arrow.setText("&#8617;")
        self.back_arrow.mousePressEvent = self.back_arrow_clicked

        

        self.back_arrow2 = QLabel(self.frame3)
        self.back_arrow2.setObjectName("back_arrow")
        self.back_arrow2.move(10,10)
        self.back_arrow2.setTextFormat(Qt.RichText)
        self.back_arrow2.setText("&#8617;")
        self.back_arrow2.mousePressEvent = self.back_arrow_clicked

        # -------------First Click Window----------------
        self.frame1_heading = QLabel(self.nframe1)
        self.frame1_heading.move(110, 8)
        self.frame1_heading.setText("COMPRESS ONE IMAGE")
        self.frame1_heading.setObjectName("frame1_heading")

        self.frame1_image = QLabel(self.nframe1)
        self.frame1_image.move(30, 55)
        self.frame1_image.setText("Select Image:")
        self.frame1_image.setObjectName("new_image1")

        # ---------------Select Directory-----------------
        self.frame1_img_path = QLineEdit(self.nframe1)
        self.frame1_img_path.setObjectName("img_path1")
        self.frame1_img_path.move(100, 90)


        
        #--------------text Box text 2--------------

        self.frame2_image = QLabel(self.nframe1)
        self.frame2_image.move(30, 125)
        self.frame2_image.setText("Select Image Quality:")
        self.frame2_image.setObjectName("new_image1")
        #--------------text Box button 2--------------
        self.image_quality1 = QLineEdit(self.nframe1)
        self.image_quality1.setObjectName("img_path2")
        self.image_quality1.move(100, 155)
        
        #-----------Compress Combo Box-----------------
        self.combo_quality = QComboBox(self.nframe1)
        self.combo_quality.addItem("High")
        self.combo_quality.addItem("Medium")
        self.combo_quality.addItem("Low")
        self.combo_quality.setObjectName("combo_box")
        self.combo_quality.move(270, 155)
        
        self.combo_quality.currentIndexChanged.connect(self.quality_change1)

        # ----------------Button for text box 1---------
        self.browse_button = QPushButton(self.nframe1)
        self.browse_button.setText("...")
        self.browse_button.move(280,90)
        self.browse_button.setObjectName("browse_button")
        self.browse_button.clicked.connect(self.select_file)

        # -------------------Button for Compress image------
        self.compress_image = QPushButton(self.nframe1)
        self.compress_image.setText("Compress Now")
        self.compress_image.setObjectName("compress_button")
        self.compress_image.move(150,250)
        self.compress_image.clicked.connect(self.resize_pic)

        # -----------------For Bulk images Window----------


        self.frame3_heading = QLabel(self.frame3)
        self.frame3_heading.move(100, 8)
        self.frame3_heading.setText("COMPRESS MULTIPLE IMAGES")
        self.frame3_heading.setObjectName("frame1_heading")

        self.frame3_image = QLabel(self.frame3)
        self.frame3_image.move(30, 55)
        self.frame3_image.setText("Select Directory:")
        self.frame3_image.setObjectName("new_image1")

        # ----------------Source Directory----------
        self.source_dir = QLineEdit(self.frame3)
        self.source_dir.setObjectName("img_path1")
        self.source_dir.move(100, 90)
        
        #--------------Destination Directory-----------
        self.dest_dir = QLineEdit(self.frame3)
        self.dest_dir.setObjectName("img_path2")
        self.dest_dir.move(100, 155)
     

        #--------------text Box text new--------------

        self.frame3_image = QLabel(self.frame3)
        self.frame3_image.move(30, 125)
        self.frame3_image.setText("Select Destination Directory:")
        self.frame3_image.setObjectName("new_image1")
        
       

        #-----------Compress Combo Box new--------------
        

        self.combo_quality3 = QPushButton(self.frame3)
        self.combo_quality3.setText("...")
        self.combo_quality3.clicked.connect(self.select_dir2)
        self.combo_quality3.move(270, 155)


        # ----------------Button for text box new-----------
        self.browse_button3 = QPushButton(self.frame3)
        self.browse_button3.setText("...")
        self.browse_button3.move(280, 90)
        self.browse_button3.setObjectName("browse_button")
        self.browse_button3.clicked.connect(self.select_dir1)
       
        # --------------Button for Compress image new-------
        self.compress_image3 = QPushButton(self.frame3)
        self.compress_image3.setText("Compress Now")
        self.compress_image3.setObjectName("compress_button")
        self.compress_image3.move(150, 300)
        self.compress_image3.clicked.connect(self.resize_folders)

        self.frame3_image = QLabel(self.frame3)
        self.frame3_image.move(30, 190)
        self.frame3_image.setText("Choose Quality:")
        self.frame3_image.setObjectName("new_image1")
    
    # ----------Select Quality---------------------
        self.image_quality2 = QLineEdit(self.frame3)
        self.image_quality2.setObjectName("img_path2")
        self.image_quality2.move(100, 220)


        self.combo_quality3 = QComboBox(self.frame3)
        self.combo_quality3.addItem("High")
        self.combo_quality3.addItem("Medium")
        self.combo_quality3.addItem("Low")
        self.combo_quality3.setObjectName("combo_box")
        self.combo_quality3.move(275, 220)
        self.combo_quality3.currentIndexChanged.connect(self.quality_change1)

                
        self.show()

#-----------------Browser Button-----------------

    def select_file(self):
        options = QFileDialog.Options()
   
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","All Files(*);;JPEG;;PNG;;JPEG (*.jpg,*.png,*.jpeg)")
        if fileName:
            print(fileName)
            self.frame1_img_path.setText(fileName)
            img = Image.open(fileName)
            self.image_width = img.width
            self.image_quality1.setText(str(self.image_width))

    def quality_change1(self):
        if self.combo_quality.currentText() == 'High':
            self.image_quality1.setText(str(int(self.image_width)))
           
        if self.combo_quality.currentText() == 'Medium':
            self.image_quality1.setText(str(int(self.image_width/2)))
            
        if self.combo_quality.currentText() == 'Low':
            self.image_quality1.setText(str(int(self.image_width/3)))
        
        if self.combo_quality3.currentText() == 'High':
            self.image_quality2.setText(str(int(self.image_width)))

        if self.combo_quality3.currentText() == 'Medium':
            self.image_quality2.setText(str(int(self.image_width/2)))

        if self.combo_quality3.currentText() == 'Low':
            self.image_quality2.setText(str(int(self.image_width/3)))

        

        
    # ----------------Resize pic for single image-------------------
    def resize_pic(self):
        old_pic = self.frame1_img_path.text()
        print(old_pic)

        print(self.image_width)
        direct1 = self.frame1_img_path.text().split("/")
        print(direct1)

        new_pic = ""
        new_pic_name, okPressed = QInputDialog.getText(
            self, "Save Image As", "Input Name:", QLineEdit.Normal, "")

        if okPressed and new_pic_name != '':
            if old_pic[-4:] == ".jpeg":
                new_pic_name += ".jpeg"

            if old_pic[-4:] == ".jpg":
                new_pic_name += ".jpg"

            if old_pic[-4:] == ".png":
                new_pic_name += ".png"
            else:
                old_pic[-4:] == "jpeg"

            print(new_pic_name)

            new_pic = ""

            for directory in direct1[:-1]:
                new_pic = new_pic + directory + "/"

            new_pic += new_pic_name
            print(new_pic)

        self.compress_pic(old_pic, new_pic,int(self.image_quality1.text()))
        self.statusBar().showMessage('Status: Compressed!!')
        # print("compressed")


    def resize_folders(self):
        
        
        directory = self.source_dir.text()
        print(directory)
        files = os.listdir(directory)
       
        dest_direcotry = self.dest_dir.text()
        for file in files:
            if file[-4:] == '.jpg' or file[-4:]=='.JPG' or file[-4:]=='.png' or file[-4:]=='.PNG' or file[-5:]=='.jpeg' or file[-5:]=='.JPEG':
                
                old_pic = directory+"/"+file
                new_pic = dest_direcotry+"/"+file


                img = Image.open(old_pic)
                self.image_width = img.width
                self.image_quality2.setText(str(self.image_width))

                self.compress_pic(old_pic, new_pic, int(self.image_quality1.text()))

            # else:
            #     continue
            self.statusBar().showMessage("Status: Compressed!")
    def compress_pic(self, old_pic, new_pic, my_width):

        try: 

            img = Image.open(old_pic)
            # my_width = int(self.image_quality1.text())

            wpercent = (my_width/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((my_width, hsize), PIL.Image.ANTIALIAS)
            img.save(new_pic)
        except Exception as e:
            self.statusBar().showMessage("Status:" + str(e))


# -----------------------Resize Pic for Single Image End------------------------
  

    def select_dir1(self):
        source_folder = QFileDialog.getExistingDirectory(self, "QFileDialog.getExistingDirectory()", "Select project folder(*)")
        print(source_folder)
        self.source_dir.setText(source_folder)

        # files = source_dir.setText(folder)
        files = os.listdir(source_folder)
        first_pic = source_folder + "/" + files[0]
        img = Image.open(first_pic)
        self.image_width = img.width
        self.image_quality2.setText(str(int(self.image_width)))
        print(files)

    def select_dir2(self):
        dest_folder = QFileDialog.getExistingDirectory(self, "QFileDialog.getExistingDirectory()", "Select project folder(*)")
        print(dest_folder)
        self.dest_dir.setText(dest_folder)
    
#---------------clicked new window Functions----------------
    def back_arrow_clicked(self, event):
        self.frame1.setVisible(True)
        self.frame2.setVisible(True)
        self.nframe1.setVisible(False)
        self.frame3.setVisible(False)

    
    def frame1_clicked(self, event):
        self.frame1.setVisible(False)
        self.frame2.setVisible(False)
        self.nframe1.setVisible(True)
        self.frame3.setVisible(False)
        self.setObjectName("main_window2")
        print("Single Clicked By Prasan")
        print(event)
    
    def frame2_clicked(self, event):
        self.frame2.setVisible(False)
        self.frame1.setVisible(False)
        self.nframe1.setVisible(False)

        self.frame3.setVisible(True)
        
        print("Dir Clicked By Prasan")
        print(event)
#-------------------- Clicked new window-----------------

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('CodersGeek.png'))
    ex = App()
    sys.exit(app.exec_())

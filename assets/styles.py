FRAME_PAGE_STYLE = """
QFrame{
    background-color: white;
    border-radius: 0px;
    margin: 0px 0px 0px 0px;
    padding: 0px;
    border: solid 0px #FFFFFF;
}
"""
DIALOG_BUTTON = """
QPushButton:enabled {
    font-family: SourceSansPro-Semibold;
    color: #FFFFFF;
    background-color: #43B54A; 
    border: none;
    border-radius: 1px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    padding: 5px 15px;
}

QPushButton:disabled {
    font-family: SourceSansPro-Semibold;
    color: #FFFFFF;
    background-color: gray; 
    border: none;
    border-radius: 1px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    padding: 5px 15px;
}
"""

LABEL_HEADER = """
QLabel {
  font-family: SourceSansPro-bold;
  font-size:19px;
  color: #373737;
  margin-bottom:1px;  
}
"""

TABLE_WIDGET_STYLE = """
QTableWidget
{
    alternate-background-color: #F5F5F5;
    background-color: #FFFFFF;
    border: none;
    gridline-color: #FFFFFF;
    font-family: SourceSansPro-Regular;
    font-size: 14px;
}

QTableWidget::item
{
    padding: 0.3ex;
    gridline-color: #FFFFFF;
}

QHeaderView
{
    font-family: SourceSansPro-bold;
    gridline-color: black;
    vertical-alignment
}

QHeaderView::section 
{
    font-size: 19px;
    border: none;
    margin-bottom:0px;
    background-color: white;    
}

QTableWidget::item:pressed
{
    background: Darkslategrey;
    color: #FFFFFF;
}

QTableWidget::item:selected:active
{
    background: Darkslategrey;
    color: #FFFFFF;
}

QTableWidget::item:selected:hover
{
    background-color: Darkslategrey;
    color: #FFFFFF;
}

QTableWidget::item:hover
{
    background-color:Darkslategrey; 
    color:#FFFFFF;
}
"""

SCROLL_AREA = """
QScrollArea {
   background: #FFFFFF;
}

QScrollBar:vertical {
   background-color: #F5F5F5;
   margin: 20px 0 20px 0;
}

QScrollBar::handle:vertical {
   border-radius: 3px;
   border: 2px solid #CBCBCB;
   background: #F1F1F1;
}

QScrollBar::add-line:vertical {
   background: #FFFFFF;
   subcontrol-origin: margin;
   subcontrol-position: bottom;
   height: 20px;
}

QScrollBar::sub-line:vertical {
   background: #FFFFFF;
   subcontrol-origin: margin;
   subcontrol-position: top;
   height: 20px;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
   background: #FAFAFA;
   border: 2px solid #CBCBCB;
   border-radius: 3px;
}

QScrollBar::up-arrow:vertical {
   image: url(assets/style/up_arrow.png);
   width: 20px;
   height: 20px;
}

QScrollBar::down-arrow:vertical {
   image: url(assets/style/down_arrow.png);
   width: 20px;
   height: 20px;
}
"""

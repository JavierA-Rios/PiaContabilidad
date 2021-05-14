import sys
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None





class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PIA"
        description = "Proyecto Final."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        #widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        #widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        #def openCloseLeftBox():
            #UIFunctions.toggleLeftBox(self, True)
        #widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        #widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        #def openCloseRightBox():
            #UIFunctions.toggleRightBox(self, True)
        #widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.Inicio)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.Inicio)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.Presupuesto_maestro) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            def moneda(dinero):
                total = "${:,.2f}".format(dinero)
                total_str = str(total)
                return total_str
#Nombre de la empresa
            nombre_empresa = str(widgets.negocio_nombre.text())
            widgets.nombre_empresa.setText(nombre_empresa)
            widgets.nombre_empresa_2.setText(nombre_empresa)
            widgets.nombre_empresa_3.setText(nombre_empresa)
            widgets.nombre_empresa_4.setText(nombre_empresa)

#1. Presupuesto de ventas
    #semestre 1 inicio
        #Producto 1 inicio
            unidades_vta1 = float(widgets.unidades_venta_1.text())
            precio_vta1 = float(widgets.precio_venta_1.text())
            suma = precio_vta1 * unidades_vta1
            suma_str = str(suma)
            widgets.importe_1.setText(moneda(suma))
        #Producto 1 fin

        #Producto 2 inicio
            unidades_vta2 = float(widgets.unidades_venta_2.text())
            precio_vta2 = float(widgets.precio_venta_2.text())
            suma2 = precio_vta2 * unidades_vta2
            suma_str2 = str(suma2)
            widgets.importe_2.setText(moneda(suma2))
        #Producto 2 fin

        #Producto 3 inicio
            unidades_vta3 = float(widgets.unidades_venta_3.text())
            precio_vta3 = float(widgets.precio_venta_3.text())
            suma3 = precio_vta3 * unidades_vta3
            suma_str3 = str(suma3)
            widgets.importe_3.setText(moneda(suma3))
        #Producto 3 fin
        #total semestre inicio
            total = (suma + suma2 + suma3)
            total_str = str(total)
            widgets.semestre1_t.setText(moneda(total))
        #total semestre fin
    #semestre 1 fin


    #semestre 2 inicio
        #Producto 1 inicio
            unidades_vtas21 = float(widgets.unidades_venta_s21.text())
            precio_vtas21 = float(widgets.precio_venta_s21.text())
            sumas21 = precio_vtas21 * unidades_vtas21
            suma_strs21 = str(sumas21)
            widgets.importe_s21.setText(moneda(sumas21))
        #Producto 1 fin

        #Producto 2 inicio
            unidades_vtas22 = float(widgets.unidades_venta_s22.text())
            precio_vtas22 = float(widgets.precio_venta_s22.text())
            sumas22 = precio_vtas22 * unidades_vtas22
            suma_strs22 = str(sumas22)
            widgets.importe_s22.setText(moneda(sumas22))
        #Producto 2 fin

        #Producto 3 inicio
            unidades_vtas23 = float(widgets.unidades_venta_s23.text())
            precio_vtas23 = float(widgets.precio_venta_s23.text())
            sumas23 = precio_vtas23 * unidades_vtas23
            suma_strs23 = str(sumas23)
            widgets.importe_s23.setText(moneda(sumas23))
        #Producto 3 fin
        #total semestre 2 inicio
            totals2 = (sumas21 + sumas22 + sumas23)
            total_strs2 = str(totals2)
            widgets.semestre2_t.setText(moneda(totals2))
        #total semestre 2 fin
    #semestre 2 fin

    #Totales presupuesto de ventas inicio
        #importes
        imp_1_t = suma + sumas21
        imp_2_t = suma2 + sumas22
        imp_3_t = suma3 + sumas23
        imp_1_str = str(imp_1_t)
        imp_2_str = str(imp_2_t)
        imp_3_str = str(imp_3_t)
        widgets.t_importes_p1.setText(moneda(imp_1_t))
        widgets.t_importes_p2.setText(moneda(imp_2_t))
        widgets.t_importes_p3.setText(moneda(imp_3_t))
        #totales finales
        s1_t = total
        s2_t = totals2
        t_fin = s1_t + s2_t
        t_fin_str = str(t_fin)
        widgets.sem_t.setText(moneda(t_fin))
    #Totales presupuesto de ventas fin

#2. Determinación del saldo de Clientes y Flujo de Entradas

        saldo_clientes = float(widgets.saldo_clientes.text())
        saldo_clientes_str = widgets.saldo_clientes.text()
        ventas_2020 = widgets.ventas2020.setText(moneda(t_fin))
        total_clients = saldo_clientes + t_fin
        total_clients_str = str(total_clients)
        total_clients_final = widgets.total_clientes.setText(moneda(total_clients))
        widgets.cobranza1.setText(moneda(saldo_clientes))
        cobranza2 = t_fin * 0.8
        cobranza2_str = str(cobranza2)
        widgets.cobranza2.setText(moneda(cobranza2))
        total_entradas = saldo_clientes + cobranza2
        total_entradas_str = str(total_entradas)
        widgets.total_entradas.setText(moneda(total_entradas))
        saldo_clientes_2020 = total_clients - total_entradas
        saldo_clientes_2020_str = str(saldo_clientes_2020)
        widgets.total_clientes_2.setText(moneda(saldo_clientes_2020))

#3. Presupuesto de producción
    #unidades venta
        unidades_vta1_str = widgets.unidades_venta_1.text()
        unidades_vta2_str = widgets.unidades_venta_2.text()
        unidades_vta3_str = widgets.unidades_venta_3.text()
    #unidades venta semestre 2
        unidades_vta1s2_str = widgets.unidades_venta_s21.text()
        unidades_vta1s2 = float(widgets.unidades_venta_s21.text())
        unidades_vta2s2 = float(widgets.unidades_venta_s22.text())
        unidades_vta3s2 = float(widgets.unidades_venta_s23.text())
        unidades_vta2s2_str = widgets.unidades_venta_s22.text()
        unidades_vta3s2_str = widgets.unidades_venta_s23.text()
    #Campos de entrada
        #semestre 1
        inventario_prod1_s1 = float(widgets.inventario_final1.text())
        inventario_prod1_s1_str = widgets.inventario_final1.text()
        inventario_prod2_s1 = float(widgets.inventario_final1prod2.text())
        inventario_prod2_s1_str = widgets.inventario_final1prod2.text()
        inventario_prod3_s1 = float(widgets.inventario_final1prod3.text())
        inventario_prod3_s1_str = widgets.inventario_final1prod3.text()
        #semestre 2
        inventario_prod1_s2 = float(widgets.inventario_final2.text())
        inventario_prod2_s2 = float(widgets.inventario_final2prod2.text())
        inventario_prod3_s2 = float(widgets.inventario_final2prod3.text())
        #inventario inicial
        inventario_inicial_p1 = float(widgets.inventario_inicial_1.text())
        inventario_inicial_p1_str = widgets.inventario_inicial_1.text()
        inventario_inicial_p2 = float(widgets.inventario_inicial_1_prod2.text())
        inventario_inicial_p2_s2 = int(widgets.inventario_final1prod2.text())
        inventario_inicial_p3 = float(widgets.inventario_final1prod3.text())

    #campos de salida
    #producto 1
            #unidades a vender
        widgets.prod1_unidades_vta1.setText("$"+unidades_vta1_str)
        widgets.prod1_unidades_vta2.setText("$"+unidades_vta1s2_str)
        total_prod_vtas = unidades_vta1 + unidades_vtas21
        total_prod_vtas_str = str(total_prod_vtas)
        widgets.prod1_unidades_tot.setText(moneda(total_prod_vtas))
            #inventario final
        inventario_total = float(widgets.inventario_final2.text())
        widgets.inventario_final_total.setText(moneda(inventario_total))
            #total de unidades semestre 1
        total_unidades = unidades_vta1 + inventario_prod1_s1
        total_unidades_str = str(total_unidades)
        widgets.unidades_total1.setText(moneda(total_unidades))
            #total de unidades semestre 2
        total_unidades_prod1s2 = float(widgets.unidades_venta_s21.text())
        total_unidades2 = total_unidades_prod1s2 + inventario_prod1_s2
        total_unidades2_str = str(total_unidades2)
        widgets.unidades_total2.setText(moneda(total_unidades2))
            #total de unidades
        tot_unidades = total_prod_vtas + inventario_total
        tot_unidades_str = str(tot_unidades)
        widgets.unidades_total_tot.setText(moneda(tot_unidades))
            #inventario inicial
        widgets.inventario_inicial_2.setText(moneda(inventario_prod1_s1))
        widgets.inventario_inicial_tot.setText(moneda(inventario_prod1_s1))
            #unidades a producir
        unidades_producir_s1 = total_unidades - inventario_inicial_p1
        unidades_producir_s1_str = str(unidades_producir_s1)
        widgets.uap1.setText(moneda(unidades_producir_s1))

        unidades_producir_s2 = total_unidades2 - inventario_inicial_p1
        unidades_producir_s2_str = str(unidades_producir_s2)
        widgets.uap2.setText(moneda(unidades_producir_s2))

        unidades_producir_t = unidades_producir_s1 + unidades_producir_s2
        unidades_producir_t_str = str(unidades_producir_t)
        widgets.uapt1.setText(moneda(unidades_producir_t))

    #producto 2
            #unidades a vender
        widgets.prod2_unidades_vta1.setText(moneda(unidades_vta2))
        widgets.prod2_unidades_vta2.setText(moneda(unidades_vta2s2))
        total_prod2_vtas = unidades_vta2 + unidades_vtas22
        total_prod2_vtas_str = str(total_prod2_vtas)
        widgets.prod2_unidades_vtatot.setText(moneda(total_prod2_vtas))
            #inventario final
        inventario_total_prod2 = float(widgets.inventario_final2prod2.text())
        widgets.inventario_final3prod2.setText(moneda(inventario_total_prod2))
            #total de unidades semestre 1
        total_unidades_prod2 = unidades_vta2 + inventario_prod2_s1
        total_unidades_prod2_str = str(total_unidades_prod2)
        widgets.unidades_total1_prod2.setText(moneda(total_unidades_prod2))
            #total de unidades semestre 2
        total_unidades_prod2_s2 = unidades_vtas22 + inventario_prod2_s2
        total_unidades2_prod2_s2_str = str(total_unidades_prod2_s2)
        widgets.unidades_total2_prod2.setText(moneda(total_unidades_prod2_s2))
            #total de unidades
        tot_unidades_p2_prod2 = total_prod2_vtas + inventario_total_prod2
        tot_unidades_p2_str = str(tot_unidades_p2_prod2)
        widgets.unidades_total3_prod2.setText(moneda(tot_unidades_p2_prod2))
            #inventario inicial
        widgets.inventario_inicial_2_prod2.setText(moneda(inventario_prod2_s1))
        widgets.inventario_inicial_3_prod2.setText(moneda(inventario_prod2_s1))
            #unidades a producir
        unidades_producir_prod2_s1 = total_unidades_prod2 - inventario_inicial_p2
        unidades_producir_prod2_s1_str = str(unidades_producir_prod2_s1)
        widgets.uap1_prod2.setText(moneda(unidades_producir_prod2_s1))

        unidades_producir_prod2_s2 = total_unidades_prod2_s2 - inventario_inicial_p2
        unidades_producir_prod2_s2_str = str(unidades_producir_prod2_s2)
        widgets.uap2_prod2.setText(moneda(unidades_producir_prod2_s2))

        unidades_producir_t_prod2 = unidades_producir_prod2_s1 + unidades_producir_prod2_s2
        unidades_producir_t_prod2_str = str(unidades_producir_t_prod2)
        widgets.uapt2.setText(moneda(unidades_producir_t_prod2))

    #producto 3
        #unidades a vender
        widgets.prod3_unidades_vta1.setText(moneda(unidades_vta3))
        widgets.prod3_unidades_vta2.setText(moneda(unidades_vta3s2))
        total_prod3_vtas = unidades_vta3 + unidades_vtas23
        total_prod3_vtas_str = str(total_prod3_vtas)
        widgets.prod3_unidades_vtatot.setText(moneda(total_prod3_vtas))
        #inventario final
        inventario_total_prod3 = float(widgets.inventario_final2prod3.text())
        widgets.inventario_final3prod3.setText(moneda(inventario_total_prod3))
        #total de unidades semestre 1
        total_unidades_prod3 = unidades_vta3 + inventario_prod3_s1
        total_unidades_prod3_str = str(total_unidades_prod3)
        widgets.unidades_total1_prod3.setText(moneda(total_unidades_prod3))
        #total de unidades semestre 2
        total_unidades_prod3_s2 = unidades_vtas23 + inventario_prod3_s2
        total_unidades2_prod3_s2_str = str(total_unidades_prod3_s2)
        widgets.unidades_total2_prod3.setText(moneda(total_unidades_prod3_s2))
        #total de unidades
        tot_unidades_p3 = total_prod3_vtas + inventario_total_prod3
        tot_unidades_p3_str = str(tot_unidades_p3)
        widgets.unidades_total3_prod3.setText(moneda(tot_unidades_p3))
        #inventario inicial
        widgets.inventario_inicial_2_prod3.setText(moneda(inventario_prod3_s1))
        widgets.inventario_inicial_tot_prod3.setText(moneda(inventario_prod3_s1))
        #unidades a producir
        unidades_producir_prod3_s1 = total_unidades_prod3 - inventario_inicial_p3
        unidades_producir_prod3_s1_str = str(unidades_producir_prod3_s1)
        widgets.uap1_prod3.setText(moneda(unidades_producir_prod3_s1))

        unidades_producir_prod3_s2 = total_unidades_prod3_s2 - inventario_inicial_p3
        unidades_producir_prod3_s2_str = str(unidades_producir_prod3_s2)
        widgets.uap2_prod3.setText(moneda(unidades_producir_prod3_s2))

        unidades_producir_t_prod3 = unidades_producir_prod3_s1 + unidades_producir_prod3_s2
        unidades_producir_t_prod3_str = str(unidades_producir_t_prod3)
        widgets.uapt3.setText(moneda(unidades_producir_t_prod3))

#4. Presupuesto de requerimiento de materiales
    #variables de entrada
    #Requerimiento de material
        #producto1
        #A
        requerimiento_de_material_A_prod1_str = widgets.requerimiento_de_material_A_prod1.text()
        requerimiento_de_material_A_prod1 = float(widgets.requerimiento_de_material_A_prod1.text())
        #B
        requerimiento_de_material_B_prod1_str = widgets.requerimiento_de_material_B_prod1.text()
        requerimiento_de_material_B_prod1 = float(widgets.requerimiento_de_material_B_prod1.text())
        #C
        requerimiento_de_material_C_prod1_str = widgets.requerimiento_de_material_C_prod1.text()
        requerimiento_de_material_C_prod1 = float(widgets.requerimiento_de_material_C_prod1.text())
        #producto 2
        #A
        requerimiento_de_material_A_prod2_str = widgets.requerimiento_de_material_A_prod2.text()
        requerimiento_de_material_A_prod2 = float(widgets.requerimiento_de_material_A_prod2.text())
        #B
        requerimiento_de_material_B_prod2_str = widgets.requerimiento_de_material_B_prod2.text()
        requerimiento_de_material_B_prod2 = float(widgets.requerimiento_de_material_B_prod2.text())
        #C
        requerimiento_de_material_C_prod2_str = widgets.requerimiento_de_material_C_prod2.text()
        requerimiento_de_material_C_prod2 = float(widgets.requerimiento_de_material_C_prod2.text())
        #producto 3
        #A
        requerimiento_de_material_A_prod3_str = widgets.requerimiento_de_material_A_prod3.text()
        requerimiento_de_material_A_prod3 = float(widgets.requerimiento_de_material_A_prod3.text())
        #B
        requerimiento_de_material_B_prod3_str = widgets.requerimiento_de_material_B_prod3.text()
        requerimiento_de_material_B_prod3 = float(widgets.requerimiento_de_material_B_prod3.text())
        #C
        requerimiento_de_material_C_prod3_str = widgets.requerimiento_de_material_C_prod3.text()
        requerimiento_de_material_C_prod3 = float(widgets.requerimiento_de_material_C_prod3.text())

    #Salidas
        #unidades a producir producto 1
        widgets.unidades_produccion_s1_prod1.setText(moneda(unidades_producir_s1))
        widgets.unidades_produccion_s2_prod1.setText(moneda(unidades_producir_s2))
        widgets.unidades_produccion_total_prod1.setText(moneda(unidades_producir_t))
        #unidades a producir producto 2
        widgets.unidades_produccion_s1_prod2.setText(moneda(unidades_producir_prod2_s1))
        widgets.unidades_produccion_s2_prod2.setText(moneda(unidades_producir_prod2_s2))
        widgets.unidades_produccion_total_prod2.setText(moneda(unidades_producir_t_prod2))
        #unidades a producir producto 3
        widgets.unidades_produccion_s1_prod3.setText(moneda(unidades_producir_prod3_s1))
        widgets.unidades_produccion_s2_prod3.setText(moneda(unidades_producir_prod3_s2))
        widgets.unidades_produccion_total_prod3.setText(moneda(unidades_producir_t_prod3))

        #Requerimiento de material semestre 2 producto 1
        #A
        widgets.requerimiento_material_A_s2_prod1.setText(moneda(requerimiento_de_material_A_prod1))
        widgets.requerimiento_material_A_total_prod1.setText(moneda(requerimiento_de_material_A_prod1))
        #B
        widgets.requerimiento_material_B_s2_prod1.setText(moneda(requerimiento_de_material_B_prod1))
        widgets.requerimiento_material_B_total_prod1.setText(moneda(requerimiento_de_material_B_prod1))
        #C
        widgets.requerimiento_material_C_s2_prod1.setText(moneda(requerimiento_de_material_C_prod1))
        widgets.requerimiento_material_C_total_prod1.setText(moneda(requerimiento_de_material_C_prod1))
        #Requerimiento de material semestre 2 producto 2
        #A
        widgets.requerimiento_material_A_s2_prod2.setText(moneda(requerimiento_de_material_A_prod2))
        widgets.requerimiento_material_A_total_prod2.setText(moneda(requerimiento_de_material_A_prod2))
        #B
        widgets.requerimiento_material_B_s2_prod2.setText(moneda(requerimiento_de_material_B_prod2))
        widgets.requerimiento_material_B_total_prod2.setText(moneda(requerimiento_de_material_B_prod2))
        #C
        widgets.requerimiento_material_C_s2_prod2.setText(moneda(requerimiento_de_material_C_prod2))
        widgets.requerimiento_material_C_total_prod2.setText(moneda(requerimiento_de_material_C_prod2))
        #Requerimiento de material semestre 2 producto 3
        #A
        widgets.requerimiento_material_A_s2_prod3.setText(moneda(requerimiento_de_material_A_prod3))
        widgets.requerimiento_material_A_total_prod3.setText(moneda(requerimiento_de_material_A_prod3))
        #B
        widgets.requerimiento_material_B_s2_prod3.setText(moneda(requerimiento_de_material_B_prod3))
        widgets.requerimiento_material_B_total_prod3.setText(moneda(requerimiento_de_material_B_prod3))
        #C
        widgets.requerimiento_material_C_s2_prod3.setText(moneda(requerimiento_de_material_C_prod3))
        widgets.requerimiento_material_C_total_prod3.setText(moneda(requerimiento_de_material_C_prod3))

        #Total Material Requerido producto 1
        #A
        #Semestre 1
        total_A_Producto1 =  unidades_producir_s1 * requerimiento_de_material_A_prod1
        total_A_Producto1_str = str(total_A_Producto1)
        widgets.material_A_requerido_s1_prod1.setText(moneda(total_A_Producto1))
        #semestre 2
        total_A_Producto1_s2 =  unidades_producir_s2 * requerimiento_de_material_A_prod1
        total_A_Producto1_s2_str = str(total_A_Producto1_s2)
        widgets.material_A_requerido_s2_prod1.setText(moneda(total_A_Producto1_s2))
        #total
        total_A_Producto1_final =  total_A_Producto1 + total_A_Producto1_s2
        total_A_Producto1_final_str = str(total_A_Producto1_final)
        widgets.material_A_requerido_total_prod1.setText(moneda(total_A_Producto1_final))
        #B
        #Semestre 1
        total_B_Producto1 =  unidades_producir_s1 * requerimiento_de_material_B_prod1
        total_B_Producto1_str = str(total_B_Producto1)
        widgets.material_B_requerido_s1_prod1.setText(moneda(total_B_Producto1))
        #semestre 2
        total_B_Producto1_s2 =  unidades_producir_s2 * requerimiento_de_material_B_prod1
        total_B_Producto1_s2_str = str(total_B_Producto1_s2)
        widgets.material_B_requerido_s2_prod1.setText(moneda(total_B_Producto1_s2))
        #total
        total_B_Producto1_final =  total_B_Producto1 + total_B_Producto1_s2
        total_B_Producto1_final_str = str(total_B_Producto1_final)
        widgets.material_B_requerido_total_prod1.setText(moneda(total_B_Producto1_final))
        #C
        #Semestre 1
        total_C_Producto1 =  unidades_producir_s1 * requerimiento_de_material_C_prod1
        total_C_Producto1_str = str(total_C_Producto1)
        widgets.material_C_requerido_s1_prod1.setText(moneda(total_C_Producto1))
        #semestre 2
        total_C_Producto1_s2 =  unidades_producir_s2 * requerimiento_de_material_C_prod1
        total_C_Producto1_s2_str = str(total_C_Producto1_s2)
        widgets.material_C_requerido_s2_prod1.setText(moneda(total_C_Producto1_s2))
        #total
        total_C_Producto1_final =  total_C_Producto1 + total_C_Producto1_s2
        total_C_Producto1_final_str = str(total_C_Producto1_final)
        widgets.material_C_requerido_total_prod1.setText(moneda(total_C_Producto1_final))

        #Total Material Requerido producto 2
        #A
        #Semestre 1
        total_A_Producto2 =  unidades_producir_prod2_s1 * requerimiento_de_material_A_prod2
        total_A_Producto2_str = str(total_A_Producto2)
        widgets.material_A_requerido_s1_prod2.setText(moneda(total_A_Producto2))
        #semestre 2
        total_A_Producto2_s2 =  unidades_producir_prod2_s2 * requerimiento_de_material_A_prod2
        total_A_Producto2_s2_str = str(total_A_Producto2_s2)
        widgets.material_A_requerido_s2_prod2.setText(moneda(total_A_Producto2_s2))
        #total
        total_A_Producto2_final =  total_A_Producto2 + total_A_Producto2_s2
        total_A_Producto2_final_str = str(total_A_Producto2_final)
        widgets.material_A_requerido_total_prod2.setText(moneda(total_A_Producto2_final))
        #B
        #Semestre 1
        total_B_Producto2 =  unidades_producir_prod2_s1 * requerimiento_de_material_B_prod2
        total_B_Producto2_str = str(total_B_Producto2)
        widgets.material_B_requerido_s1_prod2.setText(moneda(total_B_Producto2))
        #semestre 2
        total_B_Producto2_s2 =  unidades_producir_prod2_s2 * requerimiento_de_material_B_prod2
        total_B_Producto2_s2_str = str(total_B_Producto2_s2)
        widgets.material_B_requerido_s2_prod2.setText(moneda(total_B_Producto2_s2))
        #total
        total_B_Producto2_final =  total_B_Producto2 + total_B_Producto2_s2
        total_B_Producto2_final_str = str(total_B_Producto2_final)
        widgets.material_B_requerido_total_prod2.setText(moneda(total_B_Producto2_final))
        #C
        #Semestre 1
        total_C_Producto2 =  unidades_producir_prod2_s1 * requerimiento_de_material_C_prod2
        total_C_Producto2_str = str(total_C_Producto2)
        widgets.material_C_requerido_s1_prod2.setText(moneda(total_C_Producto2))
        #semestre 2
        total_C_Producto2_s2 =  unidades_producir_prod2_s2 * requerimiento_de_material_C_prod2
        total_C_Producto2_s2_str = str(total_C_Producto2_s2)
        widgets.material_C_requerido_s2_prod2.setText(moneda(total_C_Producto2_s2))
        #total
        total_C_Producto2_final =  total_C_Producto2 + total_C_Producto2_s2
        total_C_Producto2_final_str = str(total_C_Producto2_final)
        widgets.material_C_requerido_total_prod2.setText(moneda(total_C_Producto2_final))

        #Total Material Requerido producto 3
        #A
        #Semestre 1
        total_A_Producto3 =  unidades_producir_prod3_s1 * requerimiento_de_material_A_prod3
        total_A_Producto3_str = str(total_A_Producto3)
        widgets.material_A_requerido_s1_prod3.setText(moneda(total_A_Producto3))
        #semestre 2
        total_A_Producto3_s2 =  unidades_producir_prod3_s2 * requerimiento_de_material_A_prod3
        total_A_Producto3_s2_str = str(total_A_Producto3_s2)
        widgets.material_A_requerido_s2_prod3.setText(moneda(total_A_Producto3_s2))
        #total
        total_A_Producto3_final =  total_A_Producto3 + total_A_Producto3_s2
        total_A_Producto3_final_str = str(total_A_Producto3_final)
        widgets.material_A_requerido_total_prod3.setText(moneda(total_A_Producto3_final))
        #B
        #Semestre 1
        total_B_Producto3 =  unidades_producir_prod3_s1 * requerimiento_de_material_B_prod3
        total_B_Producto3_str = str(total_B_Producto3)
        widgets.material_B_requerido_s1_prod3.setText(moneda(total_B_Producto3))
        #semestre 2
        total_B_Producto3_s2 =  unidades_producir_prod3_s2 * requerimiento_de_material_B_prod3
        total_B_Producto3_s2_str = str(total_B_Producto3_s2)
        widgets.material_B_requerido_s2_prod3.setText(moneda(total_B_Producto3_s2))
        #total
        total_B_Producto3_final =  total_B_Producto3 + total_B_Producto3_s2
        total_B_Producto3_final_str = str(total_B_Producto3_final)
        widgets.material_B_requerido_total_prod3.setText(moneda(total_B_Producto3_final))
        #C
        #Semestre 1
        total_C_Producto3 =  unidades_producir_prod3_s1 * requerimiento_de_material_C_prod3
        total_C_Producto3_str = str(total_C_Producto3)
        widgets.material_C_requerido_s1_prod3.setText(moneda(total_C_Producto3))
        #semestre 2
        total_C_Producto3_s2 =  unidades_producir_prod3_s2 * requerimiento_de_material_C_prod3
        total_C_Producto3_s2_str = str(total_C_Producto3_s2)
        widgets.material_C_requerido_s2_prod3.setText(moneda(total_C_Producto3_s2))
        #total
        total_C_Producto3_final =  total_C_Producto3 + total_C_Producto3_s2
        total_C_Producto3_final_str = str(total_C_Producto3_final)
        widgets.material_C_requerido_total_prod3.setText(moneda(total_C_Producto3_final))
        #Total de requerimientos
        #semestre 1
        #A
        total_metros_A = (total_A_Producto1  + total_A_Producto2 + total_A_Producto3)
        total_metros_A_str = str(total_metros_A)
        widgets.material_A_metros_s1.setText(moneda(total_metros_A))
        #B
        total_metros_B = (total_B_Producto1 + total_B_Producto2 + total_B_Producto3)
        total_metros_B_str = str(total_metros_B)
        widgets.material_B_metros_s1.setText(moneda(total_metros_B))
        #C
        total_metros_C = (total_C_Producto1 + total_C_Producto2 + total_C_Producto3)
        total_metros_C_str = str(total_metros_C)
        widgets.material_C_metros_s1.setText(moneda(total_metros_C))

        #semestre 2
        #A
        total_metros_A_s2 = (total_A_Producto1_s2  + total_A_Producto2_s2 + total_A_Producto3_s2)
        total_metros_A_s2_str = str(total_metros_A_s2)
        widgets.material_A_metros_s2.setText(moneda(total_metros_A_s2))
        #B
        total_metros_B_s2 = (total_B_Producto1_s2 + total_B_Producto2_s2 + total_B_Producto3_s2)
        total_metros_B_s2_str = str(total_metros_B_s2)
        widgets.material_B_metros_s2.setText(moneda(total_metros_B_s2))
        #C
        total_metros_C_s2 = (total_C_Producto1_s2 + total_C_Producto2_s2 + total_C_Producto3_s2)
        total_metros_C_s2_str =  str(total_metros_C_s2)
        widgets.material_C_metros_s2.setText(moneda(total_metros_C_s2))

        #Total Materiales
        #A
        metros_A_total = total_metros_A + total_metros_A_s2
        metros_A_total_str = str(metros_A_total)
        widgets.material_A_metros_total.setText(moneda(metros_A_total))
        #B
        metros_B_total = total_metros_B + total_metros_B_s2
        metros_B_total_str = str(metros_B_total)
        widgets.material_B_metros_total.setText(moneda(metros_B_total))
        #C
        metros_C_total = total_metros_C + total_metros_C_s2
        metros_C_total_str = str(metros_C_total)
        widgets.material_C_metros_total.setText(moneda(metros_C_total))

#5. Presupuesto de Compra de Materiales.
    #Material A
        #Requerimiento de material
            #Semestre 1
        widgets.requerimiento_materiales_semestre1.setText(moneda(total_metros_A))
        #semestre 2
        widgets.requerimiento_materiales_semestre2.setText(moneda(total_metros_A_s2))
        #Total
        widgets.requerimiento_materiales_total.setText(moneda(metros_A_total))
    #inventario Final
        #semestre 1
        inventario_final_material_A_s1 = float(widgets.inventario_final_s1.text())
        inventario_final_material_A_s1_str = widgets.inventario_final_s1.text()
        #semestre 2
        inventario_final_material_A_s2 = float(widgets.inventario_final_s2.text())
        inventario_final_material_A_s2_str = widgets.inventario_final_s2.text()
        #Total
        widgets.inventario_final_totales.setText(moneda(inventario_final_material_A_s2))
    #total de materiales
        #semestre 1
        total_material_A = total_metros_A + inventario_final_material_A_s1
        total_material_A_str = str(total_material_A)
        widgets.total_materiales_semestre1.setText(moneda(total_material_A))
        #semestre 2
        total_material_A_s2 = total_metros_A_s2 + inventario_final_material_A_s2
        total_material_A_s2_str = str(total_material_A_s2)
        widgets.total_materiales_semestre2.setText(moneda(total_material_A_s2))
        #final
        total_material_final = metros_A_total +  inventario_final_material_A_s2
        total_material_final_str = str(total_material_final)
        widgets.total_materiales_final.setText(moneda(total_material_final))
    #Inventario inicial
        #Semestre 1
        inventario_inicial_s1 = float(widgets.inventario_inicial_s1.text())
        #semestre 2
        widgets.inventario_inicial_s2.setText(moneda(inventario_final_material_A_s1))
        #total
        widgets.inventario_inicial_total.setText(moneda(inventario_final_material_A_s1))
    #Material a comprar
        #semestre 1
        material_A_comprar_s1 = total_material_A - inventario_inicial_s1
        material_A_comprar_s1_str = str(material_A_comprar_s1)
        widgets.material_a_comprar_s1.setText(moneda(material_A_comprar_s1))
        #Semestre 2
        material_A_comprar_s2 = total_material_A_s2 - inventario_inicial_s1
        material_A_comprar_s2_str = str(material_A_comprar_s2)
        widgets.material_a_comprar_s2.setText(moneda(material_A_comprar_s2))
        #Total
        material_A_comprar_total = total_material_final - inventario_inicial_s1
        material_A_comprar_total_str = str(material_A_comprar_total)
        widgets.material_a_comprar_total.setText(moneda(material_A_comprar_total))
    #Precio de compra
        #Semestre 1
        precio_compra_s1_material_A = float(widgets.precio_compra_s1.text())
        #Semestre 2
        precio_compra_s2_material_A = float(widgets.precio_compra_s2.text())
    #Total de Material A en $
        #Semestre 1
        total_material_A_dinero_s1 = material_A_comprar_s1 * precio_compra_s1_material_A
        total_material_A_dinero_s1_str = str(total_material_A_dinero_s1)
        widgets.total_material_A_s1.setText(moneda(total_material_A_dinero_s1))
        #Semestre 2
        total_material_A_dinero_s2 = material_A_comprar_s2 * precio_compra_s2_material_A
        total_material_A_dinero_s2_str = str(total_material_A_dinero_s2)
        widgets.total_material_A_s2.setText(moneda(total_material_A_dinero_s2))
        #Total
        total_material_A_dinero_final = total_material_A_dinero_s1 + total_material_A_dinero_s2
        total_material_A_dinero_final_str = str(total_material_A_dinero_final)
        widgets.total_material_A_totales.setText(moneda(total_material_A_dinero_final))

    #Material B
    #Requerimiento de material
        #Semestre 1
        widgets.requerimiento_materiales_semestre1_material_B.setText(moneda(total_metros_B))
        #semestre 2
        widgets.requerimiento_materiales_semestre2_material_B.setText(moneda(total_metros_B_s2))
        #Total
        widgets.requerimiento_materiales_total_material_B.setText(moneda(metros_B_total))

    #inventario Final
        #semestre 1
        inventario_final_material_B_s1 = float(widgets.inventario_final_s1_material_B.text())
        inventario_final_material_B_s1_str = widgets.inventario_final_s1_material_B.text()
        #semestre 2
        inventario_final_material_B_s2 = float(widgets.inventario_final_s2_material_B.text())
        inventario_final_material_B_s2_str = widgets.inventario_final_s2_material_B.text()
        #Total
        widgets.inventario_final_totales_material_B.setText(moneda(inventario_final_material_B_s2))
    #total de materiales
        #semestre 1
        total_material_B = total_metros_B + inventario_final_material_B_s1
        total_material_B_str = str(total_material_B)
        widgets.total_materiales_semestre1_material_B.setText(moneda(total_material_B))
        #semestre 2
        total_material_B_s2 = total_metros_B_s2 + inventario_final_material_B_s2
        total_material_B_s2_str = str(total_material_B_s2)
        widgets.total_materiales_semestre2_material_B.setText(moneda(total_material_B_s2))
        #final
        total_material_final_B = metros_B_total +  inventario_final_material_B_s2
        total_material_final_B_str = str(total_material_final_B)
        widgets.total_materiales_final_material_B.setText(moneda(total_material_final_B))
    #Inventario inicial
        #Semestre 1
        inventario_inicial_s1_B = float(widgets.inventario_inicial_s1_material_B.text())
        #semestre 2
        widgets.inventario_inicial_s2_material_B.setText(moneda(inventario_final_material_B_s1))
        #total
        widgets.inventario_inicial_total_material_B.setText(moneda(inventario_final_material_B_s1))
    #Material a comprar
        #semestre 1
        material_B_comprar_s1 = total_material_B - inventario_inicial_s1_B
        material_B_comprar_s1_str = str(material_B_comprar_s1)
        widgets.material_a_comprar_s1_material_B.setText(moneda(material_B_comprar_s1))
        #Semestre 2
        material_B_comprar_s2 = total_material_B_s2 - inventario_inicial_s1_B
        material_B_comprar_s2_str = str(material_B_comprar_s2)
        widgets.material_a_comprar_s2_material_B.setText(moneda(material_B_comprar_s2))
        #Total
        material_B_comprar_total = total_material_final_B - inventario_inicial_s1_B
        material_B_comprar_total_str = str(material_B_comprar_total)
        widgets.material_a_comprar_total_material_B.setText(moneda(material_B_comprar_total))
    #Precio de compra
        #Semestre 1
        precio_compra_s1_material_B = float(widgets.precio_compra_s1_material_B.text())
        #Semestre 2
        precio_compra_s2_material_B = float(widgets.precio_compra_s2_material_B.text())
    #Total de Material B en $
        #Semestre 1
        total_material_B_dinero_s1 = material_B_comprar_s1 * precio_compra_s1_material_B
        total_material_B_dinero_s1_str = str(total_material_B_dinero_s1)
        widgets.total_material_B_s1.setText(moneda(total_material_B_dinero_s1))
        #Semestre 2
        total_material_B_dinero_s2 = material_B_comprar_s2 * precio_compra_s2_material_B
        total_material_B_dinero_s2_str = str(total_material_B_dinero_s2)
        widgets.total_material_B_s2.setText(moneda(total_material_B_dinero_s2))
        #Total
        total_material_B_dinero_final = total_material_B_dinero_s1 + total_material_B_dinero_s2
        total_material_B_dinero_final_str = str(total_material_B_dinero_final)
        widgets.total_material_B_totales.setText(moneda(total_material_B_dinero_final))

    #Material C
    #Requerimiento de material
        #Semestre 1
        widgets.requerimiento_materiales_semestre1_material_C.setText(moneda(total_metros_C))
        #semestre 2
        widgets.requerimiento_materiales_semestre2_material_C.setText(moneda(total_metros_C_s2))
        #Total
        widgets.requerimiento_materiales_total_material_C.setText(moneda(metros_C_total))

    #inventario Final
        #semestre 1
        inventario_final_material_C_s1 = float(widgets.inventario_final_s1_material_C.text())
        inventario_final_material_C_s1_str = widgets.inventario_final_s1_material_C.text()
        #semestre 2
        inventario_final_material_C_s2 = float(widgets.inventario_final_s2_material_C.text())
        inventario_final_material_C_s2_str = widgets.inventario_final_s2_material_C.text()
        #Total
        widgets.inventario_final_totales_material_C.setText(moneda(inventario_final_material_C_s2))
    #total de materiales
        #semestre 1
        total_material_C = total_metros_C + inventario_final_material_C_s1
        total_material_C_str = str(total_material_C)
        widgets.total_materiales_semestre1_material_C.setText(moneda(total_material_C))
        #semestre 2
        total_material_C_s2 = total_metros_C_s2 + inventario_final_material_C_s2
        total_material_C_s2_str = str(total_material_C_s2)
        widgets.total_materiales_semestre2_material_C.setText(moneda(total_material_C_s2))
        #final
        total_material_final_C = metros_C_total +  inventario_final_material_C_s2
        total_material_final_C_str = str(total_material_final_C)
        widgets.total_materiales_final_material_C.setText(moneda(total_material_final_C))
    #Inventario inicial
        #Semestre 1
        inventario_inicial_s1_C = float(widgets.inventario_inicial_s1_material_C.text())
        #semestre 2
        widgets.inventario_inicial_s2_material_C.setText(moneda(inventario_final_material_C_s1))
        #total
        widgets.inventario_inicial_total_material_C.setText(moneda(inventario_final_material_C_s1))
    #Material a comprar
        #semestre 1
        material_C_comprar_s1 = total_material_C - inventario_inicial_s1_C
        material_C_comprar_s1_str = str(material_C_comprar_s1)
        widgets.material_a_comprar_s1_material_B.setText(moneda(material_C_comprar_s1))
        #Semestre 2
        material_C_comprar_s2 = total_material_C_s2 - inventario_inicial_s1_C
        material_C_comprar_s2_str = str(material_C_comprar_s2)
        widgets.material_a_comprar_s2_material_C.setText(moneda(material_C_comprar_s2))
        #Total
        material_C_comprar_total = total_material_final_C - inventario_inicial_s1_C
        material_C_comprar_total_str = str(material_C_comprar_total)
        widgets.material_a_comprar_total_material_c.setText(moneda(material_C_comprar_total))
    #Precio de compra
        #Semestre 1
        precio_compra_s1_material_C = float(widgets.precio_compra_s1_material_C.text())
        #Semestre 2
        precio_compra_s2_material_C = float(widgets.precio_compra_s2_material_C.text())
    #Total de Material C en $
        #Semestre 1
        total_material_C_dinero_s1 = material_C_comprar_s1 * precio_compra_s1_material_C
        total_material_C_dinero_s1_str = str(total_material_C_dinero_s1)
        widgets.total_material_C_s1.setText(moneda(total_material_C_dinero_s1))
        #Semestre 2
        total_material_C_dinero_s2 = material_C_comprar_s2 * precio_compra_s2_material_C
        total_material_C_dinero_s2_str = str(total_material_C_dinero_s2)
        widgets.total_material_C_s2.setText(moneda(total_material_C_dinero_s2))
        #Total
        total_material_C_dinero_final = total_material_C_dinero_s1 + total_material_C_dinero_s2
        total_material_C_dinero_final_str = str(total_material_C_dinero_final)
        widgets.total_material_C_totales.setText(moneda(total_material_C_dinero_final))
    #compras totales
        #Semestre 1
        compras_totales_semestre_1 = (total_material_A_dinero_s1 + total_material_B_dinero_s1 + total_material_C_dinero_s1)
        compras_totales_semestre_1_str = str(compras_totales_semestre_1)
        widgets.compras_totales_s1.setText(moneda(compras_totales_semestre_1))
        #Semestre 2
        compras_totales_semestre_2 = (total_material_A_dinero_s2 + total_material_B_dinero_s2 + total_material_C_dinero_s2)
        compras_totales_semestre_2_str = str(compras_totales_semestre_2)
        widgets.compras_totales_s2.setText(moneda(compras_totales_semestre_2))
        #total
        compras_totales_final = compras_totales_semestre_1 + compras_totales_semestre_2
        compras_totales_final_str = str(compras_totales_final)
        widgets.compras_totales_final.setText(moneda(compras_totales_final))

#6. Determinación del saldo de Proveedores y Flujo de Salidas.

    #saldo proveedores
        saldo_proveedores_total = float(widgets.saldo_de_proveedores_total.text())
        saldo_proveedores_total_str = widgets.saldo_de_proveedores_total.text()
    #Compras 2020
        widgets.compras_2020.setText(moneda(compras_totales_final))
    #Total de proveedores
        total_proveedores_2020 = compras_totales_final + saldo_proveedores_total
        total_proveedores_2020_str = str(total_proveedores_2020)
        widgets.total_de_proveedores.setText(moneda(total_proveedores_2020))
    #Por proveedores 2019
        widgets.por_proveedores_2019.setText(moneda(saldo_proveedores_total))
    #Por proveedores 2020
        proveedores_2020 = compras_totales_final * 0.5
        proveedores_2020_str = str(proveedores_2020)
        widgets.por_proveedores_2020.setText(moneda(proveedores_2020))
    #Total de salidas 2020
        total_salidas_2020 = saldo_proveedores_total + proveedores_2020
        total_salidas_2020_str = str(total_salidas_2020)
        widgets.total_salidas.setText(moneda(total_salidas_2020))
    #Saldo de proveedores 2020
        Saldo_de_proveedores_2020 = total_proveedores_2020 - total_salidas_2020
        Saldo_de_proveedores_2020_str = str(Saldo_de_proveedores_2020)
        widgets.total_provedores_2020.setText(moneda(Saldo_de_proveedores_2020))

#7. Presupuesto de Mano de Obra Directa.
    #Producto 1
        #unidades a producir
        #semestre 1
        widgets.unidades_a_producir_s1_producto_1.setText(moneda(unidades_producir_s1))
        #semestre 2
        widgets.unidades_a_producir_s2_producto_1.setText(moneda(unidades_producir_s2))
        #total
        widgets.unidades_a_producir_total_producto_1.setText(moneda(unidades_producir_t))

        #horas requeridas por unidad
        #semestre 1
        horas_por_unidad_semestre_1_producto_1 = float(widgets.horas_por_unidad_s1_producto_1.text())
        horas_por_unidad_semestre_1_producto_1_str = widgets.horas_por_unidad_s1_producto_1.text()
        #semestre 2
        widgets.horas_por_unidad_s2_producto_1.setText(moneda(horas_por_unidad_semestre_1_producto_1))
        #total
        widgets.horas_por_unidad_total_producto_1.setText(moneda(horas_por_unidad_semestre_1_producto_1))
        #Total de horas requeridas
        #semestre 1
        horas_requeridas_s1_producto_1 = unidades_producir_s1 * horas_por_unidad_semestre_1_producto_1
        horas_requeridas_s1_producto_1_str = str(horas_requeridas_s1_producto_1)
        widgets.horas_requeridas_s1_producto_1.setText(moneda(horas_requeridas_s1_producto_1))
        #semestre 2
        horas_requeridas_s2_producto_1 = unidades_producir_s2 * horas_por_unidad_semestre_1_producto_1
        horas_requeridas_s2_producto_1_str = str(horas_requeridas_s2_producto_1)
        widgets.horas_requeridas_s2_producto_1.setText(moneda(horas_requeridas_s2_producto_1))
        #Total
        total_horas_requeridas_producto_1 = horas_requeridas_s1_producto_1 + horas_requeridas_s2_producto_1
        total_horas_requeridas_producto_1_str = str(total_horas_requeridas_producto_1)
        widgets.horas_requeridas_total_producto_1.setText(moneda(total_horas_requeridas_producto_1))

        #cuota por hora
        #semestre 1
        cuota_por_hora_s1_producto_1 = float(widgets.cuota_hora_s1_producto_1.text())
        cuota_por_hora_s1_producto_1_str = str(cuota_por_hora_s1_producto_1)
        #semestre 2
        cuota_por_hora_s2_producto_1 = float(widgets.cuota_hora_s2_producto_1.text())
        cuota_por_hora_s2_producto_1_str = str(cuota_por_hora_s2_producto_1)

        #importe de MOD
        #semestre 1
        importe_s1_producto_1 = horas_requeridas_s1_producto_1 * cuota_por_hora_s1_producto_1
        importe_s1_producto_1_str = str(importe_s1_producto_1)
        widgets.importe_mod_s1_producto_1.setText(moneda(importe_s1_producto_1))
        #semestre 2
        importe_s2_producto_1 = horas_requeridas_s2_producto_1 * cuota_por_hora_s2_producto_1
        importe_s2_producto_1_str = str(importe_s2_producto_1)
        widgets.importe_mod_s2_producto_1.setText(moneda(importe_s2_producto_1))
        #total
        importe_total_producto_1 = importe_s1_producto_1 + importe_s2_producto_1
        importe_total_producto_1_str = str(importe_total_producto_1)
        widgets.importe_mod_total_producto_1.setText(moneda(importe_total_producto_1))

    #Producto 2
        #unidades a producir
        #semestre 1
        widgets.unidades_a_producir_s1_producto_2.setText(moneda(unidades_producir_prod2_s1))
        #semestre 2
        widgets.unidades_a_producir_s2_producto_2.setText(moneda(unidades_producir_prod2_s2))
        #total
        widgets.unidades_a_producir_total_producto_2.setText(moneda(unidades_producir_t_prod2))

        #horas requeridas por unidad
        #semestre 1
        horas_por_unidad_semestre_1_producto_2 = float(widgets.horas_por_unidad_s1_producto_2.text())
        horas_por_unidad_semestre_1_producto_2_str = widgets.horas_por_unidad_s1_producto_2.text()
        #semestre 2
        widgets.horas_por_unidad_s2_producto_2.setText(moneda(horas_por_unidad_semestre_1_producto_2))
        #total
        widgets.horas_por_unidad_total_producto_2.setText(moneda(horas_por_unidad_semestre_1_producto_2))
        #Total de horas requeridas
        #semestre 1
        horas_requeridas_s1_producto_2 = unidades_producir_prod2_s1 * horas_por_unidad_semestre_1_producto_2
        horas_requeridas_s1_producto_2_str = str(horas_requeridas_s1_producto_2)
        widgets.horas_requeridas_s1_producto_2.setText(moneda(horas_requeridas_s1_producto_2))
        #semestre 2
        horas_requeridas_s2_producto_2 = unidades_producir_prod2_s2 * horas_por_unidad_semestre_1_producto_2
        horas_requeridas_s2_producto_2_str = str(horas_requeridas_s2_producto_2)
        widgets.horas_requeridas_s2_producto_2.setText(moneda(horas_requeridas_s2_producto_2))
        #Total
        total_horas_requeridas_producto_2 = horas_requeridas_s1_producto_2 + horas_requeridas_s2_producto_2
        total_horas_requeridas_producto_2_str = str(total_horas_requeridas_producto_2)
        widgets.horas_requeridas_total_producto_2.setText(moneda(total_horas_requeridas_producto_2))

        #cuota por hora
        #semestre 1
        widgets.cuota_hora_s1_producto_2.setText(moneda(cuota_por_hora_s1_producto_1))
        cuota_por_hora_s1_producto_2 = float(widgets.cuota_hora_s1_producto_1.text())
        cuota_por_hora_s1_producto_2_str = str(cuota_por_hora_s1_producto_2)
        #semestre 2
        widgets.cuota_hora_s2_producto_2.setText(moneda(cuota_por_hora_s2_producto_1))
        cuota_por_hora_s2_producto_2 = float(widgets.cuota_hora_s2_producto_1.text())
        cuota_por_hora_s2_producto_2_str = str(cuota_por_hora_s2_producto_2)

        #importe de MOD
        #semestre 1
        importe_s1_producto_2 = horas_requeridas_s1_producto_2 * cuota_por_hora_s1_producto_2
        importe_s1_producto_2_str = str(importe_s1_producto_2)
        widgets.importe_mod_s1_producto_2.setText(moneda(importe_s1_producto_2))
        #semestre 2
        importe_s2_producto_2 = horas_requeridas_s2_producto_2 * cuota_por_hora_s2_producto_2
        importe_s2_producto_2_str = str(importe_s2_producto_2)
        widgets.importe_mod_s2_producto_2.setText(moneda(importe_s2_producto_2))
        #total
        importe_total_producto_2 = importe_s1_producto_2 + importe_s2_producto_2
        importe_total_producto_2_str = str(importe_total_producto_2)
        widgets.importe_mod_total_producto_2.setText(moneda(importe_total_producto_2))

    #Producto 3
        #unidades a producir
        #semestre 1
        widgets.unidades_a_producir_s1_producto_3.setText(moneda(unidades_producir_prod3_s1))
        #semestre 2
        widgets.unidades_a_producir_s2_producto_3.setText(moneda(unidades_producir_prod3_s2))
        #total
        widgets.unidades_a_producir_total_producto_3.setText(moneda(unidades_producir_t_prod3))

        #horas requeridas por unidad
        #semestre 1
        horas_por_unidad_semestre_1_producto_3 = float(widgets.horas_por_unidad_s1_producto_3.text())
        horas_por_unidad_semestre_1_producto_3_str = widgets.horas_por_unidad_s1_producto_3.text()
        #semestre 2
        widgets.horas_por_unidad_s2_producto_3.setText(moneda(horas_por_unidad_semestre_1_producto_3))
        #total
        widgets.horas_por_unidad_total_producto_3.setText(moneda(horas_por_unidad_semestre_1_producto_3))
        #Total de horas requeridas
        #semestre 1
        horas_requeridas_s1_producto_3 = unidades_producir_prod3_s1 * horas_por_unidad_semestre_1_producto_3
        horas_requeridas_s1_producto_3_str = str(horas_requeridas_s1_producto_3)
        widgets.horas_requeridas_s1_producto_3.setText(moneda(horas_requeridas_s1_producto_3))
        #semestre 2
        horas_requeridas_s2_producto_3 = unidades_producir_prod3_s2 * horas_por_unidad_semestre_1_producto_3
        horas_requeridas_s2_producto_3_str = str(horas_requeridas_s2_producto_3)
        widgets.horas_requeridas_s2_producto_3.setText(moneda(horas_requeridas_s2_producto_3))
        #Total
        total_horas_requeridas_producto_3 = horas_requeridas_s1_producto_3 + horas_requeridas_s2_producto_3
        total_horas_requeridas_producto_3_str = str(total_horas_requeridas_producto_3)
        widgets.horas_requeridas_total_producto_3.setText(moneda(total_horas_requeridas_producto_3))

        #cuota por hora
        #semestre 1
        widgets.cuota_hora_s1_producto_3.setText(moneda(cuota_por_hora_s1_producto_1))
        cuota_por_hora_s1_producto_3 = float(widgets.cuota_hora_s1_producto_1.text())
        cuota_por_hora_s1_producto_3_str = str(cuota_por_hora_s1_producto_3)
        #semestre 2
        widgets.cuota_hora_s2_producto_3.setText(moneda(cuota_por_hora_s2_producto_1))
        cuota_por_hora_s2_producto_3 = float(widgets.cuota_hora_s2_producto_1.text())
        cuota_por_hora_s2_producto_3_str = str(cuota_por_hora_s2_producto_3)

        #importe de MOD
        #semestre 1
        importe_s1_producto_3 = horas_requeridas_s1_producto_3 * cuota_por_hora_s1_producto_3
        importe_s1_producto_3_str = str(importe_s1_producto_3)
        widgets.importe_mod_s1_producto_3.setText(moneda(importe_s1_producto_3))
        #semestre 2
        importe_s2_producto_3 = horas_requeridas_s2_producto_3 * cuota_por_hora_s2_producto_3
        importe_s2_producto_3_str = str(importe_s2_producto_3)
        widgets.importe_mod_s2_producto_3.setText(moneda(importe_s2_producto_3))
        #total
        importe_total_producto_3 = importe_s1_producto_3 + importe_s2_producto_3
        importe_total_producto_3_str = str(importe_total_producto_3)
        widgets.importe_mod_total_producto_3.setText(moneda(importe_total_producto_3))

    #Total horas requeridas por semestre
        #semestre 1
        horas_requeridas_total_s1 = (horas_requeridas_s1_producto_1 + horas_requeridas_s1_producto_2 + horas_requeridas_s1_producto_3)
        horas_requeridas_total_s1_str = str(horas_requeridas_total_s1)
        widgets.total_horas_semestre_1.setText(moneda(horas_requeridas_total_s1))
        #semestre 2
        horas_requeridas_total_s2 = (horas_requeridas_s2_producto_1 + horas_requeridas_s2_producto_2 + horas_requeridas_s2_producto_3)
        horas_requeridas_total_s2_str = str(horas_requeridas_total_s2)
        widgets.total_horas_semestre_2.setText(moneda(horas_requeridas_total_s2))
        #total
        horas_requeridas_total = horas_requeridas_total_s1 + horas_requeridas_total_s2
        horas_requeridas_total_str = str(horas_requeridas_total)
        widgets.total_horas_semestres.setText(moneda(horas_requeridas_total))

    #Total Mod por semestre
        #semestre 1
        importe_mod_total_s1 = (importe_s1_producto_1 + importe_s1_producto_2 + importe_s1_producto_3)
        importe_mod_total_s1_str = str(importe_mod_total_s1)
        widgets.total_mod_semestre_1.setText(moneda(importe_mod_total_s1))
        #semestre 2
        importe_mod_total_s2 = (importe_s2_producto_1 + importe_s2_producto_2 + importe_s2_producto_3)
        importe_mod_total_s2_str = str(importe_mod_total_s2)
        widgets.total_mod_semestre_2.setText(moneda(importe_mod_total_s2))
        #Total
        importe_mod_total_semestres = importe_mod_total_s1 + importe_mod_total_s2
        importe_mod_total_semestres_str = str(importe_mod_total_semestres)
        widgets.total_mod_semestres.setText(moneda(importe_mod_total_semestres))

#8. Presupuesto de Gastos Indirectos de Fabricación.
    #Depreciación
        depreciacion_total = float(widgets.depreciacion_total.text())
        depreciacion_total_str = str(depreciacion_total)
        depreciacion_semestre = depreciacion_total/2
        depreciacion_semestre_str = str(depreciacion_semestre)
        widgets.depreciacion_semestre_1.setText(moneda(depreciacion_semestre))
        widgets.depreciacion_semestre_2.setText(moneda(depreciacion_semestre))
    #seguros
        seguros_total = float(widgets.seguro_total.text())
        seguro_total_semestre = seguros_total/2
        seguro_total_semestre_str = str(seguro_total_semestre)
        widgets.seguro_semestre_1.setText(moneda(seguro_total_semestre))
        widgets.seguro_semestre_2.setText(moneda(seguro_total_semestre))
    #Mantenimiento
        mantenimiento_total_semestre_1 = float(widgets.mantenimiento_semestre_1.text())
        mantenimiento_total_semestre_2 = float(widgets.mantenimiento_semestre_2.text())
        mantenimiento_total = mantenimiento_total_semestre_1 + mantenimiento_total_semestre_2
        mantenimiento_total_str = str(mantenimiento_total)
        widgets.mantenimiento_total.setText(moneda(mantenimiento_total))
    #Energéticos
        energeticos_semestre_1 = float(widgets.energeticos_semestre_1.text())
        energeticos_semestre_2 = float(widgets.energeticos_semestre_2.text())
        energeticos_total = energeticos_semestre_1 + energeticos_semestre_2
        energeticos_total_str = str(energeticos_total)
        widgets.energeticos_total.setText(moneda(energeticos_total))
    #varios
        varios_total = float(widgets.varios_total.text())
        varios_semestres = varios_total/2
        varios_semestres_str = str(varios_semestres)
        widgets.varios_semestre_1.setText(moneda(varios_semestres))
        widgets.varios_semestre_2.setText(moneda(varios_semestres))
    #Total G.I.F por semestre
        #semestre 1
        total_gif_semestre_1 = (depreciacion_semestre + seguro_total_semestre + mantenimiento_total_semestre_1 + energeticos_semestre_1 + varios_semestres)
        total_gif_semestre_1_str = str(total_gif_semestre_1)
        widgets.GIF_semestre_1.setText(moneda(total_gif_semestre_1))
        #semestre 2
        total_gif_semestre_2 = (depreciacion_semestre + seguro_total_semestre + mantenimiento_total_semestre_2 + energeticos_semestre_2 + varios_semestres)
        total_gif_semestre_2_str = str(total_gif_semestre_2)
        widgets.GIF_semestre_2.setText(moneda(total_gif_semestre_2))
        #Total
        total_gif_semestres = total_gif_semestre_1 + total_gif_semestre_2
        total_gif_semestres_str = str(total_gif_semestres)
        widgets.GIF_total.setText(moneda(total_gif_semestres))
    #Total de G.I.F
        widgets.total_de_gif.setText(moneda(total_gif_semestres))
    #Total horas MOD
        widgets.total_horas_mod.setText(moneda(horas_requeridas_total))
    #Costo por hora de G.I.F
        costo_hora_gif = total_gif_semestres / horas_requeridas_total
        costo_hora_gif_str = str(costo_hora_gif)
        widgets.costo_por_hora_gif.setText(moneda(costo_hora_gif))

#9. Presupuesto de Gastos de Operación.
    #Depreciacion
        #Total
        depreciacion_total_operacion = float(widgets.depreciacion_semestres.text())
        #semestre 1
        depreciacion = depreciacion_total_operacion / 2
        widgets.depreciacion_semestre_3.setText(moneda(depreciacion))
        #semestre 2
        widgets.depreciacion_semestre_4.setText(moneda(depreciacion))
    #Sueldos y salarios
        #Total
        sueldos = float(widgets.sueldos_y_salarios_semestre_total.text())
        #semestre 1
        sueldos_semestres = sueldos / 2
        widgets.sueldos_y_salarios_semestre_1.setText(moneda(sueldos_semestres))
        #semestre 2
        widgets.sueldos_y_salarios_semestre_2.setText(moneda(sueldos_semestres))
    #Comisiones
        #semestre 1
        comisiones_semestre_1 = ((s1_t * 1)/100)
        widgets.comisiones_semestre_1.setText(moneda(comisiones_semestre_1))
        #semestre 2
        comisiones_semestre_2 = (s2_t * 1)/100
        widgets.comisiones_semestre_2.setText(moneda(comisiones_semestre_2))
        #total
        total_comisiones = comisiones_semestre_1 + comisiones_semestre_2
        widgets.comisiones_semestres.setText(moneda(total_comisiones))
    #Varios
        #Semestre 1
        varios_semestre_1 = float(widgets.varios_semestre_3.text())
        #Semestre 2
        varios_semestre_2 = float(widgets.varios_semestre_4.text())
        #Total
        varios_semestre_total = varios_semestre_1 + varios_semestre_2
        widgets.varios_semestre_total.setText(moneda(varios_semestre_total))
    #Intereses
        #Total
        intereses_total = float(widgets.intereses_prestamo_semestres.text())
        #Semestre 1 y 2
        intereses_semestre_1 = intereses_total/2
        widgets.intereses_prestamo_semestre_1.setText(moneda(intereses_semestre_1))
        widgets.intereses_prestamo_semestre_2.setText(moneda(intereses_semestre_1))
    #Total de gastos de operacion
        total_gastos_semestre_1 = (depreciacion+sueldos_semestres+comisiones_semestre_1+varios_semestre_1+intereses_semestre_1)
        total_gastos_semestre_2 = (depreciacion+sueldos_semestres+comisiones_semestre_2+varios_semestre_2+intereses_semestre_1)
        total_gastos = total_gastos_semestre_1 + total_gastos_semestre_2
        widgets.gastos_de_operacion_semestre_1.setText(moneda(total_gastos_semestre_1))
        widgets.gastos_de_operacion_semestre_2.setText(moneda(total_gastos_semestre_2))
        widgets.gastos_de_operacion_total.setText(moneda(total_gastos))

#10. Determinación del Costo Unitario de Productos Terminados.
    #Producto 1
        #materiales
        #Material A
        costo_material_A_producto_1 = float(widgets.costo_material_A_producto_1.text())
        cantidad_material_A_producto_1 = float(widgets.cantidad_material_A_producto_1.text())
        costo_unitario_material_A_producto_1 = costo_material_A_producto_1 * cantidad_material_A_producto_1
        widgets.costo_unitario_material_A_producto_1.setText(moneda(costo_unitario_material_A_producto_1))
        #Material B
        costo_material_B_producto_1 = float(widgets.costo_material_B_producto_1.text())
        cantidad_material_B_producto_1 = float(widgets.cantidad_material_B_producto_1.text())
        costo_unitario_material_B_producto_1 = costo_material_B_producto_1 * cantidad_material_B_producto_1
        widgets.costo_unitario_material_B_producto_1.setText(moneda(costo_unitario_material_B_producto_1))
        #Material C
        costo_material_C_producto_1 = float(widgets.costo_material_C_producto_1.text())
        cantidad_material_C_producto_1 = float(widgets.cantidad_material_C_producto_1.text())
        costo_unitario_material_C_producto_1 = costo_material_C_producto_1 * cantidad_material_C_producto_1
        widgets.costo_unitario_material_C_producto_1.setText(moneda(costo_unitario_material_C_producto_1))
        #Mano de obra
        costo_mano_de_obra_producto_1 = float(widgets.costo_mano_de_obra_producto_1.text())
        cantidad_mano_obra_producto_1 = float(widgets.cantidad_mano_de_obra_producto_1.text())
        costo_unitaio_mano_obra_producto_1 = costo_mano_de_obra_producto_1 * cantidad_mano_obra_producto_1
        widgets.costo_unitario_mano_obra_producto_1.setText(moneda(costo_unitaio_mano_obra_producto_1))
        #Gastos Indirectos de Fabricacion (GIF)
        widgets.costo_gastos_indirectos_fabricacion_producto_1.setText(moneda(costo_hora_gif))
        widgets.cantidad_gastos_de_fabricacion_producto_1.setText(moneda(cantidad_mano_obra_producto_1))
        total_gastos_indirectos_producto_1 = costo_hora_gif * cantidad_mano_obra_producto_1
        widgets.costo_unitario_gastos_fabricacion_producto_1.setText(moneda(total_gastos_indirectos_producto_1))
        #costo unitario
        costo_unitario_total_producto_1 = (costo_unitario_material_A_producto_1+costo_unitario_material_B_producto_1+costo_unitario_material_C_producto_1+costo_unitaio_mano_obra_producto_1+total_gastos_indirectos_producto_1)
        widgets.costo_unitario_total_producto_1.setText(moneda(costo_unitario_total_producto_1))

    #Producto 2
        #materiales
        #Material A
        widgets.costo_material_A_producto_2.setText(moneda(costo_material_A_producto_1))
        cantidad_material_A_producto_2 = float(widgets.cantidad_material_A_producto_2.text())
        costo_unitario_material_A_producto_2 = costo_material_A_producto_1 * cantidad_material_A_producto_2
        widgets.costo_unitario_material_A_producto_2.setText(moneda(costo_unitario_material_A_producto_2))
        #Material B
        widgets.costo_material_B_producto_2.setText(moneda(costo_material_B_producto_1))
        cantidad_material_B_producto_2 = float(widgets.cantidad_material_B_producto_2.text())
        costo_unitario_material_B_producto_2 = costo_material_B_producto_1 * cantidad_material_B_producto_2
        widgets.costo_unitario_material_B_producto_2.setText(moneda(costo_unitario_material_B_producto_2))
        #Material C
        widgets.costo_material_C_producto_2.setText(moneda(costo_material_C_producto_1))
        cantidad_material_C_producto_2 = float(widgets.cantidad_material_C_producto_2.text())
        costo_unitario_material_C_producto_2 = costo_material_C_producto_1 * cantidad_material_C_producto_2
        widgets.costo_unitario_material_C_producto_2.setText(moneda(costo_unitario_material_C_producto_2))
        #Mano de obra
        widgets.costo_mano_de_obra_producto_2.setText(moneda(costo_mano_de_obra_producto_1))
        cantidad_mano_obra_producto_2 = float(widgets.cantidad_mano_de_obra_producto_2.text())
        costo_unitaio_mano_obra_producto_2 = costo_mano_de_obra_producto_1 * cantidad_mano_obra_producto_2
        widgets.costo_unitario_mano_obra_producto_2.setText(moneda(costo_unitaio_mano_obra_producto_2))
        #Gastos Indirectos de Fabricacion (GIF)
        widgets.costo_gastos_indirectos_fabricacion_producto_2.setText(moneda(costo_hora_gif))
        widgets.cantidad_gastos_de_fabricacion_producto_2.setText(moneda(cantidad_mano_obra_producto_2))
        total_gastos_indirectos_producto_2 = costo_hora_gif * cantidad_mano_obra_producto_2
        widgets.costo_unitario_gastos_fabricacion_producto_2.setText(moneda(total_gastos_indirectos_producto_2))
        #costo unitario
        costo_unitario_total_producto_2 = (costo_unitario_material_A_producto_2+costo_unitario_material_B_producto_2+costo_unitario_material_C_producto_2+costo_unitaio_mano_obra_producto_2+total_gastos_indirectos_producto_2)
        widgets.costo_unitario_total_producto_2.setText(moneda(costo_unitario_total_producto_2))

    #Producto 3
        #materiales
        #Material A
        widgets.costo_material_A_producto_3.setText(moneda(costo_material_A_producto_1))
        cantidad_material_A_producto_3 = float(widgets.cantidad_material_A_producto_3.text())
        costo_unitario_material_A_producto_3 = costo_material_A_producto_1 * cantidad_material_A_producto_3
        widgets.costo_unitario_material_A_producto_3.setText(moneda(costo_unitario_material_A_producto_3))
        #Material B
        widgets.costo_material_B_producto_3.setText(moneda(costo_material_B_producto_1))
        cantidad_material_B_producto_3 = float(widgets.cantidad_material_B_producto_3.text())
        costo_unitario_material_B_producto_3 = costo_material_B_producto_1 * cantidad_material_B_producto_3
        widgets.costo_unitario_material_B_producto_3.setText(moneda(costo_unitario_material_B_producto_3))
        #Material C
        widgets.costo_material_C_producto_3.setText(moneda(costo_material_C_producto_1))
        cantidad_material_C_producto_3 = float(widgets.cantidad_material_C_producto_3.text())
        costo_unitario_material_C_producto_3 = costo_material_C_producto_1 * cantidad_material_C_producto_3
        widgets.costo_unitario_material_C_producto_3.setText(moneda(costo_unitario_material_C_producto_3))
        #Mano de obra
        widgets.costo_mano_de_obra_producto_3.setText(moneda(costo_mano_de_obra_producto_1))
        cantidad_mano_obra_producto_3 = float(widgets.cantidad_mano_de_obra_producto_3.text())
        costo_unitaio_mano_obra_producto_3 = costo_mano_de_obra_producto_1 * cantidad_mano_obra_producto_3
        widgets.costo_unitario_mano_obra_producto_3.setText(moneda(costo_unitaio_mano_obra_producto_3))
        #Gastos Indirectos de Fabricacion (GIF)
        widgets.costo_gastos_indirectos_fabricacion_producto_3.setText(moneda(costo_hora_gif))
        widgets.cantidad_gastos_de_fabricacion_producto_3.setText(moneda(cantidad_mano_obra_producto_3))
        total_gastos_indirectos_producto_3 = costo_hora_gif * cantidad_mano_obra_producto_3
        widgets.costo_unitario_gastos_fabricacion_producto_4.setText(moneda(total_gastos_indirectos_producto_3))
        #costo unitario
        costo_unitario_total_producto_3 = (costo_unitario_material_A_producto_3+costo_unitario_material_B_producto_3+costo_unitario_material_C_producto_3+costo_unitaio_mano_obra_producto_3+total_gastos_indirectos_producto_3)
        widgets.costo_unitario_total_producto_3.setText(moneda(costo_unitario_total_producto_3))

#11. Valuación de Inventarios Finales.
    #inventario final de materiales
        #Material A
        #unidades
        widgets.unidades_material_A.setText(moneda(inventario_final_material_A_s2))
        #Costo unitario
        widgets.costo_unitario_material_A.setText(moneda(costo_material_A_producto_1))
        #Costo total
        costo_total = inventario_final_material_A_s2 * costo_material_A_producto_1
        widgets.costo_total_material_A.setText(moneda(costo_total))
        #Material B
        #unidades
        widgets.unidades_material_B.setText(moneda(inventario_final_material_B_s2))
        #Costo unitario
        widgets.costo_unitario_material_B.setText(moneda(costo_material_B_producto_1))
        #Costo total
        costo_total_material_B = inventario_final_material_B_s2 * costo_material_B_producto_1
        widgets.costo_total_material_B.setText(moneda(costo_total_material_B))
        #Material C
        #unidades
        widgets.unidades_material_C.setText(moneda(inventario_final_material_C_s2))
        #Costo unitario
        widgets.costo_unitario_material_C.setText(moneda(costo_material_C_producto_1))
        #Costo total
        costo_total_material_C = inventario_final_material_C_s2 * costo_material_C_producto_1
        widgets.costo_total_material_C.setText(moneda(costo_total_material_C))
        #Inventario final de materiales
        inventario_final_de_materiales = costo_total + costo_total_material_B + costo_total_material_C
        widgets.costo_total_materiales.setText(moneda(inventario_final_de_materiales))
    #Inventario final de producto terminado
        #producto 1
        #unidades
        widgets.unidades_producto_1.setText(moneda(inventario_total))
        #Costo unitario
        widgets.costo_unitario_producto_1.setText(moneda(costo_unitario_total_producto_1))
        #Costo Total
        costo_total_producto_1 = inventario_total * costo_unitario_total_producto_1
        widgets.costo_total_producto_1.setText(moneda(costo_total_producto_1))

        #producto 2
        #unidades
        widgets.unidades_producto_2.setText(moneda(inventario_total_prod2))
        #Costo unitario
        widgets.costo_unitario_producto_2.setText(moneda(costo_unitario_total_producto_2))
        #Costo Total
        costo_total_producto_2 = inventario_total_prod2 * costo_unitario_total_producto_2
        widgets.costo_total_producto_2.setText(moneda(costo_total_producto_2))

        #producto 3
        #unidades
        widgets.unidades_producto_3.setText(moneda(inventario_total_prod3))
        #Costo unitario
        widgets.costo_unitario_producto_3.setText(moneda(costo_unitario_total_producto_3))
        #Costo Total
        costo_total_producto_3 = inventario_total_prod3 * costo_unitario_total_producto_3
        widgets.costo_total_producto_3.setText(moneda(costo_total_producto_3))

        #producto terminado
        producto_terminado = costo_total_producto_1 + costo_total_producto_2 + costo_total_producto_3
        widgets.costo_total_productos.setText(moneda(producto_terminado))

#Presupuesto Financiero
    #Estado de Costo de Producción y Ventas.
        #saldo inicial
        saldo_inicial_materiales = float(widgets.saldo_inicial_materiales.text())
        #compras
        widgets.compras_materiales.setText(moneda(compras_totales_final))
        #material disponible
        material_disponible = saldo_inicial_materiales + compras_totales_final
        widgets.material_disponible.setText(moneda(material_disponible))
        #inventario final materiales
        widgets.inventario_final_materiales.setText(moneda(inventario_final_de_materiales))
        #materiales utilizados
        materiales_utilizados = material_disponible - inventario_final_de_materiales
        widgets.materiales_utilizados.setText(moneda(materiales_utilizados))
        #mano de obra directa
        widgets.mano_obra_directa.setText(moneda(importe_mod_total_semestres))
        #Gastos de fabricacion indirectos
        widgets.gastos_fabricacion_indirectos.setText(moneda(total_gif_semestres))
        #Costo de produccion
        Costo_de_produccion = materiales_utilizados + importe_mod_total_semestres + total_gif_semestres
        widgets.costo_produccion.setText(moneda(Costo_de_produccion))
        #Inventario inicial productos terminados
        inventario_inicial_productos_terminados = float(widgets.inventario_inicial_productos_terminados.text())
        #total de produccion disponible
        total_produccion_disponible = Costo_de_produccion + inventario_inicial_productos_terminados
        widgets.total_produccion_disponible.setText(moneda(total_produccion_disponible))
        #inventario final de productos terminados
        widgets.inventario_final_productos_terminados.setText(moneda(producto_terminado))
        #costo de ventas
        costo_de_ventas = total_produccion_disponible - producto_terminado
        widgets.costo_de_ventas.setText(moneda(costo_de_ventas))
    #Estado de Resultados.
        #ventas
        widgets.ventas.setText(moneda(t_fin))
        #costo de ventas
        widgets.costo_de_ventas_2.setText(moneda(costo_de_ventas))
        #utilidad bruta
        utilidad_bruta = t_fin - costo_de_ventas
        widgets.utilidad_bruta.setText(moneda(utilidad_bruta))
        #Gastos de operacion
        widgets.gastos_de_operacion.setText(moneda(total_gastos))
        #utilidad de operacion
        utilidad_de_operacion = utilidad_bruta - total_gastos
        widgets.utilidad_operacion.setText(moneda(utilidad_de_operacion))
        #ISR
        isr = utilidad_de_operacion * 0.3
        widgets.ISR.setText(moneda(isr))
        #PTU
        ptu = utilidad_de_operacion * 0.1
        widgets.PTU.setText(moneda(ptu))
        #Utilidad neta
        utilidad_neta = utilidad_de_operacion - isr - ptu
        widgets.utilidad_neta.setText(moneda(utilidad_neta))

    #Estado de Flujo de Efectivo.
        #saldo inicial
        saldo_inicial = float(widgets.saldo_inicial.text())
        #cobranza 2020
        widgets.cobranza_2020.setText(moneda(cobranza2))
        #Cobranza 2019
        widgets.cobranza_2019.setText(moneda(saldo_clientes))
        #total entradas
        total_entradas_flujo = cobranza2 + saldo_clientes
        widgets.total_de_entradas.setText(moneda(total_entradas_flujo))
        #efectivo disponible
        efectivo_disponible = saldo_inicial + total_entradas_flujo
        widgets.efectivo_disponible.setText(moneda(efectivo_disponible))
        #proveedores 2020
        widgets.proveedores_2020.setText(moneda(proveedores_2020))
        #proveedores 2019
        widgets.proveedores_2019.setText(moneda(saldo_proveedores_total))
        #pago mano de obra directa
        widgets.pago_mano_de_obra_directa.setText(moneda(importe_mod_total_semestres))
        #pago gastos indirectos de fabricacion
        pago_gif = total_gif_semestres - depreciacion_total
        widgets.gastos_indirectos_fabricacion.setText(moneda(pago_gif))
        #pago gastos de operacion
        pago_gastos_operacion = total_gastos - depreciacion_total_operacion
        widgets.pago_gastos_operacion.setText(moneda(pago_gastos_operacion))
        #compra de maquinaria
        maquinaria = float(widgets.compra_maquinaria.text())
        #pago isr
        pago_isr = float(widgets.pago_isr.text())
        #Total de salidas
        total_salidas = (proveedores_2020 + saldo_proveedores_total + importe_mod_total_semestres + pago_gif + pago_gastos_operacion + maquinaria + pago_isr)
        widgets.total_de_salidas.setText(moneda(total_salidas))
        #flujo de efectivo anual
        flujo_efectivo = efectivo_disponible - total_salidas
        widgets.flujo_de_efectivo_anual.setText(moneda(flujo_efectivo))

    #balance general
        #efectivo
        widgets.efectivo.setText(moneda(flujo_efectivo))
        #moneda
        widgets.clientes.setText(moneda(saldo_clientes_2020))
        #deudores diversos
        deudores_diversos = float(widgets.deudores_diversos.text())
        #funcionarios y empleados
        funcionarios = float(widgets.funcionarios_y_empleados.text())
        #inventario de materiales
        widgets.inventario_materiales.setText(moneda(inventario_final_de_materiales))
        #inventario de producto terminado
        widgets.inventario_producto_terminado.setText(moneda(producto_terminado))
        #total activos circulantes
        total_activos_circulantes = (flujo_efectivo + saldo_clientes_2020 + deudores_diversos + funcionarios + inventario_final_de_materiales + producto_terminado)
        widgets.total_activo_circulante_total.setText(moneda(total_activos_circulantes))
        #terreno
        terreno = float(widgets.terreno.text())
        #planta y equipo
        planta_entrada = float(widgets.planta_y_equipo_entrada.text())
        planta_y_equipo = planta_entrada + maquinaria
        widgets.planta_y_equipo.setText(moneda(planta_y_equipo))
        #depreciacion acumulada
        depreciacion_acumulada = float(widgets.depreciacion_acumulada_entrada.text())
        depreciacion_acumulada_total = (depreciacion_acumulada + depreciacion_total_operacion + depreciacion_total)
        widgets.depreciacion_acumulada.setText(moneda(depreciacion_acumulada_total))
        #total activos no circulante
        total_activo_no_circulante = (terreno + planta_y_equipo)- depreciacion_acumulada_total
        widgets.total_activo_no_circulante_total.setText(moneda(total_activo_no_circulante))
        #activo total
        activo_total = (total_activos_circulantes + total_activo_no_circulante)
        widgets.activo_total.setText(moneda(activo_total))
        #provedores
        widgets.proveedores.setText(moneda(Saldo_de_proveedores_2020))
        #documentos por pagar
        doc_por_pagar = float(widgets.coumentos_por_pagar.text())
        #isr por pagar
        widgets.isr_por_pagar.setText(moneda(isr))
        #ptu por pagar
        widgets.ptu_por_pagar.setText(moneda(ptu))
        #total pasivo corto plazo
        total_pasivo_corto_plazo = (Saldo_de_proveedores_2020 + doc_por_pagar + isr + ptu)
        widgets.total_pasivo_corto_plazo.setText(moneda(total_pasivo_corto_plazo))
        #prestamos bancarios
        prestamos_bancarios = float(widgets.prestamos_bancarios.text())
        #total de pasivo largo plazo
        widgets.total_pasivo_largo_plazo.setText(moneda(prestamos_bancarios))
        #pasivo total
        pasivo_total = total_pasivo_corto_plazo + prestamos_bancarios
        widgets.pasivo_total.setText(moneda(pasivo_total))
        #capital aportado
        capital_aportado = float(widgets.capital_aportado.text())
        #capital ganado
        capital_ganado = float(widgets.capital_ganado.text())
        #utilidad del ejercicio
        widgets.utilidad_del_ejercicio.setText(moneda(utilidad_neta))
        #total capital contable
        total_capital_contable = (capital_aportado + capital_ganado + utilidad_neta)
        widgets.total_capital_contable.setText(moneda(total_capital_contable))
        #suma del pasivo y capital
        suma_pasivo_capital = pasivo_total + total_capital_contable
        widgets.suma_pasivo_capital.setText(moneda(suma_pasivo_capital))
##########

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())

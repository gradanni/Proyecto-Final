# -*- coding: utf-8 -*- 
#Danny Barton
#danny.abm23@gmail.com
#Dania Galvez
#daniagalvez04@gmail.com
#Graciela Rodriguez
#gracielart11@gmail.com

import wx
import wx.xrc
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


###########################################################################
## Class Plano1 que se encarga de configurar la interfaz grafica
###########################################################################

class Plano1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 620,520 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Modelo Depredador-Presa de Lotka-Volterra ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 14, 74, 90, 92, False, "Arial" ) )
		
		bSizer1.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Ppredador = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.Ppredador, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Poblacion inicial predadores", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Ppresa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Ppresa, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Poblacion inicial presas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.meses = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.meses, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Meses", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.a = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.a, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u" Tasa instantánea de aumento de las presas en ausencia de predadores", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.b = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.b, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Tasa instantánea de disminución de predadores en el caso de ausencia de presas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.c = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.c, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u" Susceptibilidad de las presas a ser cazados", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.d = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.d, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u" Capacidad de depredación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnPob = wx.Button( self, wx.ID_ANY, u"Mostrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.btnPob, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Grafica de Población", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.btnDiag = wx.Button( self, wx.ID_ANY, u"Mostrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.btnDiag, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Diagrama de Espacio-Fase", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnPob.Bind( wx.EVT_BUTTON, self.OnClick )
		self.btnDiag.Bind( wx.EVT_BUTTON, self.OnClick1 )
	
	def __del__( self ):
		pass


	
	# Programando botones que muestran las dos diferentes graficas
	def OnClick( self, event ):
	    
	   #obteniendo los valores de los campos en blanco 
	    mes=self.meses.GetValue()
	    pres=self.Ppresa.GetValue()
	    pred=self.Ppredador.GetValue()
	    a1=self.a.GetValue()
	    b1=self.b.GetValue()
	    c1=self.c.GetValue()
	    d1=self.d.GetValue()
	    
	    #Validando que se deben llenar todos los datos
	    if (mes==''or pres==' 'or pred==' 'or a1==''or b1==''or c1==''or d1==''):
	        wx.MessageBox("LLene todos los datos", 'Validacion',wx.OK| wx.ICON_INFORMATION)
	    else:
	        #Ecuaciones Simultaneas
           	    def dP_dt(P, t):
           	        a=self.a.GetValue()
           	        b=self.b.GetValue()
           	        c=self.c.GetValue()
           	        d=self.d.GetValue()
           	        return [P[0]*(float(a) - float(b)*P[1]), -P[1]*(float(c) - float(d)*P[0])]
		
           	    #Definicion de Tiempo (pasos de solucion de la ecuacion)
           	    ts = np.linspace(0, float(mes), 100)
           	    
           	    #Valores poblacionales iniciales (presas y predadores)
           	    P0 = [float(pres), float(pred)]
           	    
           	    #Resulucion matematica del modelo
           	    Ps = odeint(dP_dt, P0, ts)
           	    
           	    #Valores calculados de cada ecuacion
           	    prey = Ps[:,0]
           	    predators = Ps[:,1]
           	    
           	    #Grafica de las poblaciones de presa y predadores
           	    plt.subplot(1, 1, 1)
           	    plt.plot(ts, prey, "r-", label="Presa")
           	    plt.plot(ts, predators, "b-", label="Predador")
           	    plt.xlabel("Tiempo (meses)")
           	    plt.ylabel("Poblacion")
           	    plt.legend();
           	    plt.show()
            
	
		 
	
	def OnClick1( self, event ):
	    
	    #obteniendo los valores de los campos en blanco 
	    mes=self.meses.GetValue()
	    pres=self.Ppresa.GetValue()
	    pred=self.Ppredador.GetValue()
	    a1=self.a.GetValue()
	    b1=self.b.GetValue()
	    c1=self.c.GetValue()
	    d1=self.d.GetValue()
	    
	    #Validando que se deben llenar todos los datos
	    if (mes==''or pres==' 'or pred==' 'or a1==''or b1==''or c1==''or d1==''):
	        wx.MessageBox("LLene todos los datos", 'Validacion',wx.OK| wx.ICON_INFORMATION)
	    else:
	        
	        #Ecuaciones Simultaneas
	        
	        def dP_dt(P, t):
	            a=self.a.GetValue()
	            b=self.b.GetValue()
	            c=self.c.GetValue()
	            d=self.d.GetValue()
	            return [P[0]*(float(a) - float(b)*P[1]), -P[1]*(float(c) - float(d)*P[0])]
  		
	    #Definicion de Tiempo (pasos de solucion de la ecuacion)
	    ts = np.linspace(0,float(mes), 100)
	    
	    #Valores poblacionales iniciales (presas y predadores)
	    P0 = [float(pres), float(pred)]
	    
	    #Resulucion matematica del modelo
	    Ps = odeint(dP_dt, P0, ts)
	    
	    #Valores calculados de cada ecuacion
	    prey = Ps[:,0]
	    predators = Ps[:,1]
	    
	    #Grafica de las poblaciones de presa y predadores
	    plt.subplot(1, 1, 1)
	    plt.plot(prey, predators, "b.")
	    plt.xlabel("Presa")
	    plt.ylabel("Predador")
	    plt.title("Diagrama de Espacio de Fase");
	    plt.show()
	    
	    
	

	

class main:

	#Creacion de la ventana
    app = wx.App(False) 
    frame = Plano1(None) 
    frame.Show(True) 

    # Start the GUI  
    app.MainLoop()
    wx.__version__
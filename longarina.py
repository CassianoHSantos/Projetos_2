'''
Sist. referência local
z <-- x
      |
      v
      y
'''

class Longarina():

    def __init__(self,tipo,tmax,I,ctoide):
        self.tipo = tipo # "C", "I"
        self.tmax = tmax # altura máxima (menor do que a espessura do perfil)
        # self.material_properties
        self.Inercia = I # [Izz,Iyy,Iyz]
        self.ctoide = ctoide # centroíde

    @classmethod
    def longarina_C(cls):
        # alma à direita
        cls.alma_t # espessura
        cls.alma_h # altura
        cls.mesa_t # espessura
        cls.mesa_l # largura
        return Longarina()
    
    @classmethod
    def longarina_I(cls,alma_t,alma_h,mesa_t,mesa_l):
        cls.alma_t = alma_t # espessura
        cls.alma_h = alma_h # altura
        cls.mesa_t = mesa_t # espessura
        cls.mesa_l = mesa_l # largura

        tipo = "I"
        tmax = alma_h + 2 * mesa_t
        Izz = (tmax**3 * mesa_l) / 12 - 2 * ((tmax-2*mesa_t)**3 * (mesa_l/2-alma_t/2)) / 12
        Iyy = (tmax * mesa_l**3) / 12 - 2 * ((tmax-2*mesa_t) * (mesa_l/2-alma_t/2)**3) / 12 - 2 * (tmax - 2*mesa_t)*(mesa_l/2-alma_t/2)*((mesa_l-alma_t)/4 + alma_t/2)**2
        Iyz = 0
        I = [Izz,Iyy,Iyz]
        ctoide = (0,0)

        return Longarina(tipo,tmax,I,ctoide)
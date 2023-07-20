class Barco:
    def __init__(self, nombre, carga_max, carga_actual, calado_min, calado_max, calado_actual, valo_total):
        self.nombre = nombre
        self.carga_max = carga_max
        self.carga_actual = carga_actual
        self.calado_min = calado_min
        self.calado_max = calado_max
        self.calado_actual = calado_actual
        self.valor_total = valo_total

    def actualizar_calado(self):
        calado_actual = (((self.calado_max-self.calado_min)*self.carga_actual)/self.carga_max) + self.calado_min
        self.calado_actual=calado_actual
        return calado_actual
    
    def actualizar_carga(self, carga_a_quitar):
        aux=self.carga_actual-carga_a_quitar
        self.carga_actual=aux
        return aux
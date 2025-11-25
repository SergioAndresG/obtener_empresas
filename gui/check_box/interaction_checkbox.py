"""
Funciones que hacen la interacción con los botones
"""

def actualizar_contador(self):
    """Actualiza el contador de municipios seleccionados"""
    seleccionados = sum(1 for var in self.checkboxes.values() if var.get())
    self.label_contador.configure(text=f"Municipios seleccionados: {seleccionados}")

def seleccionar_todos(self):
    """Marca todos los checkboxes"""
    for var in self.checkboxes.values():
        var.set(True)

def deseleccionar_todos(self):
    """Desmarca todos los checkboxes"""
    for var in self.checkboxes.values():
        var.set(False)

def obtener_municipios_seleccionados(self):
    """Retorna lista de municipios seleccionados"""
    return [
        municipio 
        for municipio, var in self.checkboxes.items() 
        if var.get()
    ]

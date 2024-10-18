import pyautogui
import math

class TouchPad:
    def __init__(self, message) -> None:
        self.data = message
        self.last_x = 0
        self.last_y = 0
        pyautogui.PAUSE = 0

    async def move(self) -> None:
        # Obtém a posição atual do mouse
        current_x, current_y = pyautogui.position()
        target_x, target_y = self.data['move']['X'], self.data['move']['Y']

        # Tolerância para a comparação das posições
        tolerance = 1  

        # Converte a posição do mousepad para a posição da tela
        target_x, target_y = await self.__convert_dimensions(target_x, target_y)

        move_x = target_x - current_x # Ajuste a fração para suavizar o movimento
        move_y = target_y - current_y  # Ajuste a fração para suavizar o movimento

        # Atualiza as posições atuais do mouse
        current_x += move_x
        current_y += move_y
        
        # Move o mouse para a nova posição
        pyautogui.moveTo(int(current_x), int(current_y), duration=0.05)

        self.last_x = target_x
        self.last_y = target_y

    async def click(self) -> None:
        x, y = await self.__convert_dimensions(self.data['click']['X'], self.data['click']['Y'])
        pyautogui.click(x, y, duration=0.15)

        self.last_x = x
        self.last_y = y

    async def __convert_dimensions(self, x, y):
        l_width, l_height = pyautogui.size()  # Dimensões da tela
        # Obtém a posição atual do mouse (a posição do mousepad pode ser referenciada aqui)
        p_x, p_y = pyautogui.position()

        # Verifica se as dimensões do mousepad são válidas
        if self.data['width'] == 0 or self.data['height'] == 0:
            raise ValueError("Width and height must be greater than zero.")
        
        # Calcular as proporções
        p_width = l_width / self.data['width']
        p_height = l_height / self.data['height']

        # Calcular a nova posição em relação ao mousepad
        target_x = x * p_width
        target_y = y * p_height

        return target_x, target_y  # Retornar as novas coordenadas


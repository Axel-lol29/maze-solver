import streamlit as st
import pandas as pd
from maze_solver import MAZE, START, END, solve_maze_bfs
import time  # Importamos el módulo para medir el tiempo

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto / Axel Mireles  #739047")

# Función para renderizar el laberinto
def render_maze(maze, path=None):
    if path is None:
        path = []
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🔵") # Inicio
            elif (r_idx, c_idx) == END:
                display_row.append("🏁") # Fin
            elif (r_idx, c_idx) in path:
                display_row.append("🟢") # Camino resuelto
            elif col == 1:
                display_row.append("🟫") # Muro
            else:
                display_row.append("⬜") # Camino libre
        display_maze.append("".join(display_row))
    
    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)

# Sidebar para controles
st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox("Selecciona el algoritmo", ["BFS (implementado)", "DFS (no implementado)", "A* (no implementado)"])
solve_button = st.sidebar.button("Resolver Laberinto")

render_maze(MAZE)

if solve_button:
    start_time = time.time()  # Tomamos el tiempo de inicio
    if algorithm == "BFS (implementado)":
        path = solve_maze_bfs(MAZE, START, END)
        if path:
            end_time = time.time()  # Tomamos el tiempo de fin
            execution_time = end_time - start_time  # Calculamos el tiempo de ejecución
            st.success(f"¡Camino encontrado con {algorithm}!")
            render_maze(MAZE, path)
            st.write(f"Tiempo de ejecución: {execution_time:.5f} segundos")  # Mostramos el tiempo
        else:
            st.error("No se encontró un camino.")
    else:
        st.warning(f"El algoritmo {algorithm} aún no está implementado. Usa BFS.")

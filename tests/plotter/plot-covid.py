from bokeh.plotting import figure, output_file, show
import csv

def Leer_CSV(ruta):
    
    titulos = []
    fecha = []
    poblacion = []
    municipio = []
    casos_confirmados = []

    with open(ruta, newline='') as File:
        reader = csv.reader(File)
        data = list(reader)
        print('Datos: \n', len(data))

        for i in range(len(data)):
            for j in range(len(data[i])):
                if i == 0:
                    if j >= 3:
                        fecha.append(data[i][j])
                    else:
                        titulos.append(data[i][j])
                elif i >= 1:
                    if j == 1:
                        poblacion.append(int(data[i][j]))
                    elif j == 2:
                        municipio.append(data[i][j])
                    elif j >= 3:
                        casos_confirmados.append(int(data[i][j]))
    # print('Fechas: \n', fecha)
    # print('Municipio: \n', municipio)
    # print('Intubados: \n', casos_confirmados)
    Crear_grafico(fecha, casos_confirmados)

def Crear_grafico(fecha, lista):
    output_file('covid_cdmx.html')
    fig1 = figure(x_range = fecha, plot_height=800, plot_width = 1800, title="Casos confirmados por COVID-19 por municipio")

    fig1.vbar(x=fecha, top=lista, width=0.9)
    fig1.xaxis.major_label_orientation = 1.2

    show(fig1)

    
if __name__ == "__main__":
    #Leer_CSV('../personas-hospitalizadas-covid19.csv')
    Leer_CSV('../Casos_Diarios_Municipio_Confirmados_20200824.csv')
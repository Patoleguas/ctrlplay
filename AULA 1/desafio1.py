#Criando uma aula sobre figuras planas
#VARIÁVEIS
lado = 2
base = 3
altura = 4
diagonal_menor = 6
diagonal_maior = 8
base_maior = 10
base_menor = 6

#ÁREAS
#Quadrado
area_quadrado = lado * lado
perimetro_quadrado = lado + lado

#Retangulo
area_retangulo = base * altura
perimetro_retangulo = (base + altura) * 2

#Triângulo
area_triangulo = base * altura / 2
perimetro_triangulo = base + altura + altura

#Losango (multiplica a diagonal menor pela maior e divide por 2)
area_losango = (diagonal_menor * diagonal_maior) / 2
perimetro_losango = lado + lado + lado + lado

#Trapézio
area_trapezio = (base_maior + base_menor) * altura / 2
perimetro_trapezio = lado + lado + lado + lado



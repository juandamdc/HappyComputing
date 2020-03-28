from sim_distribuciones import sim_exponencial, sim_normal, sim_poisson, sim_serv_type
from collections import deque
import math

class HappyComputing:
    def __init__(self, hours):
        self.time = hours * 60

    def run(self):
        num_in = 0

        #ganancia obtenida hasta el mmomento
        ganancia = 0

        #tiempo en que se encuentra la simulacion
        time_proc = 0
        
        # variables para las colas de los servicios
        num_wait_v = deque()
        num_wait_t = deque()
        num_wait_te = 0

        # tiempo de llegada del proximo cleinte
        time_next_in = sim_poisson(20)

        # tiempo de finalizacion de la atencion del empleado a su cliente actual 
        time_end_v1 = math.inf
        time_end_v2 = math.inf

        time_end_t1 = math.inf
        time_end_t2 = math.inf
        time_end_t3 = math.inf

        time_end_te1 = math.inf

        # tipo de servicio del cliente que esta atendiendo el empleado
        type_v1 = 0
        type_v2 = 0

        type_t1 = 0
        type_t2 = 0
        type_t3 = 0

        type_te1 = 0

        while True:
            if time_next_in == min(time_next_in, time_end_v1, time_end_v2, time_end_t1, time_end_t2, time_end_t3, time_end_te1) and time_next_in <= self.time:
                time_proc = time_next_in
                
                num_in += 1
                num_wait_v.appendleft(sim_serv_type())

                time_next_in = time_proc + sim_poisson(20)

                if time_end_v1 == math.inf:
                    type_v1 = num_wait_v.pop()
                    time_end_v1 = time_proc + abs(sim_normal(5,2))

                elif time_end_v2 == math.inf:
                    type_v2 = num_wait_v.pop()
                    time_end_v2 = time_proc + abs(sim_normal(5,2))

            elif time_end_v1 != math.inf and time_end_v1 == min(time_end_v1, time_end_v2, time_end_t1, time_end_t2, time_end_t3, time_end_te1):
                time_proc = time_end_v1

                if type_v1 == 4:
                    ganancia += 750

                elif type_v1 == 1 or type_v1 == 2:
                    num_wait_t.appendleft(type_v1)

                    if time_end_t1 == math.inf:
                        type_t1 = num_wait_t.pop()
                        time_end_t1 = time_proc + sim_exponencial(20)

                    elif time_end_t2 == math.inf:
                        type_t2 = num_wait_t.pop()
                        time_end_t2 = time_proc + sim_exponencial(20)

                    elif time_end_t3 == math.inf:
                        type_t3 = num_wait_t.pop()
                        time_end_t3 = time_proc + sim_exponencial(20)

                    elif time_end_te1 == math.inf and num_wait_te == 0:
                        type_te1 = num_wait_t.pop()
                        time_end_te1 = time_proc + sim_exponencial(15)

                else:
                    num_wait_te += 1

                    if time_end_te1 == math.inf:
                        num_wait_te -= 1
                        type_te1 = type_v1
                        time_end_te1 = time_proc + sim_exponencial(15)

                if len(num_wait_v) == 0:
                    type_v1 = 0
                    time_end_v1 = math.inf

                else:
                    type_v1 = num_wait_v.pop()
                    time_end_v1 = time_proc + abs(sim_normal(5,2))

            elif time_end_v2 != math.inf and time_end_v2 == min(time_end_v2, time_end_t1, time_end_t2, time_end_t3, time_end_te1):
                time_proc = time_end_v2

                if type_v2 == 4:
                    ganancia += 750

                elif type_v2 == 1 or type_v2 == 2:
                    num_wait_t.appendleft(type_v2)

                    if time_end_t1 == math.inf:
                        type_t1 = num_wait_t.pop()
                        time_end_t1 = time_proc + sim_exponencial(20)

                    elif time_end_t2 == math.inf:
                        type_t2 = num_wait_t.pop()
                        time_end_t2 = time_proc + sim_exponencial(20)

                    elif time_end_t3 == math.inf:
                        type_t3 = num_wait_t.pop()
                        time_end_t3 = time_proc + sim_exponencial(20)

                    elif time_end_te1 == math.inf and num_wait_te == 0:
                        type_te1 = num_wait_t.pop()
                        time_end_te1 = time_proc + sim_exponencial(15)

                else:
                    num_wait_te += 1

                    if time_end_te1 == math.inf:
                        num_wait_te -= 1
                        type_te1 = type_v2
                        time_end_te1 = time_proc + sim_exponencial(15)

                if len(num_wait_v) == 0:
                    type_v2 = 0
                    time_end_v2 = math.inf

                else:
                    type_v2 = num_wait_v.pop()
                    time_end_v2 = time_proc + abs(sim_normal(5,2))

            elif time_end_t1 != math.inf and time_end_t1 == min(time_end_t1, time_end_t2, time_end_t3, time_end_te1):
                time_proc = time_end_t1

                if type_t1 == 1:
                    ganancia += 0
                else:
                    ganancia += 350

                if len(num_wait_t) == 0:
                    type_t1 = 0
                    time_end_t1 = math.inf
                
                else:
                    type_t1 = num_wait_t.pop()
                    time_end_t1 = time_proc + sim_exponencial(20)

            elif time_end_t2 != math.inf and time_end_t2 == min(time_end_t2, time_end_t3, time_end_te1):
                time_proc = time_end_t2

                if type_t2 == 1:
                    ganancia += 0
                else:
                    ganancia += 350

                if len(num_wait_t) == 0:
                    type_t2 = 0
                    time_end_t2 = math.inf
                
                else:
                    type_t2 = num_wait_t.pop()
                    time_end_t2 = time_proc + sim_exponencial(20)

            elif time_end_t3 != math.inf and time_end_t3 == min(time_end_t3, time_end_te1):
                time_proc = time_end_t3

                if type_t3 == 1:
                    ganancia += 0
                else:
                    ganancia += 350

                if len(num_wait_t) == 0:
                    type_t3 = 0
                    time_end_t3 = math.inf
                
                else:
                    type_t3 = num_wait_t.pop()
                    time_end_t3 = time_proc + sim_exponencial(20)

            elif time_end_te1 != math.inf:
                time_proc = time_end_te1

                if type_te1 == 1:
                    ganancia += 0
                elif type_te1 == 2:
                    ganancia += 350
                else:
                    ganancia +=  500

                if num_wait_te == 0:
                    if len(num_wait_t) == 0:
                        type_te1 = 0
                        time_end_te1 = math.inf
                    else:
                        type_te1 = num_wait_t.pop()
                        time_end_te1 = time_proc + sim_exponencial(15)

                else:
                    num_wait_te -= 1
                    type_te1 = 3
                    time_end_te1 = time_proc + sim_exponencial(15)

            else:
                return ganancia
    
    def calc_estimado(self, dias):
        acc = 0

        for _ in range(dias):
            acc += self.run()

        return acc/dias


proc = HappyComputing(8)
print(proc.calc_estimado(135))
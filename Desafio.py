class Paciente:
    pacientes = []

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []
        self.paciente = {'Nome': self.nome, 'Idade': self.idade, 'Historico': self.historico}
        Paciente.pacientes.append(self.paciente)

        print(f"""\n****** PACIENTE CADASTRADO COM SUCESSO *****\n
                \n Nome: {self.nome}
                \n Idade: {self.idade}\n""")

class Funcionario:
    funcionarios = []

    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo  

    def visualizarConsulta(self):
        for paciente in Paciente.pacientes:
            for consulta in paciente['Historico']:
                print(f"""\n*********** CONSULTAS AGENDADAS ***********\n
                            \n Data da consulta: {consulta[0]}
                            \n Paciente: {consulta[1]}
                            \n Médico: {consulta[2]}
                            \n Especialidade: {consulta[3]}
                            \n Regitrado por: {consulta[4]}\n""")
                
class Atendente(Funcionario):
    def __init__(self, nome, cargo):
        super().__init__(nome, cargo)
        self.funcionario = {'Nome': self.nome, 'Cargo': self.cargo}
        Funcionario.funcionarios.append(self.funcionario)

        print(f"""\n****** ATENDENTE CADASTRADO COM SUCESSO *****\n
                \n Atendente: {self.nome}
                \n Cargo: {self.cargo}\n""")
        
    def agendarConsulta(self, data_cs, paciente_nome, medico_nome, especialidade):
        responsavel = self.nome
        for paciente in Paciente.pacientes:
            if paciente['Nome'] == paciente_nome:
                for funcionario in Funcionario.funcionarios:
                    if funcionario['Nome'] == medico_nome:
                        consulta = (data_cs, paciente_nome, medico_nome, especialidade, responsavel)
                        paciente['Historico'].append(consulta)
                        self.visualizarConsulta()
                        break
                    else:
                        print('Médico não encontrado na base de dados.')
            else:
                print('Paciente não encontrado na base de dados.')
        
class Medico(Funcionario):
    def __init__(self, nome, cargo, especialidade, crm):
        super().__init__(nome, cargo)
        self.especialidade = especialidade
        self.crm = crm
        self.funcionario = {'Nome': self.nome, 'Cargo': self.cargo, 'Especialidade': self.especialidade, 'CRM': self.crm}
        Funcionario.funcionarios.append(self.funcionario)

        print(f"""\n****** MÉDICO CADASTRADO COM SUCESSO *****\n
                \n Médico: {self.nome}
                \n Cargo: {self.cargo}
                \n Especialidade: {self.especialidade}
                \n CRM: {self.crm}\n""")

    def prescreverMedicamento(self, paciente_nome, medicamento, prescricao):
        medico = self.nome
        for paciente in Paciente.pacientes:
            if paciente['Nome'] == paciente_nome:
                print(f"""\n*********** RECEITA ***********\n
                        \n Paciente: {paciente_nome}
                        \n Medicamento: {medicamento}
                        \n Prescrição: {prescricao}
                        \n Assinatura do Médico: {medico}\n""")
                break
            else:
                print('Paciente não encontrado.')

    def realizarExame(self, data_ex, paciente_nome, exame_nome):
        medico = self.nome
        for paciente in Paciente.pacientes:
            if paciente['Nome'] == paciente_nome:
                exame = (data_ex, paciente_nome, medico, exame_nome)
                paciente['Historico'] += exame
                print(f"""\n ************* EXAME *************\n
                        \n Data do exame: {data_ex}
                        \n Exame: {exame_nome}
                        \n Paciente: {paciente_nome}
                        \n Médico responsável: {medico}
                        \n Registro concluído com sucesso!\n""")
            else:
                print('Paciente não encontrado.')
                
class Enfermeiro(Funcionario):
    def __init__(self, nome, cargo, coren):
        super().__init__(nome, cargo)
        self.coren = coren
        self.funcionario = {'Nome': self.nome, 'Cargo': self.cargo, 'COREN': self.coren}
        Funcionario.funcionarios.append(self.funcionario)
        # print(Funcionario.funcionarios)

        print(f"""\n****** ENFERMEIRO CADASTRADO COM SUCESSO *****\n
                \n Enfermeiro: {self.nome}
                \n Cargo: {self.cargo}
                \n COREN: {self.coren}\n""")
        
    def aplicarInjecao(self, paciente_nome, medicamento):
        enfermeiro = self.nome
        for paciente in Paciente.pacientes:
            if paciente['Nome'] == paciente_nome:
                print(f"""\n ************ MEDICAÇÃO *************\n
                        \n Tipo de medicação: Injeção
                        \n Medicamento: {medicamento}
                        \n Paciente: {paciente_nome}
                        \n Enfermeiro responsável: {enfermeiro}
                        \n Medicação aplicada com sucesso!""")
        

pac = Paciente('Caroline', '26')
med = Medico('José', 'Médico', 'Oftalmologista', 12345)
ate = Atendente('Fernando', 'Atendente')
enf = Enfermeiro('Julia', 'Enfermeira', 54321)

ate.agendarConsulta('06/03/2024', 'Caroline', 'José', 'Oftalmologista')

# ate.visualizarConsulta()
# med.visualizarConsulta()
# enf.visualizarConsulta()

med.prescreverMedicamento('Caroline','Dipirona','tomar de 8 em 8h')

med.realizarExame('10/03/2024','Caroline','Refração')

enf.aplicarInjecao('Caroline','Benzetacil')


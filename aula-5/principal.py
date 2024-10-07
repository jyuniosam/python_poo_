from funcionario import Funcionario, Engenheiro, Supervisor

f1 = Funcionario("joana", 3000)
engenheiro1 = Engenheiro("Koala",3000)
Supervisor = Supervisor ("thavyla",4000)

f1.informacoes()
engenheiro1.bonusEngenheiro()
engenheiro1.informacoes()

Supervisor.relatorio()
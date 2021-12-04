from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    # O argumento de entrada é passado entre %
    # para que seja feito o uso do like no SQL
    args = (f'%{nome}%',)

    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)

document.addEventListener('DOMContentLoaded', function() {
    // Obter referência ao formulário
    const emprestimoForm = document.getElementById('emprestimoForm');

    // Adicionar evento de envio do formulário
    emprestimoForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Obter os valores dos campos do formulário
        const nome = document.getElementById('nomeCliente').value;
        const cpf = document.getElementById('cpfCliente').value;
        const endereco = document.getElementById('enderecoCliente').value;
        const valorEmprestimo = document.getElementById('valorEmprestimoCliente').value;

        const data = { nome: nome,
                       cpf: cpf,
                       endereco: endereco,
                       valorEmprestimo: valorEmprestimo };

        fetch("http://0.0.0.0:8000/api/v1/emprestimos/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "token 39b9d24f2cf5535dca00ee2587bf6a8b23d6485c"
        },
        body: JSON.stringify(data),
        })
        .then((response) => response.json())
        .then((data) => {
            alert("Sua solicitação de empréstimo foi enviada com sucesso!", data);
            console.log(data)
        })
        .catch((error) => {
            alert("Houve um erro ao processar sua solicitação de empréstimo.", error);
            console.log(data)
        });

        // Limpar os campos do formulário
        emprestimoForm.reset();
    });
    
});

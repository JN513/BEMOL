'use strict';

const limparformulario = (endereco) => {
    document.getElementById('uf').value = ''; 
    document.getElementById('localidade').value = '';
    document.getElementById('bairro').value = '';
    document.getElementById('logradouro').value = '';
}

const preencherFormulario = (endereco) => {
    document.getElementById('uf').value = endereco.uf; 
    document.getElementById('localidade').value = endereco.localidade;
    document.getElementById('bairro').value = endereco.bairro;
    document.getElementById('logradouro').value = endereco.logradouro;
}

const eNumero = (numero) => /^[0-9]+$/.test(numero);
const cepValido = (cep) => cep.length == 8 && eNumero(cep); 

const pesquisarCep = async () => {
    limparformulario();
    const cep = document.getElementById('cep').value;
    const url = `http://viacep.com.br/ws/${cep}/json/`;

    if (cepValido(cep)){
        const dados =  await fetch(url)
        const endereco = await dados.json();
        if (endereco.hasOwnProperty('erro')){
            document.getElementById('cep').value = 'CEP não encontrado';
        } else {
            preencherFormulario(endereco)
        }
    }
    
    else {
        document.getElementById('cep').value = 'CEP incorreto';
    }
    // console.log (endereco);
}

document.getElementById('cep')
        .addEventListener('focusout',pesquisarCep);
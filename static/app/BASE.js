function limpa_form_endereco(id_rua,id_bairro, id_cidade ,id_uf){
    $(id_bairro).val("");
    $(id_cidade).val("");
    $(id_uf).val("");
    $(id_rua).val("");
}

function busca_endereco(id_cep='#cep', id_rua='#endereco',id_bairro='#bairro', id_cidade='#cidade', id_uf='#estado'){
    var cep = $(id_cep).val().replace(/\D/g, '');
    if (cep != "") {
        var validacep = /^[0-9]{8}$/;
        if (validacep.test(cep)) {
            $(id_rua).val("...");
            $(id_bairro).val("...");
            $(id_cidade).val("...");
            $(id_uf).val("...");
            $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {
                if (!("erro" in dados)) {
                    var end = dados.logradouro +" "+ dados.bairro +" "+ dados.localidade +"-"+ dados.uf;
                    $(id_rua).val(dados.logradouro);
                    $(id_bairro).val(dados.bairro);
                    $(id_cidade).val(dados.localidade);
                    $(id_uf).val(dados.uf);
                }
                else {
                    limpa_form_endereco(id_rua,id_bairro,id_cidade,id_uf);
                    alert("CEP não encontrado.")        
                }
            });
        }
        else {
            limpa_form_endereco(id_rua,id_bairro,id_cidade,id_uf);
            alert("Formato de CEP inválido.")
        }
    }
    else {
        limpa_form_endereco(id_rua,id_bairro,id_cidade,id_uf);
    }

}
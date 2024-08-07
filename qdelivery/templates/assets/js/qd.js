let carrinho = document.querySelector(".carrinho");
document.querySelector("#cart").onclick = () => {
    carrinho.classList.toggle('active');

    login.classList.remove('active');
    menuResponsivo.classList.remove('active');
    console.log("ok")

}

let login = document.querySelector('.login-form');
document.querySelector('#login').onclick = () => {
    login.classList.toggle('active');
    carrinho.classList.remove('active');
    menuResponsivo.classList.remove('active');
    console.log("ok")
}

//Atualizar quantidade CARRINHO
/* document.querySelectorAll('.quantity-input').forEach(input => {
    input.addEventListener('change', function() {
        const itemId = this.dataset.itemId;
        const quantidade = this.value;

        fetch("{% url 'atualizar_quantidade' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify({ item_id: itemId, quantidade: quantidade })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('total_carrinho').innerText = data.total_carrinho;
            } else {
                alert('Erro ao atualizar quantidade.');
            }
        })
        .catch(error => console.error('Erro:', error));
    });
}); */

//Menu Responsivo
/* 
let menuResponsivo = document.querySelector('.menu-site');
document.querySelector('#menu').onclick = () => {
    menuResponsivo.classList.toggle('active');
    login.classList.remove('active');
    carrinho.classList.remove('active');
};

window.onscroll = () =>{
    login.classList.remove('active');
    carrinho.classList.remove('active');
    menuResponsivo.classList.remove('active');
}

var swiper = new Swiper(".home-slider",{
    
    autoplay:{
        delay: 2500,
        disableOnInteraction:false,
    },
    grapCursor:true,
    loop:true,
    centeredSlides:true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    
})
var swiper = new Swiper(".menu-slider",{
    
    grapCursor:true,
    loop:true,
    autoHeight:true,
    centeredSlides:true,
    spaceBetwwen:20,
    pagination: {
        el: '.swiper-pagination',
        clickable:true,
      },
    
})


 JANELA MODAL SITE 

// Seleciona o modal e o botão de fechamento
let verModalCorpo = document.querySelector(".menu-modal-container");
let verModalBox = verModalCorpo.querySelector(".menu-modal");

// Adiciona um evento de clique em todos os produtos
document.querySelectorAll(".box").forEach(menu => {
    menu.onclick = () => {
        // Obtém o ID do produto clicado
        let produtoId = menu.getAttribute('data-name');
        
        // Exibe o modal
        verModalCorpo.style.display = 'flex';
        
        // Faz uma solicitação AJAX para obter os dados do produto
        fetch(`/produto/${produtoId}/`)
            .then(response => response.json())
            .then(data => {
                // Preenche o modal com os dados do produto
                verModalBox.querySelector('#modal-titulo').textContent = data.titulo;
                verModalBox.querySelector('#modal-descricao').innerHTML = data.descricao;
                verModalBox.querySelector('#modal-preco').textContent = `R$ ${data.preco}`;
                // Atualize as estrelas se necessário
                // verModalBox.querySelector('#modal-estrelinhas').innerHTML = ...; 
            })
            .catch(error => console.error('Erro:', error));
    };
});

// Adiciona um evento de clique no botão de fechamento do modal
verModalCorpo.querySelector('#fechar').onclick = () => {
    verModalCorpo.style.display = 'none';
};
 */
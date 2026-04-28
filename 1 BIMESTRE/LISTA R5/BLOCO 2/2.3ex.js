class Estoque {
  constructor() {
    this._produtos = [];
  }

  cadastrar(nome, quantidade) {
    const existe = this._produtos.find(p => p.nome === nome);
    if (existe) {
      console.log("Produto já cadastrado.");
    } else {
      this._produtos.push({ nome, quantidade });
    }
  }

  entrada(nome, quantidade) {
    const produto = this._produtos.find(p => p.nome === nome);
    if (produto) {
      produto.quantidade += quantidade;
    } else {
      console.log("Produto não encontrado.");
    }
  }

  saida(nome, quantidade) {
    const produto = this._produtos.find(p => p.nome === nome);
    if (produto) {
      if (produto.quantidade - quantidade < 0) {
        console.log("Quantidade insuficiente.");
      } else {
        produto.quantidade -= quantidade;
      }
    } else {
      console.log("Produto não encontrado.");
    }
  }

  exibir() {
    this._produtos.forEach(p => {
      console.log(`${p.nome}: ${p.quantidade} unidades`);
    });
  }
}

const estoqueLoja = new Estoque();
estoqueLoja.cadastrar('Caneta', 20);
estoqueLoja.cadastrar('Caderno', 5);
estoqueLoja.entrada('Caneta', 10);
estoqueLoja.entrada('Caderno', 3);
estoqueLoja.saida('Caderno', 4)

estoqueLoja.exibir();
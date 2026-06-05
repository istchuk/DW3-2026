import {
  ProdutoIdInvalidoError,
  ProdutoNaoEncontradoError
} from "./produto.errors.js";

const produtos = [
  { id: 1, nome: "Monitor", preco: 500 },
  { id: 2, nome: "Fone", preco: 120 }
];

export async function buscarProdutoPorId(id) {
  const idNumerico = Number(id);

  if (Number.isNaN(idNumerico)) {
    throw new ProdutoIdInvalidoError();
  }

  const produto = produtos.find((produto) => produto.id === idNumerico);

  if (!produto) {
    throw new ProdutoNaoEncontradoError();
  }

  return produto;
}
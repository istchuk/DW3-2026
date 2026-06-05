import { AppError } from "../../shared/errors/app-error.js";

export class ProdutoIdInvalidoError extends AppError {
  constructor() {
    super("O ID precisa ser um número.", 400);
  }
}

export class ProdutoNaoEncontradoError extends AppError {
  constructor() {
    super("Produto não encontrado.", 404);
  }
}
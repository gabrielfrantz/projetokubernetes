CREATE database cadastros;

\c cadastros;

CREATE TABLE "enderecos" (
    id SERIAL PRIMARY KEY,
    endereco TEXT NOT NULL
);
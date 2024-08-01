import React, { useState } from 'react';
import './App.css';

function App() {
  const [cpf, setCpf] = useState('');
  const [idade, setIdade] = useState('');
  const [aceitaTermos, setAceitaTermos] = useState(false);
  const [message, setMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = {
      cpf: cpf,
      idade: parseInt(idade),
      aceita_termos: aceitaTermos
    };

    console.log('Submitting form:', formData);

    try {
      const response = await fetch('http://127.0.0.1:5000/pessoas', { // Ensure this URL matches your backend
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      console.log('Response received:', response);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      setMessage(`Pessoa criada com sucesso! ID: ${result.id}`);
    } catch (error) {
      setMessage(`Erro ao criar pessoa: ${error.message}`);
    }
  };

  return (
    <div className="formulario">
      <form onSubmit={handleSubmit}>
        <label>
          CPF:
          <input type="text" value={cpf} onChange={(e) => setCpf(e.target.value)} required />
        </label>
        <label>
          Idade:
          <input type="number" value={idade} onChange={(e) => setIdade(e.target.value)} required />
        </label>
        <label>
          Aceita Termos:
          <input type="checkbox" checked={aceitaTermos} onChange={(e) => setAceitaTermos(e.target.checked)} />
        </label>
        <button type="submit">Enviar</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default App;
